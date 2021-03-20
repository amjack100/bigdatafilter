import bigdatafilter as bdf

import os
import pathlib
import ffmpeg

# bigdatafilter.map()


def extract_frames(video_path):

    video_name = pathlib.Path(video_path).stem.replace(" ", "-")

    # print(f"Extracting: {video_name}")

    output_file = f"%04d{video_name}.bmp"
    ffmpeg.input(video_path).filter("fps", fps=1).output(output_file).run(quiet=True)


input_dir = "./videosA"
output_dir = "./framesB"


bdf.map(input_dir, extract_frames, output_dir=output_dir, concurrent=True)


# m.execute()
