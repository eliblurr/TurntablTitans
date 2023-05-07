import os
import ssl
import torch
from glob import glob
from hackproject.code.api.app.enums import STTModel
from hackproject.code.api.app.utils import Decoder, prepare_model_input, split_into_batches, read_batch

# Dangerous
ssl._create_default_https_context = ssl._create_unverified_context

def stt(audio_file, language:str):

    if STTModel.exists(language):
        _model = STTModel[language.upper()]
        if not os.path.isfile(_model.path()):
            torch.hub.download_url_to_file(_model.value['package'], _model.path()) 

        model = torch.jit.load(_model.path())
        decoder = Decoder(model.labels)

    batches = split_into_batches(audio_file.file.read(), batch_size=10)
    input = prepare_model_input(read_batch(batches[0]), device=torch.device("cpu"))
    output = model(input)
    return " ".join([decoder(data.cpu()) for data in output])
