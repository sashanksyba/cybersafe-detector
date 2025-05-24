import gradio as gr
from transformers import pipeline

classifier = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-sms-spam-detection")

def detect_spam(message):
    result = classifier(message)[0]
    label = result['label']
    score = result['score']
    
    if label.lower() == "spam":
        user_friendly_label = "Scam/Spam Message"
        tips = "Do NOT click on suspicious links or share personal info."
    else:
        user_friendly_label = "Safe / Legitimate Message"
        tips = "No warning. But always be cautious with unknown sources."

    explanation = f"""
**Result:** {user_friendly_label}
**Confidence:** {score:.2f}
**Model Prediction:** {label}

**Safety Tips:** {tips}
    """
    return explanation.strip()

iface = gr.Interface(
    fn=detect_spam,
    inputs=gr.Textbox(lines=4, placeholder="Paste a message or email"),
    outputs=gr.Markdown(),
    title="CyberSafe: Scam Message Detector",
    description="An AI-powered tool to help detect scam or spam messages. Built using Transformers and Gradio."
)

iface.launch()