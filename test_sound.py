import speech_recognition as sr

# Optional: List available microphones
print("Available microphones:")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{index}: {name}")

recognizer = sr.Recognizer()

# You can change device_index to the correct mic index from the above list
with sr.Microphone(device_index=0) as source:
    print("Adjusting for ambient noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

    print("Listening... Speak something:")
    try:
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        print("Processing your voice...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.WaitTimeoutError:
        print("Timeout: No speech detected.")
    except sr.UnknownValueError:
        print("Speech was unclear.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
