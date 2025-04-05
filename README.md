# 🩺 AI Medical Symptom Checker

A lightweight and intuitive web application that allows users to input their symptoms and get AI-generated suggestions for **possible health conditions** and **general advice** using the **DeepSeek language model**. Built with **Gradio** for a user-friendly interface.

> ⚠️ **Disclaimer:** This tool is for informational purposes only. It is **not a substitute** for professional medical advice, diagnosis, or treatment.

---

## 🚀 Features

- Accepts free-text symptom input.
- Uses DeepSeek AI (via Ollama) to analyze symptoms.
- Displays possible conditions and general health advice.
- Clean, responsive Gradio interface.
- Includes example inputs for ease of use.

---

## 🛠️ Requirements

Before running the project, make sure the following are installed:

- Python 3.8+
- pip
- [Ollama](https://ollama.com/) (for running DeepSeek model locally)

---

## 📦 Installation

Follow these steps to run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-medical-symptom-checker.git
cd ai-medical-symptom-checker
```
### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```
### 3. Install Python Dependencies

You can also install manually:
```bash
pip install requests gradio
```


🤖 Setup DeepSeek Model with Ollama
1. Install Ollama
Download and install Ollama from the official site.

2. Pull the DeepSeek Model
Open a terminal and run:
```bash
ollama pull deepseek
```

3. Start the Ollama Server
Make sure the Ollama server is running. You can do this by simply running:
```bash
ollama run deepseek
```
The app connects to the local Ollama API at: http://localhost:11434/api/generate

▶️ Run the App
Once dependencies are installed and the Ollama server is running:
```bash
python symptom_checker.py
```

This will launch a Gradio web interface in your browser, usually at:http://127.0.0.1:7860


🧪 Example Inputs
You can try the following example symptoms to test:

fever, sore throat, body ache

headache, blurred vision, nausea

cough, fatigue, chest pain



![Screenshot 2025-04-05 232201](https://github.com/user-attachments/assets/1d1c7649-6292-431e-b47b-fa687706373c)



![Screenshot 2025-04-05 232121](https://github.com/user-attachments/assets/8527e86b-8a55-4b98-b6f7-3dc92e2bbf56)



🙋‍♂️ Author
Developed by Harsh
B.Tech Student, Parul University, Vadodara, Gujarat
