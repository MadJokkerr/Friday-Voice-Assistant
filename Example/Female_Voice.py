import speech_recognition as sr
import pyttsx3
import time

# Initialize speech recognition and synthesis engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Index 1 usually corresponds to a female voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return ""

def fail_safe(custom_task):
    speak("Initiating fail-safe. Performing custom task.")
    for i in range(5):
        time.sleep(1)  # Simulate some time-consuming operation
        print(f"Custom task iteration {i+1}")
    speak("Fail-safe complete. Task performed.")

# Main loop
def main():
    speak("Hello, I am Friday. How can I assist you today?")
    
    while True:
        command = listen()
        
        if "fail safe" in command:
            fail_safe("Your custom task goes here.")
        elif "exit" in command:
            speak("Goodbye!")
            break
        elif command:
            # Handle other commands
            speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    main()
