# Autor: Rafael Cardoso
# Data Criacao: 20/02/2026
# Descrição: Validação dos formulários de análise de crédito para PF e PJ

@modulo_analise_credito @regressivo
Funcionalidade: Solicitação de Análise de Crédito
  Como um parceiro integrador da SolAgora
  Quero enviar os dados do meu cliente
  Para verificar se ele tem crédito aprovado para o projeto solar

  Contexto:
    Dado que inicio um novo projeto na plataforma SolAgora

  @pf @smoke
  Cenário: Enviar dados de Pessoa Física para análise com sucesso
    Quando preencho as informações pessoais com nome e CPF válidos
    E informo os dados de contato do cliente
    E preencho o endereço de instalação com um CEP válido
    E clico em "Enviar para análise de crédito"
    Então o sistema deve processar a solicitação com sucesso

   @pf @smoke
  Cenário: Enviar dados de Pessoa Jurídica para análise com sucesso
    Quando seleciono a opção de Pessoa Jurídica
    E preencho a Razão Social e o CNPJ
    E informo os dados de contato do sócio representante legal
    E preencho o endereço de instalação
    E clico em "Enviar para análise de crédito"
    Então a solicitação da empresa deve ser enviada para processamento

  @validacao_cep @negativo
  Cenário: Tentar avançar com CEP de instalação inválido
    Quando preencho os dados iniciais do cliente
    Mas informo um CEP inexistente no endereço de instalação
    E tento enviar para análise de crédito
    Então o sistema