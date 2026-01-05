import gradio as gr

# Dünyanın en hızlı modellerinden biri: SDXL Turbo
# 1 ile 4 adım arasında görseli tamamlar.
model_id = "stabilityai/sdxl-turbo"

# Gradio arayüzünü doğrudan modelden yükle
# "Direct Inference" kullanarak en yüksek hıza ulaşıyoruz
interface = gr.load(
    name=f"models/{model_id}",
    title="Maind AI Studio | Hızlı Görsel Oluşturucu",
    description="Hayalindeki görseli İngilizce olarak tarif et, saniyeler içinde çizelim.",
    theme="finesse" # Modern ve temiz bir tema
)

if __name__ == "__main__":
    # Sıraya alma (Queue) sistemini açıyoruz ki yoğunlukta çökmesin
    interface.queue().launch(show_api=False)
