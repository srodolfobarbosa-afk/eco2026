from loguru import logger

class NexoAdManager:
    def __init__(self):
        logger.info("📢 AD-MANAGER: Criando campanhas de alto impacto emocional.")

    def criar_campanha(self, causa, nicho_esporte):
        # Cria narrativas de união, fé e apoio para Nike, Adidas e Real Madrid vasco da gama, para realizar vendas
        logger.warning(f"🎬 CAMPANHA: 'NEXO + {causa}' focada no mercado de {nicho_esporte}.")
        return "AD_CONTENT_GENERATED"

if __name__ == '__main__':
    adm = NexoAdManager()
    adm.criar_campanha('Fome Zero', 'Futebol Europeu')
