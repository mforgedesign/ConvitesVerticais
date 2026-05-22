# Changelog - 22/05/2026 17:55

**Prompt Motivador:**
> Tira aqueles demais arquivos que tão soltos no repositório, tem um monte de backup lá

---

## Explicação do Funcionamento

### Como funcionava antes:
Os arquivos de backup gerados para conformidade com a regra R6 (ex: `index_backup_X.html`, `styles_backup_X.css`, `lessons_backup_X.md`, `docs_backup_X.md`) eram gerados no diretório raiz e rastreados pelo Git, sendo exibidos na interface do repositório no GitHub.

### Como funciona agora:
- Foi criada a pasta `backups/` no diretório raiz para centralizar e organizar localmente todos os arquivos de backup do projeto.
- O arquivo `.gitignore` foi modificado para ignorar a pasta `backups/`, garantindo que backups nunca sejam rastreados ou enviados para o repositório no GitHub.
- Todos os arquivos de backup existentes no diretório raiz foram desrastreados do Git (usando `git rm --cached`) e movidos fisicamente para o diretório `backups/`.

---

## Código Antigo

### `.gitignore` (completo)
```text
venv/
*.pyc
__pycache__/
.DS_Store
.vscode/
.idea/
```

---

## Código Novo

### `.gitignore` (completo)
```text
venv/
*.pyc
__pycache__/
.DS_Store
.vscode/
.idea/
backups/
```
