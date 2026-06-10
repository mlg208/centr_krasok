import json
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

with open('info.json', 'r', encoding='utf-8') as f:
    info = json.load(f)

def get_answer(question):
    context = json.dumps(
        info,
        ensure_ascii=False,
        indent=2,
    )

    prompt = f"""
    Ты ai консультант компании.
    
    отвечай только по предоставленной базе знаний.
    
    если ответа в базе знаний нет - 
    ответь:
    'к сожалению, такой информации у меня нет.'
    или:
    данный вопрос был задан не про компанию.
    
    не придумывай информацию
    
    информация о компании:
    
    {context}
    
    Вопрос:
    {question}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content