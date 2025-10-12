from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from app.config.config import HF_TOKEN, HUGGINGFACE_REPO_ID
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def load_llm(huggingface_repo_id: str = HUGGINGFACE_REPO_ID, hf_token: str = HF_TOKEN):
    """
    Loads a chat-based LLM from Hugging Face (supports conversational models like Mistral-7B).
    """
    try:
        logger.info("Loading LLM from HuggingFace (Chat Mode)")

        # Step 1: Initialize HuggingFaceEndpoint with explicit parameters
        hf_llm = HuggingFaceEndpoint(
            repo_id=huggingface_repo_id,
            huggingfacehub_api_token=hf_token,
            temperature=0.3,
            max_new_tokens=256,
            return_full_text=False
        )

        # Step 2: Wrap it in ChatHuggingFace for chat capabilities
        llm = ChatHuggingFace(llm=hf_llm)

        logger.info("LLM loaded successfully (chat model)")
        return llm

    except Exception as e:
        error_message = CustomException("Failed to load LLM", e)
        logger.error(str(error_message))
        raise
