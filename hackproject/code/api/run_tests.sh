#!/bin/bash
DIR=$(dirname "$(readlink -f "$0")")

python -m pytest -rA $DIR/tests/services/prompt_service
python -m pytest -rA $DIR/tests/services/chat_service
python -m pytest -rA $DIR/tests/services/model_service
python -m pytest -rA $DIR/tests/services/translation_service