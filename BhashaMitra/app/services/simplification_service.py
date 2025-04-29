from transformers import pipeline

simplifier = pipeline("text2text-generation", model="google/flan-t5-small")

def simplify_text(text):
    prompt = f"Simplify this: {text}"
    result = simplifier(prompt, max_length=512, do_sample=False)
    return result[0]['generated_text']