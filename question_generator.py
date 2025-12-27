from transformers import pipeline

def generate_questions(text):
    question_generator = pipeline("text2text-generation", model="valhalla/t5-base-qg-hl")
    return [question_generator(text)[0]['generated_text']]