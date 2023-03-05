import os
import platform
import sys
import zipfile

import wget


def progress_bar(current, total,width=80):
	current_mb = current / 1024 / 1024
	total_mb = total / 1024 / 1024
	progress_message = "Downloading: %d%% [%d MB / %d MB] bytes" % (current_mb / total_mb * 100, current_mb, total_mb)
	# Don't use print() as it will print in new line every time.
	sys.stdout.write("\r" + progress_message)
	sys.stdout.flush()


def windows_strategy():
	# Download ffmpeg
	url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-n6.0-latest-win64-lgpl-6.0.zip"
	wget.download(url, 'ffmpeg.zip',bar=progress_bar)

	# Extract ffmpeg
	with zipfile.ZipFile('ffmpeg.zip', 'r') as zip_ref:
		# Extract /bin folder to /bin
		zip_ref.extract('bin/ffmpeg.exe', path="bin")
		zip_ref.extract('bin/ffprobe.exe', path="bin")
		zip_ref.extract('bin/ffplay.exe', path="bin")

	# Clean up
	os.remove('ffmpeg.zip')


def mac_strategy():
	# Download ffmpeg
	ffmpeg_url = "https://evermeet.cx/ffmpeg/ffmpeg-109934-g891ed24f77.7z"
	ffprobe_url = "https://evermeet.cx/ffmpeg/ffprobe-109934-g891ed24f77.7z"
	ffplay_url = "https://evermeet.cx/ffmpeg/ffplay-107951-g90aa2a88f9.7z"

	wget.download(ffmpeg_url, 'ffmpeg.zip',bar=progress_bar)
	wget.download(ffprobe_url, 'ffprobe.zip',bar=progress_bar)
	wget.download(ffplay_url, 'ffplay.zip',bar=progress_bar)

	# Extract ffmpeg
	with zipfile.ZipFile('ffmpeg.zip', 'r') as zip_ref:
		zip_ref.extract('ffmpeg', path="bin")

	with zipfile.ZipFile('ffprobe.7z', 'r') as zip_ref:
		zip_ref.extract('ffprobe', path="bin")

	with zipfile.ZipFile('ffplay.7z', 'r') as zip_ref:
		zip_ref.extract('ffplay', path="bin")

	# Clean up
	os.remove('ffmpeg.7z')
	os.remove('ffprobe.7z')
	os.remove('ffplay.7z')


def download_ffmpeg():
	system = platform.system()
	machine = platform.machine()

	if not os.path.exists('bin'):
		os.mkdir("bin")


	if system == 'Windows':
		windows_strategy()

	# Check if Linux ARM
	elif system == 'Linux':
		if machine == 'armv7l':
			url = "https://evermeet.cx/ffmpeg/ffmpeg-6.0-armv7l.tar.xz"
		elif machine == 'aarch64':
			url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-n6.0-latest-linuxarm64-lgpl-6.0.tar.xz"
		elif machine == 'x86_64':
			url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-n6.0-latest-linux64-lgpl-6.0.tar.xz"



	elif system == 'Darwin':
		mac_strategy()

	if url is None:
		# Raise platform exception
		raise Exception(f"Platform not supported: {system}")
