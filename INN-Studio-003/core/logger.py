from pathlib import Path
from datetime import datetime
LOG=Path('logs'); LOG.mkdir(exist_ok=True)
def info(msg):
    with open(LOG/'studio.log','a',encoding='utf-8') as f:
        f.write(f'[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}\n')
