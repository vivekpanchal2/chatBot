from django.shortcuts import render
from django.http import JsonResponse
import openai


openai.api_key = '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'

def get_openai_response(prompt):
    try:
        # Make a request to the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
            temperature=0.7,
        )

        # Extract the content from the response
        if response.choices:
            answer = response.choices[0].message["content"].strip()
            return answer
        else:
            return "No valid response from OpenAI."

    except Exception as e:
        return f"Error from OpenAI: {e}"

# Example prompt
user_prompt = "Tell me a joke."

# Get the OpenAI response for the given prompt
openai_response = get_openai_response(user_prompt)

# Print the response
print("User Prompt:", user_prompt)
print("OpenAI Response:", openai_response)


def chatbot(request):

    if request.method == 'POST':
        message = request.POST.get('message')
        response = get_openai_response(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')

