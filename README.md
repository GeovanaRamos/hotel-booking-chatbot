# Hotel Booking Chatbot


## Description

This repository contains files for replicating research done in the paper *An Approach to Formal Verification of Chatbot Conversational Flows With Model Checking*.

## Chatbot Requirements

The requirements refer to a fictional chatbot that books rooms for a hotel. Although the hotel does not exist, the chatbot was designed and implemented in a way that it could be used in a real scenario or it could be expanded to more complex scenarios.

For the hotel, consider as a constraint that there is only one room type, that is, there is no difference among rooms. Consequently, all rooms have a (fictional) standard price per night. 

ID | Requirement 
---|---
R01 | The reservation must have the date of check-in. 
R02 | The reservation must have the date of check-out. 
R03 | The reservation must have at least one adult guest and four at most. 
R04 | The reservation can have up to six children. 
R05 | The reservation must have at least one room to be booked and four at most. 
R06 | The chatbot must call an external service to check for room availability according to the number of rooms requested. 
R07 | The chatbot must ask the user if it can proceed in case there is at least the number of rooms requested, otherwise, it should request the user to adjust registration data. 
R08 | The reservation must have the names and identity numbers of all guests. 
R09 | The reservation must have the age of all children guests. 

## Repository Organization

**./uppaal_model:** contains files for the hotel booking chatbot modeled in Uppaal that initially verified the proposed requirements. 

**./rasa_chatbot:** files for running the resulting chatbot implemented with Rasa framework based on the automata specification in Uppaal. 

Open the *README.md* of each folder for additional information of the model and the chatbot.