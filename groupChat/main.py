import autogen
import dotenv
import os
os.makedirs("code", exist_ok=True)


dotenv.load_dotenv()

config_list = autogen.config_list_from_dotenv(
    dotenv_file_path=".env",
    model_api_key_map={"gpt-3.5-turbo":"OPENAI_API_KEY"}
)

llm_config = {
    "cache_seed":42,
    "temperature":0,
    "config_list":config_list,
    "timeout":120,
}

user_proxy = autogen.UserProxyAgent(
    name="Admin",
    system_message="A human admin. Interact with the planner to discuss the plan. Plan execution needs to be approved "
                   "by this admin.",
    code_execution_config={
        "work_dir":"code",
        "use_docker":False
    },
    human_input_mode="TERMINATE",               
)

engineer = autogen.AssistantAgent(
    name="Engineer",
    llm_config=llm_config,
    system_message="""Scientist. You follow an approved plan. You are able to categorize papers after seeing their 
    abstracts printed. You don't write code."""
)

scientist = autogen.AssistantAgent(
    name="Scientist",
    llm_config=llm_config,
    system_message="""Scientist. You follow an approved plan. You are able to categorize papers after seeing their 
    abstracts printed. You don't write code."""
)

planner = autogen.AssistantAgent(
    name="Planner",
    system_message="""Planner. Suggest a plan. Revise the plan based on feedback from admin and critic, until admin approval.
The plan may involve an engineer who can write code and a scientist who doesn't write code.
Explain the plan first. Be clear which step is performed by an engineer, and which step is performed by a scientist.
""",
llm_config=llm_config,
)


critic = autogen.AssistantAgent(
    name="Critic",
    system_message="Critic. Double check plan, claims, code from other agents and provide feedback. Check whether the "
                   "plan includes adding verifiable info such as source URL.",
    llm_config=llm_config,
)

group_chat = autogen.GroupChat(
    agents=[user_proxy,engineer,scientist,planner,critic],messages=[],max_round=20
)

manager = autogen.GroupChatManager(groupchat=group_chat, llm_config=llm_config)

try:
    user_proxy.initiate_chat(
        manager,
        message="""
        Find papers on LLM applications from arxiv in the last week, create a markdown table of different domains.
        """,
    )
except Exception as e:
    print("An error occurred:", str(e))
