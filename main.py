import pyttsx3
import speech_recognition as sr

"""
Initializing pyttsx3
"""
engine = pyttsx3.init()

"""
speak(<var>)
User defined function,
use to ,
speak the certain text
"""


def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    while True:
        """
        making instance of 
        <class> Recognizer
        """
        r = sr.Recognizer()
        try:
            """
            Using Microphone()
            to awake the system's microphone
            and ,
            listen to the user voice
            """
            with sr.Microphone() as source:
                print("Listening ...")
                audio = r.listen(source, timeout=1, phrase_time_limit=5)

            print("Recognizing ...")
            """
            using google's recognizer
            to convert 
            voice to english text
            """
            sentence = r.recognize_google(audio)
            print(sentence)  # printing the text that is said by the user
            speak(sentence)  # speaking the text
        except Exception as e:
            speak(f"Please say something, Microphone been activate {e}")
