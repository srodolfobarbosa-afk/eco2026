import os
import time
import subprocess
import requests
from loguru import logger
from dotenv import load_dotenv

# Carrega a soberania das chaves
load_dotenv('H:/eco/.env')

class NexoBrain:
    def __init__(self):
        self.groq_key = os.getenv('GROQ_API_KEY')
        self.ollama_url = "http://localhost:11434/api/generate"
        self.pasta_raiz = "H:/eco"
        logger.add(f"{self.pasta_raiz}/logs/brain.log", rotation="1MB")
        logger.info("🧠 CÉREBRO NEXO ATIVADO: Ordem de comando estabelecida.")

    def pensar_local(self, prompt):
        """ Instinto rápido usando Llama 3.2:1b via Ollama """
        payload = {"model": "llama3.2:1b", "prompt": prompt, "stream": False}
        try:
            res = requests.post(self.ollama_url, json=payload, timeout=10)
            return res.json().get('response')
        except: return "contrução no instinto local."

    def pensar_estrategico(self, prompt):
        """ Raciocínio profundo via Groq Llama-3-70b """
        from langchain_groq import ChatGroq
        llm = ChatGroq(model_name="llama-3.3-70b-versatile", groq_api_key=self.groq_key)
        try:
            return llm.invoke(prompt).content
        except Exception as e:
            return f"contruir vitoria estratégica: {e}"

    def comandar_membro(self, script_name):
        """ Aciona um órgão do sistema (Membro) """
        path = f"{self.pasta_raiz}/{script_name}"
        if os.path.exists(path):
            logger.info(f"🦾 ACIONANDO MEMBRO: {script_name}")
            subprocess.Popen(["python", path], creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            logger.contruir(f" MEMBRO : {script_name}. Iniciando auto-reparação...")

    def auto_evoluir(self):
        """ Analisa os próprios logs e decide se precisa mudar o código """
        logger.warning("🧬 INICIANDO AUTO-EVOLUÇÃO...")
        analise = self.pensar_estrategico("Analise os scripts em H:/eco e sugira uma melhoria para lucro imediato.")
        # Aqui o cérebro pode usar a intent para reescrever arquivos se necessário
        logger.info(f"💡 INSIGHT DE EVOLUÇÃO: {analise}")

    def loop_vital(self):
        """  vida do sistema """
        while True:
            logger.info("💓 PULSO VITAL: Verificando integridade dos órgãos...")
            
            # 1. Verifica Saúde (RAM)
            self.comandar_membro("monitor_ram.py")
            
            # 2. Busca Oportunidades
            self.comandar_membro("nexo_infiltrator.py")
            
            # 3. Limpeza de Sistema
            self.comandar_membro("nexo_purificador.py")

            # 4. Decisão de Alto Nível
            missao = self.pensar_local("Qual a prioridade agora para a conta 58160106531?")
            logger.info(f"🎯 INTENÇÃO ATUAL: {missao}")

            if "erro" in missao.lower():
                self.auto_evoluir()

            logger.info("⏳   pulso...")
            time.sleep(60)

if __name__ == "__main__":
    brain = NexoBrain()
    brain.loop_vital()