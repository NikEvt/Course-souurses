import openai

openai.api_key = "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"
while(1):
    prompt = input()

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "assistant", "content": prompt + ".\n Сократи оставив основную мысль"}
        ],
        max_tokens = 150,
        n = 1,
        temperature = 0.5,
    )

    print(response.choices[0].message["content"])