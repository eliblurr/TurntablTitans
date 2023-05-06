#!/bin/bash
DIR=$(dirname "$(readlink -f "$0")")

cat $DIR/requirements.txt | xargs -n 1 -L 1 pip install

MODEL_DIR=$DIR/app/tmp/models
AUDIO_DIR=$DIR/app/tmp/audio

echo $MODEL_DIR

mkdir -p $MODEL_DIR $AUDIO_DIR

[ ! -e "$MODEL_DIR/en_model.pt" ] && curl https://models.silero.ai/models/tts/en/v3_en.pt --output $MODEL_DIR/en_model.pt
[ ! -e "$MODEL_DIR/de_model.pt" ] && curl https://models.silero.ai/models/tts/de/v3_de.pt --output $MODEL_DIR/de_model.pt
[ ! -e "$MODEL_DIR/es_model.pt" ] && curl https://models.silero.ai/models/tts/es/v3_es.pt --output $MODEL_DIR/es_model.pt
[ ! -e "$MODEL_DIR/fr_model.pt" ] && curl https://models.silero.ai/models/tts/fr/v3_fr.pt --output $MODEL_DIR/fr_model.pt
[ ! -e "$MODEL_DIR/ru_model.pt" ] && curl https://models.silero.ai/models/tts/ru/v3_1_ru.pt --output $MODEL_DIR/ru_model.pt