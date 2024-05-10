import polars as pl
import polars.selectors as cs
from io import StringIO

from modules.types.constants_sedds import dtypes
from modules.types.constants_api import progressed_schema, recommendation_schema, APIDataProgressed, APIDataRecommendation

def load_data(path: str = '../../data/sedds_df.csv', dtypes: dict = dtypes) -> pl.DataFrame:
    data = (pl.read_csv(path, dtypes = dtypes, null_values = ['NA'])
              .drop('index')
            )
    return data


def preprocess_progressed_data(data: APIDataProgressed) -> pl.DataFrame:
    # Get dictionary representation of the data
    data_serializable = data.model_dump()
    X = pl.DataFrame(data_serializable, schema=progressed_schema)
    
    # Add new feature to the data
    X = X.with_columns([
        (pl.col("API_water_sol") * pl.col("oil_total") + 
         pl.col("API_water_sol") * pl.col("surfactant_total") * pl.col("s_HLB") +
         pl.col("API_water_sol") * pl.col("cosolvent_total")).alias("solubility_impact")
    ])

    # we need data in padas format to use it in the model
    return X.to_pandas()

def preprocess_recommendation_data(data: APIDataRecommendation) -> pl.DataFrame:
    # Get dictionary representation of the data
    data_serializable = data.model_dump()
    X = pl.DataFrame(data_serializable, schema=recommendation_schema)

    # # Add new feature to the data
    X = X.with_columns([
            (pl.col('API_water_sol') * pl.col('API_mol_wt') * pl.col('c_density') * pl.col('c_mol_wt')).alias('API_molwt_c_density_interaction'), 
            (pl.col('API_melt_temp') * pl.col('API_water_sol') / pl.col('API_polar_sa')).alias('melt_sol_polar_ratio')
        ])

    # we need data in padas format to use it in the model
    return X.to_pandas()