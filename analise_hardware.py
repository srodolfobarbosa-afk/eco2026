import psutil
import platform
import os

def analisar_sistema():
    print("--- 🔍 ANALISADOR DE MEMÓRIA NEXO ---")
    
    # Memória RAM
    memoria = psutil.virtual_memory()
    total_gb = memoria.total / (1024**3)
    disponivel_gb = memoria.available / (1024**3)
    
    # Processador
    processador = platform.processor()
    
    print(f"Sitema Operacional: {platform.system()} {platform.release()}")
    print(f"Processador: {processador}")
    print(f"RAM Total: {total_gb:.2f} GB")
    print(f"RAM Disponível agora: {disponivel_gb:.2f} GB")
    
    print("\n--- 🤖 RECOMENDAÇÃO DE LLM ---")
    if total_gb < 8:
        print("⚠️ Recomendação: Modelos Tiny (Ex: Phi-3 3.8B ou TinyLlama) com quantização 4-bit.")
    elif total_gb <= 16:
        print("✅ Recomendação: Modelos Small (Ex: Llama-3.2 3B ou Mistral 7B) via Ollama.")
    else:
        print("🚀 Recomendação: Modelos de 7B a 14B com alta performance.")

if __name__ == "__main__":
    analisar_sistema()