import os
from collections import Counter

def gerar_metricas_bdd(diretorio='features'):
    total_features = 0
    total_cenarios = 0
    modulos_contador = Counter()

    # Percorre todas as pastas procurando arquivos .feature
    for root, _, files in os.walk(diretorio):
        for file in files:
            if file.endswith('.feature'):
                total_features += 1
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    tag_atual = "@modulo_nao_identificado"
                    
                    for linha in f:
                        linha_limpa = linha.strip()
                        
                        # Captura a tag que indica o módulo (ex: @modulo_pagamento)
                        if linha_limpa.startswith('@modulo_'):
                            tag_atual = linha_limpa.split()[0]
                            
                        # Conta os cenários e associa ao último módulo encontrado
                        if linha_limpa.startswith(('Cenário:', 'Cenario:', 'Esquema do Cenário:', 'Scenario:')):
                            total_cenarios += 1
                            modulos_contador[tag_atual] += 1

    return total_features, total_cenarios, modulos_contador

if __name__ == '__main__':
    # 1. Roda a contagem
    features, cenarios, modulos = gerar_metricas_bdd()
    
    # 2. Imprime o resultado no formato Markdown (Pronto para o GitHub/Gestão)
    print("## 📊 Dashboard de Cobertura BDD (Gerado Automaticamente)\n")
    print(f"**🔹 Total de Funcionalidades (Features):** {features}")
    print(f"**🔹 Total de Cenários Mapeados:** {cenarios}\n")
    print("### 📂 Cobertura por Módulo:")
    
    for modulo, qtd in modulos.most_common():
        print(f"- `{modulo}`: {qtd} cenário(s)")