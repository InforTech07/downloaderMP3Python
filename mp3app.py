import os
import subprocess
import youtube_dl


def mp3Download():
    # solicita el ingrese de la url
    print("________Aplicacion para descargar mp3__________")
    video_url = input("Ingrese URL: ")
    
    # Descarga y lo convierte a mp3
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    filename = os.path.join(os.path.expanduser('~'),'Music'+'/') + f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    # abre el archivo de musica
    subprocess.call(["open", filename])
    print('Descarga Finalizada vaya a su carpeta de musica..!')
    


if __name__ == '__main__':
    mp3Download()


