import argparse

from . import __version__
from .translate import translate
import os

def main(args=None):
	parser = argparse.ArgumentParser(description="A simple CLI for downloading ffmpeg")

	parser.add_argument("filename",metavar="filename", type=str, help="The audio file to translate")

	os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
	if args is None:
		args = parser.parse_args()
	translate(args.filename,"example.txt")
