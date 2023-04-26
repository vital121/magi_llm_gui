# Magi LLM GUI
A Qt GUI for large language models

For Windows, Linux (and Mac?)

Currently works with https://github.com/oobabooga/text-generation-webui/ and https://github.com/ggerganov/llama.cpp

Uses https://github.com/abetlen/llama-cpp-python for llama.cpp support

Launch the WebUi with the ```--listen``` flag to enable the text-generation-webui API and add ```--no-stream``` if you don't want to use streaming mode.

Has been tested with commit 49aa05054ae13f381381440a9860ce0d68200e80 for text-generation-webui. 

To install (optionally create a virtual environment): 
```
git clone https://github.com/shinomakoi/magi_llm_gui
cd magi_llm_gui
pip install -r requirements.txt
```

Then to launch the Magi LLM GUI, use: 
```
python magi_llm_app.py
```
You can set the generation parameters in File > Parameters

![image](https://user-images.githubusercontent.com/112139428/234652796-6fe1c935-25f8-401c-b96e-ab4bbe825173.png)


Includes prompts from https://github.com/f/awesome-chatgpt-prompts
