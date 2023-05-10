
# NLP Chatbot for Document Understanding

[![Apache License 2.0](https://www.apache.org/img/asf_logo.png)](https://www.apache.org/licenses/LICENSE-2.0)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Next Steps](#next-steps)
- [Credits and Acknowledgements](#credits-and-acknowledgements)

## Introduction

Our NLP chatbot solution aims to help people with disabilities understand complex documents by providing them with a simplified and easily understandable version of the document. This solution is built using natural language processing techniques and machine learning algorithms to analyze and process the document text.

The chatbot interface allows users to interact with the system using natural language commands, and the system responds with a summary of the document or answers to the user's questions.

## Features

- Supports multiple document formats, including PDF, .docx, and plain text files.
- Uses natural language processing to understand user queries and provide relevant information.
- Provides a summary of the document content in an easily understandable format.
- Allows for questions on document content.

## Installation

To install the chatbot system, please follow these steps:

1. Clone the repository to your local machine.
2. CD into hackproject/code/api/app directory.
3. Run ./setup.sh.

## Usage

To use the chatbot system, follow these steps:

1. Open a terminal window and navigate to the project directory.
2. Run the command `uvicorn hackproject.code.api.app.main:app` to start the chatbot server.
3. Upload a document or type in a query or command to interact with the system.
4. The system will respond with a summary of the document or answer to the user's query.

## Next Steps

- Adding more languages: currently, for text-to-speech we can only support 5 languages (English, French, Russian, Dutch, Spanish), while only English is supported for speech-to-text. Adding support for more languages could increase its usefulness and appeal to a wider audience.

- Improving accuracy, reliability and cost savings: It may be worth investing in further development to improve the accuracy and reliability of the text-to-speech and speech-to-text functions. It will also be good to look into an open source Large Language Model, so we can reduce operational costs to zero.

- Enhancing accessibility: Enhancing accessibility, such as support for Braille displays or integration with assistive technology.

## Credits and Acknowledgements
- The embedding model used in the project is the open souce "all-mpnet-base-v2" model
- The Large Language model used in the project is the "text-davinci-003" model from OpenAI.
- Speech-to-Text and Text-to-Speech was achieved using models from Silero.