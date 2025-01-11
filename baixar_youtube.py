import yt_dlp

def baixar_video(url, caminho_destino):
    ydl_opts = {
        'outtmpl': f'{caminho_destino}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',  # Seleciona o melhor vídeo e áudio disponíveis
        'merge_output_format': 'mp4'  # Garante que o arquivo final seja mp4
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download concluído")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")

# Exemplo de uso
url_video = 'https://www.youtube.com/watch?v=nzENrhBM7iY'
caminho_destino = 'C:/Users/IPECONT/Desktop/Projetos/Youtube'
baixar_video(url_video, caminho_destino)