import openai

openai.api_key = "your-openai-api-key"

def ask_chatbot(question, context):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a helpful tutor."},
            {"role": "user", "content": f"Context: {context}\nQuestion: {question}"}
        ]
    )
    return response['choices'][0]['message']['content']