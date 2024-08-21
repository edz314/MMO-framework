# src/data/data_manager.py

import json
import os

class DataManager:
    def __init__(self, save_directory="saves"):
        """
        Initialize the DataManager with a directory for saving and loading NPC data.
        :param save_directory: The directory where save files will be stored.
        """
        self.save_directory = save_directory
        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)

    def save_npc_data(self, npc_data, filename):
        """
        Save the NPC data to a file.
        :param npc_data: An instance of NPCData.
        :param filename: The name of the file to save the data to.
        """
        filepath = os.path.join(self.save_directory, f"{filename}.json")
        with open(filepath, 'w') as file:
            json.dump(npc_data.__dict__, file, indent=4)
        print(f"NPC data saved to {filepath}")

    def load_npc_data(self, filename):
        """
        Load NPC data from a file.
        :param filename: The name of the file to load the data from.
        :return: An instance of NPCData with the loaded data.
        """
        filepath = os.path.join(self.save_directory, f"{filename}.json")
        if not os.path.exists(filepath):
            print(f"File {filepath} does not exist.")
            return None

        with open(filepath, 'r') as file:
            data = json.load(file)

        # Create a new NPCData object from the loaded data
        npc_data = NPCData(name=data['name'], health=data['health'], inventory=data['inventory'])
        npc_data.set_current_state_name(data.get('current_state_name', 'Neutral'))
        npc_data.position = tuple(data.get('position', (0, 0)))

        print(f"NPC data loaded from {filepath}")
        return npc_data

    def delete_npc_data(self, filename):
        """
        Delete the saved NPC data file.
        :param filename: The name of the file to delete.
        """
        filepath = os.path.join(self.save_directory, f"{filename}.json")
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"File {filepath} deleted.")
        else:
            print(f"File {filepath} does not exist.")

    def list_saved_npcs(self):
        """
        List all saved NPC files.
        :return: A list of filenames of saved NPCs.
        """
        files = [f for f in os.listdir(self.save_directory) if f.endswith('.json')]
        return [os.path.splitext(f)[0] for f in files]

