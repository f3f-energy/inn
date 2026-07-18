from pathlib import Path
import subprocess

def branch(path='.'):
    try:
        return subprocess.check_output(
            ['git','branch','--show-current'],
            cwd=path,text=True).strip()
    except:
        return 'desconhecida'

def status(path='.'):
    try:
        out=subprocess.check_output(
            ['git','status','--short'],
            cwd=path,text=True)
        return 'LIMPO' if not out.strip() else 'ALTERAÇÕES'
    except:
        return 'SEM GIT'
