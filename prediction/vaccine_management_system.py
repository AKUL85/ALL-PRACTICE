"""
================================================================================
        VACCINE MANAGEMENT SYSTEM - ML-POWERED SUPPLY CHAIN OPTIMIZER
================================================================================

LOGIC FLOW (Supply Chain Closed Loop):
┌─────────────────────────────────────────────────────────────────────┐
│                    INPUT: Area Demographics                          │
│  Population, Age Distribution, Infection Rate, Infrastructure, etc  │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                    ┌────────▼────────┐
                    │  DEMAND BRANCH  │
                    │  Random Forest  │
                    │   REGRESSOR     │
                    └────────┬────────┘
                             │
                ┌────────────▼────────────────┐
                │  PREDICTED VACCINE DOSES    │
                │  Required for Coverage      │
                └────────────┬────────────────┘
                             │
                    ┌────────▼────────┐
                    │  WASTE BRANCH   │
                    │  Random Forest  │
                    │  CLASSIFIER     │
                    └────────┬────────┘
                             │
           ┌─────────────────▼─────────────────┐
           │  WASTE RISK: LOW|MEDIUM|HIGH      │
           │  Indicates storage/distribution   │
           │  challenges                       │
           └─────────────────┬─────────────────┘
                             │
                    ┌────────▼────────┐
                    │  OPTIMIZATION   │
                    │  LOGIC:         │
                    │  - Adjust stock │
                    │  - Route plan   │
                    │  - Alerts       │
                    └─────────────────┘

================================================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score, classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)


# ================================================================================
# 1. SYNTHETIC DATA GENERATION
# ================================================================================

def generate_synthetic_vaccine_data(n_samples=500, save_to_csv=True):
    """
    Generate synthetic vaccine management dataset with realistic distributions.
    
    Features:
    - Population: Area population size (1000-500000)
    - Age_Dist: Age distribution index (0-1, higher = older population)
    - Past_7_Days: Vaccine doses administered in past 7 days
    - Infection_Rate: COVID-19 infection rate (%)
    - Awareness: Vaccination awareness score (0-100)
    - Power_Stability: Grid stability index (0-1)
    - Distance_from_Hub: Distance from distribution hub (km)
    
    Targets:
    - Demand: Daily vaccine doses needed (Regression)
    - Waste_Risk: Low (0), Medium (1), High (2) (Classification)
    """
    
    data = {
        'Population': np.random.uniform(1000, 500000, n_samples),
        'Age_Dist': np.random.uniform(0, 1, n_samples),
        'Past_7_Days': np.random.uniform(50, 5000, n_samples),
        'Infection_Rate': np.random.uniform(0.1, 10, n_samples),
        'Awareness': np.random.uniform(20, 100, n_samples),
        'Power_Stability': np.random.uniform(0.3, 1, n_samples),
        'Distance_from_Hub': np.random.uniform(5, 500, n_samples),
    }
    
    df = pd.DataFrame(data)
    
    # Generate realistic targets based on features
    # Demand: influenced by population, infection rate, awareness
    df['Demand'] = (
        (df['Population'] / 1000) * 0.3 +
        df['Infection_Rate'] * 50 +
        (df['Awareness'] / 100) * 100 +
        np.random.normal(0, 50, n_samples)
    ).clip(0, 10000)
    
    # Waste Risk: influenced by power stability, distance, past performance
    waste_score = (
        (1 - df['Power_Stability']) * 50 +
        (df['Distance_from_Hub'] / 500) * 40 +
        (100 - df['Awareness']) / 100 * 30 +
        np.random.normal(0, 10, n_samples)
    )
    df['Waste_Risk'] = pd.cut(waste_score, bins=[-np.inf, 40, 70, np.inf], 
                               labels=[0, 1, 2]).astype(int)
    
    if save_to_csv:
        csv_path = '/home/akul/AllPractice/prediction/vaccine_data.csv'
        df.to_csv(csv_path, index=False)
        print(f"✓ Synthetic data saved to: {csv_path}")
    
    return df


# ================================================================================
# 2. DATA PREPROCESSING WITH PIPELINES
# ================================================================================

class VaccineDataProcessor:
    """Handles data preprocessing for vaccine management models."""
    
    def __init__(self):
        self.scaler_pipeline = None
        self.feature_names = None
        
    def get_preprocessing_pipeline(self):
        """Create scikit-learn pipeline for feature scaling."""
        pipeline = Pipeline([
            ('scaler', StandardScaler())
        ])
        return pipeline
    
    def preprocess_data(self, df, fit=True):
        """
        Preprocess features for model training.
        
        Args:
            df: Input DataFrame
            fit: Whether to fit the scaler
            
        Returns:
            X_processed: Processed feature matrix
            y_demand: Demand target
            y_waste: Waste risk target
        """
        X = df[['Population', 'Age_Dist', 'Past_7_Days', 'Infection_Rate', 
                'Awareness', 'Power_Stability', 'Distance_from_Hub']].copy()
        
        y_demand = df['Demand'].copy()
        y_waste = df['Waste_Risk'].copy()
        
        self.feature_names = X.columns.tolist()
        
        if fit:
            self.scaler_pipeline = self.get_preprocessing_pipeline()
            X_processed = self.scaler_pipeline.fit_transform(X)
        else:
            X_processed = self.scaler_pipeline.transform(X)
        
        return X_processed, y_demand, y_waste


# ================================================================================
# 3. MODEL TRAINING
# ================================================================================

class VaccineManagementModels:
    """Train and manage both demand and waste prediction models."""
    
    def __init__(self):
        self.demand_model = None
        self.waste_model = None
        self.processor = VaccineDataProcessor()
        self.feature_names = None
        
    def train_models(self, df):
        """
        Train both Random Forest models.
        
        Args:
            df: Input DataFrame with features and targets
        """
        print("\n" + "="*70)
        print("TRAINING VACCINE MANAGEMENT MODELS")
        print("="*70)
        
        # Preprocess data
        X_processed, y_demand, y_waste = self.processor.preprocess_data(df, fit=True)
        self.feature_names = self.processor.feature_names
        
        # Train-test split
        X_train, X_test, y_train_demand, y_test_demand, y_train_waste, y_test_waste = \
            train_test_split(X_processed, y_demand, y_waste, test_size=0.2, random_state=42)
        
        # --- DEMAND PREDICTOR (Regressor) ---
        print("\n📊 Training Demand Predictor (Random Forest Regressor)...")
        self.demand_model = RandomForestRegressor(
            n_estimators=100,
            max_depth=15,
            min_samples_split=5,
            random_state=42,
            n_jobs=-1
        )
        self.demand_model.fit(X_train, y_train_demand)
        
        y_pred_demand = self.demand_model.predict(X_test)
        mse = mean_squared_error(y_test_demand, y_pred_demand)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test_demand, y_pred_demand)
        
        print(f"   ✓ RMSE: {rmse:.2f} doses")
        print(f"   ✓ R² Score: {r2:.4f}")
        
        # --- WASTE PREDICTOR (Classifier) ---
        print("\n⚠️  Training Waste Risk Predictor (Random Forest Classifier)...")
        self.waste_model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            min_samples_split=5,
            random_state=42,
            n_jobs=-1
        )
        self.waste_model.fit(X_train, y_train_waste)
        
        y_pred_waste = self.waste_model.predict(X_test)
        waste_accuracy = (y_pred_waste == y_test_waste).mean()
        
        print(f"   ✓ Accuracy: {waste_accuracy:.4f}")
        print(f"\n{classification_report(y_test_waste, y_pred_waste, 
                                         target_names=['Low', 'Medium', 'High'])}")
        
        print("="*70 + "\n")
        
        return X_test, y_test_demand, y_test_waste, y_pred_demand, y_pred_waste
    
    def get_feature_importance(self):
        """Extract feature importance from both models."""
        demand_importance = self.demand_model.feature_importances_
        waste_importance = self.waste_model.feature_importances_
        
        return pd.DataFrame({
            'Feature': self.feature_names,
            'Demand_Importance': demand_importance,
            'Waste_Importance': waste_importance
        }).sort_values('Demand_Importance', ascending=False)


# ================================================================================
# 4. VACCINE STRATEGY FUNCTION (Core Logic)
# ================================================================================

def get_vaccine_strategy(area_data, models, processor):
    """
    Generate vaccine supply strategy for a specific area.
    
    Args:
        area_data: Dict or DataFrame with area features
        models: Trained VaccineManagementModels instance
        processor: VaccineDataProcessor instance
    
    Returns:
        Dict with predicted demand, waste risk, and actionable recommendations
    """
    
    # Convert to DataFrame if needed
    if isinstance(area_data, dict):
        area_df = pd.DataFrame([area_data])
    else:
        area_df = area_data.copy()
    
    # Preprocess
    X_processed = processor.scaler_pipeline.transform(
        area_df[processor.feature_names]
    )
    
    # Predictions
    predicted_demand = models.demand_model.predict(X_processed)[0]
    waste_risk_numeric = models.waste_model.predict(X_processed)[0]
    waste_risk_label = ['Low', 'Medium', 'High'][int(waste_risk_numeric)]
    
    # Decision Logic
    recommendations = []
    
    if predicted_demand > 1000:
        recommendations.append("🚚 HIGH DEMAND: Increase vaccine shipment frequency")
    else:
        recommendations.append("📦 MODERATE DEMAND: Standard supply chain")
    
    if waste_risk_label == 'High':
        recommendations.append("⚠️  HIGH WASTE RISK: Implement cold chain monitoring")
        recommendations.append("📋 Action: Deploy backup power systems")
    elif waste_risk_label == 'Medium':
        recommendations.append("🔍 MEDIUM WASTE RISK: Monitor infrastructure closely")
    else:
        recommendations.append("✓ LOW WASTE RISK: Standard operations sufficient")
    
    # Get waste risk probability
    waste_proba = models.waste_model.predict_proba(X_processed)[0]
    
    return {
        'Predicted_Demand': round(predicted_demand, 2),
        'Waste_Risk': waste_risk_label,
        'Waste_Risk_Probabilities': {
            'Low': round(waste_proba[0], 4),
            'Medium': round(waste_proba[1], 4),
            'High': round(waste_proba[2], 4)
        },
        'Recommendations': recommendations,
        'Confidence_Score': round(max(waste_proba), 4)
    }


# ================================================================================
# 5. VISUALIZATION
# ================================================================================

def plot_feature_importance(importance_df, figsize=(14, 6)):
    """
    Create publication-ready feature importance visualization.
    
    Args:
        importance_df: DataFrame with feature importance scores
        figsize: Figure size tuple
    """
    fig, axes = plt.subplots(1, 2, figsize=figsize)
    fig.suptitle('Feature Importance Analysis - Vaccine Management System', 
                 fontsize=16, fontweight='bold', y=1.02)
    
    # Demand Model Importance
    ax1 = axes[0]
    importance_df_sorted = importance_df.sort_values('Demand_Importance', ascending=True)
    ax1.barh(importance_df_sorted['Feature'], importance_df_sorted['Demand_Importance'], 
             color='steelblue', alpha=0.8)
    ax1.set_xlabel('Importance Score', fontweight='bold')
    ax1.set_title('Demand Predictor\n(Random Forest Regressor)', fontweight='bold')
    ax1.grid(axis='x', alpha=0.3)
    
    # Waste Model Importance
    ax2 = axes[1]
    importance_df_sorted = importance_df.sort_values('Waste_Importance', ascending=True)
    ax2.barh(importance_df_sorted['Feature'], importance_df_sorted['Waste_Importance'], 
             color='coral', alpha=0.8)
    ax2.set_xlabel('Importance Score', fontweight='bold')
    ax2.set_title('Waste Risk Predictor\n(Random Forest Classifier)', fontweight='bold')
    ax2.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/akul/AllPractice/prediction/feature_importance.png', dpi=300, bbox_inches='tight')
    print("✓ Feature importance plot saved: feature_importance.png")
    plt.show()


def plot_model_performance(X_test, y_test_demand, y_pred_demand, 
                          y_test_waste, y_pred_waste):
    """
    Visualize model performance metrics.
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Model Performance Dashboard', fontsize=16, fontweight='bold')
    
    # Demand Actual vs Predicted
    ax = axes[0, 0]
    ax.scatter(y_test_demand, y_pred_demand, alpha=0.6, color='steelblue')
    ax.plot([y_test_demand.min(), y_test_demand.max()], 
            [y_test_demand.min(), y_test_demand.max()], 'r--', lw=2)
    ax.set_xlabel('Actual Demand', fontweight='bold')
    ax.set_ylabel('Predicted Demand', fontweight='bold')
    ax.set_title('Demand Predictor: Actual vs Predicted')
    ax.grid(alpha=0.3)
    
    # Demand Residuals
    ax = axes[0, 1]
    residuals = y_test_demand - y_pred_demand
    ax.scatter(y_pred_demand, residuals, alpha=0.6, color='steelblue')
    ax.axhline(y=0, color='r', linestyle='--', lw=2)
    ax.set_xlabel('Predicted Demand', fontweight='bold')
    ax.set_ylabel('Residuals', fontweight='bold')
    ax.set_title('Demand Residual Plot')
    ax.grid(alpha=0.3)
    
    # Waste Confusion Matrix
    ax = axes[1, 0]
    cm = confusion_matrix(y_test_waste, y_pred_waste)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
                xticklabels=['Low', 'Medium', 'High'],
                yticklabels=['Low', 'Medium', 'High'])
    ax.set_xlabel('Predicted', fontweight='bold')
    ax.set_ylabel('Actual', fontweight='bold')
    ax.set_title('Waste Risk Confusion Matrix')
    
    # Waste Classification Report
    ax = axes[1, 1]
    ax.axis('off')
    report_text = classification_report(y_test_waste, y_pred_waste,
                                        target_names=['Low', 'Medium', 'High'])
    ax.text(0.1, 0.5, report_text, fontsize=10, family='monospace',
            verticalalignment='center')
    ax.set_title('Waste Risk Classification Report')
    
    plt.tight_layout()
    plt.savefig('/home/akul/AllPractice/prediction/model_performance.png', dpi=300, bbox_inches='tight')
    print("✓ Performance dashboard saved: model_performance.png")
    plt.show()


# ================================================================================
# 6. MAIN EXECUTION
# ================================================================================

def main():
    """
    Run complete vaccine management system demo.
    """
    
    print("\n" + "🔬 "*20)
    print("VACCINE MANAGEMENT SYSTEM - ML PIPELINE")
    print("🔬 "*20 + "\n")
    
    # Step 1: Generate synthetic data
    print("Step 1️⃣  : Generating synthetic vaccine data...")
    df = generate_synthetic_vaccine_data(n_samples=500, save_to_csv=True)
    print(f"   ✓ Generated {len(df)} samples")
    print(f"\nDataset Preview:")
    print(df.head())
    print(f"\nDataset Statistics:")
    print(df.describe())
    
    # Step 2: Train models
    print("\n\nStep 2️⃣  : Building and training ML models...")
    models = VaccineManagementModels()
    X_test, y_test_demand, y_test_waste, y_pred_demand, y_pred_waste = models.train_models(df)
    
    # Step 3: Feature importance
    print("Step 3️⃣  : Extracting feature importance...")
    importance_df = models.get_feature_importance()
    print(importance_df.to_string(index=False))
    
    # Step 4: Test vaccine strategy function
    print("\n\nStep 4️⃣  : Testing vaccine strategy function...")
    test_area = {
        'Population': 150000,
        'Age_Dist': 0.35,
        'Past_7_Days': 2500,
        'Infection_Rate': 3.5,
        'Awareness': 75,
        'Power_Stability': 0.85,
        'Distance_from_Hub': 45
    }
    
    strategy = get_vaccine_strategy(test_area, models, models.processor)
    print("\n📋 VACCINE STRATEGY REPORT FOR SAMPLE AREA:")
    print("-" * 60)
    print(f"Predicted Daily Demand: {strategy['Predicted_Demand']} doses")
    print(f"Waste Risk Category: {strategy['Waste_Risk']}")
    print(f"Confidence Score: {strategy['Confidence_Score']}")
    print(f"\nWaste Risk Probabilities:")
    for risk, prob in strategy['Waste_Risk_Probabilities'].items():
        print(f"  • {risk}: {prob:.2%}")
    print(f"\n📊 Recommendations:")
    for rec in strategy['Recommendations']:
        print(f"  {rec}")
    print("-" * 60)
    
    # Step 5: Visualizations
    print("\n\nStep 5️⃣  : Generating visualizations for judges...")
    plot_feature_importance(importance_df)
    plot_model_performance(X_test, y_test_demand, y_pred_demand, 
                          y_test_waste, y_pred_waste)
    
    print("\n" + "✅ "*20)
    print("VACCINE MANAGEMENT SYSTEM READY FOR HACKATHON DEMO!")
    print("✅ "*20 + "\n")
    
    return models, models.processor, df


# ================================================================================
# ADDITIONAL UTILITY: Batch Processing
# ================================================================================

def batch_vaccine_strategy(areas_df, models, processor):
    """
    Generate strategies for multiple areas.
    
    Args:
        areas_df: DataFrame with multiple areas
        models: Trained VaccineManagementModels
        processor: VaccineDataProcessor
    
    Returns:
        DataFrame with strategies for all areas
    """
    results = []
    for idx, row in areas_df.iterrows():
        strategy = get_vaccine_strategy(row.to_dict(), models, processor)
        results.append({
            'Area_ID': idx,
            'Predicted_Demand': strategy['Predicted_Demand'],
            'Waste_Risk': strategy['Waste_Risk'],
            'Confidence': strategy['Confidence_Score']
        })
    return pd.DataFrame(results)


# ================================================================================
# ENTRY POINT
# ================================================================================

if __name__ == "__main__":
    models, processor, df = main()
