import ollama

try:
    with open('prompts.txt', 'r', encoding="utf8") as prompts: #opens and reads textfile with prompts
        prompt_list = [line.rstrip('\n') for line in prompts] #puts prompts into list
        #print(prompt_list)
except FileNotFoundError:
    print("file not found")


for p in prompt_list:
    response = ollama.generate(model='phi3', prompt=p) #generates a response with given prompt denoted as 'p'
    with open('responses.txt', 'a', encoding="utf8") as output:
        #prints prompt and response to response.txt
        output.write(p) 
        output.write("\n")
        output.write(response['response'])
        output.write("\n\n")


