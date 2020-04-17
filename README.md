# Contact Tracing Simulator
This code runs a simulation of proximity interactions between a single subject and a collection of other handsets that belong to family, friends, coworkers, and other random people.

## How to Run
You can run the simulation in Google Colab [here](https://colab.research.google.com/drive/1eR2hP5rGvkPgjZBPxrCJqZKloU37lTxQ).

Press the PLAY ▶️button at every block of code and wait results.

You can set the simulation parameters for 

- Number of family members, friends, coworkers and others.
- Simulation starting date

You can then download the generated report of the simlation pression the **Download Report** button

![contactracing](https://user-images.githubusercontent.com/163333/79594544-79559100-80dd-11ea-966a-774073e0b36a.png)



## Disclaimer
The original Python implementation based on **Apple + Google Contact Tracing** by Gretel.ai - https://github.com/gretelai/contact-tracing-experiment

## Source code:
https://github.com/loretoparisi/contacttracing

## Example report

```
Simulation Start Time: 2020-04-17T10:38:15

Family Count: 5
Friend Count: 17
Coworker Count: 38
Other Count: 98

--------------------
Handset ID: cea23f1308af416c8495a45e8d04f793
Relation to subject: family [SIMULATION DATA ONLY, would not be revealed real-world] 
Contact periods:
		2020-04-17T12:30:00
		2020-04-18T20:30:00
		2020-04-19T11:30:00
		2020-04-20T12:30:00
		2020-04-20T19:30:00
		2020-04-20T20:30:00
		2020-04-21T12:30:00
		2020-04-21T19:30:00
		2020-04-22T16:30:00
		2020-04-24T12:30:00
		2020-04-25T20:30:00
		2020-04-25T21:30:00
		2020-04-26T19:30:00
		2020-04-26T20:30:00
		2020-04-27T12:30:00
		2020-04-27T21:30:00
		2020-04-29T16:30:00
--------------------
Handset ID: 669c9380dd0141d5a2b68b41a104d389
Relation to subject: family [SIMULATION DATA ONLY, would not be revealed real-world] 
Contact periods:
		2020-04-18T12:30:00
		2020-04-18T21:30:00
		2020-04-21T11:30:00
		2020-04-22T11:30:00
		2020-04-23T11:30:00
		2020-04-23T12:30:00
		2020-04-23T17:30:00
		2020-04-24T18:30:00
		2020-04-26T12:30:00
		2020-04-27T22:30:00
		2020-04-28T19:30:00
		2020-04-28T20:30:00
		2020-04-29T12:30:00
		2020-04-29T17:30:00
		2020-04-30T11:30:00
		2020-04-30T16:30:00
--------------------
Handset ID: ac2891cf409d4985a2ccd4c219d4882a
Relation to subject: family [SIMULATION DATA ONLY, would not be revealed real-world] 
Contact periods:
		2020-04-17T20:30:00
		2020-04-18T11:30:00
		2020-04-19T12:30:00
		2020-04-19T21:30:00
		2020-04-20T11:30:00
		2020-04-22T17:30:00
		2020-04-23T16:30:00
		2020-04-25T12:30:00
		2020-04-27T11:30:00
		2020-04-28T12:30:00
		2020-04-29T11:30:00
		2020-04-30T12:30:00
--------------------
Handset ID: adcac1ad5c7a45f5ab12432e5e601810
Relation to subject: family [SIMULATION DATA ONLY, would not be revealed real-world] 
Contact periods:
		2020-04-21T20:30:00
		2020-04-24T11:30:00
		2020-04-24T19:30:00
		2020-04-26T11:30:00
		2020-04-28T11:30:00
		2020-04-29T13:30:00
		2020-04-30T13:30:00
		2020-04-30T17:30:00
--------------------
```


