# CHANGELOG

## INN v1.010 — Formulário, Águia e publicação

Data: 21/07/2026

### Cadastro de leads

* Adicionados os campos `contato` (responsável) e `segmento` (classificação de mercado) à tabela `leads` no Supabase.
* Incluídos os campos Contato Responsável e Segmento de Mercado no formulário aberto pelo botão `+`.
* Contato passou a participar da busca por duplicidade, da ficha do lead e da exportação CSV.
* Segmento passou a participar da ficha do lead e da exportação CSV.
* Tipos de cliente ampliados: Residencial, Empresarial, Rural, Industrial e Outro.
* Preço automático: Rural usa R$ 3.500/kWp e Industrial usa R$ 3.200/kWp.
* Concessionária continua com Equatorial como padrão; o campo avançado oferece lista de distribuidoras e permite digitar outra opção.

### Águia

* Criada a ferramenta Águia para criar leads por foto ou câmera.
* OCR local lê cartões, fichas e fachadas; a imagem é ampliada e tratada para melhorar a leitura de placas.
* A localização GPS da foto, ou a localização autorizada do aparelho, gera um link para o Google Maps salvo em Referência.
* A localização não é mais repetida no Histórico/Informações.
* Limitação conhecida: fotos inclinadas, com reflexo ou fachada parcialmente obstruída podem exigir correção manual pelo botão Revisar.

### Publicação

* `salvar.bat` passou a publicar a branch atual com `git push origin HEAD:main`.
* Vercel configurado para revalidar o `index.html`, reduzindo o risco de celular abrir uma interface antiga em cache.

## INN v1.006

Data: 16/06/2026

### Governança

* Criado README.md
* Criado docs/MASTER_CONTEXT.md
* Estruturada documentação oficial do projeto

### Identidade

* Removido o termo CRM do planejamento futuro
* Nome oficial definido como INN

### Arquitetura

* Definido modelo Cliente + Histórico
* Definida estratégia anti-duplicidade

### Problemas conhecidos

* Parser de voz precisa evoluir
* Histórico de atividades ainda não implementado
* Leads duplicados ainda podem ocorrer
