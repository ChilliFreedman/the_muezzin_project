class DataToJson:
    def __init__(self,file_path,metadata_dict):
        self.file_path = file_path
        self.metadata_dict = metadata_dict

    def combin_to_json(self):
       all_data =  {"file_path":self.file_path,"metadata_dict":self.metadata_dict}
       return all_data

if __name__ == "__main__":
    from creating_metadata import SetMetadata
    set_metadata = SetMetadata()
    file_path = set_metadata.file_path
    metadata = set_metadata.get_metadata()
    data_to_json = DataToJson(file_path,metadata)
    all_data = data_to_json.combin_to_json()
    print(all_data)