import sys
import argparse
import asyncio
from pytube import YouTube



def main():
    parser = argparse.ArgumentParser(description='arquivo com links')
    parser.add_argument("arquivo")
     
    args = parser.parse_args()
    arquivo = open(args.arquivo,'r')
    for linha in arquivo:
        youtube = YouTube(linha)
        youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
       
    return 0
 
if __name__ == '__main__':
    sys.exit(main())