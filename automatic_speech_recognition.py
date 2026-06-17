import librosa
from transformers import pipeline
audio, sr = librosa.load(r"C:\Users\user\Desktop\applied ai\sa3.wav", sr=16000, mono=True)
asr = pipeline("automatic-speech-recognition"
)
result = asr(audio)

print(result["text"])