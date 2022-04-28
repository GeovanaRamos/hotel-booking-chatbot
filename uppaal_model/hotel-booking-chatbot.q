//This file was generated from (Commercial) UPPAAL 4.0.15 rev. CB6BB307F6F681CB, November 2019

/*
Always the fact that the chatbot is asking for the guest age implies that the number of children read is less than the number of children requested.
*/
A[] dm.guest_X_age imply c_read<n_children

/*
Always the fact that the chatbot finished the reservation implies that the number of children and adults read is equal to the number of children and adults requested, respectively.
*/
A[] dm.done imply (c_read==n_children && a_read==n_adults)

/*
Whether the chatbot starts collecting guest names, eventually it will finish the reservation.
*/
dm.guest_X_name --> dm.done

/*
Whether the chatbot is waiting for the rooms manager response and the number of rooms requested is greater than the number of rooms available, 
eventually the chatbot will ask the user to adjust the reservation data.
*/
(dm.waiting && n_rooms>n_available) --> dm.adjust

/*
Always the fact that the chatbot asked to proceed with the reservation implies that the number of rooms available is greater or equal than the number of rooms requested.
*/
A[] dm.proceed imply n_available>=n_rooms

/*
Always the fact that the chatbot asked for adjusting reservation data implies that the number of requested rooms is less than the number of available rooms.
*/
A[] dm.adjust imply (n_rooms > n_available)

/*
Always the fact that the chatbot asked for adjusting reservation data implies that there are no rooms available.
*/
A[] dm.adjust imply !vacancy 

/*
Always the fact that the chatbot asked to proceed with the reservation implies that there are rooms available.
*/
A[] dm.proceed imply vacancy

/*
Whether the rooms manager is verifying for room availability, eventually the chatbot will ask if it can proceed with the reservation or ask the user to adjust the reservation data.
*/
rm.verifying --> (dm.proceed || dm.adjust)

/*
Always the fact that the chatbot finished the reservation implies that the user informed between 1 and 4 rooms.
*/
A[] dm.done imply (n_rooms > 0 && n_rooms <= 4)

/*
Always the fact that the chatbot finished the reservation implies that the user informed between 0 and 6 children guests.
*/
A[] dm.done imply (n_children >= 0 && n_children <= 6)

/*
Always the fact that the chatbot finished the reservation implies that the user informed between 1 and 4 adult guests.
*/
A[] dm.done imply (n_adults > 0 && n_adults <= 4)

/*
Eventually, the chatbot will ask for a check-out date. 
*/
A<> dm.check_out

/*
Eventually, the chatbot will ask for a check-in date.
*/
A<> dm.check_in

/*

*/
A[] not deadlock
