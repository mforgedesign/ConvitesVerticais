# Changelog - 22/05/2026 17:30

**Prompt Motivador:**
> Transforme o repositório https://github.com/mforgedesign/ConvitesVerticais em um GithubPages, e então publique os convites para que eu possa ter o url cliqueparaabrir.mforge.com. O CNAME já foi configurado no hostgator.
> 
> ghp_************************************ (github api key token classic)

---

## Explicação do Funcionamento

### Como funcionava antes:
O projeto era apenas local, sem controle de versão git inicializado, sem repositório remoto configurado para publicação e sem as configurações de deploy necessárias para servir os convites sob o domínio personalizado no GitHub Pages.

### Como funciona agora:
- Foi inicializado um repositório Git local no diretório do projeto.
- Criado o arquivo [CNAME](file:///c:/Users/Acer/Documents/VerticalBuilder/Testes/ConviteRoseGold/CNAME) apontando para o domínio `cliqueparaabrir.mforge.com` para que o GitHub Pages saiba para qual domínio direcionar as requisições HTTP.
- Criado o arquivo [.gitignore](file:///c:/Users/Acer/Documents/VerticalBuilder/Testes/ConviteRoseGold/.gitignore) para evitar o upload de arquivos temporários, caches e o ambiente virtual Python (`venv/`).
- O repositório local foi conectado ao repositório remoto `https://github.com/mforgedesign/ConvitesVerticais.git` utilizando autenticação via token pessoal do GitHub.
- Todos os arquivos do projeto foram publicados no ramo `main` do repositório remoto.
- O GitHub Pages foi ativado via API para servir os arquivos a partir da raiz `/` do ramo `main`, configurando o domínio customizado `cliqueparaabrir.mforge.com`.

---

## Código Antigo

*Nenhum arquivo anterior existia no repositório remoto (foi feita a publicação inicial do zero).*

---

## Código Novo

### `.gitignore`
```text
venv/
*.pyc
__pycache__/
.DS_Store
.vscode/
.idea/
```

### `CNAME`
```text
cliqueparaabrir.mforge.com
```
