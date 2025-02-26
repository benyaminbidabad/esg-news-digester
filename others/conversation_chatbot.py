from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.schema import AIMessage,SystemMessage,HumanMessage

load_dotenv()
model=ChatOpenAI(model="gpt-3.5-turbo")
chat_history=[]

system_message=SystemMessage(content="You are a ESG expert in the finance industry.")
chat_history.append(system_message)


while True:
    query=input("You: ")
    human_message=HumanMessage(content=query)
    if query.lower()=="exit":
        break
    chat_history.append(human_message)
    response=model.invoke(chat_history)
    print("System:",response.content)
    chat_history.append(AIMessage(content=response.content))

print("Chat Ended")
print(chat_history)