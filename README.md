# Video and Audio Downloader

Este é um script simples em Python que permite baixar vídeos e áudios de várias plataformas, incluindo YouTube, TikTok, Twitter, Facebook, entre outros. O script usa a poderosa biblioteca `yt-dlp` para realizar os downloads e converter os formatos de vídeo e áudio automaticamente para MP4 e MP3, respectivamente.

## Funcionalidades

- **Download de Vídeos:** Baixe vídeos de diversas plataformas e converta-os automaticamente para o formato MP4.
- **Download de Áudios:** Extraia o áudio dos vídeos e converta-o para MP3.
- **Suporte a Playlists:** Baixe playlists inteiras com apenas um comando.
- **Compatibilidade:** Suporte a diversas plataformas como YouTube, TikTok, Twitter, Facebook, Instagram, Vimeo, e muito mais.

## Pré-requisitos

Certifique-se de que você tem o Python 3 instalado em sua máquina. Para instalar as dependências necessárias, execute:

```bash
pip install -r requirements.txt
```

## Menu de Opções
- **1- Informações:** Exibe informações sobre as plataformas suportadas.
- **2- Video (MP4):** Baixa vídeos no formato MP4.
- **3- Audio (MP3):** Baixa o áudio de vídeos no formato MP3.
- **0- Sair:** Encerra o programa.

## Observações
**Qualidade e Formato Fixos:** Para simplificar, os vídeos são sempre convertidos para MP4 e os áudios para MP3. Se necessário, o menu pode ser reformulado para permitir mais opções de escolha para o usuário.

## Dependências
**yt-dlp:** Ferramenta de download de vídeos e áudios de várias plataformas.
Python 3.6+

## Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
