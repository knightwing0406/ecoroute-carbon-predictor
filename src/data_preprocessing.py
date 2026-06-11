"""
EcoRoute Production Telemetry Preprocessing Module
Design Architecture: Leak-proof, isolated pipeline transformation blocks.
"""

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder, TargetEncoder
from sklearn.impute import SimpleImputer

def build_production_preprocessor(num_features, low_card_cat, high_card_cat):
    """
    Constructs and returns an isolated data transformation transformer assembly
    to prevent data leakage during cross-validation training cycles.
    """
    # Numerical processing pipeline
    num_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    # Low-cardinality categorical configuration
    low_cat_transformer = Pipeline([
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])
    
    # High-cardinality categorical processing (Target Bayesian smoothing)
    high_cat_transformer = Pipeline([
        ('target_enc', TargetEncoder(smooth="auto", random_state=42))
    ])
    
    # Bundle transformations into unified mapping operator
    preprocessor = ColumnTransformer(transformers=[
        ('num', num_transformer, num_features),
        ('low_cat', low_cat_transformer, low_card_cat),
        ('high_cat', high_cat_transformer, high_card_cat)
    ])
    
    return preprocessor
