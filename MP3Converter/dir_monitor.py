import os
from typing import List
import time
import mp3_conv

class DirMonitor:
    def __init__(self, dir_path, ext=".mp4"):
        self.dir_path = dir_path
        self.ext = ext


    def list_files(self) -> List:
        files = []
        for file in os.listdir(self.dir_path):
            full_file_path = os.path.join(self.dir_path, file)
            file, extension = os.path.splitext(full_file_path)
            if extension == self.ext:
                files.append(full_file_path)

        return files

    def watch(self):
        files_status = self.list_files()
        while True:
            time.sleep(5)
            current_files = self.list_files()
            new_files = list(set(current_files) - set(files_status))
            for file in new_files:
                mp3_conv.convert(file)

            files_status = current_files


