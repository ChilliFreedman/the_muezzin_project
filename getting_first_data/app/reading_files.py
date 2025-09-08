import os
from utils.checking_logs import Logger



class ReadFiles:
    def __init__(self,folder_path = r"C:\PycharmProjects\PycharmProjects\the_muezzin_project\data\podcasts"):
        self.folder_path = folder_path
        self.logger = Logger.get_logger()

    def get_all_file_paths(self):
        file_paths = []
        try:
            for root, _, files in os.walk(self.folder_path):
                for file in files:
                    file_paths.append(os.path.join(root, file))
            #print(self.folder_path)
            if len(file_paths) > 0:
                self.logger.info("In file 'reading_files' the connection with the file folder path was successful.")
            else:
                self.logger.error("In file 'reading_files' empty or folder or not exist")
            return file_paths
        except Exception as e:
            self.logger.exception(f"In file 'reading_files' an unexpected error occurred: {e}")

    def get_first_path(self):
        all_files = self.get_all_file_paths()
        return all_files[0]
#check if it gets a good path the return
if __name__ == "__main__":
    read_files = ReadFiles()
    all_files = read_files.get_all_file_paths()
    print("len of files")
    print(len(all_files))
    # print("\nfirst file path")
    # print(read_files.get_first_path())
    print("\nall file paths")
    for path in all_files:
        print(path)
