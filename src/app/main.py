from fastapi import FastAPI, HTTPException
from modules.utils import load_model, data_utils
from modules.types import constants_api
import polars as pl

app = FastAPI()
model_progressed = load_model.load_progressed_model
model_recommendations = load_model.load_recommendation_model

# can be extended to log the error in a log file, moved to another file
raise_exception = lambda e: HTTPException(status_code=500, detail=str(e))

@app.post("/predict/progressed")
async def predict_progressed(data: constants_api.APIDataProgressed):
    X = data_utils.preprocess_progressed_data(data)

    try:
        y_hat = model_progressed.predict(X)
        y_hat = pl.from_numpy(y_hat, schema=constants_api.progressed_target)

        progressed_value = y_hat.select('progressed')[0].item()
    except Exception as e:
        raise raise_exception(e)

    return "This formulation will progress." if progressed_value == '1' else "This formulation will not progress."    

@app.post("/predict/formulation_content_recommendation")
async def predict_formulation_recommendations(data: constants_api.APIDataRecommendation):
    X = data_utils.preprocess_recommendation_data(data)
 
    try:
        y_hat = model_recommendations.predict(X)
        y_hat = pl.from_numpy(y_hat, schema=constants_api.multi_target)

        return {
            "oil_total_required (% w/w)": y_hat.get_column('oil_total')[0],
            "other_total_required (% w/w)": y_hat.get_column('other_total')[0],
            "surfactant_total_required (% w/w)": y_hat.get_column('surfactant_total')[0],
            "cosolvent_total_required (% w/w)": y_hat.get_column('cosolvent_total')[0],
            "API_prop_required (% w/w)": y_hat.get_column('API_prop')[0],
        }
    except Exception as e:
        raise raise_exception(e)
