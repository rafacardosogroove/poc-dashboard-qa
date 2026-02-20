import os
from collections import Counter, defaultdict
from datetime import datetime

def gerar_metricas_bdd(diretorio='features'):
    total_features = 0
    total_cenarios = 0
    tags_contador = Counter()
    dados_features = [] # Lista para guardar nome, quantidade e data

    for root, _, files in os.walk(diretorio):
        for file in files:
            if file.endswith('.feature'):
                caminho_arquivo = os.path.join(root, file)
                
                # Captura a data da última modificação do arquivo
                timestamp = os.path.getmtime(caminho_arquivo)
                data_modificacao = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y')
                
                total_features += 1
                cenarios_desta_feature = 0
                nome_feature = "Feature sem nome"
                
                with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                    for linha in f:
                        linha_limpa = linha.strip()
                        
                        # Captura Tags
                        palavras = linha_limpa.split()
                        for palavra in palavras:
                            if palavra.startswith('@'):
                                tags_contador[palavra] += 1
                                
                        # Captura Nome da Feature
                        if linha_limpa.startswith(('Funcionalidade:', 'Feature:')):
                            nome_feature = linha_limpa.split(':', 1)[1].strip()
                            
                        # Conta Cenários
                        if linha_limpa.startswith(('Cenário:', 'Cenario:', 'Esquema do Cenário:', 'Scenario:')):
                            total_cenarios += 1
                            cenarios_desta_feature += 1
                
                dados_features.append({
                    'nome': nome_feature,
                    'qtd': cenarios_desta_feature,
                    'data': data_modificacao
                })

    return total_features, total_cenarios, dados_features, tags_contador

if __name__ == '__main__':
    features, cenarios, lista_features, tags_contador = gerar_metricas_bdd()
    
    print("# 📊 Dashboard Executivo de Qualidade (BDD)\n")
    print(f"> 🕒 *Última atualização do dashboard: {datetime.now().strftime('%d/%m/%Y %H:%M')}*\n")
    
    print("## 🎯 Resumo Global")
    print(f"- **Total de Funcionalidades:** {features}")
    print(f"- **Total de Cenários de Teste:** {cenarios}\n")
    
    print("---")
    print("## 📂 Detalhamento por Funcionalidade")
    print("| Feature | Cenários | Última Modificação |")
    print("|:---|:---:|:---:|")
    for f in lista_features:
        print(f"| **{f['nome']}** | {f['qtd']} | {f['data']} |")
        
    print("\n---")
    print("## 🏷️ Mapeamento de Tags")
    print("| Tag | Quantidade de Usos |")
    print("|---|---|")
    for tag, qtd in tags_contador.most_common():
        print(f"| `{tag}` | {qtd} |")