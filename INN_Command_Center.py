import os
import webbrowser
import zipfile
from pathlib import Path

BASE = Path.cwd()
VERSION = BASE / 'version.txt'

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def versao():
    if VERSION.exists():
        return VERSION.read_text(encoding='utf-8').strip()
    return 'Nao definida'

def backup_zip():
    backup_dir = BASE / 'backups'
    backup_dir.mkdir(exist_ok=True)
    zip_path = backup_dir / 'INN_Backup.zip'

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in BASE.rglob('*'):
            if backup_dir in p.parents:
                continue
            if p.is_file():
                z.write(p, p.relative_to(BASE))

    print(f'Backup criado: {zip_path}')

while True:
    cls()
    print('=' * 55)
    print('INN COMMAND CENTER')
    print('=' * 55)
    print('Versao Atual:', versao())
    print()
    print('[1] Abrir INN')
    print('[2] Abrir GitHub')
    print('[3] Abrir Pasta do Projeto')
    print('[4] Gerar Backup ZIP')
    print('[5] Atualizar Versao')
    print('[0] Sair')
    print()

    op = input('Escolha: ').strip()

    if op == '1':
        webbrowser.open('https://inn-crm.vercel.app')
    elif op == '2':
        webbrowser.open('https://github.com/f3f-energy/inn-crm')
    elif op == '3':
        try:
            os.startfile(BASE)
        except Exception:
            print(BASE)
            input('ENTER...')
    elif op == '4':
        backup_zip()
        input('ENTER para continuar...')
    elif op == '5':
        v = input('Nova versao: ').strip()
        VERSION.write_text(v, encoding='utf-8')
        input('Versao atualizada. ENTER...')
    elif op == '0':
        break
