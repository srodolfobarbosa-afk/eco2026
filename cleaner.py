import os
import shutil
import ctypes
from loguru import logger

class NexoPurificador:
    def __init__(self):
        # LISTA BRANCA: O que NÃO pode ser apagado de jeito nenhum
        self.preservar_raiz = [
            "Windows", "Program Files", "Program Files (x86)", 
            "Users", "Eco", "Recovery", "PerfLogs", "$Recycle.Bin", 
            "System Volume Information", "bootmgr", "BOOTNXT"
        ]
        self.drive_alvo = "C:\\"
        logger.add("C:/Eco/logs/limpeza_total.log", rotation="1 MB")

    def e_administrador(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def executar_limpeza(self):
        if not self.e_administrador():
            logger.error("❌ Erro: O Purificador precisa de privilégios de Administrador!")
            return

        logger.info("🛡️ Iniciando Varredura Geral do Ecossistema...")

        # 1. Varredura na Raiz do C:
        for item in os.listdir(self.drive_alvo):
            caminho_completo = os.path.join(self.drive_alvo, item)
            
            if item not in self.preservar_raiz:
                self.remover_intruso(caminho_completo)

        # 2. Limpeza de Pastas Temporárias (Lixo de sistema)
        pastas_temp = [
            os.environ.get('TEMP'),
            "C:\\Windows\\Temp"
        ]
        for pasta in pastas_temp:
            if pasta and os.path.exists(pasta):
                logger.info(f"🧹 Limpando resíduos temporários em: {pasta}")
                self.limpar_conteudo_pasta(pasta)

    def remover_intruso(self, caminho):
        try:
            if os.path.isdir(caminho):
                logger.warning(f"🗑️ Removendo PASTA intrusa: {caminho}")
                shutil.rmtree(caminho)
            else:
                logger.warning(f"📄 Removendo ARQUIVO intruso: {caminho}")
                os.remove(caminho)
        except Exception as e:
            logger.error(f"⚠️ Não foi possível remover {caminho}. Motivo: {e}")

    def limpar_conteudo_pasta(self, pasta):
        for item in os.listdir(pasta):
            caminho = os.path.join(pasta, item)
            try:
                if os.path.isdir(caminho): shutil.rmtree(caminho)
                else: os.remove(caminho)
            except:
                continue

if __name__ == "__main__":
    purificador = NexoPurificador()
    print("--- NEXO V4.0: PURIFICADOR DE SISTEMA ---")
    confirmacao = input("Deseja apagar TUDO que não é padrão do Windows ou da pasta Eco? (S/N): ")
    
    if confirmacao.upper() == 'S':
        purificador.executar_limpeza()
        print("✅ Higienização concluída. Ordem restabelecida.")
    else:
        print("Operação cancelada.")