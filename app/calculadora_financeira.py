# app/calculadora_financeira.py

def calcular_juros_compostos(capital: float, taxa: float, tempo: int) -> float:
    """
    Calcula o montante final com base em juros compostos.
    :param capital: Valor inicial
    :param taxa: Taxa de juros (ex: 0.05 para 5%)
    :param tempo: Período em meses/anos
    :return: Montante total acumulado
    """
    if capital < 0 or taxa < 0 or tempo < 0:
        raise ValueError("Valores numéricos não podem ser negativos.")
    
    montante = capital * ((1 + taxa) ** tempo)
    return round(montante, 2)


def calcular_desconto(valor: float, percentual_desconto: float) -> float:
    """
    Aplica um percentual de desconto sobre um valor.
    """
    if valor < 0 or percentual_desconto < 0:
        raise ValueError("Valores não podem ser negativos.")
    
    desconto = valor * (percentual_desconto / 100)
    return round(valor - desconto, 2)