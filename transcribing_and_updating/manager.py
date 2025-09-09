from elastic_dal import ElasticDAL
from mongo_dal import MongoDal
from transcribe_WAV_file import Convert
import io
from pydub import AudioSegment
class Manager:
    def __init__(self):
        self.convert = Convert()
        self.mongodal = MongoDal()
        self.elastidal = ElasticDAL()

#    def run(self):
    def get_all(self,):
        list_file_id = self.mongodal.get_all_id()
        for file_id in list_file_id:

            grid_out = self.mongodal.fs.get(file_id)
            audio_bytes = io.BytesIO(grid_out.read())
            audio = AudioSegment.from_wav(audio_bytes)
            temp_wav_path = "temp_audio.wav"
            audio.export(temp_wav_path, format="wav")
            text = self.convert.convert_with_path(temp_wav_path)

            import os
            if os.path.exists(temp_wav_path):
                os.remove(temp_wav_path)
            self.elastidal.update_mapping_and_data(text,file_id)

if __name__ == "__main__":
    manager = Manager()
    manager.get_all()