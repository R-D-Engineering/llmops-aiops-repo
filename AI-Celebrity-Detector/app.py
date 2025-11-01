from app import create_app
from dotenv import load_dotenv

if __name__=="__main__":
    load_dotenv()
    app = create_app()
    print("MAX_CONTENT_LENGTH =", app.config['MAX_CONTENT_LENGTH'])
    app.run(host="0.0.0.0" , port=5000 , debug=True)