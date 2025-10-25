python3.12 -m venv venv
source venv/Scripts/activate
python -V
python.exe -m pip install --upgrade pip
pip install -e .

streamlit run app.py