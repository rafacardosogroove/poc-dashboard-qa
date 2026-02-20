import os
from collections import Counter, defaultdict

def gerar_metricas_bdd(diretorio='features'):
    total_features = 0
    total_cenarios = 0
    tags_contador = Counter()
    cenarios_por_feature = defaultdict(int)

    for root, _, files in os.walk(diretorio):
        for file in files:
            if file.endswith('.feature'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    feature_atual = "Feature Desconhecida"
                    tem_feature = False
                    
                    for linha in f:
                        linha_limpa = linha.strip()
                        
                        # 1. Captura todas as tags da linha (palavras que começam com @)
                        palavras = linha_limpa.split()
                        for palavra in palavras:
                            if palavra.startswith('@'):
                                tags_contador[palavra] += 1
                                
                        # 2. Identifica o nome da Funcionalidade
                        if linha_limpa.startswith(('Funcionalidade:', 'Feature:')):
                            feature_atual = linha_limpa.split(':', 1)[1].strip()
                            if not tem_feature:
                                total_features += 1
                                tem_feature = True
                            
                        # 3. Conta os cenários e vincula à funcionalidade atual
                        if linha_limpa.startswith(('Cenário:', 'Cenario:', 'Esquema do Cenário:', 'Scenario:')):
                            total_cenarios += 1
                            cenarios_por_feature[feature_atual] += 1

    return total_features, total_cenarios, cenarios_por_feature, tags_contador

if __name__ == '__main__':
    features, cenarios, cenarios_por_feature, tags_contador = gerar_metricas_bdd()
    
    # Gerando o Markdown com cara de Dashboard Profissional
    print("# 📊 Dashboard Executivo de Qualidade (BDD)\n")
    print("*(Relatório gerado e atualizado automaticamente)*\n")
    
    print("## 🎯 Resumo Global")
    print(f"- **Total de Funcionalidades (Features):** {features}")
    print(f"- **Total de Cenários de Teste:** {cenarios}\n")
    
    print("---")
    print("## 📂 Cenários por Funcionalidade")
    for feature, qtd in cenarios_por_feature.items():
        print(f"- **{feature}**: {qtd} cenário(s)")
        
    print("\n---")
    print("## 🏷️ Mapeamento de Tags")
    print("| Tag | Quantidade de Usos |")
    print("|---|---|")
    
    # Mostra as tags da mais usada para a menos usada
    for tag, qtd in tags_contador.most_common():
        print(f"| `{tag}` | {qtd} |")