# doculoom-server

An LLM based contextual question answering chatbot

## Local setup

### Prerequisites to use local models (LLAMA/Mistral)

1. Install [Ollama](https://ollama.com/download/linux)
2. Start the server
3. Run ```ollama pull llama3.2```

### Prerequisites to use OpenAI models

1. Set openai env var 
```commandline
export OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
```
2. Set default model to LLAMA3_2_3B
```commandline
export MODEL=LLAMA3_2_3B
```

### Install dependencies

```bash
pip install poetry && poetry install --no-dev
```

### Start the server
```bash
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 6666
```


## Docker setup 

To run the server, follow these steps:

1. **Build the Docker Image**

   ```bash
   docker build -t doculoom .
   ```
   
2. **Start the server**

   ```bash
   docker run -it --rm -p 6666:6666 doculoom
   ```

