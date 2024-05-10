import polars as pl
from enum import Enum

# *dtypes* dictionary is used for casting the data types of columns when reading the original CSV file
dtypes = {
    'progressed': pl.Categorical,
    'size': pl.Float32,
    'PDI': pl.Float32,
    'API_prop': pl.Float32,
    'API_mol_wt': pl.Float32,
    'logp_chemaxon': pl.Float32,
    'API_melt_temp': pl.Float32,
    'API_water_sol': pl.Float32,
    'API_polar_sa': pl.Float32,
    'API_rot_bond': pl.Float32,
    'API_H_bond_donor': pl.Float32,
    'API_H_bond_accept': pl.Float32,
    'oil_total': pl.Float32,
    'o_num': pl.Float32,
    'o_LC': pl.Categorical,
    'o_sat': pl.Categorical,
    'surfactant_total': pl.Float32,
    's_num': pl.Float32,
    's_HLB': pl.Float32,
    'cosolvent_total': pl.Float32,
    'c_num': pl.Float32,
    'c_mol_wt': pl.Float32,
    'c_melt_temp': pl.Float32,
    'c_boil_temp': pl.Float32,
    'c_density': pl.Float32,
    'c_viscosity': pl.Float32,
    'other_total': pl.Float32,
    'other_num': pl.Float32,
    'cplx_minmax_norm': pl.Float32
}

# Drug related features
drug_features = [
    'API_prop', 'API_mol_wt', 'logp_chemaxon', 'API_melt_temp', 'API_water_sol', 
    'API_polar_sa', 'API_rot_bond', 'API_H_bond_donor', 'API_H_bond_accept'
]

# Oil related features
oil_features = [
    'oil_total', 'o_num', 'o_LC', 'o_sat'
]

# Surfactant related features
surfactant_features = [
    'surfactant_total', 's_num', 's_HLB'
]

# Cosolvent related features
cosolvent_features = [
    'cosolvent_total', 'c_num', 'c_mol_wt', 'c_melt_temp', 
    'c_boil_temp', 'c_density', 'c_viscosity'
]

# Other ingredient related features
other_ingredient_features = [
    'other_total', 'other_num'
]

# SEDDS related features
sedds_features = [
    'size', 'PDI', 'cplx_minmax_norm', 'progressed'
]

# Each category corresponds to a specific group of features related to the formulation components in sedds dataset
class FeatureCategory(Enum):
    DRUG = drug_features
    OIL = oil_features
    SURFACTANT = surfactant_features
    COSOLVENT = cosolvent_features
    OTHER_INGREDIENT = other_ingredient_features
    SEDDS = sedds_features



