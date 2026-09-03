from langgraph.graph import StateGraph ,START,END
from langchain_openai import ChatOpenAI
from typing import TypedDict,Annotated,Literal
from dotenv import load_dotenv
from pydantic import BaseModel,Field
import operator
from langchain_core.messages import SystemMessage, HumanMessage,BaseMessage
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

CONFIG={'configurable':{'thread_id':'thread-1'}}

load_dotenv()

from langgraph.graph.message import add_messages
class ChatState(TypedDict):
  message:Annotated[list[BaseMessage],add_messages]
llm=ChatOpenAI()

def chat_node(state: ChatState):
  #take user query from state 
  message=state['message']
  #send to llm 
  response=llm.invoke(message)
  #resoponse store in state
  return {'message':[response]}

conn=sqlite3.connect('chatboat.db',check_same_thread=False)  # Connect to the SQLite database (or create it if it doesn't exist)

#checkpointer
checkpointer=SqliteSaver(conn=conn)

graph=StateGraph(ChatState)
#node
graph.add_node('chat_node',chat_node)
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)
chatboat = graph.compile(checkpointer=checkpointer)


def get_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])
    return all_threads

print("Backend imported")