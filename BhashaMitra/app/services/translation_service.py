from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "ai4bharat/indictrans2-en-indic"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def translate_text(text, target_lang):
    lang_code = {"Marathi": "mr", "Tamil": "ta", "Bengali": "bn"}.get(target_lang, "mr")
    input_text = f"translate English to {lang_code}: {text}"
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(**inputs)
    translated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated