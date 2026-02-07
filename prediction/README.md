# Vaccine Management System — Frontend Guide

This folder contains an interactive Streamlit frontend for the Vaccine Management System (ML-powered supply chain optimizer).

## Frontend URL (default)
- Local (default): http://localhost:8501
- If you run the server binding to all interfaces, access from another machine at: http://<HOST_IP>:8501

> Note: The Streamlit server must be running to access the URL.

## Quick start — recommended (uses the project's virtual environment)
Open a terminal and run:

```bash
cd /home/akul/AllPractice/prediction

source /home/akul/AllPractice/.venv/bin/activat
/home/akul/AllPractice/.venv/bin/python -m pip install -r requirements.txt
/home/akul/AllPractice/.venv/bin/streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0
```

Streamlit will print a local URL (usually http://localhost:8501). Open that in your browser.

## Pages & How to Use
- **Home**: Overview and quick navigation buttons.
- **Strategy Predictor**: Manual or random sample inputs for an area.
  - Enter `Population`, `Age_Dist`, `Past_7_Days`, `Infection_Rate`, `Awareness`, `Power_Stability`, `Distance_from_Hub`.
  - Click **Generate Strategy** to see:
    - Predicted daily demand (doses)
    - Waste risk category (Low/Medium/High) and probabilities
    - Actionable recommendations and visualizations
- **Model Analysis**: View feature importance and model configuration.
- **Batch Processing**: Run strategy for multiple sampled areas and download results CSV.
- **Data Overview**: Preview synthetic dataset and distributions.

## Outputs (saved to this folder)
- `vaccine_data.csv` — synthetic dataset (if generated with save_to_csv=True)
- `feature_importance.png` — feature importance chart
- `model_performance.png` — model performance dashboard

## Stopping the server
- Press `Ctrl+C` in the terminal running Streamlit.

## Troubleshooting
- If Streamlit reports `ModuleNotFoundError` for any package, install the requirements:

```bash
/home/akul/AllPractice/.venv/bin/python -m pip install -r requirements.txt
```

- If the page does not load from another machine, ensure the server was started with `--server.address 0.0.0.0` and check firewall rules.

## Useful commands
- Run headless on a specific port:

```bash
/home/akul/AllPractice/.venv/bin/streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0
```

- Run using the Python executable directly (if streamlit CLI isn't available):

```bash
/home/akul/AllPractice/.venv/bin/python -m streamlit run streamlit_app.py
```

## Where to find code
- Frontend entry: `streamlit_app.py` (this file)
- ML pipeline and demo script: `vaccine_management_system.py`

If you want, I can start the server now and confirm the exact URL reachable from your machine (or change the port). Would you like me to start it?  

---
*README generated automatically.*



start comand
cd /home/akul/AllPractice/prediction
source /home/akul/AllPractice/.venv/bin/activate
/home/akul/AllPractice/.venv/bin/streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0