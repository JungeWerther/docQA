# DocQA

Simple docker container that exposes a gradio interface for automatic invoice processing, using docQuery.

Simply pull the repo and run `docker compose up -d`

Alternatively `pip install -r requirements.txt` and `python src/main.py` (make sure you have tesseract-ocr and poppler-utils installed) 

A Gradio interface will be running on localhost:7860.

On the first run it should take about 30s to pull the model. After that inference takes about ~1s (on a 3090 GPU).
