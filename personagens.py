
"""
AI VIDEO STUDIO
SISTEMA DE PERSONAGENS

Define personagens e mantém suas características
visuais consistentes durante as histórias.
"""

ESTILO_BASE = """
Animação cartoon 2D.
Cabeças expressivas e olhos grandes.
Contornos escuros e bem definidos.
Cores suaves e ilustração detalhada.
Aparência visual consistente em todas as cenas.
"""


def criar_personagem(
    nome,
    idade,
    cabelo,
    roupa,
    caracteristicas,
    personalidade
):
    return {
        "nome": nome,
        "idade": idade,
        "cabelo": cabelo,
        "roupa": roupa,
        "caracteristicas": caracteristicas,
        "personalidade": personalidade,
        "estilo_visual": ESTILO_BASE
    }


def descrever_personagem(personagem):
    return f"""
PERSONAGEM: {personagem['nome']}

Idade: {personagem['idade']}
Cabelo: {personagem['cabelo']}
Roupa: {personagem['roupa']}
Características: {personagem['caracteristicas']}
Personalidade: {personagem['personalidade']}

ESTILO VISUAL:
{personagem['estilo_visual']}

IMPORTANTE:
Manter o mesmo rosto, cabelo, roupas,
proporções corporais e cores em todas as cenas.
Não criar um personagem diferente.
"""


def criar_prompt_cena(personagem, acao, emocao):
    return f"""
{descrever_personagem(personagem)}

AÇÃO:
{acao}

EXPRESSÃO:
{emocao}

Criar uma cena de animação cartoon 2D
com o personagem mantendo sua identidade visual.
"""


if __name__ == "__main__":
    exemplo = criar_personagem(
        nome="Explorador",
        idade="30 anos",
        cabelo="castanho curto",
        roupa="jaqueta laranja e calça escura",
        caracteristicas="olhos grandes e sobrancelhas expressivas",
        personalidade="curioso e corajoso"
    )

    print(descrever_personagem(exemplo))
