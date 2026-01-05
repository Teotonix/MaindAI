import gradio as gr
from transformers import pipeline
import torch
import requests
import io
from PIL import Image

# Yazı modeli
text_model = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16, device_map="auto")

# Görsel oluşturma fonksiyonu (Hugging Face üzerinden)
def generate_image(prompt):
    # Not: Bu kısım için ücretsiz bir API kullanacağız
    API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
    # Buraya kendi HF Token'ını eklemen gerekebilir, şimdilik basit tutalım
    response = requests.post(API_URL, json={"inputs": prompt})
    return Image.open(io.BytesIO(response.content))

def chat(message, history):
    if "resim çiz" in message.lower() or "görsel oluştur" in message.lower():
        prompt = message.replace("resim çiz", "").replace("görsel oluştur", "").strip()
        img = generate_image(prompt)
        return "İşte istediğin görsel: ", img # Gradio bunu otomatik işler
    
    # Normal sohbet kısmı (Eski kodun devamı)
    # ... (Önceki yazdığımız chat mantığı buraya gelecek)
