import os
import ssl
import torch
from hackproject.code.api.app.enums import STTModel, AUDIO_PATH
from hackproject.code.api.app.utils import Decoder, prepare_model_input, split_into_batches, read_batch, save_file, remove_file, get_random_string

# Dangerous
ssl._create_default_https_context = ssl._create_unverified_context

def stt(audio_file, language:str):

    if STTModel.exists(language):
        _model = STTModel[language.upper()]
        torch.hub.set_dir(_model.path())
        if not os.path.isfile(_model.path()):
            torch.hub.download_url_to_file(_model.value['package'], _model.path()) 

        model = torch.jit.load(_model.path())
        decoder = Decoder(model.labels)

        path = save_file(os.path.join(AUDIO_PATH, get_random_string(6)), audio_file)

        f = [path]
        batches = split_into_batches(f, batch_size=10)
        input = prepare_model_input(read_batch(batches[0]), device=torch.device('cpu'))
        output = model(input)
        remove_file(path=path)
        return " ".join([decoder(data.cpu()) for data in output])

    raise ValueError("invalid language selection")
