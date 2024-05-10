import pickle

model_path_progressed: str = 'models/progressed_model.pkl'
model_path_recommendation: str = 'models/multi_output_model.pkl'

def load_model(model_path: str=model_path_progressed):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    return model


load_progressed_model = load_model(model_path_progressed)
load_recommendation_model = load_model(model_path_recommendation)