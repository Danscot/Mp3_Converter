from moviepy.editor import VideoFileClip

import os


class Mp3:

    def __init__(self, file, output):

        self.file_path = file

        self.file_name = f'{os.path.splitext(os.path.basename(self.file_path))[0]}.mp3'

        self.file_size = os.path.getsize(self.file_path)

        self.file = VideoFileClip(file)

        self.audio = self.file.audio

        self.output_path = output

    def convert_to_audio(self):

        self.audio.write_audiofile(f'{self.output_path}/{self.file_name}')


