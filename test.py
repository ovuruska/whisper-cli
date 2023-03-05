import whisper
import sys

if __name__ == "__main__":

	with open('out.txt', 'w') as sys.stdout:
		model = whisper.load_model("base")
		result = model.transcribe("audio.mp3",verbose=True)
