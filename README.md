# KI-storyline chatbot demo

### Download
```bash
git clone git@github.com:smaeland/ki-storyline.git
cd ki-storyline
```

### Set up environment
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Add OpenAI API key

First create a key at https://platform.openai.com/api-keys, and then make it
available to our app by writing it to `.streamlit/secrets.toml`

```bash
echo OPENAI_API_KEY = \"<my-secret-key>\" > .streamlit/secrets.toml
```

### Run locally
```bash
streamlit run Hjem.py
```

