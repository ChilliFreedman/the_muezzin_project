import speech_recognition as sr

# Initialize the recognizer
class Convert:
    def __init__(self):

        self.r = sr.Recognizer()
    def convert_with_path(self,file_path = r"C:\PycharmProjects\PycharmProjects\the_muezzin_project\data\podcasts\podcast_1.wav"):
        # Path to your WAV file
        # Load the audio file
        try:
            with sr.AudioFile(file_path) as source:
                audio_data = self.r.record(source)  # Read the entire audio file

            # Transcribe the audio using Google Web Speech API
            text = self.r.recognize_google(audio_data)
            print("Transcription: " + text)
            return text

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")

if __name__ == "__main__":
    convert = Convert()
    convert.convert_with_path()