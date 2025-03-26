import openai


openai.api_key ="";
def generate_product_recommendation(customer_profile):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Based on the following customer profile, suggest a personalized product recommendation:\n{customer_profile}",
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Example: Get a personalized recommendation
customer_profile = "Customer: 25, Male, Lives in New York, Likes Electronics, Positive sentiment towards tech."
print(generate_product_recommendation(customer_profile))
