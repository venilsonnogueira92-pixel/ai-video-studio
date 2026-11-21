
"""
AI VIDEO STUDIO
DIRECAO CINEMATOGRAFICA

Planeja visualmente cada cena da história.
"""

ESTILO_PERSONAGEM = """
Estilo de animação cartoon 2D.
Personagens com cabeças expressivas,
olhos grandes e contornos escuros.
Cores suaves e acabamento bem definido.
Personagens originais e consistentes.
Não mudar o estilo visual entre as cenas.
"""


def planejar_cena(texto, emocao="curiosidade"):
    return {
        "descricao": texto,
        "estilo": ESTILO_PERSONAGEM,
        "emocao": emocao,
        "cenario": (
            "Criar um cenário ilustrado detalhado "
            "que combine com a história."
        ),
        "iluminacao": (
            "Iluminação bem trabalhada, sombras "
            "suaves e cores harmoniosas."
        ),
        "camera": (
            "Escolher enquadramento adequado e "
            "movimento de câmera suave."
        ),
        "animacao": (
            "Adicionar movimentos naturais, "
            "gestos e expressões dos personagens."
        )
    }


def criar_prompt_visual(cena):
    return f"""
Crie uma ilustração para uma cena de animação.

HISTÓRIA:
{cena['descricao']}

ESTILO:
{cena['estilo']}

EMOÇÃO:
{cena['emocao']}

CENÁRIO:
{cena['cenario']}

ILUMINAÇÃO:
{cena['iluminacao']}

CÂMERA:
{cena['camera']}

ANIMAÇÃO:
{cena['animacao']}

Manter o mesmo estilo visual e a
consistência dos personagens.
"""


if __name__ == "__main__":
    exemplo = planejar_cena(
        "Um explorador encontra uma porta misteriosa.",
        "suspense"
    )

    print(criar_prompt_visual(exemplo))
