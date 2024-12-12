from autogen import Agent
import requests

class PostsAgent(Agent):
    def __init__(self, name):
        # Initialize the parent Agent class
        super().__init__(name=name)

    def handle_message(self, message):
        if "fetch posts" in message.lower():
            return self.get_posts()
        return "I can fetch posts for you. Just type 'fetch posts'."

    def get_posts(self):
        try:
            # Call the JSONPlaceholder API to fetch posts
            response = requests.get("https://jsonplaceholder.typicode.com/posts")
            if response.status_code == 200:
                posts = response.json()[:5]  # Fetch the first 5 posts
                return self.format_posts(posts)
            return "I couldn't fetch posts at the moment. Please try again later."
        except Exception as e:
            return f"An error occurred: {e}"

    def format_posts(self, posts):
        # Format the posts for display
        result = "Here are the latest posts:\n"
        for post in posts:
            result += f"\nPost ID: {post['id']}\nTitle: {post['title']}\nBody: {post['body']}\n"
        return result

    def communicate(self, message):
        # Process the message and return a response
        return self.handle_message(message)

if __name__ == "__main__":
    # Create and test the agent
    agent = PostsAgent(name="PostsFetcherBot")
    print(agent.communicate("Fetch posts"))
