import json
from pathlib import Path
def load():
    f=Path('version.json')
    return json.loads(f.read_text(encoding='utf-8')) if f.exists() else {}
