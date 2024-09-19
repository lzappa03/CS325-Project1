import ollama

response = ollama.generate(model='phi3', prompt='create a short story about two birds that fall in love please')
print(response)