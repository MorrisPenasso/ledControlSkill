from flask import Flask, render_template
from flask_ask import Ask, statement, question
import RPi.GPIO as GPIO #use GPIO library

#initializing GPIO
GPIO.setwarnings(False)
ledPin = 11 #pin 11 is connected to the led anode (+ve pin)
GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(ledPin, GPIO.OUT)   # Set ledPin's mode as output
GPIO.output(ledPin, GPIO.LOW) # Set ledPin low to turn off the led

#initializing flask ask
app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launch():
    welcome_text = render_template('welcome_text')
    return question(welcome_text)

@ask.intent('AMAZON.FallbackIntent')
def fallback():
    reprompt_text = render_template('command_reprompt')
    return question(reprompt_text)

@ask.intent('onOffIntent')
def control(OnOff): #slot Alexa value on the parameter
    command = OnOff
    if command is None:
        #no command was given
        reprompt_text = render_template('command_reprompt')
        return question(reprompt_text)
    elif command == "attiva" or command == "disattiva":
        if command == "disattiva":
            #turn OFF
            GPIO.output(ledPin, GPIO.LOW)
        else:
            #turn ON
            GPIO.output(ledPin, GPIO.HIGH)
        response_text = render_template('command', onOffCommand=command)
        return statement(response_text).simple_card('Comando:', response_text)
    else:
        #a valid command was not given
        reprompt_text = render_template('command_reprompt')
        return question(reprompt_text)

if __name__ == '__main__':
    app.run(debug=True)
