# REGRAS DE NEGÓCIO

## REGRA 001 - CLIENTE ÚNICO

Cada cliente possui apenas um cadastro principal.

Não criar novo cliente quando já existir:

* Mesmo telefone
* Mesmo documento
* Nome muito semelhante

---

## REGRA 002 - HISTÓRICO OBRIGATÓRIO

Toda interação deve gerar histórico.

Exemplos:

* Ligação
* Visita
* Proposta
* Follow-up
* Contrato
* Observação

---

## REGRA 003 - ANTI-DUPLICIDADE

Antes de criar um cliente:

1. Buscar telefone.
2. Buscar documento.
3. Buscar nome semelhante.

Se existir:

* Atualizar histórico.

Se não existir:

* Criar cliente.

---

## REGRA 004 - VOZ CONVERSACIONAL

O sistema deve solicitar informações faltantes.

Exemplo:

Usuário:
Criar cliente

Sistema:
Qual o nome do cliente?

---

## REGRA 005 - FONTE DA VERDADE

A documentação oficial do INN está no GitHub.

Arquivos oficiais:

* MASTER_CONTEXT.md
* CHANGELOG.md
* ROADMAP.md
* REGRAS_NEGOCIO.md
