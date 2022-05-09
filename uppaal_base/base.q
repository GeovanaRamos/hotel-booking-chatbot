//This file was generated from (Commercial) UPPAAL 4.0.15 rev. CB6BB307F6F681CB, November 2019

/*
In all paths (A), all locations ([]) with es.verification (when external service template is in location verification) imply dm.waiting (the dm template is in location waiting). 
*/
A[] es.verification imply dm.waiting

/*
In all paths (A), at least one location (<>) is dm.done (location done from the dm template). 
*/
A<> dm.done

/*
In all paths (A), all locations ([]) are free of deadlocks. 
*/
A[] not deadlock
