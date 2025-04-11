from googletrans import Translator

class ChangeLanguage:
    def __init__(self,language:str,contents:list):
        self.language = language
        self.contents = contents

    def translate_content(self):
        return_content = []
        translator = Translator()
        translations = translator.translate(self.contents, dest=self.language)
        for translation in translations: return_content.append(translation.text)
        return return_content