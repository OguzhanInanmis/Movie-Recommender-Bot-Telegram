"""Record all the details of each dialogue in the conversation in it's raw form.
If required, it also saves the dialogue acts.
"""
import json
import os


class RecorderBot:
    """Record all the details of each dialogue in the conversation in it's raw form.
    If required, it also saves the dialogue acts."""

    def __init__(self, history_folder):
        """Initializes the Recorder"""
        if os.path.isdir(history_folder):
            self.path = history_folder
        else:
            raise FileNotFoundError(
                'History path "{}" not found.'.format(history_folder))
        self.user_context = {}
        self.previous_dialogue_record = {}

    def record_user_data(self, user_id, record_data):
        """Records the current dialogue utterance for the user """
        user_history_path = self.path + 'user_' + user_id + '.json'
        if not os.path.isfile(user_history_path):
            self.create_record(user_id, user_history_path, record_data)
        else:
            self.update_record(user_id, user_history_path, record_data)

    def update_record(self, user_id, record_path, record_data):
        """Update an already existing json file"""
        with open(record_path) as hist_file:
            data = json.load(hist_file)
        data.append(record_data)
        with open(record_path, 'w') as hist_file:
            json.dump(data, hist_file, indent=4)

    def create_record(self, user_id, record_path, record_data):
        """Saves all the dialogues in the conversation to a file"""
        with open(record_path, 'w') as hist_file:
            json.dump([record_data], hist_file, indent=4)

    def load_user_data(self, user_id):
        """Loads the previously saved conversation log"""
        user_history_path = self.path + 'user_' + user_id + '.json'
        if os.path.isfile(user_history_path):
            with open(user_history_path) as hist_file:
                user_context = json.load(hist_file)
                return user_context


