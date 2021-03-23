<h1 align="center">bigdatafilter </h1>
<p>
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

Easily map functions to big datasets

## Installation

```bash
pip install bigdatafilter
```

## Usage

```python
import bigdatafilter as bdf
```

## Example

Create a sequential pipeline that downloads a list of youtube video urls and extracts the frames, in just a few lines

```python
p1 = "./videosA"
p2 = "./framesB"

bdf.map(urls, download_yt_video, working_dir=p1, concurrent=True)
bdf.dirmap(p1, extract_frames, working_dir=p2, concurrent=True)
```

<!-- ![](./docs/out1.gif) -->
