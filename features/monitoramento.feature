# Autor: Rafael Cardoso
# Data Criacao: 20/02/2026
# Descrição: Fluxo final de monitoramento e conclusão da proposta

@modulo_monitoramento @regressivo
Funcionalidade: Monitoramento e Conclusão do Projeto
  Como integrador da SolAgora
  Quero fornecer as evidências de instalação e dados de geração
  Para concluir a jornada do projeto com sucesso

  Contexto:
    Dado que o projeto está na etapa de "Monitoramento"

  @envio_monitoramento_sucesso @prioridade_alta
  Cenário: Enviar evidências e dados de equipamento para monitoramento
    Quando faço o upload das fotos dos inversores e módulos instalados
    E preencho os dados do Inversor e dos Módulos (fabricante e potência)
    E clico em "Confirmar dados de monitoramento"
    Então o projeto deve ser enviado para análise da SolAgora
    E a tela deve exibir o status "Aguardando dados do integrador"

  @conclusao_projeto @smoke @sucesso
  Cenário: Visualizar a tela de projeto concluído
    Dado que todas as análises e documentos foram aprovados pela SolAgora
    Quando acesso o status final da jornada do projeto
    Então devo ver a mensagem "Esse projeto está concluído!"
    E devo conseguir avaliar a experiência do integrador na plataforma