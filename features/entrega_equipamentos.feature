# Autor: Rafael Cardoso
# Data Criacao: 20/02/2026
# Descrição: Confirmação de entrega de equipamentos no local de instalação

@modulo_entrega @regressivo
Funcionalidade: Confirmação de Entrega de Equipamentos
  Como integrador da SolAgora
  Quero confirmar que a entrega foi realizada
  Para que o cliente receba a notificação de confirmação

  Contexto:
    Dado que o projeto está na etapa de "Entrega dos equipamentos"

  @confirma_entrega_integrador @smoke
  Cenário: Confirmar a entrega no endereço do cliente
    Quando visualizo o modal de confirmação do endereço de instalação
    E clico no botão "Confirmar entrega e avisar cliente"
    Então o sistema deve registrar a entrega
    E o status deve mudar para "Aguardando confirmação do consumidor"

  @reenvio_notificacao_cliente @notificacao
  Cenário: Reenviar notificação de recebimento para o cliente
    Dado que a entrega já foi confirmada pelo integrador
    Quando clico no botão "Reenviar mensagem e notificação"
    Então uma nova mensagem de WhatsApp deve ser enviada ao cliente final