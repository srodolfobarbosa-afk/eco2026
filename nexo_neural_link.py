import os
import json
import time
from datetime import datetime
from supabase import create_client
from loguru import logger
from dotenv import load_dotenv

load_dotenv('H:/eco/.env')

class NeuralLink:
    def __init__(self, membro_nome):
        self.membro = membro_nome
        self.root = "H:/eco"
        self.supabase = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY'))
        self.brain_intent_path = f"{self.root}/brain_intent.json"
        logger.add(f"{self.root}/logs/neural_{membro_nome}.log", rotation="1MB")

    def transmitir(self, status, dados, urgencia="BAIXA"):
        """ Transmite o estado do órgão para o Supabase e para o Cérebro Local """
        pacote = {
            "membro": self.membro,
            "status": status,
            "dados": dados,
            "urgencia": urgencia,
            "timestamp": datetime.now().isoformat()
        }
        
        # 1. Registro em Nuvem (Soberania)
        try:
            self.supabase.table("memoria_nexo").insert(pacote).execute()
        except Exception as e:
            logger.error(f"📡 Falha na transmissão nuvem: {e}")

        # 2. Comunicação Direta com o Cérebro (Latência Zero)
        with open(self.brain_intent_path, "w") as f:
            json.dump(pacote, f, indent=4)
        
        logger.info(f"🧬 {self.membro} sincronizado com o organismo.")

    def ouvir_cerebro(self):
        """ Escuta ordens de evolução vindas do cérebro """
        if os.path.exists(self.brain_intent_path):
            with open(self.brain_intent_path, "r") as f:
                return json.load(f)
        return None

# Exemplo de uso para os outros scripts:
# link = NeuralLink("Infiltrator")
# link.transmitir("ATACANDO", {"alvo": "leilao_x", "roi_estimado": 0.45})