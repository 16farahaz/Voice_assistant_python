import pyttsx3 #A library for text-to-speech (TTS) synthesis.
import speech_recognition as sr   #(alias sr): A library for speech-to-text (STT) recognition.
import eel   #A library for creating simple web-based GUI applications with Python and JavaScript.

def speak(text):
    engine = pyttsx3.init('sapi5')  # Initializes the text-to-speech engine using the 'sapi5' driver (Windows Speech API).
    voices = engine.getProperty('voices')  # Gets the available voices on the system.
    engine.setProperty('voice', voices[1].id)  # Sets the voice (e.g., 1 for female voice, 0 for male voice).
    engine.setProperty('rate', 174)  # Sets the speech rate (speed of speaking).
    print(voices)  # Debug: Prints the list of voices available on the system.
    engine.say(text)  # Prepares the engine to say the provided text.
    engine.runAndWait()  # Starts speaking the text.


@eel.expose
def takecommand():
    r = sr.Recognizer()  # Creates an instance of the speech recognizer.
    with sr.Microphone() as source:  # Accesses the microphone as the input source.
        print('listening ...')  
        eel.DisplayMessage('listening')
        r.pause_threshold = 1  # Waits for 1 second after the user stops speaking.
        r.adjust_for_ambient_noise(source)  # Adjusts for background noise.
        
        audio = r.listen(source, 10, 6)  # Listens to the audio for up to 10 seconds with a timeout of 6 seconds.

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing ... ') 
        query = r.recognize_google(audio, language='en-en')  # Uses Google's STT API to recognize the speech in English-Arabic mode.
        print(f"user said: {query}")  # Prints the recognized text.
        eel.DisplayMessage(query)
        speak(query)  # Calls the `speak` function to repeat the recognized text.
        eel.ShowHood()
    except Exception as e:
        return ""  # If recognition fails, return an empty string.

    return query.lower()  # Returns the recognized text in lowercase.

