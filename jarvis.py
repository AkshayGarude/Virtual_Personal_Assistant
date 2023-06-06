import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listerner = aa.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()


def input_instruction():
    instruction = ""

    try:
        with aa.Microphone() as origin:
            print("Listening.......")
            speech = listerner.listen(origin)
            instruction = listerner.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', '')
                print(instruction)

    except:
        pass

    return instruction


def play_jarvis():
    instruction = input_instruction()
    print(instruction)

    if "play" in instruction:
        songs = instruction.replace('play', "")
        talk("playing " + songs)
        pywhatkit.playonyt(songs)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('Current Time: ' + time)
    
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk('Today\'s date: ' + date)
    
    elif 'how are you ' in instruction:
        talk('I am fine, how about you?')

    elif 'Say my name  ' in instruction:
        talk('Your name is Akshay')
    
    elif 'What is your name ' in instruction:
        talk('I am Jarvis, what can I do for you?')
    
    elif 'Who is ' in instruction:
        human = instruction.replace('who is ')
        info = wikipedia.summary(human,1)
        print(info)
        talk(info)

    elif 'bye' in instruction:
        talk('Bye. See you later.')
        exit()
        
    elif 'what is the weather' in instruction:
        try:
            weather = Weather()
            weather_data = weather.get_weather()
            talk(weather_data)
        except:
            talk("Sorry, I am unable to fetch the weather at this moment.")


play_jarvis()
