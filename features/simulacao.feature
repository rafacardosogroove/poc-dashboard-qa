# Autor: Rafael Cardoso
# Data Criacao: 20/02/2026
# Descrição: Validação da simulação de financiamento na criação do projeto

@modulo_simulacao @regressivo
Funcionalidade: Simulação de Financiamento
  Como um integrador logado
  Quero simular os valores do projeto
  Para iniciar uma nova proposta de crédito

  Contexto:
    Dado que estou na tela de Simulação de Financiamento

  @simulacao_sucesso @smoke
  Cenário: Realizar simulação com dados válidos
    Quando preencho CPF/CNPJ e a renda comprovada
    E preencho o valor do projeto e seleciono o distribuidor
    E informo o valor gasto com energia e o valor da entrada
    E defino a data de vencimento da primeira parcela
    E clico no botão "Iniciar simulação"
    Então o sistema deve processar a simulação e avançar de etapa

  @simulacao_limite_valor @negativo
  Cenário: Bloquear simulação com valor do projeto inválido
    Quando preencho os dados do cliente e da simulação
    Mas o valor do projeto não respeita a regra de 50% do valor do equipamento
    E clico no botão "Iniciar simulação"
    Então o sistema não deve permitir o avanço e exibir um alerta de erro