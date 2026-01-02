import os
from loguru import logger

class NexoAuto:
    def __init__(self):
        self.output_dir = 'H:/eco/solucoes'
        if not os.path.exists(self.output_dir): os.makedirs(self.output_dir)

    def gerar_solucao(self, tema):
        logger.info('??? Engenharia: Processando inteligencia capturada...')
        try:
            with open('H:/eco/inteligencia_capturada.txt', 'r', encoding='utf-8') as f:
                dados = f.read()[:500] # Pega o resumo para o plano
            
            file_path = os.path.join(self.output_dir, 'plano_operacional.txt')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f'ANALISE DE MERCADO REAL: {tema}\n\nRECOLHIDO DA WEB:\n{dados}')
            logger.success(f'?? PLANO OPERACIONAL GERADO COM DADOS REAIS: {file_path}')
        except Exception as e:
            logger.r(f'?? ao ler inteligencia: {e}')
