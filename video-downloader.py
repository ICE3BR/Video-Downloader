import subprocess # 

# OBS: Deixei os formatos fixos em mp4 e mp3, pois as vezes estava dando erro pela url não ter suporte ao formato desejado.
# A ideia principal era deixar o usuário decidir a qualidade e formato do video/audio entre as opçãos válidas fornecidas.
# Talvez deva reformaular o menu para primeiro pedir a URL e depois fazer uma analise (a biblioteca tem essa opção) e então retornar as opções válidas de download e conversão.

def menu():
    """
    Exibe o menu principal do programa.
    """
    print("""
    Menu do Instalador:
    1- Informações
    2- Video (MP4)
    3- Audio (MP3)
    0- Sair
    """)

def info():
    """
    Exibe informações sobre as plataformas suportadas pelo programa.
    """
    print("""
    Temos suporte a Múltiplas Plataformas:
    
    Aceitamos centenas de sites além de:
    - YouTube
    - Twitter (X)
    - TikTok
    - Facebook
    - Instagram
    - Reddit
    - Vimeo
    - Dailymotion
    - SoundCloud
    - e muitos outros
    """)

def check_video_qualide(user_qualidade):
    """
    Verifica e retorna a qualidade de vídeo desejada com base na entrada do usuário.

    :param user_qualidade: Qualidade informada pelo usuário ('pior', 'melhor', '720p', '1080p').
    :return: Retorna a string correspondente à qualidade para uso no yt-dlp, ou False se inválido.
    """
    user_qualidade = user_qualidade.lower()  # Converte a entrada para minúsculas para evitar erros
    if user_qualidade in ["pior", "melhor", "720p", "1080p"]:
        return "worst" if user_qualidade == "pior" else "best" if user_qualidade == "melhor" else user_qualidade
    return False

def check_video_list(user_playlist):
    """
    Verifica se o usuário informou que o link é de uma playlist.

    :param user_playlist: Resposta do usuário (S para sim, N para não).
    :return: Retorna True se for uma playlist, False caso contrário.
    """
    return user_playlist.upper() == "S"

def download_video(link, qualidade="best", playlist=False):
    """
    Baixa um vídeo ou uma playlist usando yt-dlp.

    :param link: URL do vídeo ou playlist a ser baixado.
    :param qualidade: Qualidade desejada do vídeo ('best', 'worst', '720p', etc.).
    :param playlist: Se True, baixa todos os vídeos da playlist.
    """
    if not isinstance(link, str) or not link:
        print("Erro: A URL do vídeo é inválida.")
        return

    if not isinstance(qualidade, str) or not qualidade:
        print("Erro: A qualidade do vídeo é inválida.")
        return

    if not isinstance(playlist, bool):
        print("Erro: O valor de playlist é inválido.")
        return

    try:
        # Monta o comando para download
        command = ["yt-dlp", "-o", f"%(title)s.%(ext)s", link]
        
        # Apenas adicionar a opção de qualidade se não for "best"
        if qualidade != "best":
            command.extend(["-f", qualidade])
        
        if playlist:
            command.append("--yes-playlist")
        
        # Garante que o arquivo seja convertido para MP4
        command.extend(["--recode-video", "mp4"])
        
        # Executa o comando
        subprocess.run(command, check=True)
        print(f"Download concluído com sucesso: {link}")
    
    except subprocess.CalledProcessError:
        print(f"Erro durante o download de vídeo: {link}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def download_audio(link, playlist=False):
    """
    Baixa o áudio de um vídeo ou de uma playlist usando yt-dlp.
    O áudio será sempre convertido para o formato MP3.
    
    :param link: URL do vídeo ou playlist a ser baixado.
    :param playlist: Se True, baixa todos os áudios da playlist.
    """
    if not isinstance(link, str) or not link:
        print("Erro: A URL do vídeo é inválida.")
        return

    if not isinstance(playlist, bool):
        print("Erro: O valor de playlist é inválido.")
        return

    try:
        # Comando para baixar o melhor áudio disponível e converter para MP3
        command = ["yt-dlp", "-f", "bestaudio", "-x", "--audio-format", "mp3", "-o", f"%(title)s.%(ext)s", link]
        
        if playlist:
            command.append("--yes-playlist")
        
        subprocess.run(command, check=True)
        print(f"Download de áudio (MP3) concluído com sucesso: {link}")
    
    except subprocess.CalledProcessError as e:
        print(f"Erro durante o download de áudio: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def main():
    """
    Função principal que exibe o menu e gerencia as opções selecionadas pelo usuário.
    """
    print("=== Downloader Videos/Audios ===")
    while True:
        menu()
        escolha_menu = input("\nEscolha uma opção: ")
        if escolha_menu == '1':  # Informações
            info()
        elif escolha_menu == "2":  # Video (MP4)
            print("---Você selecionou Opção Video (MP4)---")
            user_url = input("Informe a URL do vídeo: ")
            user_qualidade = input("Qualidade-[pior|melhor|720p|1080p]: ")
            user_playlist = input("É uma playlist [S|N]: ")
            
            qualidade = check_video_qualide(user_qualidade)
            playlist = check_video_list(user_playlist)
            
            if not qualidade:
                print("Erro: A qualidade de vídeo escolhida não é válida. Por favor, escolha entre: pior, melhor, 720p, ou 1080p.")
            else:
                download_video(user_url, qualidade, playlist)
        elif escolha_menu == "3":  # Audio (MP3)
            print("---Você selecionou Opção Audio (MP3)---")
            user_url = input("Informe a URL do vídeo: ")
            user_playlist = input("É uma playlist [S|N]: ")
            
            playlist = check_video_list(user_playlist)
            download_audio(user_url, playlist)
        elif escolha_menu == "0":  # Sair
            break
        else:  # Opção inválida
            print("Escolha uma opção válida")

# Executa o programa
main()