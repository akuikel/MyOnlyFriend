import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "AIzaSyDaZ12RxmXsnJLSiIN5u6HGNA_1d--IW7k"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("My girlfriend left me")
print(response.text)

