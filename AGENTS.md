# INN CRM — Contexto para Codex

## O que é este projeto
CRM solar da F3F Energy chamado **INN** (Innovatis). Gerencia leads de energia solar do funil de vendas completo. Roda como um único `index.html` com React via CDN + Supabase como banco de dados. Hospedado no Vercel com deploy automático via GitHub.

## Estrutura de arquivos

```
C:\_a\inn\
├── index.html          ← APP COMPLETO (único arquivo editável do frontend)
├── vercel.json         ← Configuração do Vercel (não editar sem necessidade)
├── version.txt         ← Versão atual (ex: 1.010) — atualizado pelo salvar.bat
├── version.json        ← Versão em JSON {"version":"1.010"}
├── salvar.bat          ← SCRIPT PRINCIPAL: backup + commit + push
├── inn-deploy.bat      ← Deploy rápido (sem mudanças locais)
├── importar_contatos.py← Importação em lote de contatos.json para Supabase
├── contatos.json       ← Base de contatos para importação
├── backups/            ← Backups automáticos com timestamp (nunca apagar)
└── docs/               ← Documentação adicional
```

## URLs canônicas — NUNCA errar estas

| Recurso | URL |
|---|---|
| App em produção | https://inn-sepia.vercel.app |
| Vercel dashboard | https://vercel.com/f3f-energy/inn |
| GitHub repo | https://github.com/f3f-energy/inn |
| Supabase projeto | https://nmzifhqivuhdfwlelmxp.supabase.co |

**ATENÇÃO:** A URL do app é `inn-sepia.vercel.app`. Nunca usar `inn-crm-f3f-energy.vercel.app` (URL antiga, incorreta).

## Supabase

- **URL:** `https://nmzifhqivuhdfwlelmxp.supabase.co`
- **Anon key:** hardcoded no `index.html` linha 26 e no `importar_contatos.py` linha 7
- A anon key é pública por design do Supabase — não é um vazamento de segurança
- Tabela principal: `leads`
- Segurança via Row Level Security (RLS) no painel do Supabase

### Schema da tabela `leads`
Campos principais usados no app:
```
id, name, type, phone1, phone2, email, status, city, state,
value, kwp, history, probability, owner, visit_or_call,
budget, proposal, delivered, closed, post_sales,
concessionaria, prospectando, referencia, indicacao, hot
```

### Status do funil (em ordem)
```
sondar → lead → agendar → visitar → prospect → proposal → contract → power-of-attorney → client
```

## Deploy — fluxo correto

```
Editar index.html
    ↓
Rodar salvar.bat   (faz backup automático + commit + push)
    ↓
Vercel detecta push na branch main → deploy automático (~30s)
    ↓
inn-sepia.vercel.app atualizado
```

**Nunca** fazer `git push --force`. **Nunca** editar `version.txt` ou `version.json` manualmente — o `salvar.bat` cuida disso.

## Stack técnica

- **Frontend:** React 18 via CDN (UMD), Babel standalone para JSX no browser
- **Banco:** Supabase (PostgreSQL gerenciado)
- **Hospedagem:** Vercel (static site, plano Hobby)
- **Versionamento:** GitHub — `f3f-energy/inn`, branch `main`
- **Sem build step:** o `index.html` é servido diretamente, sem npm/webpack/vite

## Regras de edição

1. **Único arquivo frontend:** todo o código React, CSS e lógica está em `index.html`
2. **Sempre backup antes de mudança grande:** rodar `salvar.bat` ou copiar manualmente para `backups/`
3. **Não criar arquivos `.js` separados** — o projeto é intencionalmente um HTML único
4. **Não adicionar npm/package.json** sem aprovação explícita do usuário
5. **Não mudar `vercel.json`** sem necessidade — está configurado corretamente

## Preços por tipo (usados no cálculo automático kWp ↔ R$)
```
Residencial: R$ 3.500/kWp
Empresarial: R$ 3.200/kWp
Outro:       R$ 3.500/kWp
```

## Importação de contatos
Para importar `contatos.json` para o Supabase:
```
cd C:\_a\inn
python importar_contatos.py
```
Usa `Prefer: resolution=ignore-duplicates` — seguro rodar múltiplas vezes.
