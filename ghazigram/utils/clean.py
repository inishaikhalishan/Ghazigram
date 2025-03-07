import os

class Clean:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def Clear(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)