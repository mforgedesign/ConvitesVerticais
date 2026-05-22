# Changelog - 22/05/2026 18:04
## Troca do slug Luana&Nauto para LuanaeNauto

### Prompt que motivou a alteração:
> "Os convites não estão abrindo. Troca o slug "Luana&Nauto" para "LuanaeNauto" pra verificar se é isso"

### Explicação do Funcionamento:
- **Antes:** Os convites eram gerados dentro da pasta `Luana&Nauto/`, que continha o caractere especial `&` no caminho da URL (ex: `https://cliqueparaabrir.mforge.com/Luana%26Nauto/NomeDoConvidado.html`). O caractere `&` causava problemas de navegação e resolução no servidor do GitHub Pages.
- **Agora:** Os convites são gerados sob a pasta `LuanaeNauto/`, permitindo uma URL limpa sem caracteres especiais e eliminando erros de resolução de link no servidor (ex: `https://cliqueparaabrir.mforge.com/LuanaeNauto/NomeDoConvidado.html`).

### Código Antigo (`generate_invitations.py`):
```python
def generate():
    template_path = "index.html"
    output_dir = "Luana&Nauto"
```

### Código Novo (`generate_invitations.py`):
```python
def generate():
    template_path = "index.html"
    output_dir = "LuanaeNauto"
```
