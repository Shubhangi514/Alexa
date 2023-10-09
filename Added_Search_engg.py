import speech_recognition as sr
import pyttsx3
from googlesearch import search
import requests
from bs4 import BeautifulSoup

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
        search_query = command
        search_results = list(search(search_query, num=1, stop=1))
        if search_results:
            web_page_url = search_results[0]
            content = get_web_page_content(web_page_url)
            if content:
                speak("Here's what I found on the web: " + content)
            else:
                speak("I'm sorry, I couldn't fetch information from the web.")
        else:
            speak("I'm sorry, I couldn't find any information on that.")

# Define a function to get web page content and extract the first paragraph
def get_web_page_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            if paragraphs:
                first_paragraph = paragraphs[0].text.strip()
                return first_paragraph
    except Exception as e:
        print(f"Error fetching web page content: {e}")
    return None

# Define a function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    command = listen_for_command()
    if command:
        respond_to_command(command)



    