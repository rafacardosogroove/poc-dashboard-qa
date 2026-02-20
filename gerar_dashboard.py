import os
import subprocess
from collections import Counter
from datetime import datetime

def get_last_committer():
    try:
        return subprocess.check_output(["git", "log", "-1", "--format=%an"]).decode(errors='ignore').strip()
    except:
        return "Robô de QA"

def get_git_commits(limit=5):
    try:
        output = subprocess.check_output(
            ["git", "log", f"-{limit}", "--format=%ad | %an | %s", "--date=format:%d/%m %H:%M"]
        ).decode(errors='ignore').strip()
        return output.split('\n')
    except:
        return ["Sem histórico de commits disponível"]

def get_top_contributors():
    try:
        output = subprocess.check_output(["git", "log", "--format=%an"]).decode(errors='ignore').strip()
        autores = output.split('\n')
        ranking = Counter(autores)
        return ranking.most_common(5)
    except:
        return []

def detalhar_arquivos(diretorio, extensao):
    lista_arquivos = []
    if os.path.exists(diretorio):
        for root, _, files in os.walk(diretorio):
            for file in files:
                if file.lower().endswith(extensao) and "__init__.py" not in file.lower():
                    nome_limpo = file.replace(extensao, "")
                    lista_arquivos.append(nome_limpo)
    return sorted(lista_arquivos)

def gerar_metricas_bdd(diretorio='features'):
    total_features, total_cenarios = 0, 0
    tags_contador = Counter()
    dados_features = []
    if os.path.exists(diretorio):
        for root, _, files in os.walk(diretorio):
            for file in files:
                if file.endswith('.feature'):
                    caminho = os.path.join(root, file)
                    data_m = datetime.fromtimestamp(os.path.getmtime(caminho)).strftime('%d/%m/%Y')
                    total_features += 1
                    cenarios_f, nome_f = 0, "Sem nome"
                    with open(caminho, 'r', encoding='utf-8') as f:
                        for linha in f:
                            l = linha.strip()
                            for p in l.split():
                                if p.startswith('@'): tags_contador[p] += 1
                            if l.startswith(('Funcionalidade:', 'Feature:')):
                                nome_f = l.split(':', 1)[1].strip()
                            if l.startswith(('Cenário:', 'Cenario:', 'Scenario:')):
                                total_cenarios += 1
                                cenarios_f += 1
                    dados_features.append({'nome': nome_f, 'qtd': cenarios_f, 'data': data_m})
    return total_features, total_cenarios, dados_features, tags_contador

if __name__ == '__main__':
    features, cenarios, lista_features, tags = gerar_metricas_bdd()
    pages_encontradas = detalhar_arquivos('pages', '.py')
    testes_encontrados = detalhar_arquivos('tests', '.py') 
    commits = get_git_commits()
    autor = get_last_committer()
    top_qas = get_top_contributors()
    
    print("# 📊 Dashboard de Engenharia de Qualidade - SolAgora")
    print(f"> 👤 **Último Push:** {autor} | 🕒 **Atualizado em:** {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
    
    print("## 🏆 Top QAs (Ranking de Commits)")
    print("| QA | Total de Pushes (Commits) |")
    print("|:---|:---:|")
    for qa, qtd in top_qas:
        print(f"| 👨‍💻 **{qa}** | {qtd} |")
    
    print("\n## 🚀 Status da Automação")
    print(f"| Categoria | Total |")
    print(f"| :--- | :---: |")
    print(f"| 📝 Cenários BDD | {cenarios} |")
    print(f"| 📄 Page Objects | {len(pages_encontradas)} |")
    print(f"| 🧪 Scripts de Teste | {len(testes_encontrados)} |")
    
    # Seção de Page Objects (Sanfona)
    print("\n### 📂 Page Objects Criados")
    if pages_encontradas:
        print("<details>")
        print(f"<summary><b>Clique para ver a lista de {len(pages_encontradas)} pages</b></summary>\n")
        print("<ul>")
        for p in pages_encontradas:
            print(f"<li><code>{p}</code></li>")
        print("</ul>")
        print("</details>")

    # NOVA Seção de Scripts de Teste (Sanfona Identica)
    print("\n### 🧪 Scripts de Teste Automatizados")
    if testes_encontrados:
        print("<details>")
        print(f"<summary><b>Clique para ver os {len(testes_encontrados)} scripts de teste</b></summary>\n")
        print("<ul>")
        for t in testes_encontrados:
            print(f"<li><code>{t}</code></li>")
        print("</ul>")
        print("</details>")
    else:
        print("*Nenhum script de teste encontrado na pasta /tests*")

    print("\n---")
    print("## 📂 Detalhamento de Negócio (Features)")
    print("| Feature | Cenários | Modificação |")
    print("|:---|:---:|:---:|")
    for f in lista_features:
        print(f"| {f['nome']} | {f['qtd']} | {f['data']} |")
        
    print("\n## 📜 Histórico Recente de Commits")
    print("| Data | Autor | Mensagem |")
    print("|:---|:---|:---|")
    for c in commits:
        cols = c.split(" | ")
        if len(cols) == 3:
            print(f"| {cols[0]} | **{cols[1]}** | {cols[2]} |")

    print("\n## 🏷️ Cobertura de Tags")
    print("| Tag | Usos |")
    print("|---|---|")
    for tag, qtd in tags.most_common():
        print(f"| `{tag}` | {qtd} |")