# doculoom-server

An LLM based contextual question answering chatbot

## Local setup

To run the server, follow these steps:

1. **Build the Docker Image**

   ```bash
   docker build -t doculoom .
   ```
   
2. **Start the server**

   ```bash
   docker run -p 6666:6666 doculoom-server

