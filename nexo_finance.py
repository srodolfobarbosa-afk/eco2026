import os
import mercadopago
from dotenv import load_dotenv
from loguru import logger

load_dotenv('H:/eco/.env')

class NexoFinance:
    def __init__(self):
        token = os.getenv("MP_ACCESS_TOKEN")
        self.sdk = mercadopago.SDK(token)
        logger.info("💰 Órgão Financeiro Ativado. Alvo: 58160106531")

    def verificar_vendas(self):
        # Filtra pagamentos recentes
        filters = {"status": "approved", "sort": "date_created", "criteria": "desc"}
        return self.sdk.payment().search(filters)

if __name__ == "__main__":
    finance = NexoFinance()
    logger.success("Financeiro em espera...")