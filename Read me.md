# Youtube Playlist Downloader

## Description

This repository contains a Python script for downloading YouTube playlists as MP3 files. It uses `pytube` to fetch videos from YouTube, `moviepy` to convert them to MP3, `BeautifulSoup` and `requests` to scrape the playlist title, and `eyed3` to add metadata to the downloaded files.

This script is designed to create a folder named after the playlist title, and download all the songs from the playlist into that folder. It also adds metadata to the MP3 files, using the video's title and description. Please note that the metadata extraction is based on the structured data provided by YouTube for each video.

Use this script responsibly, respecting copyrights, and adhere to the YouTube's terms of service.

## Installation

### Python

Python can be installed by visiting the [official Python website](https://www.python.org/) and downloading the installer appropriate for your operating system. Make sure to download Python 3, as this script is not compatible with Python 2.

### Libraries

Once Python is installed, you can install the necessary libraries by using pip, which is a package manager for Python and should be included with the Python installation. Open a terminal (Command Prompt for Windows, Terminal app for macOS), and type:

```bash
pip install pytube moviepy beautifulsoup4 requests eyed3
```

## Usage

To run the script, save it to a file, e.g. `youtube_downloader.py`, navigate to the folder containing the script in the terminal (using `cd path_to_folder`) and type:

```bash
python youtube_downloader.py
```

When the script starts, it will ask you for the URL of the YouTube playlist and the directory where you want to save the downloaded files. After providing these details, the script will start downloading the MP3 files.