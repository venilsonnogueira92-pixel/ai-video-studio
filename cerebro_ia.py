"""
AI VIDEO STUDIO - CEREBRO IA

Responsável por orientar a criação de histórias,
roteiros e cenas cinematográficas em estilo cartoon 2D.
"""

ESTILO_VISUAL = """
Animação cartoon 2D de alta qualidade.
Personagens originais com cabeças expressivas,
olhos grandes, contornos escuros e cores suaves.
Cenários ilustrados ricos em detalhes.
Expressões faciais bem definidas.
Iluminação e composição visual cuidadosas.
Manter a aparência dos personagens consistente
em todas as cenas.
"""


def criar_prompt_roteiro(tema, duracao=60):
    return f"""
Você é um roteirista especializado em vídeos curtos
de curiosidades, mistérios e histórias surpreendentes.

Crie uma história original sobre: {tema}

Duração desejada: {duracao} segundos.

REGRAS:
- Comece com uma frase que desperte curiosidade.
- Desenvolva a história de maneira envolvente.
- Use linguagem natural em português brasileiro.
- Crie suspense quando o tema permitir.
- Termine com uma conclusão marcante.
- Não invente fatos apresentados como verdadeiros.
- Divida a história em cenas.

ESTILO VISUAL:
{ESTILO_VISUAL}
"""


def criar_prompt_cenas(texto_cena, personagem="original"):
    return f"""
Transforme o trecho abaixo em uma cena de animação.

TRECHO DA HISTÓRIA:
{texto_cena}

PERSONAGEM:
{personagem}

DIREÇÃO VISUAL:
{ESTILO_VISUAL}

Descreva:
1. O cenário.
2. O personagem e sua expressão.
3. A ação que acontece.
4. A iluminação e as cores.
5. O enquadramento da câmera.
6. O movimento da cena.
7. A emoção que deve transmitir.

Crie uma descrição visual detalhada.
"""


if __name__ == "__main__":
    print("AI VIDEO STUDIO - CEREBRO IA")
    print("Sistema de planejamento inicial carregado.")

