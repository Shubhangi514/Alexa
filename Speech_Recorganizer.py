import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to listen to the user's voice command
def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said: " + command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your command.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

# Define a function to respond to user commands
def respond_to_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "what is your name" in command:
        speak("I am a simple voice assistant.")
    elif "goodbye" in command:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("I'm sorry, I don't understand that command.")

# Define a function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    command = listen_for_command()
    if command:
        respond_to_command(command)
