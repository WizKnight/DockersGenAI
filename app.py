from fastapi import FastAPI
from transformers import pipeline

## Create new FASTAPI app instance
app = FASTAPI()

## Initialize text generation pipeline
pipe = pipeline("text2text-generation", model="google/flan-t5-small")


@app.get("/")
def home():
    return {"message": "Hello User!"}

## Define a function to handle the GET request as '/generate'

@app.get('/generate')
def generate(text:str):
    ## Use the pipeline to generate text from given input text
    output = pipe(text)
    
    ## return the generated text in json response
    return {"output":output[0]['generated_text']}