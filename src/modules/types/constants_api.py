import polars as pl
from pydantic import BaseModel, Field

# Used for constructing Polars dataframes from the output of the model.
progressed_schema = {
    'API_prop': pl.Float32,
    'oil_total': pl.Float32,
    'surfactant_total': pl.Float32,
    'cosolvent_total': pl.Float32,
    'other_total': pl.Float32,
    'o_num': pl.Float32,
    's_num': pl.Float32,
    'c_num': pl.Float32,
    'other_num': pl.Float32,
    'API_mol_wt': pl.Float32,
    'logp_chemaxon': pl.Float32,
    'API_melt_temp': pl.Float32,
    'API_water_sol': pl.Float32,
    'API_polar_sa': pl.Float32,
    'API_rot_bond': pl.Float32,
    'API_H_bond_donor': pl.Float32,
    'API_H_bond_accept': pl.Float32,
    'o_LC': pl.Categorical,
    'o_sat': pl.Categorical,
    's_HLB': pl.Float32,
    'c_mol_wt': pl.Float32,
    'c_melt_temp': pl.Float32,
    'c_boil_temp': pl.Float32,
    'c_density': pl.Float32,
    'c_viscosity': pl.Float32,
}
recommendation_schema = {
    'API_mol_wt': pl.Float32,
    'logp_chemaxon': pl.Float32,
    'API_melt_temp': pl.Float32,
    'API_water_sol': pl.Float32,
    'API_polar_sa': pl.Float32,
    'API_rot_bond': pl.Float32,
    'API_H_bond_donor': pl.Float32,
    'API_H_bond_accept': pl.Float32,
    'o_LC': pl.Categorical,
    'o_sat': pl.Categorical,
    's_HLB': pl.Float32,
    'c_mol_wt': pl.Float32,
    'c_melt_temp': pl.Float32,
    'c_boil_temp': pl.Float32,
    'c_density': pl.Float32,
    'c_viscosity': pl.Float32,
}

# The classes `APIDataProgressed` and `APIDataRecommendation` inherit from Pydantic's `BaseModel`, which
# provides automatic data validation, serialization, and documentation generation. These classes are used
# to define the structure of data for progressed and recommendation APIs.
class APIDataProgressed(BaseModel):
    API_prop: float = Field(..., description="Property of the API")
    oil_total: float = Field(..., description="Total oil content")
    surfactant_total: float = Field(..., description="Total amount of surfactant")
    cosolvent_total: float = Field(..., description="Total amount of cosolvent")
    other_total: float = Field(..., description="Total amount of other components")
    o_num: float = Field(..., description="Number associated with oil")
    s_num: float = Field(..., description="Number associated with surfactant")
    c_num: float = Field(..., description="Number associated with cosolvent")
    other_num: float = Field(..., description="Number associated with other components")
    API_mol_wt: float = Field(..., description="Molecular weight of the API")
    logp_chemaxon: float = Field(..., description="LogP value from ChemAxon")
    API_melt_temp: float = Field(..., description="Melting temperature of the API")
    API_water_sol: float = Field(..., description="Water solubility of the API")
    API_polar_sa: float = Field(..., description="Polar surface area of the API")
    API_rot_bond: float = Field(..., description="Number of rotatable bonds in the API")
    API_H_bond_donor: float = Field(..., description="Number of hydrogen bond donors in the API")
    API_H_bond_accept: float = Field(..., description="Number of hydrogen bond acceptors in the API")
    o_LC: str = Field(..., description="Liquid crystal property of oil")
    o_sat: str = Field(..., description="Saturation level of oil")
    s_HLB: float = Field(..., description="Hydrophilic-lipophilic balance of surfactant")
    c_mol_wt: float = Field(..., description="Molecular weight of cosolvent")
    c_melt_temp: float = Field(..., description="Melting temperature of cosolvent")
    c_boil_temp: float = Field(..., description="Boiling temperature of cosolvent")
    c_density: float = Field(..., description="Density of cosolvent")
    c_viscosity: float = Field(..., description="Viscosity of cosolvent")

class APIDataRecommendation(BaseModel):
    API_mol_wt: float = Field(..., description="Molecular weight of the API")
    logp_chemaxon: float = Field(..., description="LogP value from ChemAxon")
    API_melt_temp: float = Field(..., description="Melting temperature of the API")
    API_water_sol: float = Field(..., description="Water solubility of the API")
    API_polar_sa: float = Field(..., description="Polar surface area of the API")
    API_rot_bond: float = Field(..., description="Number of rotatable bonds in the API")
    API_H_bond_donor: float = Field(..., description="Number of hydrogen bond donors in the API")
    API_H_bond_accept: float = Field(..., description="Number of hydrogen bond acceptors in the API")
    o_LC: str = Field(..., description="Liquid crystal property of oil")
    o_sat: str = Field(..., description="Saturation level of oil")
    s_HLB: float = Field(..., description="Hydrophilic-lipophilic balance of surfactant")
    c_mol_wt: float = Field(..., description="Molecular weight of cosolvent")
    c_melt_temp: float = Field(..., description="Melting temperature of cosolvent")
    c_boil_temp: float = Field(..., description="Boiling temperature of cosolvent")
    c_density: float = Field(..., description="Density of cosolvent")
    c_viscosity: float = Field(..., description="Viscosity of cosolvent")

# Used for constructing Polars dataframes from the output of the model.
multi_target = ['oil_total', 'other_total', 'surfactant_total', 'cosolvent_total', 'API_prop']
progressed_target = ['progressed']