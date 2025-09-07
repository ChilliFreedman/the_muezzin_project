from pathlib import Path
from datetime import datetime
class SetMetadata:
    def __init__(self,file_path = r"C:\PycharmProjects\PycharmProjects\the_muezzin_project\data\podcasts\podcast_1.wav"):
        self.file_path = file_path

    def get_metadata(self):
        metadata = {}
        my_path = Path(self.file_path)
        metadata["file_name"] = my_path.name
        file_stats = my_path.stat()
        #print(file_stats)
        metadata["file_size_bytes"] = file_stats.st_size
        creation_timestamp = file_stats.st_ctime
        creation_date = datetime.fromtimestamp(creation_timestamp)
        metadata["file_creation_timestamp"] = str(creation_date)



        return metadata


if __name__ == "__main__":
    set_metadata = SetMetadata()
    metadata = set_metadata.get_metadata()
    print(metadata)


