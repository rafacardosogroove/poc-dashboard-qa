@modulo_pagamento
Funcionalidade: Retirada de equipamento
  
  Cenário: Analise de credito 1
    Dado que escolho Pix
    Então vejo o QR Code

  Cenário: Pagamento via Boleto
    Dado que escolho Boleto
    Então o código de barras é gerado


    Cenário: Analise de credito 2
    Dado que escolho Cartão
    Então a compra é processada

@modulo_equipamentos
 Cenário: Analise de credito 3
    Dado que escolho Cartão
    Então a compra é processada

@modulo_equipamentos_old
 Cenário: Analise de credito 4
    Dado que escolho Cartão
    Então a compra é processada

