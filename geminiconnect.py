import google.generativeai as genai

# to generate the api key, login  to  https://aistudio.google.com/app/apikey
google_api_key = 'AIzaSyAINogrrbtIUVBJBH8787cRgw5Bno'
genai.configure(api_key=google_api_key)

# below code will print the available models names. for testing we use the gemini-pro model 
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

model =genai.GenerativeModel('gemini-pro')
response = model.generate_content("give me 5 points on the future of AI ?") 
print(response.text)  
