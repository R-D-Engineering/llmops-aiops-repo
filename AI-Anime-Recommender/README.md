python pipeline/build_pipeline.py
pip install --upgrade langchain langchain-community langchain-text-splitters
streamlit run app/app.py
pip install -U langchain langchain-community langchain-core langchain-groq


pip uninstall langchain langchain-core langchain-community -y
pip install langchain==0.0.352 langchain-community==0.0.20 langchain-groq