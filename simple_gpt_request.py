import openai

openai.api_key = "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"

prompt = input()

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "assistant", "content": prompt}
    ],
    max_tokens=150,
    n=1,
    temperature=0.5,
)

print(response.choices[0].message["content"])
