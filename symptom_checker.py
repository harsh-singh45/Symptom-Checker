import requests
import gradio as gr

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def analyze_symptoms(symptoms):
    if not symptoms or len(symptoms.strip()) < 3:
        return "⚠️ Please enter valid symptoms to analyze."

    prompt = f"Analyze the following symptoms and suggest possible health conditions:\n\nSymptoms: {symptoms}\n\n" \
             "Provide a short list of possible causes and general advice (no treatment recommendations)."
    
    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json().get("response", "No information available.")
    except requests.exceptions.RequestException as e:
        return f"❌ Request failed: {str(e)}"

# Gradio UI
with gr.Blocks(theme=gr.themes.Base(), css=".gr-textbox { font-size: 16px; }") as interface:
    gr.Markdown("## 🩺 AI Medical Symptom Checker")
    gr.Markdown(
        "Enter your symptoms below and let the AI suggest **possible health conditions** and **general advice**.\n\n"
        "⚠️ This tool is for informational purposes only and **not a replacement** for professional medical advice."
    )

    with gr.Row():
        with gr.Column(scale=2):
            symptoms_input = gr.Textbox(
                label="Enter Symptoms",
                placeholder="E.g., fever, headache, sore throat, fatigue",
                lines=4,
                max_lines=6
            )
            submit_btn = gr.Button("🔍 Analyze Symptoms", variant="primary")

        with gr.Column(scale=3):
            result_output = gr.Textbox(
                label="Possible Conditions and Advice",
                lines=10,
                max_lines=20,
                interactive=False,
                show_copy_button=True
            )

    examples = gr.Examples(
        examples=[
            ["fever, sore throat, body ache"],
            ["headache, blurred vision, nausea"],
            ["cough, fatigue, chest pain"]
        ],
        inputs=[symptoms_input],
    )

    submit_btn.click(fn=analyze_symptoms, inputs=[symptoms_input], outputs=[result_output])

# Launch app
if __name__ == "__main__":
    interface.launch()
