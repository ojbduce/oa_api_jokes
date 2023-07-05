import anvil.server
import openai

# Stage 1 - We will alter this to randaomise the response and make sure we get a new joke each time.

@anvil.server.callable
def connect_to_open_ai():
  openai.api_key = "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"
  prompt = "Hello tell me a joke?"
  model_engine = "text-davinci-002"
  response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5,)
  print(response.choices[0].text)
  return (response.choices[0].text)