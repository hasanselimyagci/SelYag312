from fastapi import FastAPI
import uvicorn
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


# Declaring our FastAPI instance
app = FastAPI()

tokenizer = AutoTokenizer.from_pretrained("bert-base-german-dbmdz-uncased")
model = AutoModelForSequenceClassification.from_pretrained("selimyagci/germanPhraseClassifier")

@app.post('/predict')
def predict(text: str):
    input = tokenizer(text, return_tensors='pt')
    logits = model(**input).logits
    predicted_class_id = logits.argmax().item()
    return {'class' : predicted_class_id}


# Defining path operation for root endpoint
@app.get('/')
def main():
    return {'message': 'Welcome to german phrase classifier'}
