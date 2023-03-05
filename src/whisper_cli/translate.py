import os
import sys
import platform
from pathlib import Path

import whisper


def translate(audio_path,out_path):
	"""
	system = platform.system().lower()
	p = Path(os.path.abspath(__file__))
	project_root = p.parent.parent

	ffmpeg_bin = project_root / "bin" / system / "ffmpeg"
	os.system(f"{ffmpeg_bin} -i {audio_path} out.mp3")
	"""

	with open(out_path, 'w') as sys.stdout:

		model = whisper.load_model("base")
		result = model.transcribe(audio_path, verbose=True)

