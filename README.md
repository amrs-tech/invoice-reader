# Invoice Reader with Small VLM
Basic Web application setup with Flask and Small Vision Language Model
It is a very straight-forward technique of a web app with a file upload, after submitting the VLM inference is called to parse the image file and describe it.

## Tools & Libraries
- Python 3.10
- Flask==3.0.3
- torch==2.6.0
- transformers
- pillow==11.1.0
- python-docx==1.1.2

## Model
SmolVLM-500M-Instruct model by HuggingfaceTB is used for inferring, as it is an Image+Text to Text small language model. 
The model size is approximtely around 1.1GB and it is downloaded only once.

NOTE : This is a basic setup for the image parsing using VLM. It can be improved further more.
