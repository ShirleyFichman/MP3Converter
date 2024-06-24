import os
from moviepy.editor import VideoFileClip

def create_destination_directory():
    mp3_directory = os.path.join(os.curdir, 'mp3_files')
    os.makedirs(mp3_directory, exist_ok=True)

    return mp3_directory

def change_extension(filename):
    file, _ = os.path.splitext(filename)
    return f"{file}.mp3"
def convert(filename):
    destination_dir = create_destination_directory()
    video_file_clip = VideoFileClip(filename)
    audio = video_file_clip.audio
    file_basename = os.path.basename(filename)
    destination_full_path = os.path.join(destination_dir, change_extension(file_basename))
    audio.write_audiofile(destination_full_path, codec="mp3")
    video_file_clip.close()