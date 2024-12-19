class Models:
    GPT3_5  =       {'id': 1, 'name': 'gpt-3.5-turbo'}
    MISTRAL =       {'id': 2, 'name': 'mistral'      }
    QWEN7B  =       {'id': 3, 'name': 'qwen:7b'      }
    PHI     =       {'id': 4, 'name': 'phi:chat'     }
    GEMMA   =       {'id': 5, 'name': 'gemma'        }
    LLAMA3_2_3B   = {'id': 5, 'name': 'llama3.2'     }


class Prompts:
    RETRIEVER_PROMPT = ("Given the above conversation, generate a search query to look up in order"
                        "to get information relevant to the conversation, its okay say that you dont know")

    INITIAL_PROMPT = ("Answer the user's questions based on the context => {context}"
                      "otherwise use your knowledge, answer straight to the point")

