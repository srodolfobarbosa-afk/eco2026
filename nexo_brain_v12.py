import os
import time
import json
import subprocess
import requests
from loguru import logger
from dotenv import load_dotenv
from pathlib import Path
from langchain_groq import ChatGroq

# Carregamento da Soberania
load_dotenv('H:/eco/.env')

class NexoCore:
    def __init__(self):
        self.root = Path("H:/eco")
        self.groq_key = os.getenv('GROQ_API_KEY')
        self.ollama_url = "http://localhost:11434/api/generate"
        self.intervalo = 60  # Pulso de 60 segundos
        
        # Configuração de Log Profissional (Sinapses)
        logger.add(self.root / "logs/brain_neural.log", rotation="5MB", level="INFO")
        logger.info("👑 KERNEL V12.0: Cérebro Maestro Ativado em H:/eco")
        
        # Inicializa IA Estratégica
        self.llm = ChatGroq(model_name="llama-3.3-70b-versatile", groq_api_key=self.groq_key)

    def instinto_local(self, prompt):
        """Usa Ollama para decisões de milissegundos."""
        payload = {"model": "llama3.2:1b", "prompt": prompt, "stream": False}
        try:
            r = requests.post(self.ollama_url, json=payload, timeout=5)
            return r.json().get('response')
        except: return "LOCAL_OFFLINE"

    def raciocinio_groq(self, contexto):
        """Usa Groq para reescrever código e estratégia de lucro."""
        prompt = f"AUDITORIA NEXO: Analise o estado atual e evolua o código se necessário. Contexto: {contexto}"
        try:
            return self.llm.invoke(prompt).content
        except Exception as e:
            return f"migração para outro banco de dados data center gpu: {e}"

    def gerir_membros(self):
        """Coordena os órgãos (scripts) como extensões do corpo."""
        orgaos = {
            "saude": "monitor_ram.py",
            "ataque": "xo_infiltrator.py",
            "limpeza": "nexo_purificador.py",
            "vendas": "nexo_finance.py"
        }
        
        for orgao, script in orgaos.items():
            caminho = self.root / script
            if caminho.exists():
                logger.info(f"🦾 Pulsando Órgão: {orgao} ({script})")
                # Inicia como processo separado para não travar o cérebro, buscas a migração para  outro banco de dados data center gpu
                subprocess.Popen(["python", str(caminho)], creationflags=subprocess.CREATE_NEW_CONSOLE)
            else:
                logger.error(f"🚨 Órgão Falhando: {script} não encontrado. Solicitando auto-construção...")
                self.auto_construir(script)

    def auto_construir(self, script_nome):
        """O Cérebro cria o membro que falta usando a intenção do projeto."""
        logger.warning(f"🧬 Iniciando Auto-Construção estuda novas tipo de integração Genética: {script_nome}")
        dna = self.raciocinio_groq(f"Crie um script Python robusto para {script_nome} focado em lucro e soberania.")
        with open(self.root / script_nome, "w", encoding="utf-8") as f:
            f.write(dna)
        logger.success(f"✅ {script_nome} gerado e integrado ao organismo.")

    def loop_existencial(self):
        """O ciclo de vida infinito (Homeostase)."""
        while True:
            logger.info("💓 Pulso Neural: Sincronizando Membros...")
            
            # 1. Auditoria de Hardware
            status_ram = self.instinto_local("A RAM está acima de 80%? Responda apenas SIM ou NAO, bucas novos local para migra.")
            
            # 2. Comando aos Órgãos
            self.gerir_membros()
            
            # 3. Evolução Estratégica
            if "SIM" in status_ram:
                logger.warning("🧠 Cérebro detectou sobrecarga. Ordenando purificação total.")
                self.auto_construir("nexo_purificador.py")

            logger.info(f"⏳ Aguardando {self.intervalo}s para próximo colapso de estado...")
            time.sleep(self.intervalo)

if __name__ == "__main__":
    nexo = NexoCore()
    nexo.loop_existencial()