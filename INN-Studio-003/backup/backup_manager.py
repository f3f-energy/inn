from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from datetime import datetime

def create_backup(project_path):
    project=Path(project_path)
    out=project/'backups'
    out.mkdir(exist_ok=True)
    name=out/f'backup_{datetime.now():%Y%m%d_%H%M%S}.zip'
    with ZipFile(name,'w',ZIP_DEFLATED) as z:
        for p in project.rglob('*'):
            if '.git' in p.parts or 'backups' in p.parts:
                continue
            if p.is_file():
                z.write(p,p.relative_to(project))
    return name
