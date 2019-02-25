import speech_recognition as sr
audio_file =(r"C:\Users\elcot.elcot-pc.000\Downloads\venna.wav")
r = sr.Recognizer()
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)
    try:
         print("audio file contain " + r.recognize_google(audio))
         au=r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google speech recognizer cant understand your audio")
    except sr.RequestError:
         print("Couldnt get the result from Google Speach Recognition")
