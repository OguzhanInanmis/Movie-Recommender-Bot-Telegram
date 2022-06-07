"""Record all the details of each dialogue in the conversation in it's raw form.
If required, it also saves the dialogue acts.
"""

class DialogueRecorder:
    """Record all the details of each dialogue in the conversation in it's raw form.
    If required, it also saves the dialogue acts."""

    def __init__(self, path, nlp):
        """Initializes the Recorder

        Args:
            path: Path where the file must be saved
            nlp: If the Dialogue Acts must also be saved 
            
        """
        self.path = path
        self.nlp = nlp
       

    def record(self):
        """Records the current dialogue utterance"""
      

    def save(self):
        """Saves all the dialogues in the conversation to a file"""
        
