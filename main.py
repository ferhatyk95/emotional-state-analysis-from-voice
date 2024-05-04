import speech_recognition as sr
from textblob import TextBlob

# Initialize the recognizer
r = sr.Recognizer()

# Load the sound file
with sr.AudioFile('ses_dosyasi.wav') as source:
    audio = r.record(source)

# Convert the audio to text
text = r.recognize_google(audio, language='tr-TR')  # Türkçe ses dosyası için

# Perform sentiment analysis on the text
blob = TextBlob(text)
sentiment = blob.sentiment.polarity

# Classify emotions based on sentiment score
if sentiment > 0.5:
    emotion = "Mutlu"
    emoji = "😊"
elif sentiment < -0.5:
    emotion = "Üzgün"
    emoji = "😢"
else:
    emotion = "Nötr"
    emoji = "😐"

# Display the sentiment score, emotion, and emoji
print(f"Duygu skoru: {sentiment}")
print(f"Sınıflandırılan duygu: {emotion}")
print(f"Emoji: {emoji}")