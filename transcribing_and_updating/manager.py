from elastic_dal import ElasticDAL
from mongo_dal import MongoDal
from transcribe_WAV_file import Convert

class Manager:
    def __init__(self):
        self.convert = Convert()
        self.mongodal = MongoDal()
        self.elastidal = ElasticDAL()


    def run_all(self,):
        list_file_id = self.mongodal.get_all_id()
        for file_id in list_file_id:
            grid_out = self.mongodal.fs.get(file_id)
            #print(f"grid_out!!! {grid_out}")
            text = self.convert.convert_with_path(grid_out)
            self.elastidal.update_mapping_and_data(text,file_id)

if __name__ == "__main__":
    manager = Manager()
    manager.run_all()