class Models:
    GPT3_5 = {'id': 1, 'name': 'gpt-3.5-turbo'}
    MISTRAL = {'id': 2, 'name': 'mistral'}


class Prompts:
    RETRIEVER_PROMPT = ("Given the above conversation, generate a search query to look up in order"
                        "to get information relevant to the conversation, its okay say that you dont know")

    INITIAL_PROMPT = ("Answer the user's questions based on the context: {context} if there is any"
                      "otherwise use your knowledge and do not prepend AI to your answers, answer straight to the "
                      "point")

