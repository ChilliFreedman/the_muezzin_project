import speech_recognition as sr
from utils.checking_logs import Logger
class Convert:
    def __init__(self):
        self.logger = Logger.get_logger()
        self.r = sr.Recognizer()
    def convert_with_path(self,file_path = r"C:\PycharmProjects\PycharmProjects\the_muezzin_project\data\podcasts\podcast_1.wav"):

        try:
            with sr.AudioFile(file_path) as source:
                audio_data = self.r.record(source)

            text = self.r.recognize_google(audio_data)
            self.logger.info("Transcription: " + text)
            return text

        except sr.UnknownValueError:
            self.logger.exception("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            self.logger.exception(f"Could not request results from Google Speech Recognition service; {e}")
        except FileNotFoundError:
            self.logger.exception(f"Error: The file '{file_path}' was not found.")

if __name__ == "__main__":
    convert = Convert()
    convert.convert_with_path()