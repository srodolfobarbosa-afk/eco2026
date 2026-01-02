import psutil
import time
import os
from loguru import logger

def vigiar_hardware_elite():
    logger.info("🛡️ MONITOR BIG TECH: Proteção e Limpeza de Cache Ativada")
    while True:
        mem = psutil.virtual_memory()
        if mem.percent > 80:
            # Mata processos de navegador órfãos para recuperar RAM instantaneamente
            os.system("taskkill /f /im chrome.exe /fi 'memusage gt 100000' 2>nul")
            os.system("taskkill /f /im msedge.exe /fi 'memusage gt 100000' 2>nul")
            # Força o Garbage Collector do Windows
            os.system("powershell.exe [System.GC]::Collect()")
            logger.warning(f"🧹 RAM em {mem.percent}%: Limpeza profunda realizada.")
        
        print(f"[NEXO-CORE] RAM: {mem.percent}% | Livre: {mem.available / (1024**3):.2f}GB", end='\r')
        time.sleep(5)

if __name__ == "__main__":
    vigiar_hardware_elite()
