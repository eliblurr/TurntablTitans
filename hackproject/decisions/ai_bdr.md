# Simplifying Complex Documents With A Natural Language Processing Chatbot.

* Status: accepted 
* Deciders: Kwame Adu - Poku Sarfo, Judith Serwaa Ofosu, Elvis Segbawu, Afsanat Ineza
* Date: 2023-05-05

## Context and Problem Statement
Our goal is to create a solution that simplifies interacting with, and understanding complex documents. The solution should allow users to submit documents, receive a short summary, and be able to ask questions on the document. These questions will be replied to using simple and easy to understand words, making sure the true meaning and intent of the original document is not lost.

## Decision Drivers <!-- optional -->

* A user with disability, who wants to consume documents.
* A company, that wants to increase compliance with relevant requirements.
* A user, who wants to save time and increase their efficiency.

## Considered Options

* An accessibility tool that converts complex documents into alternative formats such as audio or braille.
* A Natural Language Processing chatbot that allows users to submit complex documents, receive a short summary of the document, and ask questions.
* A tool that summarizes complex documents and provides a short summary to users. Users can then ask questions on the summary.

## Options Decision Outcome

Chosen option: "A Natural Language Processing chatbot that allows users to submit complex documents, receive a short summary of the document and be able to ask questions", because it will let users have a better understanding of the documents they are interacting with, as well as provide a personalized experience.

## Proposed Design

* An intuitive and easy to use user interface, with clear instructions and guidance on how to upload and interact with documents. 
* Document processing with advanced Natural Language Processing(NLP) models.
* Question answering that allows users to ask questions about the document using natural language queries.
* Accessibility features such as audio playback, screen reader compatibility.
* Protected user data in compliance with relevant regulations and standards.

## Considerations

* Quality and accuracy of the Natural Language Processing models
* Availability, licensing, and or cost of the models
* Technical requirements for using the models.

## Design Decisions

* Made use of an open source embedding model (all-mpnet-base-v2
) and a GPT-3 language model, both trained on extensive datasets for our usecases to ensure quality and accuracy
* The use of the open source embedding model (all-mpnet-base-v2
), from our tests and analysis, will reduce operational costs by 91%
* Due to hardware limitations, made use of a paid large language model, accounting for 8% of total operational costs