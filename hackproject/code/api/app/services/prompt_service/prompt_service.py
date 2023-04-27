import os.path
from abc import abstractmethod
from llama_index import SimpleDirectoryReader


class PromptService:
    @abstractmethod
    def upload_file(self, path: str):
        pass

    @abstractmethod
    def submit_text_prompt(self, prompt: str):
        pass

    @abstractmethod
    def submit_voice_prompt(self, prompt: str):
        pass

class PromptServiceImpl(PromptService):
    def upload_file(self, path: str):
        if os.path.exists(path):
            document = SimpleDirectoryReader(input_files=[path]).load_data()
            return document
        else:
            raise FileNotFoundError("Invalid file path")

    def submit_text_prompt(self, text_prompt: str):
        return text_prompt

    def submit_voice_prompt(self, voice_prompt: str):
        return voice_prompt