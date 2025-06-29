
# Bias Buster — AI Response Checker

Deployed app : https://bias-buster-usckahxdmvqz7cpph7crvy.streamlit.app/
Bias Buster is a web app that analyzes AI-generated responses to detect potential bias or toxicity and suggests a more neutral rewrite. It is built with Streamlit and powered by Google Gemini (Generative AI API).

## Features

- Analyze text for bias or toxic language
- Get an explanation of the bias detected
- Receive a rewritten, more neutral version
- Fun facts about AI and bias
- Modern UI with animated background and Lottie illustrations

## Technologies Used

- Python 3
- [Streamlit](https://streamlit.io)
- Google Generative AI (Gemini)
- streamlit-lottie (for animations)
- tsParticles.js (for animated background)
- HTML + CSS for UI customization

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/AsmiSharma017/bias-buster.git
cd bias-buster
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your Gemini API Key

You can either:

* **Option 1**: Hardcode it in `app.py` (for quick testing):

  ```python
  genai.configure(api_key="your_api_key_here")
  ```

* **Option 2 (Recommended)**: Add it securely using `.streamlit/secrets.toml`

Create a file at:

```
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

Then use in code:

```python
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
```

### 5. Run the App

```bash
streamlit run app.py
```

Visit: [http://localhost:8501](http://localhost:8501)

## Deployment

This app can be deployed on:

* **[Streamlit Cloud](https://streamlit.io/cloud)** (Free hosting)
* Vercel (with custom configuration)
* Localhost or your own server

Make sure to securely store your API key using secrets management.

## License

This project is for educational and research purposes only. Use responsibly.


