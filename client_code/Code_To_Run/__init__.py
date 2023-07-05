from ._anvil_designer import Code_To_RunTemplate
from anvil import *
import anvil.server



class Code_To_Run(Code_To_RunTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def label_1_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    self.text_area_joke.text = anvil.server.call('connect_to_open_ai')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')

  

    



