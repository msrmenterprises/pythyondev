from autogen import Agent
import requests

class JokeAgent(Agent):
    def __init__(self, name):
        # Initialize the parent Agent class
        super().__init__(name=name)

    def handle_message(self, message):
        if "joke" in message.lower():
            return self.get_joke()
        return "I can only fetch jokes for now. Please ask me for a joke!"

    def get_joke(self):
        try:
            # Call the joke API
            response = requests.get("https://official-joke-api.appspot.com/random_joke")
            if response.status_code == 200:
                data = response.json()
                return f"Here's a joke for you:\n{data['setup']} ... {data['punchline']}"
            return "I couldn't fetch a joke at the moment. Please try again later."
        except Exception as e:
            return f"An error occurred: {e}"

    def communicate(self, message):
        # Process the message and return a response
        return self.handle_message(message)

if __name__ == "__main__":
    # Create and test the agent
    agent = JokeAgent(name="JokeBot")
    print(agent.communicate("Tell me a joke"))
