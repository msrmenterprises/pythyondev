import autogen
import os

def main():

    # Ensure work directory exists
    work_dir = "coding"
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)

    config_list = autogen.config_list_from_json(
        env_or_file="OAI_CONFIG_LIST.json"
    )

    assistant = autogen.AssistantAgent(
        name="Assistant",
        llm_config={
            "config_list":config_list
        }
    )

    user_proxy = autogen.UserProxyAgent(
        name="user",
        human_input_mode="NEVER",
        code_execution_config={
            "work_dir": work_dir  # Removed 'user_docker'
        }
    )

    print("Initiating chat...")
    user_proxy.initiate_chat(assistant, message="""Plot a chart of their stock price change YTD. Save the data to stock_price_ytd.csv, and save the plot to stock_price_ytd.png.""")


if __name__ == "__main__":
    main()