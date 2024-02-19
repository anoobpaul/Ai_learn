import google.generativeai as genai
from IPython.display import Markdown
import textwrap

# to generate the api key, login  to  https://aistudio.google.com/app/apikey
google_api_key = 'AIzaSyrerGHJBI8678687jbKJB7cRgw5Bno'
genai.configure(api_key=google_api_key)


# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '', predicate=lambda _: True))



model =genai.GenerativeModel('gemini-pro')
response = model.generate_content("where is banglore ?") 

print(response.text)

markdown_text  = to_markdown(response.text)
print(markdown_text.data)

