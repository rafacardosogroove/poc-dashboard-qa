@modulo_equipamento
Funcionalidade: Teste de Pagamento
  
  Cenário: equipamento 1
    Então vejo o QR Code

@modulo_equipamento
  Cenário: equipamento 2
    Dado que escolho Boleto
    Então o código de barras é gerado


    Cenário: equipamento 3
    Dado que escolho Cartão
    Então a compra é processada

@modulo_equipamentos
 Cenário:equipamento 4
    Dado que escolho Cartão
    Então a compra é processada

