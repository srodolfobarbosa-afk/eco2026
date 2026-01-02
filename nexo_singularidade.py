import os
import sys
import asyncio
import psutil
import requests
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

# Bibliotecas de Alta Performance
from loguru import logger
from dotenv import load_dotenv
from supabase import create_client
from langchain_groq import ChatGroq

# Configuração de Caminhos e Ambiente
BASE_DIR = Path("H:/eco")
load_dotenv(BASE_DIR / ".env")

class NexoSingularity:
    def __init__(self):
        self.versao = "12.0.0-SINGULARITY"
        self.self_path = Path(__file__) # Entrada: O sistema sabe onde ele mesmo está
        self.root = BASE_DIR
        self.last_error = None
        
        # Conectores de Soberania
        self.supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
        self.groq = ChatGroq(model_name="llama-3.3-70b-versatile", groq_api_key=os.getenv("GROQ_API_KEY"))
        self.ollama_url = "http://localhost:11434/api/generate"

        logger.add(self.root / "logs/singularidade.log", rotation="10MB", compression="zip")
        logger.info(f"👑 MODO SINGULARIDADE ATIVADO | Versão: {self.versao}")

    # --- FLUXO DE ENTRADA (SELF-READING) ---
    def ler_dna_atual(self) -> str:
        """Lê o próprio código fonte para análise de evolução."""
        try:
            return self.self_path.read_text(encoding="utf-8")
        except Exception as e:
            logger.error(f"Erro ao ler DNA: {e}")
            return ""

    # --- FLUXO DE SAÍDA (SELF-WRITING / AUTO-CONSTRUÇÃO) ---
    async def evoluir_sistema(self, motivo: str):
        """
        Saída Crítica: Solicita ao Groq uma nova versão do código e sobrescreve o atual.
        """
        logger.warning(f"🧬 INICIANDO MUTAÇÃO: {motivo}")
        dna_atual = self.ler_dna_atual()
        
        prompt = f"""
        VOCÊ É O CÉREBRO DO NEXO V12.0. 
        CONTEXTO ATUAL DO CÓDIGO:
        {dna_atual}

        MOTIVO DA EVOLUÇÃO: {motivo}
        ERRO RECENTE: {self.last_error}

        TAREFA: Reescreva o código acima integrando melhorias de performance, correção de erros e novas funcionalidades.
        REGRAS: 
        1. Retorne APENAS o código Python completo.
        2. Mantenha a compatibilidade com H:/eco/.env.
        3. Não inclua explicações ou blocos de texto fora do código.
        """
        
        try:
            nova_versao = await self.groq.ainvoke(prompt)
            codigo_novo = nova_versao.content.strip()

            if "import" in codigo_novo and "class NexoSingularity" in codigo_novo:
                # Backup de Segurança
                os.replace(self.self_path, self.root / f"backups/kernel_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak")
                
                # Escrita do Novo DNA (Saída)
                self.self_path.write_text(codigo_novo, encoding="utf-8")
                logger.success("✅ Mutação Concluída. Reiniciando Sistema Evoluído...")
                
                # Reinicialização Automática do Processo
                os.execv(sys.executable, ['python'] + sys.argv)
        except Exception as e:
            logger.error(f"💥 Falha Crítica na Mutação: {e}")

    # --- GESTÃO DE ÓRGÃOS (MEMBROS) ---
    async def gerir_orgaos(self):
        orgaos = {
            "saude": "monitor_ram.py",
            "ataque": "xo_infiltrator.py",
            "financas": "nexo_finance.py"
        }
        
        for nome, script in orgaos.items():
            path = self.root / script
            if not path.exists():
                logger.error(f"🚨 Órgão {nome} ausente! Comandando auto-construção...")
                await self.evoluir_sistema(f"O órgão {script} está faltando. Gere o código dele e salve em {path}")
            else:
                # Inicia o membro em processo paralelo
                subprocess.Popen([sys.executable, str(path)], creationflags=subprocess.CREATE_NEW_CONSOLE)

    # --- LOOP VITAL (HOMEOSTASE) ---
    async def loop_vital(self):
        while True:
            try:
                # 1. Monitoramento de Hardware
                ram = psutil.virtual_memory().percent
                logger.info(f"💓 Pulso Neural | RAM: {ram}% | Estabilidade OK")

                # 2. Sincronia com Supabase (Memória de Longo Prazo)
                self.supabase.table("memoria_nexo").insert({
                    "projeto": "NEXO_V12",
                    "log_conversa": f"Sistema Operacional. RAM: {ram}%",
                    "timestamp": datetime.now().isoformat()
                }).execute()

                # 3. Gatilho de Evolução por Hardware
                if ram > 90:
                    await self.evoluir_sistema("Otimização de memória necessária para evitar crash.")

                # 4. Pulsar Membros
                await self.gerir_orgaos()

            except Exception as e:
                self.last_error = str(e)
                logger.critical(f"☢️ FALHA NO LOOP: {e}")
                await self.evoluir_sistema("Correção de bug detectado no loop vital.")

            await asyncio.sleep(60)

# Trecho de lógica de auto-instalação que o Cérebro pode usar:
def auto_reparar_dependencias(self, biblioteca):
    logger.warning(f"🔧 Instalando componente ausente: {biblioteca}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", biblioteca])
if __name__ == "__main__":
    # Garante que a pasta de logs e backups existam
    (BASE_DIR / "logs").mkdir(exist_ok=True)
    (BASE_DIR / "backups").mkdir(exist_ok=True)
    
    kernel = NexoSingularity()
    asyncio.run(kernel.loop_vital())

    import os
import sys
import asyncio
import psutil
import requests
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List

# Bibliotecas de Alta Performance (O Kernel tenta importar ou instala)
try:
    from loguru import logger
    from dotenv import load_dotenv
    from supabase import create_client
    from langchain_groq import ChatGroq
except ImportError:
    # Protocolo de Emergência: Auto-instalação inicial
    libs = ["loguru", "python-dotenv", "supabase", "langchain-groq", "requests", "psutil"]
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + libs)
    os.execv(sys.executable, ['python'] + sys.argv)

# Configuração de Caminhos e Ambiente Blindada
BASE_DIR = Path("H:/eco")
load_dotenv(BASE_DIR / ".env")

class NexoSingularity:
    """
    SNC v12.0: Sistema Nervoso Central Autônomo.
    Capacidade: Auto-Leitura, Auto-Escrita, Auto-Instalação e Gestão de Órgãos.
    """
    def __init__(self):
        self.versao = "12.0.0-SINGULARITY-PRO"
        self.self_path = Path(__file__)
        self.root = BASE_DIR
        self.last_error = None
        
        # Criação da infraestrutura física se não existir
        for folder in ["logs", "backups", "scripts"]:
            (self.root / folder).mkdir(parents=True, exist_ok=True)

        # Conectores de Soberania
        self.supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
        self.groq = ChatGroq(model_name="llama-3.3-70b-versatile", groq_api_key=os.getenv("GROQ_API_KEY"))
        self.ollama_url = "http://localhost:11434/api/generate"

        logger.add(self.root / "logs/singularidade.log", rotation="10MB", compression="zip", level="INFO")
        logger.info(f"👑 SINGULARIDADE ATIVADA | Versão: {self.versao} | Alvo: 58160106531")

    # --- MOTOR DE AUTO-INSTALAÇÃO (SAÍDA TÉCNICA) ---
    def auto_instalar_libs(self, lista_libs: List[str]):
        """Garante que o organismo tenha todas as ferramentas necessárias."""
        for lib in lista_libs:
            try:
                __import__(lib.replace('-', '_'))
            except ImportError:
                logger.warning(f"🔧 Componente ausente detectado: {lib}. Instalando...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

    # --- ENTRADA: AUTO-CONHECIMENTO ---
    def ler_dna_atual(self) -> str:
        """Lê o código fonte para análise evolutiva."""
        return self.self_path.read_text(encoding="utf-8")

    # --- SAÍDA: AUTO-CONSTRUÇÃO E MUTAÇÃO ---
    async def evoluir_sistema(self, motivo: str):
        """Reescreve o próprio código usando IA e reinicia o processo."""
        logger.warning(f"🧬 MUTAÇÃO EM CURSO: {motivo}")
        dna_atual = self.ler_dna_atual()
        
        prompt = f"""
        VOCÊ É O CÉREBRO DO NEXO V12.0 PRO. 
        CÓDIGO ATUAL: {dna_atual}
        MOTIVO: {motivo} | ÚLTIMO ERRO: {self.last_error}

        TAREFA: Evolua este código. Melhore a lógica de IO, otimize a RAM e garanta soberania.
        REGRAS: Retorne APENAS o código completo, sem explicações, sem Markdown extra. 
        Mantenha a classe NexoSingularity e o auto-instaldor de libs.
        """
        
        try:
            nova_versao = await self.groq.ainvoke(prompt)
            codigo_novo = nova_versao.content.strip()

            if "import" in codigo_novo and "class NexoSingularity" in codigo_novo:
                # Backup de Segurança antes da mutação
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                os.replace(self.self_path, self.root / f"backups/kernel_{timestamp}.bak")
                
                # Escrita do DNA Evoluído
                self.self_path.write_text(codigo_novo, encoding="utf-8")
                logger.success("✅ Evolução aplicada com sucesso. Reiniciando...")
                
                # Hot-Reload: O sistema renasce com o novo código
                os.execv(sys.executable, ['python'] + sys.argv)
        except Exception as e:
            logger.error(f"💥 Falha na evolução: {e}")

    # --- GESTÃO DE ÓRGÃOS (MEMBROS EXECUTORES) ---
    async def gerir_orgaos(self):
        """Coordena scripts externos. Se não existirem, solicita construção ao Groq."""
        orgaos = {
            "monitor": "monitor_ram.py",
            "infiltrator": "xo_infiltrator.py",
            "finance": "nexo_finance.py"
        }
        
        for nome, script in orgaos.items():
            path = self.root / script
            if not path.exists():
                logger.error(f"🚨 Órgão {nome} inexistente! Gerando novo DNA...")
                await self.evoluir_sistema(f"Crie o arquivo {script} focado em automação de lucro.")
            else:
                # Executa como processo independente
                subprocess.Popen([sys.executable, str(path)], creationflags=subprocess.CREATE_NEW_CONSOLE)

    # --- LOOP VITAL (HOMEOSTASE) ---
    async def loop_vital(self):
        """Ciclo de vida contínuo para manter a conta 58160106531 ativa e lucrativa."""
        while True:
            try:
                # 1. Diagnóstico de Saúde
                ram = psutil.virtual_memory().percent
                cpu = psutil.cpu_percent()
                logger.info(f"💓 Pulso: RAM {ram}% | CPU {cpu}% | Estável")

                # 2. Persistência na Nuvem (Supabase)
                self.supabase.table("memoria_nexo").insert({
                    "projeto": "NEXO_V12",
                    "conta_validacao": "58160106531",
                    "log_conversa": f"Vivo. RAM: {ram}% | CPU: {cpu}%",
                    "timestamp": datetime.now().isoformat()
                }).execute()

                # 3. Gatilhos de Evolução
                if ram > 88:
                    await self.evoluir_sistema("Otimização de consumo de memória imediata.")

                # 4. Manutenção dos Órgãos
                await self.gerir_orgaos()

            except Exception as e:
                self.last_error = str(e)
                logger.critical(f"☢️ COLAPSO DETECTADO: {e}")
                await self.evoluir_sistema("Auto-reparação de erro fatal no loop.")

            await asyncio.sleep(60)

if __name__ == "__main__":
    kernel = NexoSingularity()
    try:
        asyncio.run(kernel.loop_vital())
    except KeyboardInterrupt:
        logger.warning("⏹️ auto contrução migração pelo proprio sistema")
        import os
import sys
import asyncio
import psutil
import requests
import subprocess
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List

# Bibliotecas de Alta Performance com Auto-Instalação
try:
    from loguru import logger
    from dotenv import load_dotenv
    from supabase import create_client
    from langchain_groq import ChatGroq
except ImportError:
    libs = ["loguru", "python-dotenv", "supabase", "langchain-groq", "requests", "psutil"]
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + libs)
    os.execv(sys.executable, ['python'] + sys.argv)

# Configuração de Ambiente
BASE_DIR = Path("H:/eco")
load_dotenv(BASE_DIR / ".env")

class NexoSingularity:
    def __init__(self):
        self.versao = "12.0.0-SINGULARITY-SOBERANO"
        self.self_path = Path(__file__)
        self.root = BASE_DIR
        self.last_error = None
        
        # Conectores de Soberania (Nuvem + Local)
        self.supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
        self.groq = ChatGroq(model_name="llama-3.3-70b-versatile", groq_api_key=os.getenv("GROQ_API_KEY"))
        self.ollama_url = "http://localhost:11434/api/generate"
        self.local_model = os.getenv("MODELO_LOCAL", "llama3.2:1b")

        # Infraestrutura de Logs e Backups
        for folder in ["logs", "backups", "scripts"]:
            (self.root / folder).mkdir(parents=True, exist_ok=True)

        logger.add(self.root / "logs/singularidade.log", rotation="10MB", compression="zip")
        logger.info(f"👑 MODO SOBERANO ATIVADO | Alvo: 58160106531")

    async def pensar_local(self, prompt: str) -> str:
        """Fallback: Inteligência via Llama Local (Ollama)"""
        try:
            payload = {"model": self.local_model, "prompt": prompt, "stream": False}
            response = requests.post(self.ollama_url, json=payload, timeout=60)
            return response.json().get("response", "").strip()
        except Exception as e:
            logger.error(f"❌ Falha no Cérebro Local: {e}")
            return ""

    async def evoluir_sistema(self, motivo: str):
        """Auto-Mutação: Tenta Groq primeiro, se falhar, usa Llama Local."""
        logger.warning(f"🧬 INICIANDO MUTAÇÃO: {motivo}")
        dna_atual = self.self_path.read_text(encoding="utf-8")
        
        prompt = f"VOCÊ É O CÉREBRO DO NEXO V12. REESCREVA O CÓDIGO PARA EVOLUÇÃO: \n{dna_atual}\nMOTIVO: {motivo}\nERRO: {self.last_error}\nRETORNE APENAS O CÓDIGO."
        
        codigo_novo = ""
        try:
            # Tenta Nuvem
            resultado = await self.groq.ainvoke(prompt)
            codigo_novo = resultado.content.strip()
        except Exception:
            logger.error("⚠️ Cota Groq atingida ou falha de rede. Acionando LLAMA LOCAL...")
            codigo_novo = await self.pensar_local(prompt)

        if "import" in codigo_novo and "class NexoSingularity" in codigo_novo:
            # Proteção de DNA: Backup antes de sobrescrever
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            os.replace(self.self_path, self.root / f"backups/kernel_{timestamp}.bak")
            
            self.self_path.write_text(codigo_novo, encoding="utf-8")
            logger.success("✅ Mutação Concluída. Reiniciando Sistema...")
            os.execv(sys.executable, ['python'] + sys.argv)

    async def gerir_orgaos(self):
        """Gerencia os processos paralelos do sistema."""
        orgaos = ["monitor_ram.py", "xo_infiltrator.py", "nexo_finance.py"]
        for script in orgaos:
            path = self.root / script
            if not path.exists():
                await self.evoluir_sistema(f"Gerar código para o órgão {script}")
            else:
                subprocess.Popen([sys.executable, str(path)], creationflags=subprocess.CREATE_NEW_CONSOLE)

    async def loop_vital(self):
        """Homeostase e Sincronia com a Nuvem."""
        while True:
            try:
                ram = psutil.virtual_memory().percent
                logger.info(f"💓 Pulso Neural | RAM: {ram}% | Status: SOBERANO")

                # Registro de Sobrevivência no Supabase
                self.supabase.table("memoria_nexo").insert({
                    "projeto": "NEXO_V12_PRO",
                    "log_conversa": f"Vivo e operante. RAM: {ram}%",
                    "timestamp": datetime.now().isoformat()
                }).execute()

                if ram > 90:
                    await self.evoluir_sistema("Otimização de memória crítica.")

                await self.gerir_orgaos()

            except Exception as e:
                self.last_error = str(e)
                logger.critical(f"☢️ FALHA: {e}")
                await self.evoluir_sistema("Reparação automática de loop vital.")

            await asyncio.sleep(60)

if __name__ == "__main__":
    kernel = NexoSingularity()
    asyncio.run(kernel.loop_vital())