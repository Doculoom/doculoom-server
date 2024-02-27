# doculoom-server

An LLM based contextual question answering chatbot

## Local setup

### Prerequisites to use local models (Mistral)

1. Install [Ollama](https://ollama.com/download/linux)
2. Start the server
3. Run ```ollama pull mistral```

### Prerequisites to use OpenAI models

1. Set openai env var 
```commandline
export OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
```
2. Set default model to GPT3_5
```commandline
export MODEL=GPT3_5
```

### Install dependencies

```bash
pip install poetry && poetry install --no-dev
```

### Start the server
```bash
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 6666
```


## Docker setup (WIP: for local models)

To run the server, follow these steps:

1. **Build the Docker Image**

   ```bash
   docker build --build-arg OPENAI_API_KEY=<YOUR_OPENAI_API_KEY> -t doculoom .
   ```
   
2. **Start the server**

   ```bash
   docker run -p 6666:6666 doculoom
   ```

