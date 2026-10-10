# app/cliente_api.py
import urllib.request
import urllib.error

class ClienteAPI:
    def __init__(self, base_url: str = "http://servico-vizinho"):
        self.base_url = base_url

    def verificar_conexao(self) -> bool:
        """
        Tenta realizar uma requisição para verificar a comunicação entre containers.
        """
        try:
            with urllib.request.urlopen(self.base_url, timeout=3) as resposta:
                return resposta.status == 200
        except urllib.error.URLError:
            return False
        except Exception as e:
            print(f"Erro ao conectar com {self.base_url}: {e}")
            return False