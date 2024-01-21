import openai

# Set up OpenAI GPT-3 API key
openai.api_key = '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'

def get_gpt3_response(user_query):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-0613",  # You can experiment with different engines
            prompt=user_query,
            max_tokens=1000  # Adjust based on the desired response length
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print("Error during API call:", e)
        return "Error during API call."

def main():
    print("Welcome to the Chatbot!")

    while True:
        user_input = input("You: ")
        
        # GPT-3 API response
        gpt3_response = get_gpt3_response(user_input)
        print("GPT-3 Bot:", gpt3_response)

if __name__ == "__main__":
    main()


