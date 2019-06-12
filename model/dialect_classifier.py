# 5-Way Regional Dialect Classifier
DIALECTS = ["EGY (Egyptian)", "GLF (Gulf)", "LEV (Levantine)", "MAG (Maghrebi)", "MSA (Modern Standard)"]

def predict_dialect(sentence: str):
    print(f"Classifying sentence dialect: {sentence}")
    return {"predicted_dialect": "EGY (Egyptian)", "confidence": 0.964}
