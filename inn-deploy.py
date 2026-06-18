import urllib.request
import urllib.error
import json
import base64
import os
import shutil
import webbrowser

TOKEN = "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"
REPO = "f3f-energy/inn-crm"

PASTA = r"C:\Users\ferna\Desktop\inn"
DOWNLOADS = r"C:\Users\ferna\Documents\Downloads"

VERCEL = "https://inn-crm.vercel.app"

print("=======================================")
print(" INN Deploy - Upload direto pro GitHub")
print("=======================================\n")

# Procurar INN.html nos Downloads
inn_download = os.path.join(DOWNLOADS, "INN.html")
inn_atual = os.path.join(PASTA, "index.html")

if os.path.exists(inn_download):
    print("[OK] Novo INN.html encontrado nos Downloads")
    shutil.copy2(inn_download, inn_atual)
    os.remove(inn_download)
    print("[OK] Copiado para index.html\n")
else:
    print("[INFO] Usando index.html atual\n")

# Ler index.html
with open(inn_atual, "r", encoding="utf-8") as f:
    content = f.read()

print(f"Arquivo lido: {len(content)} bytes")

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "INN-Deploy",
    "Content-Type": "application/json"
}

# Obter SHA atual
print("Conectando ao GitHub...")

req = urllib.request.Request(
    f"https://api.github.com/repos/{REPO}/contents/index.html",
    headers=headers
)

try:
    with urllib.request.urlopen(req, timeout=15) as r:
        data = json.loads(r.read())
        sha = data.get("sha", "")
        print(f"[OK] SHA atual: {sha[:12]}...")
except Exception as e:
    print(f"[ERRO] {e}")
    sha = ""

# Upload
print("Fazendo upload...")

payload = json.dumps({
    "message": "INN deploy automatico",
    "content": base64.b64encode(
        content.encode("utf-8")
    ).decode("utf-8"),
    "sha": sha
}).encode("utf-8")

req2 = urllib.request.Request(
    f"https://api.github.com/repos/{REPO}/contents/index.html",
    data=payload,
    method="PUT",
    headers=headers
)

try:
    with urllib.request.urlopen(req2, timeout=60) as r:
        result = json.loads(r.read())

        print("\n[OK] Publicado com sucesso")
        print(
            f"Commit: {result['commit']['sha'][:12]}"
        )

        print("\n=======================================")
        print(" Aguarde 30 segundos")
        print(f" {VERCEL}")
        print("=======================================")

except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f"[ERRO] {e.code}")
    print(body[:500])

except Exception as e:
    print(f"[ERRO] {e}")

resp = input(
    "\nAbrir o INN no navegador? (S/N): "
)

if resp.upper() == "S":
    webbrowser.open(VERCEL)

input("\nPressione ENTER para fechar...")