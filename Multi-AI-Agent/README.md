https://github.com/data-guru0/MULTI-AI-AGENT-PROJECTS


python3.12 -m venv venv

source venv/Scripts/activate

python -V

pip install -e .



python app/main.py

update the package for backend
pip install -U langchain-tavily

pip uninstall langchain-community -y
pip install -U langchain-tavily

pip install -U langchain langchain-tavily langchain-openai