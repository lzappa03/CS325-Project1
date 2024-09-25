# CS325-Project1

<p>Written by Lorenzzi Zappa for class Software Engineering (CS325)<br>
September 25, 2024</p>

-----------

This program generates responses to given prompts from a textfile, then writes those responses to a separate textfile. The language model used is Microsoft Phi3-mini that runs through ollama.  

## How it works
* It starts with opening and reading an already made .txt file (*prompts.txt*) that has the prompts written in it already.
* The prompts are then put into a list, *prompt_list*. *Prompts.txt* is closed.
* The list is iterated through with one prompt going through the phi3 model, generating a response, then printing both the prompt and the response into another .txt file (*responses.txt*). Then *responses.txt* is closed after completing the list.
* **Extra Note:** *responses.txt* is appended to after each run. Clear *responses.txt* after each run if you only want one execution at a time on the file. 

## Requirements
* Ollama 0.3.11
* Phi3 mini
* python 3.12.5