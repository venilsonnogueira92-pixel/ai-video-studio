
"""
AI VIDEO STUDIO
EDITOR DE VIDEO

Responsável pela montagem das cenas,
movimentos, legendas e exportação.
"""

import os
import numpy as np

from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import (
    ImageClip,
    AudioFileClip,
    CompositeVideoClip,
    concatenate_videoclips
)


LARGURA = 1080
ALTURA = 1920
FPS = 30


def criar_movimento_zoom(imagem, duracao, intensidade=0.12):
    """
    Cria um movimento suave de aproximação.
    """

    clip = ImageClip(imagem).set_duration(duracao)

    clip = clip.resize(
        lambda t: 1 + intensidade * t / duracao
    )

    clip = clip.set_position("center")

    return clip


def criar_legenda(texto, duracao, tamanho=58):
    """
    Cria legendas brancas com contorno escuro.
    """

    imagem = Image.new(
        "RGBA",
        (LARGURA, 220),
        (0, 0, 0, 0)
    )

    desenho = ImageDraw.Draw(imagem)

    try:
        fonte = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            tamanho
        )
    except OSError:
        fonte = ImageFont.load_default()

    palavras = texto.split()
    linhas = []
    linha = ""

    for palavra in palavras:
        teste = (linha + " " + palavra).strip()

        if desenho.textbbox((0, 0), teste, font=fonte)[2] < 1000:
            linha = teste
        else:
            linhas.append(linha)
            linha = palavra

    if linha:
        linhas.append(linha)

    altura_linha = tamanho + 18
    inicio_y = (220 - len(linhas) * altura_linha) // 2

    for i, linha in enumerate(linhas):
        caixa = desenho.textbbox((0, 0), linha, font=fonte)
        largura_texto = caixa[2] - caixa[0]

        x = (LARGURA - largura_texto) // 2
        y = inicio_y + i * altura_linha

        desenho.text(
            (x, y),
            linha,
            font=fonte,
            fill="white",
            stroke_width=4,
            stroke_fill="black"
        )

    return ImageClip(np.array(imagem)).set_duration(duracao)


def montar_cena(cena):
    """
    Monta uma cena com imagem, duração e legenda.
    """

    imagem = cena["imagem"]
    duracao = cena["duracao"]
    texto = cena.get("texto", "")

    fundo = ImageClip(imagem).set_duration(duracao)

    fundo = fundo.resize(
        height=ALTURA
    )

    if fundo.w < LARGURA:
        fundo = fundo.resize(width=LARGURA)

    fundo = fundo.crop(
        x_center=fundo.w / 2,
        y_center=fundo.h / 2,
        width=LARGURA,
        height=ALTURA
    )

    if texto:
        legenda = criar_legenda(texto, duracao)
        legenda = legenda.set_position(
            ("center", ALTURA - 350)
        )

        fundo = CompositeVideoClip(
            [fundo, legenda],
            size=(LARGURA, ALTURA)
        ).set_duration(duracao)

    return fundo


def montar_video(cenas, arquivo_saida):
    """
    Junta todas as cenas e exporta o vídeo.
    """

    if not cenas:
        raise ValueError("Nenhuma cena foi fornecida.")

    clips = []

    for cena in cenas:
        clips.append(montar_cena(cena))

    video = concatenate_videoclips(
        clips,
        method="compose"
    )

    pasta = os.path.dirname(arquivo_saida)

    if pasta:
        os.makedirs(pasta, exist_ok=True)

    video.write_videofile(
        arquivo_saida,
        fps=FPS,
        codec="libx264",
        audio_codec="aac"
    )

    video.close()

    for clip in clips:
        clip.close()

    return arquivo_saida


def adicionar_narracao(video, arquivo_audio):
    """
    Adiciona uma narração ao vídeo.
    """

    audio = AudioFileClip(arquivo_audio)

    return video.set_audio(audio)


if __name__ == "__main__":
    print("AI VIDEO STUDIO - EDITOR DE VIDEO")
    print("Modulo de montagem carregado.")
