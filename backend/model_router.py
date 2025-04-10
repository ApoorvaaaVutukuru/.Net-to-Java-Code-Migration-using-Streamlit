from backend.mistral7b import convert_with_mistral_7b
from backend.mistrallarge2 import convert_with_mistral_large2
from backend.codegen2 import convert_with_codegen2

def route_model_conversion(model_name, cs_code):
    if "Mistral-7B" in model_name:
        return convert_with_mistral_7b(cs_code)
    elif "Mixtral" in model_name:
        return convert_with_mistral_large2(cs_code)
    elif "codegen2" in model_name:
        return convert_with_codegen2(cs_code)
    else:
        return "Unsupported model selected."
