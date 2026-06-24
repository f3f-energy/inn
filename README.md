# INN — CRM Solar F3F Energy

CRM de vendas de energia solar. Gerencia o funil completo desde a prospecção até o fechamento.

## Acesso rápido

| | |
|---|---|
| **App** | https://inn-sepia.vercel.app |
| **Banco** | Supabase — projeto `nmzifhqivuhdfwlelmxp` |
| **Repo** | https://github.com/f3f-energy/inn |

## Como publicar uma atualização

1. Edite `index.html`
2. Execute **`salvar.bat`** — ele faz tudo automaticamente:
   - Cria backup com timestamp em `backups/`
   - Incrementa a versão
   - Commit + push para o GitHub
   - Vercel faz o deploy em ~30 segundos

## Funil de vendas

```
Sondar → Lead → Agendar → Visitar → Prospect → Proposta → Contrato → Procuração → Fechado
```

## Importar contatos

```bash
python importar_contatos.py
```

Lê `contatos.json` e envia em lotes para o Supabase. Seguro rodar múltiplas vezes (ignora duplicatas).

## Stack

- React 18 (via CDN) + Babel standalone
- Supabase (PostgreSQL)
- Vercel (deploy automático no push para `main`)
- Arquivo único: `index.html`
