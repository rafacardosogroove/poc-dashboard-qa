@modulo_pagamento
Funcionalidade: Teste de Pagamento
  
  Cenário: Pagamento via Pix aprovado
    Dado que escolho Pix
    Então vejo o QR Code

  Cenário: Pagamento via Boleto
    Dado que escolho Boleto
    Então o código de barras é gerado