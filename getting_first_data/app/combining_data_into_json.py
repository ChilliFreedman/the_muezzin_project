from utils.checking_logs import Logger
class DataToJson:
    def __init__(self,file_path,metadata_dict):
        self.file_path = file_path
        self.metadata_dict = metadata_dict
        self.logger = Logger.get_logger()

    def combin_to_json(self):
        try:
           all_data =  {"file_path":self.file_path,"metadata_dict":self.metadata_dict}
           self.logger.info("In file 'combining_data_into_json' the combin was successful")
           return all_data
        except Exception as e:
            self.logger.exception(f"In file 'combining_data_into_json' an unexpected error occurred: {e}")

if __name__ == "__main__":
    from creating_metadata import SetMetadata
    set_metadata = SetMetadata()
    file_path = set_metadata.file_path
    metadata = set_metadata.get_metadata()
    data_to_json = DataToJson(file_path,metadata)
    all_data = data_to_json.combin_to_json()
    print(all_data)