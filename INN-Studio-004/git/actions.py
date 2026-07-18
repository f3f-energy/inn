import subprocess

def run(args,cwd='.'):
    return subprocess.run(args,cwd=cwd,text=True,capture_output=True)

def pull(cwd='.'): return run(['git','pull'],cwd)
def push(cwd='.'): return run(['git','push'],cwd)
def commit(msg,cwd='.'):
    run(['git','add','.'],cwd)
    return run(['git','commit','-m',msg],cwd)
