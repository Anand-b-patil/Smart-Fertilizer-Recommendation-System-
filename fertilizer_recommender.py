
class ImprovedFertilizerRecommender:
    def __init__(self):
        self.fertilizer_npk_content = {
            'Urea': {'N': 46, 'P': 0, 'K': 0},
            'DAP': {'N': 18, 'P': 46, 'K': 0},
            '10-26-26': {'N': 10, 'P': 26, 'K': 26},
            '14-35-14': {'N': 14, 'P': 35, 'K': 14},
            '17-17-17': {'N': 17, 'P': 17, 'K': 17},
            '20-20': {'N': 20, 'P': 20, 'K': 0},
            '28-28': {'N': 28, 'P': 28, 'K': 0}
        }

        self.crop_requirements = {
            'Maize': {'N': 120, 'P': 60, 'K': 40},
            'Rice': {'N': 100, 'P': 50, 'K': 50},
            'Paddy': {'N': 100, 'P': 50, 'K': 50},
            'Wheat': {'N': 150, 'P': 60, 'K': 40},
            'Cotton': {'N': 110, 'P': 50, 'K': 60},
            'Sugarcane': {'N': 200, 'P': 80, 'K': 120},
            'Ground Nuts': {'N': 25, 'P': 75, 'K': 50},
            'Pulses': {'N': 30, 'P': 60, 'K': 40},
            'Millets': {'N': 80, 'P': 40, 'K': 30},
            'Tobacco': {'N': 120, 'P': 60, 'K': 100},
            'Oil seeds': {'N': 100, 'P': 60, 'K': 40},
            'Barley': {'N': 120, 'P': 60, 'K': 40}
        }

        self.model = None
        self.encoders = {}

    def rule_based_recommendation(self, nitrogen, phosphorous, potassium, crop_type):
        '''
        Primary recommendation method based on agricultural science
        '''
        needs = self.crop_requirements.get(crop_type, {'N': 100, 'P': 50, 'K': 50})
        n_deficit = max(0, needs['N'] - nitrogen)
        p_deficit = max(0, needs['P'] - phosphorous) 
        k_deficit = max(0, needs['K'] - potassium)

        if n_deficit > 80 and p_deficit < 20 and k_deficit < 20:
            return 'Urea'
        elif p_deficit > 30 and n_deficit > 10:
            return 'DAP'
        elif n_deficit > 15 and p_deficit > 15 and k_deficit < 15:
            return '28-28'
        elif abs(n_deficit - p_deficit) < 10 and abs(n_deficit - k_deficit) < 10 and n_deficit > 10:
            return '17-17-17'
        elif p_deficit > 25 and k_deficit > 15:
            return '14-35-14'
        elif k_deficit > 20 and p_deficit > 20:
            return '10-26-26'
        elif n_deficit > 20 and p_deficit > 15:
            return '20-20'
        else:
            return '17-17-17'

    def create_logical_dataset(self, n_samples=5000):
        '''
        Generate training data with proper agricultural relationships
        '''
        np.random.seed(42)
        data = []

        crops = list(self.crop_requirements.keys())
        soil_types = ['Sandy', 'Loamy', 'Black', 'Red', 'Clayey']

        for _ in range(n_samples):
            temp = np.clip(np.random.normal(28, 6), 15, 42)
            humidity = np.clip(np.random.normal(60, 15), 30, 85)
            moisture = np.clip(np.random.normal(45, 15), 20, 70)
            crop = np.random.choice(crops)
            soil = np.random.choice(soil_types)
            soil_factors = {
                'Black': {'N': 35, 'P': 25, 'K': 25},
                'Red': {'N': 20, 'P': 30, 'K': 20}, 
                'Clayey': {'N': 30, 'P': 20, 'K': 15},
                'Loamy': {'N': 25, 'P': 22, 'K': 20},
                'Sandy': {'N': 15, 'P': 15, 'K': 12}
            }
            base = soil_factors[soil]
            nitrogen = max(5, np.random.normal(base['N'], 12))
            phosphorous = max(5, np.random.normal(base['P'], 10))
            potassium = max(5, np.random.normal(base['K'], 8))
            fertilizer = self.rule_based_recommendation(nitrogen, phosphorous, potassium, crop)
            data.append({
                'Temparature': round(temp, 1),
                'Humidity': round(humidity, 1),
                'Moisture': round(moisture, 1),
                'Soil Type': soil,
                'Crop Type': crop,
                'Nitrogen': round(nitrogen, 0),
                'Potassium': round(potassium, 0),
                'Phosphorous': round(phosphorous, 0),
                'Fertilizer Name': fertilizer
            })
        return pd.DataFrame(data)

    def engineer_features(self, df):
        '''
        Create meaningful features for ML model
        '''
        enhanced_df = df.copy()
        enhanced_df['Soil_Health_Index'] = (enhanced_df['Nitrogen'] + 
                                            enhanced_df['Phosphorous'] + 
                                            enhanced_df['Potassium']) / 3
        enhanced_df['Temp_Stress'] = ((enhanced_df['Temparature'] > 35) | 
                                      (enhanced_df['Temparature'] < 20)).astype(int)
        enhanced_df['Moisture_Stress'] = ((enhanced_df['Moisture'] < 30) | 
                                          (enhanced_df['Moisture'] > 70)).astype(int)
        enhanced_df['N_Level'] = pd.cut(enhanced_df['Nitrogen'], 
                                        bins=[0, 20, 40, 100], 
                                        labels=['Low', 'Medium', 'High'])
        enhanced_df['P_Level'] = pd.cut(enhanced_df['Phosphorous'], 
                                        bins=[0, 15, 30, 100], 
                                        labels=['Low', 'Medium', 'High'])
        enhanced_df['K_Level'] = pd.cut(enhanced_df['Potassium'], 
                                        bins=[0, 10, 20, 100], 
                                        labels=['Low', 'Medium', 'High'])
        return enhanced_df

    def prepare_data(self, df):
        '''
        Prepare data for machine learning
        '''
        df_enhanced = self.engineer_features(df)
        categorical_cols = ['Soil Type', 'Crop Type', 'N_Level', 'P_Level', 'K_Level']
        for col in categorical_cols:
            le = LabelEncoder()
            df_enhanced[f'{col}_Encoded'] = le.fit_transform(df_enhanced[col].astype(str))
            self.encoders[col] = le
        feature_cols = ['Temparature', 'Humidity', 'Moisture', 'Nitrogen', 'Potassium', 
                        'Phosphorous', 'Soil_Health_Index', 'Temp_Stress', 'Moisture_Stress'] + \
                       [f'{col}_Encoded' for col in categorical_cols]
        X = df_enhanced[feature_cols]
        y = df_enhanced['Fertilizer Name']
        return X, y

    def train_hybrid_system(self, df=None):
        '''
        Train the hybrid recommendation system
        '''
        if df is None:
            print("Creating logical training dataset...")
            df = self.create_logical_dataset(5000)
        print("Preparing features...")
        X, y = self.prepare_data(df)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        print("Training ML backup model...")
        self.model = RandomForestClassifier(
            n_estimators=200, 
            max_depth=15, 
            min_samples_split=5,
            random_state=42
        )
        self.model.fit(X_train, y_train)
        ml_pred = self.model.predict(X_test)
        ml_accuracy = accuracy_score(y_test, ml_pred)
        rule_predictions = []
        for idx, row in X_test.iterrows():
            original_idx = df.index[idx] if idx in df.index else df.iloc[idx % len(df)].name
            original_row = df.loc[original_idx]
            rule_pred = self.rule_based_recommendation(
                original_row['Nitrogen'],
                original_row['Phosphorous'], 
                original_row['Potassium'],
                original_row['Crop Type']
            )
            rule_predictions.append(rule_pred)
        rule_accuracy = accuracy_score(y_test, rule_predictions)
        print(f"\nModel Performance:")
        print(f"Rule-based accuracy: {rule_accuracy:.4f} ({rule_accuracy*100:.2f}%)")
        print(f"ML model accuracy: {ml_accuracy:.4f} ({ml_accuracy*100:.2f}%)")
        return rule_accuracy, ml_accuracy

    def predict(self, temperature, humidity, moisture, nitrogen, phosphorous, 
                potassium, soil_type, crop_type):
        '''
        Make fertilizer recommendation using hybrid approach
        '''
        rule_recommendation = self.rule_based_recommendation(
            nitrogen, phosphorous, potassium, crop_type
        )
        ml_recommendation = None
        confidence = "High"
        if self.model is not None:
            try:
                input_data = {
                    'Temparature': temperature,
                    'Humidity': humidity,
                    'Moisture': moisture,
                    'Nitrogen': nitrogen,
                    'Potassium': potassium,
                    'Phosphorous': phosphorous,
                    'Soil Type': soil_type,
                    'Crop Type': crop_type,
                    'Fertilizer Name': 'temp'
                }
                input_df = pd.DataFrame([input_data])
                X_input, _ = self.prepare_data(input_df)
                ml_recommendation = self.model.predict(X_input.iloc[:1])[0]
                if rule_recommendation != ml_recommendation:
                    confidence = "Medium"
            except Exception as e:
                ml_recommendation = "Error in ML prediction"
        return {
            'primary_recommendation': rule_recommendation,
            'ml_recommendation': ml_recommendation,
            'confidence': confidence,
            'explanation': self._get_explanation(nitrogen, phosphorous, potassium, crop_type)
        }

    def _get_explanation(self, nitrogen, phosphorous, potassium, crop_type):
        '''
        Provide explanation for the recommendation
        '''
        needs = self.crop_requirements.get(crop_type, {'N': 100, 'P': 50, 'K': 50})
        n_deficit = max(0, needs['N'] - nitrogen)
        p_deficit = max(0, needs['P'] - phosphorous)
        k_deficit = max(0, needs['K'] - potassium)
        explanations = []
        if n_deficit > 20:
            explanations.append(f"Nitrogen deficit: {n_deficit:.0f} kg/ha")
        if p_deficit > 15:
            explanations.append(f"Phosphorus deficit: {p_deficit:.0f} kg/ha")
        if k_deficit > 15:
            explanations.append(f"Potassium deficit: {k_deficit:.0f} kg/ha")
        if not explanations:
            return f"Soil nutrient levels adequate for {crop_type}. Maintenance fertilizer recommended."
        else:
            return f"Deficiencies detected: {', '.join(explanations)}"