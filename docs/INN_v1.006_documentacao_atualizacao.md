# INN - Atualização de Documentação v1.006

## REGRAS_NEGOCIO.md

### REGRA 006 - ÚLTIMA INTERAÇÃO

O INN deve priorizar relacionamento e não apenas cadastro.

Sempre que ocorrer qualquer interação:
- Ligação
- Visita
- Proposta
- Follow-up
- Observação
- Contrato

o sistema deve atualizar o campo:

ultima_interacao

A listagem principal de clientes deve ser ordenada por:

ultima_interacao DESC

e não por data de criação.

Objetivo:
Clientes ativos devem aparecer primeiro.

Exemplo:
Pedro Fábio foi cadastrado há 3 meses.
Se houve interação hoje, ele deve aparecer acima de clientes criados recentemente sem movimentação.

O INN deve funcionar como memória comercial do usuário.

---

## ROADMAP.md

### INN v1.007

#### Prioridade P1
- Eliminar duplicidade de clientes
- Implementar histórico de atividades
- Implementar campo ultima_interacao
- Ordenar clientes por última interação
- Criar lista de clientes recentes

#### Prioridade P2
- Criar lista de clientes esquecidos
- Alertas de follow-up

---

## MASTER_CONTEXT.md

### Descoberta 001

O INN não deve ser apenas um cadastro de clientes.

O INN deve atuar como memória comercial.

Todo cliente movimentado recentemente deve retornar ao topo da lista através do campo ultima_interacao.

Origem da descoberta:
Caso do cliente Pedro Fábio, que permaneceu ativo por meses mas não apareceu entre os registros recentes.
