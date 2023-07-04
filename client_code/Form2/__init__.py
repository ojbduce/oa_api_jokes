#CLIENT - SERVER CODE
# CLIENT
# Call server function to prompt ChatGPT to tell a joke
# return joke text to text area
def label_1_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    self.text_area_joke = anvil.server.call('connect_to_open_ai')
# SERVER
# Function to prompt ChatGPT
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