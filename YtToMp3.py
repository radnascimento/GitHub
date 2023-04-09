from pytube import YouTube
import os

path = []

path.append("https://youtu.be/oygrmJFKYZY")


print('Início do download')


for path in path:
    print(f'Baixando {path}')

    yt = YouTube(str(path))

    video = yt.streams.filter(only_audio=True).first()

  
    # download the file
    out_file = video.download(output_path="C:\\Python_Download_YT\\")
  
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)


print('Fim do download')