import os
import webbrowser
import speech_recognition as sr
import subprocess

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            user_input = recognizer.recognize_google(audio)
            print(f"You said: {user_input}")
            return user_input.lower()  
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
        return None

def open_application(command):
    apps = {
        "notepad": "notepad.exe",
        "vs code": "code",
        "chrome": "chrome.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
    }

    for app_name, app_path in apps.items():
        if app_name in command:
            print(f"Opening {app_name}...")
            subprocess.Popen(app_path, shell=True)
            return True
    return False

def open_website(command):
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://www.github.com",
        "facebook": "https://www.facebook.com",
    }

    for site_name, site_url in websites.items():
        if site_name in command:
            print(f"Opening {site_name}...")
            webbrowser.open(site_url)
            return True
    return False

def open_path(command):
    if os.path.exists(command):
        print(f"Opening path: {command}")
        os.startfile(command)
        return True
    return False

def process_command(command):
    if open_application(command):
        return
    if open_website(command):
        return
    if open_path(command):
        return
    print(f"Sorry, I don't know how to handle: {command}")

voice_input = get_voice_input()

if voice_input:
    process_command(voice_input)