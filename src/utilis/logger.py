import csv 
from pathlib import Path
class Logger():

    def __init__(self, filename):
        self.filename = filename
        current_dir = Path(__file__).resolve().parent
        folder = current_dir.parent.parent
        subfolder = folder / "data"

        subfolder.mkdir(parents=True, exist_ok=True)
        self.filepath = subfolder / self.filename

        self.file_exists = self.filepath.exists()
        self.file = open(self.filepath, mode='a', newline='')
        self.writer = csv.writer(self.file)

    def log(self, row):
        self.writer.writerow([row])
        self.file.flush()

    def close(self):
        if hasattr(self, 'file'):
            self.file.close()

    def info(self, info):
        print(info)


  

