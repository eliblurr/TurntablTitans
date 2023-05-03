import os, ssl, torch, yaml
from hackproject.code.api.app.enums import TTSModel, AUDIO_PATH

# Dangerous
ssl._create_default_https_context = ssl._create_unverified_context

def get_model(language:str):
    device = torch.device('cpu')
    torch.set_num_threads(4)
    if TTSModel.exists(language):
        _model = TTSModel[language.upper()]
        if not os.path.isfile(_model.path()):
            torch.hub.download_url_to_file(_model.value['package'], _model.path()) 
        model = torch.package.PackageImporter(_model.path()).load_pickle("tts_models", "model")
        model.to(device)
        return model, _model.value['speaker']  
    raise ValueError("invalid language selection")

def tts(text:str, language:str, message_id:str, sample_rate:int=48000):
    model, speaker = get_model(language=language)
    return model.save_wav(text=text, speaker=speaker, audio_path=f"{AUDIO_PATH}/{message_id}.wav", sample_rate=sample_rate)