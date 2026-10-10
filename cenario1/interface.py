# interface.py
import time
from app.calculadora_financeira import calcular_juros_compostos, calcular_desconto
from app.cliente_api import ClienteAPI

def main():
    print("==========================================")
    print("   Iniciando Calculadora App (Docker)     ")
    print("==========================================")
    
    # Exemplo de uso dos módulos
    capital_final = calcular_juros_compostos(1000, 0.05, 12)
    print(f"Exemplo Cálculo Juros (R$ 1000 a 5% por 12 meses): R$ {capital_final}")
    
    cliente = ClienteAPI()
    print(f"Status Conexão Vizinho: {cliente.verificar_conexao()}")
    print("==========================================")

if __name__ == "__main__":
    main()
    
    # Loop contínuo para manter o container rodando no Docker Compose
    print("Container ativo e pronto para receber comandos...")
    while True:
        time.sleep(3600)