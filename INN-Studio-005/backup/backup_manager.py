from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from datetime import datetime
def create_backup(project_path):
    p=Path(project_path)
    out=p/'backups'
    out.mkdir(exist_ok=True)
    dest=out/f'backup_{datetime.now():%Y%m%d_%H%M%S}.zip'
    with ZipFile(dest,'w',ZIP_DEFLATED) as z:
        for f in p.rglob('*'):
            if f.is_file() and '.git' not in f.parts and 'backups' not in f.parts:
                z.write(f,f.relative_to(p))
    return dest
