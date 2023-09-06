from ._anvil_designer import Machine1Template
from anvil import *

class Machine1(Machine1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
