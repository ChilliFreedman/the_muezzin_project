import base64
class Processor:
    def __init__(self):
        self.process_hostile_words_against_israel = None
        self.process_less_hostile_words_against_israel = None
        self.text = None


    def decode_and_lowercase_lists(self):
        hostile_words_against_israel = "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT"
        less_hostile_words_against_israel = "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="
        decoded_bytes_hostile = base64.b64decode(hostile_words_against_israel)
        decoded_hostile_words_against_israel = decoded_bytes_hostile.decode('utf-8')
        list_of_hostile_words = decoded_hostile_words_against_israel.split(",")
        self.process_hostile_words_against_israel = [word.lower() for word in list_of_hostile_words]
        decoded_bytes_less_hostile = base64.b64decode(less_hostile_words_against_israel)
        decoded_less_hostile_words_against_israel = decoded_bytes_less_hostile.decode('utf-8')
        list_of_less_hostile_words = decoded_less_hostile_words_against_israel.split(",")
        self.process_less_hostile_words_against_israel = [word.lower() for word in list_of_less_hostile_words]

    def clean_text(self,text):
        process_text = text.lower()
        self.text = process_text

    def get_percent(self)-> float:
        counter_hostile = 0
        for word in self.process_hostile_words_against_israel:
            counter_hostile += self.text.count(word) * 2

        counter_less_hostile = 0
        for word in self.process_less_hostile_words_against_israel:
            counter_less_hostile += self.text.count(word)

        percent = (counter_hostile + counter_less_hostile) * 100 / len(self.text.split(" "))
        return percent

    def get_is_bds(self)-> bool:
        return self.get_percent() > 40

    def get_bds_threat_level(self)->str:
        percent = self.get_percent()
        if percent <= 20:
            return "none"
        elif 20 <= percent <= 50:
            return "medium"
        else:
            return "high"







if __name__ == "__main__":
    processor = Processor()
    processor.decode_and_lowercase_lists()
    print(processor.process_hostile_words_against_israel)
    print(processor.process_less_hostile_words_against_israel)
    processor.clean_text("the protests are growing Millions demanding a ceasefire chanting for justice people see the occupation for what it is apartheid exactly Liberation movements always begin with protest that's how power shifts and BDS gives those protests economic and cultural teeth the blockade can't erase resilience resistance is alive and so is Hope")
    print(processor.text)
    print(processor.get_percent())
    print(processor.get_is_bds())
    print(processor.get_bds_threat_level())

