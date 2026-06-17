import librosa
from transformers import pipeline

audio, sr = librosa.load(r"C:\Users\user\Desktop\applied ai\sa3.wav", sr=16000)

audio_classifier = pipeline("audio-classification")
result = audio_classifier(audio)

print(result)