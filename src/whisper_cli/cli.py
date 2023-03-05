import argparse
import sys

from .download_ffmpeg import download_ffmpeg
from . import __version__

def main(args = None):


	parser = argparse.ArgumentParser(description="A simple CLI for downloading ffmpeg")
	parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
	parser.add_argument("-d", "--download", action="store_true", help="Download ffmpeg")
	parser.add_argument("-u", "--update", action="store_true", help="Update whisper_cli")
	parser.add_argument("-a","--analyze", action="store_true", help="Analyze an audio file")

	if args is None:
		args = sys.argv[1:]

	args = parser.parse_args(args)

	if args.download:
		print("Downloading ffmpeg")
		download_ffmpeg()
