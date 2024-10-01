from yaml import safe_load

API_KEY = "LWqc9zRcUXiCO7uPPYmslu26O0jJsb46"
TEXT_MODEL = "mistral-large-latest"
IMAGE_TO_TEXT_MODEL = "pixtral-12b-2409"


with open("llmmodel/promts/prompts.yaml", encoding="utf-8") as f:
    prompts = safe_load(f)


MAIN_SYSTEM_PROMPT = prompts["main_system_prompt"]
MAIN_CONTEXT_PROMPT = prompts["main_context_prompt"]
IMAGE_TO_TEXT_CONTEXT_PROMPT = prompts["image_to_text_context_prompt"]
