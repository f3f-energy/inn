import urllib.request, json

TOKEN = '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'
GIST = 'dc604652e59c3126043b3a7a3a6e02a4'

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

payload = json.dumps({'files': {'inn.html': {'content': content}}}).encode()
req = urllib.request.Request('https://api.github.com/gists/' + GIST, data=payload, method='PATCH')
req.add_header('Authorization', 'token ' + TOKEN)
req.add_header('Content-Type', 'application/json')
req.add_header('User-Agent', 'INN')

try:
    r = urllib.request.urlopen(req, timeout=30)
    print('Gist atualizado com sucesso!')
except Exception as e:
    print('Erro:', e)

input('Pressione Enter para fechar...')
