import google.generativeai as genai 

genai.configure(api_key="AIzaSyDYxUOBV8MEy5TyWrCNQzAxX09v6Bsg4l0")

for m in genai.list_models():
    print(m.name)