import google.generativeai as genai


google_api_key = 'AIzaS12132342343453534543KN57cRgw5Bno'
genai.configure(api_key=google_api_key)

model =genai.GenerativeModel('gemini-pro')
response = model.generate_content("Write a java program to add 2 integers?") 
print(response.text)  
