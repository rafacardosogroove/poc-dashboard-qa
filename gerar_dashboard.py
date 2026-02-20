import os
import subprocess
from collections import Counter
from datetime import datetime

def get_last_committer():
    try:
        # Comando para pegar o nome do último autor no Git
        return subprocess.check_output(["git", "log", "-1", "--format=%an"]).decode().strip()
    except:
        return "Robô de QA"

def contar_arquivos(diretorio, extensao):
    contador = 0
    if os.path.exists(diretorio):
        for root, _, files in os.walk(diretorio):
            for file in files:
                if file.endswith(extensao):
                    contador += 1
    return contador

def gerar_metricas_bdd(diretorio='features'):
    total_features = 0
    total_cenarios = 0
    tags_contador = Counter()
    dados_features = []

    if os.path.exists(diretorio):
        for root, _, files in os.walk(diretorio):
            for file in files:
                if file.endswith('.feature'):
                    caminho_arquivo = os.path.join(root, file)
                    timestamp = os.path.getmtime(caminho_arquivo)
                    data_modificacao = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y')
                    
                    total_features += 1
                    cenarios_desta_feature = 0
                    nome_feature = "Sem nome"
                    
                    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                        for linha in f:
                            linha_limpa = linha.strip()
                            palavras = linha_limpa.split()
                            for p in palavras:
                                if p.startswith('@'): tags_contador[p] += 1
                            if linha_limpa.startswith(('Funcionalidade:', 'Feature:')):
                                nome_feature = linha_limpa.split(':', 1)[1].strip()
                            if linha_limpa.startswith(('Cenário:', 'Cenario:', 'Scenario:')):
                                total_cenarios += 1
                                cenarios_desta_feature += 1
                    
                    dados_features.append({'nome': nome_feature, 'qtd': cenarios_desta_feature, 'data': data_modificacao})

    return total_features, total_cenarios, dados_features, tags_contador

if __name__ == '__main__':
    # Coleta dados de Negócio (BDD)
    features, cenarios, lista_features, tags = gerar_metricas_bdd()
    
    # Coleta dados Técnicos (Automação) - Ajuste os nomes das pastas se precisar!
    total_pages = contar_arquivos('pages', '.py')
    total_tests = contar_arquivos('tests', '.py')
    autor = get_last_committer()
    
    print("# 📊 Dashboard de Engenharia de Qualidade - GrooveTech")
    print(f"> 👤 **Último Push por:** {autor} | 🕒 **Atualizado em:** {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
    
    print("## 🚀 Status da Automação")
    print(f"| Categoria | Quantidade |")
    print(f"| :--- | :---: |")
    print(f"| 📝 Cenários BDD | {cenarios} |")
    print(f"| 📄 Page Objects | {total_pages} |")
    print(f"| 🧪 Scripts de Teste | {total_tests} |")
    
    print("\n## 📂 Detalhamento de Negócio (Features)")
    print("| Feature | Cenários | Modificação |")
    print("|:---|:---:|:---:|")
    for f in lista_features:
        print(f"| {f['nome']} | {f['qtd']} | {f['data']} |")
        
    print("\n## 🏷️ Cobertura de Tags")
    print("| Tag | Usos |")
    print("|---|---|")
    for tag, qtd in tags.most_common():
        print(f"| `{tag}` | {qtd} |")