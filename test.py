import bigdatafilter as bdf
import youtube_dl
import os
import pathlib
import ffmpeg

# bigdatafilter.map()
urls = [
    "https://www.youtube.com/watch?v=2ksu-07FjXw",
    "https://www.youtube.com/watch?v=Snd5rM8GRYs",
]


def download_yt_video(url):

    options = {
        "outtmpl": "%(title)s-%(id)s.%(ext)s",
        "quiet": True,
        "no_warnings": True,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])


def extract_frames(video_path):

    video_name = pathlib.Path(video_path).stem.replace(" ", "-")

    # print(f"Extracting: {video_name}")

    output_file = f"%04d{video_name}.bmp"
    ffmpeg.input(video_path).filter("fps", fps=1).output(output_file).run(quiet=True)


p1 = "./videosA"
p2 = "./framesB"

bdf.map(urls, download_yt_video, concurrent=True, working_dir=p1)
bdf.dirmap(p1, extract_frames, working_dir=p2, concurrent=True)

# bdf.map(input_dir, extract_frames, working_dir=output_dir, concurrent=True)


# m.execute()
