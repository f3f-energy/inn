import urllib.request
import urllib.error
import json
import time

SUPA_URL = "https://nmzifhqivuhdfwlelmxp.supabase.co"
SUPA_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5temlmaHFpdnVoZGZ3bGVsbXhwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQxMTgzNzgsImV4cCI6MjA4OTY5NDM3OH0.AFi43M_euM7iztzOyCamh1HGen3SiBUXQtfknBoWTcc"

print("Lendo contatos...")

with open("contatos.json", "r", encoding="utf-8") as f:
    contatos = json.load(f)

print(f"Total: {len(contatos)} contatos para importar")

sucesso = 0
erros = 0
LOTE = 50

for i in range(0, len(contatos), LOTE):

    lote = contatos[i:i + LOTE]

    payload = json.dumps(lote, ensure_ascii=False).encode("utf-8")

    req = urllib.request.Request(
        f"{SUPA_URL}/rest/v1/leads",
        data=payload,
        method="POST"
    )

    req.add_header("apikey", SUPA_KEY)
    req.add_header("Authorization", f"Bearer {SUPA_KEY}")
    req.add_header("Content-Type", "application/json")
    req.add_header("Prefer", "resolution=ignore-duplicates")

    try:

        with urllib.request.urlopen(req, timeout=30) as r:
            sucesso += len(lote)
            print(f"OK: {sucesso}/{len(contatos)}")

    except urllib.error.HTTPError as e:

        erros += len(lote)

        print("\n")
        print("=" * 60)
        print(f"ERRO NO LOTE {i}")
        print("=" * 60)

        try:
            detalhe = e.read().decode("utf-8")
            print(detalhe)
        except:
            print("Sem detalhes retornados pelo Supabase.")

        print("=" * 60)
        print("\n")

    except Exception as e:

        erros += len(lote)

        print("\n")
        print("=" * 60)
        print(f"ERRO GERAL NO LOTE {i}")
        print("=" * 60)
        print(str(e))
        print("=" * 60)
        print("\n")

    time.sleep(0.2)

print("\n")
print("=" * 60)
print("IMPORTAÇÃO FINALIZADA")
print("=" * 60)
print(f"Sucesso: {sucesso}")
print(f"Erros:   {erros}")
print("=" * 60)

input("\nPressione ENTER para fechar...")

