# UPPAAL Model

## Enviroment

The following environments were used for development:

**OS**: Ubuntu 20.04 <br>
**UPPAAL**: 4.0.15 <br>
**OpenJDK**: 11.0.15 <br>

## Instalation 

Download the UPPAAL executable at the [official page](https://uppaal.org/downloads/).

## Running

1. Run UPPAAL with Java;
2. Open the system (Ctrl+O) selecting the *hotel-booking-chatbot.xml* file;
3. Click on "Verifier" tab;
4. Select all properties by holding Ctrl;
5. Click on "Check".

## Files

**hotel-booking-chatbot.xml:** holds the automata definition. Select this file when opening the system on UPPAAL.

**hotel-booking-chatbot.q:** holds the queries for verification. This file is loaded automatically by loading the *.xml*.
