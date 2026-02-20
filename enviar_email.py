import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def enviar_relatorio():
    # Pega os dados dos Secrets do GitHub
    email_remetente = os.environ.get('EMAIL_USER')
    senha_remetente = os.environ.get('EMAIL_PASS')
    
    # ⚠️ MUDE PARA O SEU E-MAIL PARA TESTAR
    email_destinatario = "seu_email_aqui@exemplo.com" 
    
    try:
        # Lê o README que o robô acabou de atualizar no GitHub
        with open('README.md', 'r', encoding='utf-8') as f:
            conteudo_dashboard = f.read()

        msg = MIMEMultipart()
        msg['From'] = email_remetente
        msg['To'] = email_destinatario
        msg['Subject'] = f"📊 Relatório de Qualidade - SolAgora ({datetime.now().strftime('%d/%m')})"

        # O corpo do e-mail será o conteúdo exato do Dashboard
        msg.attach(MIMEText(conteudo_dashboard, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_remetente, senha_remetente)
        server.send_message(msg)
        server.quit()
        print("✅ E-mail enviado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")

if __name__ == '__main__':
    enviar_relatorio()