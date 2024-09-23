#import ollama

try:
    with open('prompts.txt', 'r', encoding="utf8") as prompts: #opens and reads textfile with prompts
        prompt_list = [line.rstrip('\n') for line in prompts] #puts prompts into list
        print(prompt_list)
except FileNotFoundError:
    print("file not found")



#generates a response with given prompt denoted as 'prompt'
#response = ollama.generate(model='phi3', prompt='create a short story about two birds that fall in love please')
#print(response)