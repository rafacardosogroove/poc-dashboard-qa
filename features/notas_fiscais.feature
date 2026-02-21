# Autor: Rafael Cardoso
# Data Criacao: 20/02/2026
# Descrição: Upload e validação das notas fiscais e documentos adicionais

@modulo_notas_fiscais @regressivo
Funcionalidade: Envio de Notas Fiscais
  Como integrador da SolAgora
  Quero enviar as notas fiscais e dados dos equipamentos
  Para avançar com a liberação do crédito

  Contexto:
    Dado que o projeto está na etapa de "Notas Fiscais"

  @envio_notas_sucesso @prioridade_alta
  Cenário: Enviar notas fiscais completas do projeto
    Quando faço o upload do PDF da Nota Fiscal do Equipamento e do Serviço
    E preencho os números e valores correspondentes das notas
    E faço o upload da Carta de Correção e Comprovante de Pagamento
    E informo os fabricantes e as quantidades de inversores e módulos
    E clico em "Enviar notas e informações"
    Então o sistema deve salvar os dados e exibir sucesso

  @envio_notas_aguardando @status
  Cenário: Verificar status de análise de notas fiscais
    Quando o envio das notas fiscais for concluído
    Então a tela deve exibir o status "Aguardando documentação de equipamento entregue"
    E informar que o tempo estimado para conclusão é de 2 dias úteis