from flask import Flask, request, jsonify
import autogen
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# AutoGen setup
work_dir = "coding"
if not os.path.exists(work_dir):
    os.makedirs(work_dir)

config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST.json")

assistant = autogen.AssistantAgent(
    name="Assistant",
    llm_config={"config_list": config_list}
)

user_proxy = autogen.UserProxyAgent(
    name="user",
    human_input_mode="NEVER",
    code_execution_config={"work_dir": work_dir}
)

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    
    # Initiate chat
    response = user_proxy.initiate_chat(assistant, message=user_input)
    
    # Debug the entire response object
    print("Debugging ChatResult object:", response.__dict__)
    
    # Extract chat history
    chat_history = response.chat_history
    
    # Extract the most relevant message
    if chat_history:
        # Search for the last meaningful assistant response
        for entry in reversed(chat_history):
            if entry['role'] == 'assistant' and entry['content'].strip():
                assistant_response = entry['content']
                break
        else:
            assistant_response = "No meaningful response found."
    else:
        assistant_response = "No chat history available."
    
    # Handle special cases like code execution outputs
    code_output = getattr(response, 'code_output', None)
    if code_output:
        assistant_response = f"Result: {code_output.strip()}"
    
    return jsonify({"response": assistant_response})

# def chat():
#     return jsonify({"error": "Simulated error"}), 500


if __name__ == '__main__':
    app.run(debug=True)
