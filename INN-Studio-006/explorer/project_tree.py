from pathlib import Path

def list_files(project):
    p=Path(project)
    items=[]
    for f in sorted(p.rglob('*')):
        if '.git' in f.parts or 'backups' in f.parts:
            continue
        items.append(str(f.relative_to(p)))
    return items
