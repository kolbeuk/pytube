#!/usr/bin/env python
# coding: utf-8

from pytube import YouTube
import concurrent.futures
import sys

def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.get_lowest_resolution()
    print(f"Downloading video: {yt.title}")
    stream.download()
    print(f"Downloaded video: {yt.title}")

def main(urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_video, urls)

if __name__ == "__main__":
    # Assuming URLs are passed as separate command-line arguments
    urls = sys.argv[1:]
    main(urls)
