import os
class ReadFiles:
    def __init__(self,folder_path = "../../data/podcasts"):
        self.folder_path = folder_path

    def get_all_file_paths(self):
        file_paths = []
        for root, _, files in os.walk(self.folder_path):
            for file in files:
                file_paths.append(os.path.join(root, file))
        return file_paths

    def get_first_path(self):
        all_files = self.get_all_file_paths()
        return all_files[0]
#check if it gets a good path the return
if __name__ == "__main__":
    read_files = ReadFiles()
    all_files = read_files.get_all_file_paths()
    print("len of files")
    print(len(all_files))
    print("\nfirst file path")
    print(read_files.get_first_path())
    print("\nall file paths")
    for path in all_files:
        print(path)
