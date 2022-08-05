# Rasa Chatbot


## Enviroment

The following environments and versions were used for development:

**OS**: Ubuntu 20.04 <br>
**Python**: 3.7.0 <br>
**Rasa**: 3.1.0 <br>
**Rasa SDK**: 3.1.1 <br>

Other environments may need different procedures than the ones below. In this case, please, recur to [Rasa official documentation](https://rasa.com/docs/rasa/installation).


## Instalation

It is recommended that you create a virtual environment to run the chatbot. 


Create environment (if possible, use `python3.7` on command)
```
python3 -m venv ./venv
```

Activate environment:

```
source ./venv/bin/activate
```

Update pip to avoid clashes:

```
pip install --upgrade pip
```

Install dependencies

```
pip install -r requirements.txt
```

## Running

First of all, train the chatbot model at least one time:

```
rasa train -d domain
```

For chatting with the chatbot, you need to have both the assistant and the action server up and running.

Run the action server in a terminal with:

```
rasa run actions
```

Run the assistant in another terminal with:

```
rasa shell
```

Now, you can chat with the assistant.

Obs: Since our hotel is fictional, there is not a real database to check for room availability. Therefore, we made a dummy `rooms_manager.py` to simulate an API verification for available rooms, which can be easily replaced with an API call. Similarly, in a real situation, the chatbot should send a request to an external service to save the reservation. Although we did not simulate that, it does not influence the conversation and it could be also added to the current flow.


## Testing

Some dialogue tests can be run to validate the conversational flow of the model. Run these tests with:

```
rasa test core --stories tests --out results 
```

Check logs if tests passed or failed. Additional details are dumped into the *results* folder.


## Example Conversation

```                                                                                                                         
Your input ->  /init_chat                                                                                                                             
Hello! Nice to meet you. Let's book you a room!
First, tell me the check-in date.
Your input ->  check in on 2/2/2022                                                                                                                   
Now, tell me the check-out date.
Your input ->  check out on 2/15/2022                                                                                                                 
How many adult guests are coming? Between 1 and 4.
Your input ->  2 adults                                                                                                                               
How many child guests are coming? Between 0 and 6.
Your input ->  1                                                                                                                                      
How many rooms do you want to book? Between 1 and 4
Your input ->  1                                                                                                                                      
Let me check if there are rooms available. Just a sec!
Done! We have rooms available. Do you wish to proceed?
Your input ->  sounds good                                                                                                                            
Nice! Now I need to collect the information of all guests. Just follow along my instructions.
I need the name of adult guest 1
Your input ->  Sienna Gordon                                                                                                                          
Inform the ID number of adult guest 1
Your input ->  1111111111                                                                                                                             
What's the name of adult guest 2?
Your input ->  Stephen Harrison                                                                                                                       
I need the ID number of adult guest 2
Your input ->  2222222222                                                                                                                             
Tell me the name of child guest 1
Your input ->  Brandon Martinez                                                                                                                       
I need the ID number of child guest 1
Your input ->  33333333333                                                                                                                            
I need the age of child guest 1
Your input ->  12                                                                                                                                     
Reservation finished! See the details below.
Check-in: 2/2/2022
Check-out: 2/15/2022
Rooms: 1
Guest 1
Name: Sienna Gordon
ID: 1111111111
Guest 2
Name: Stephen Harrison
ID: 2222222222
Guest 3
Name: Brandon Martinez
ID: 33333333333
Age: 12
Just call me if you need me again ;)
```