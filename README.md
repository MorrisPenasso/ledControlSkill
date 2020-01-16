# ledControlSkill
Control a led connected at Raspberry Pi with Alexa

<b>Hardware configuration:</b>

- For connect your Raspberry at your led, see image "Led Circuit" into this project.
- For control the connections, see image "PIN_GPIO Raspberry" into this project.

<b>Software configuration:</b>

- You must create a custom skill into Amazon developer console,
- Create a custom skill into Amazon developer console.
- Set invocation name
- Create an intent with the name "onOffIntent"
- Create a slot type: OnOffValue with value "on" and "off" for specify that can have only two values
- Create an intent slot: OnOff into Intent: onOffIntent with slot type: OnOffValue that you have created
- On this intent,confirm: Is this slot required to fulfill the intent?
- Write the sentence that alexa will say to ask you what you do
- On the user utterances, write: {OnOff}. With this command, all words that will say, alexa get this for a slot value
- On the Raspberry, use the ngrok to publishing your entire project folder.
- Copy https link and set this into endpoint option of custom skill.
- Change command "Attiva " and "disattiva" with commands that you prefer.
- Compile your file "led-control.py".

Try it!!!

See my video dimostration to see how it work: https://drive.google.com/open?id=1Eo4MbbOyEQoxQOfQbHq7g02o8UbzcvQK
