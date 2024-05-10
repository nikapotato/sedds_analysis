## Setup Requirements

1. **Docker**: Verify that Docker is installed on your local machine

2. **Poetry**: This project uses Poetry for Python dependency management

## Installation and Running the Project

### Running the Docker Container with the API

To run the Docker container which hosts the API, use the following command:
```
docker-compose up
```

then this should work ;)

http://0.0.0.0/docs

## Examples of request body

Here we are presenting examples of real data.

### POST /predict/formulation_content_recommendation

```
{"API_mol_wt":435.5190124512,"logp_chemaxon":5.2699999809,"API_melt_temp":116.5,"API_water_sol":0.0233999994,"API_polar_sa":112.0699996948,"API_rot_bond":10.0,"API_H_bond_donor":2.0,"API_H_bond_accept":6.0,"o_LC":"0","o_sat":"0","s_HLB":14.3999996185,"c_mol_wt":0.0,"c_melt_temp":0.0,"c_boil_temp":0.0,"c_density":0.0,"c_viscosity":0.0}

{"API_mol_wt":853.9060058594,"logp_chemaxon":3.5399999619,"API_melt_temp":216.5,"API_water_sol":0.00557,"API_polar_sa":221.2899932861,"API_rot_bond":14.0,"API_H_bond_donor":4.0,"API_H_bond_accept":10.0,"o_LC":"0","o_sat":"1","s_HLB":13.5,"c_mol_wt":400.0,"c_melt_temp":6.0,"c_boil_temp":250.0,"c_density":1.1000000238,"c_viscosity":90.0}
```

###  POST /predict/progressed

```
{"API_prop":19.0499992371,"oil_total":42.8600006104,"surfactant_total":38.0999984741,"cosolvent_total":0.0,"other_total":0.0,"o_num":1.0,"s_num":2.0,"c_num":0.0,"other_num":0.0,"API_mol_wt":314.4700012207,"logp_chemaxon":6.3299999237,"API_melt_temp":67.0,"API_water_sol":0.0126,"API_polar_sa":40.4599990845,"API_rot_bond":6.0,"API_H_bond_donor":2.0,"API_H_bond_accept":2.0,"o_LC":"0","o_sat":"1","s_HLB":11.5,"c_mol_wt":0.0,"c_melt_temp":0.0,"c_boil_temp":0.0,"c_density":0.0,"c_viscosity":0.0}

{"API_prop":10.0,"oil_total":18.0,"surfactant_total":54.0,"cosolvent_total":18.0,"other_total":0.0,"o_num":1.0,"s_num":1.0,"c_num":1.0,"other_num":0.0,"API_mol_wt":314.4700012207,"logp_chemaxon":6.3299999237,"API_melt_temp":67.0,"API_water_sol":0.0126,"API_polar_sa":40.4599990845,"API_rot_bond":6.0,"API_H_bond_donor":2.0,"API_H_bond_accept":2.0,"o_LC":"0","o_sat":"1","s_HLB":12.3999996185,"c_mol_wt":76.0999984741,"c_melt_temp":-59.0,"c_boil_temp":188.1999969482,"c_density":1.0,"c_viscosity":56.0}

{"API_prop":7.5,"oil_total":10.8000001907,"surfactant_total":58.5,"cosolvent_total":20.7000007629,"other_total":2.5,"o_num":1.0,"s_num":4.0,"c_num":1.0,"other_num":1.0,"API_mol_wt":314.4700012207,"logp_chemaxon":6.3299999237,"API_melt_temp":67.0,"API_water_sol":0.0126,"API_polar_sa":40.4599990845,"API_rot_bond":6.0,"API_H_bond_donor":2.0,"API_H_bond_accept":2.0,"o_LC":"1","o_sat":"0","s_HLB":11.5,"c_mol_wt":46.0999984741,"c_melt_temp":-114.0999984741,"c_boil_temp":78.4000015259,"c_density":0.8000000119,"c_viscosity":1.1000000238}
```

First two examples should not progress.


### Installing Dependencies for running jupyter notebooks
They are necessary for running the the notebooks with data analysis and experiments. To install these dependencies, run the command from project root
:

```
poetry install
```

python 3.12 is required 


## Project Structure

   - `src`: The application's source code.
   - `models`: Files containing stored models.
   - `notebooks`: Jupyter Notebooks for tasks such as data preprocessing, exploratory analysis and model training.
   - `other configuration files`

### API Documentation

The API documentation is automatically generated using OpenAPI. 

### TODO
There is a lot of other task which we can do in longer timeframe, such as:

- More advanced feature engineering based on better domain knowledge.
- Analysis based on concrete drug used in SEDDS formulation.
- dode refactoring and optimization
- proper docker-compose
- optimal combination of excipients
- outliers
- etc.  