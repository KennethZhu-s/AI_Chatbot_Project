from flask import Flask, request, jsonify, render_template
from chat import get_agent_response

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits.csv.base import create_csv_agent


app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base2.html")

# Specify the path of csv and create the agent.
tmp_file_path = 'data/meta_data_sample.csv'
agent_gpt = create_csv_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613",
                   openai_api_key='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'),
        tmp_file_path,
        # verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )

#
@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_agent_response(text, agent_gpt)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
