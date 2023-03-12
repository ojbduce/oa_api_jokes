import anvil.server
from openai import openai

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
openai.api_key = "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"


prompt = "Hello tell me a joke?"
model_engine = "text-davinci-002"

response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5,
)

print(response.choices[0].text)