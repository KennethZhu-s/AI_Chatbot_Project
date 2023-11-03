import sys, os
import json
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits.csv.base import create_csv_agent



bot_name = "Sam"

# Create a new csv agent
tmp_file_path = 'data/meta_data_sample.csv'
agent_gpt = create_csv_agent(
        ChatOpenAI(temperature=0,
                   model="gpt-3.5-turbo-0613",
                   request_timeout=120,
                   openai_api_key='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'),
        tmp_file_path,
        #verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )

# Create a response module
def get_agent_response(user_input, agent):
    response = agent.run(user_input)
    return response

# Run the bot
if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        sentence = input("You: ")
        if sentence == "quit":
            break
        resp = get_agent_response(sentence, agent_gpt)
        print(resp)

