from unittest import TestCase

from src.whisper_cli.cli import main


class TestFFMpegDownload(TestCase):

	def test_download(self):
		main(["-d"])