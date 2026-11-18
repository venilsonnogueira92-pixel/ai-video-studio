
import json
from pathlib import Path

from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import (
    ImageClip,
    AudioFileClip,
    concatenate_videoclips,
)

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "saida"
AUDIO_DIR = OUTPUT_DIR / "audio"
SLIDES_DIR = OUTPUT_DIR / "slides"

WIDTH = 1920
HEIGHT = 1080
FPS = 24


def carregar_fonte(tamanho):
    caminhos = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]

    for caminho in caminhos:
        if Path(caminho).exists():
            return ImageFont.truetype(caminho, tamanho)

    return ImageFont.load_default()


def criar_slide(texto, caminho):
    imagem = Image.new(
        "RGB",
        (WIDTH, HEIGHT),
        (16, 24, 40)
    )

    desenho = ImageDraw.Draw(imagem)
    fonte = carregar_fonte(64)

    palavras = texto.split()
    linhas = []
    linha = ""

    for palavra in palavras:
        teste = f"{linha} {palavra}".strip()
        largura = desenho.textbbox(
            (0, 0), teste, font=fonte
        )[2]

        if largura < 1550:
            linha = teste
        else:
            linhas.append(linha)
            linha = palavra

    if linha:
        linhas.append(linha)

    altura_linha = 90
    altura_total = len(linhas) * altura_linha
    y = (HEIGHT - altura_total) // 2

    for linha in linhas:
        largura = desenho.textbbox(
            (0, 0), linha, font=fonte
        )[2]

        x = (WIDTH - largura) // 2

        desenho.text(
            (x, y),
            linha,
            font=fonte,
            fill=(255, 255, 255)
        )

        y += altura_linha

    imagem.save(caminho)


def gerar_video():
    roteiro_path = BASE_DIR / "roteiro.json"

    if not roteiro_path.exists():
        raise FileNotFoundError("Arquivo roteiro.json não encontrado.")

    with open(roteiro_path, "r", encoding="utf-8") as arquivo:
        roteiro = json.load(arquivo)

    cenas = roteiro.get("cenas", [])

    if not cenas:
        raise ValueError("O roteiro não possui cenas.")

    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    SLIDES_DIR.mkdir(parents=True, exist_ok=True)

    clips = []
    audios = []

    for indice, cena in enumerate(cenas):
        texto = cena.get("texto", "").strip()

        if not texto:
            continue

        print(f"Gerando cena {indice + 1}...")

        audio_path = AUDIO_DIR / f"audio_{indice}.mp3"
        slide_path = SLIDES_DIR / f"slide_{indice}.png"

        voz = gTTS(text=texto, lang="pt")
        voz.save(str(audio_path))

        audio = AudioFileClip(str(audio_path))
        audios.append(audio)

        criar_slide(texto, slide_path)

        duracao = max(
            audio.duration + 0.5,
            float(cena.get("duracao", 0))
        )

        clip = (
            ImageClip(str(slide_path))
            .set_duration(duracao)
            .set_audio(audio)
        )

        clips.append(clip)

    if not clips:
        raise ValueError("Nenhuma cena válida foi encontrada.")

    print("Montando vídeo...")

    video = concatenate_videoclips(clips, method="compose")

    destino = OUTPUT_DIR / "video_final.mp4"

    video.write_videofile(
        str(destino),
        fps=FPS,
        codec="libx264",
        audio_codec="aac",
        preset="medium"
    )

    video.close()

    for clip in clips:
        clip.close()

    for audio in audios:
        audio.close()

    print(f"Vídeo criado com sucesso: {destino}")


if __name__ == "__main__":
    gerar_video()
  
