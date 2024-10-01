import google.generativeai as genai
import os

api_key = "AIzaSyCm8A-ip22RQQA4Cabq8_oNIXuQnZjAbGU"
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(input("Enter the description: "))
print(response.text)


