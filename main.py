import moviepy.editor as mp
from os import listdir
from os.path import isfile, join
from pathlib import Path


def convert(dir_path, output_dir):
    # Convert
    print(f"Getting list of files in ${dir_path}")
    video_files = [ join(dir_path, filename) for filename in listdir(dir_path) if isfile(join(dir_path, filename))]
    for video_file in video_files:
        # read video file
        print(f"Reading {video_file}")
        video = mp.VideoFileClip(video_file)

        # Extract audio
        print("Extracting audio...")
        audio_output_path = output_dir + "/" + str(Path(video_file).stem) + ".mp3"
        video.audio.write_audiofile(audio_output_path)
        print(f"Audio saved to {audio_output_path}")

    print("\n\n\nDone!")


if __name__ == '__main__':
    inputDirectory = "<path to input directory with all video files>"
    outputDirectory = "<path to output directory>"
    convert(inputDirectory, outputDirectory)
