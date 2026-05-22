# Changelog - 22/05/2026 18:15
## slugs_de_convites_como_pastas

### Prompt Motivador
"Não tá abrindo. Você escreveu os slugs na lista mas não configurou no github, pelo visto."

### Funcionamento Anterior
Os convites individuais eram gerados como arquivos HTML individuais (ex: `LuanaeNauto/CleoniceeCelio.html`) diretamente na subpasta. No entanto, para suportar URLs amigáveis sem a extensão `.html` (ex: `https://cliqueparaabrir.mforge.com/LuanaeNauto/CleoniceeCelio`), o GitHub Pages exige que cada recurso seja uma pasta contendo um arquivo `index.html`. Da maneira anterior, a requisição resultava em erro 404 (Not Found).

### Funcionamento Atual
Agora, o script `generate_invitations.py` cria um diretório específico para cada casal de padrinhos (ex: `LuanaeNauto/CleoniceeCelio/`) e gera o arquivo `index.html` dentro dele. Os caminhos relativos de estilo e imagens foram atualizados de `../` para `../../` para subir os dois níveis de diretório necessários. Com essa estrutura, o GitHub Pages resolve a URL limpa corretamente, servindo o convite do padrinho sem a extensão `.html`.

### Código Antigo (`generate_invitations.py`)
```python
def sanitize_filename(name):
    # Normalize unicode characters to decompose them into letters and diacritics
    name = unicodedata.normalize('NFKD', name)
    # Remove diacritics
    name = "".join([c for c in name if not unicodedata.combining(c)])
    # Remove spaces
    name = name.replace(" ", "")
    # Remove any other non-alphanumeric characters (keeping case)
    name = re.sub(r'[^a-zA-Z0-9]', '', name)
    return f"{name}.html"

# ...
    for pair in padrinhos:
        filename = sanitize_filename(pair)
        filepath = os.path.join(output_dir, filename)
        
        # Replace the placeholders in the template
        content = template_content.replace(
            "<title>Convite Especial - Bruna e Vitor</title>",
            f"<title>Convite Especial - {pair}</title>"
        )
        content = content.replace(
            '<h1 class="names">Bruna e Vitor</h1>',
            f'<h1 class="names">{pair}</h1>'
        )
        content = content.replace('styles.css', '../styles.css')
        content = content.replace('assets/processed/', '../assets/processed/')
```

### Código Novo (`generate_invitations.py`)
```python
def sanitize_foldername(name):
    # Normalize unicode characters to decompose them into letters and diacritics
    name = unicodedata.normalize('NFKD', name)
    # Remove diacritics
    name = "".join([c for c in name if not unicodedata.combining(c)])
    # Remove spaces
    name = name.replace(" ", "")
    # Remove any other non-alphanumeric characters (keeping case)
    name = re.sub(r'[^a-zA-Z0-9]', '', name)
    return name

# ...
    for pair in padrinhos:
        foldername = sanitize_foldername(pair)
        guest_dir = os.path.join(output_dir, foldername)
        os.makedirs(guest_dir, exist_ok=True)
        filepath = os.path.join(guest_dir, "index.html")
        
        # Replace the placeholders in the template
        content = template_content.replace(
            "<title>Convite Especial - Bruna e Vitor</title>",
            f"<title>Convite Especial - {pair}</title>"
        )
        content = content.replace(
            '<h1 class="names">Bruna e Vitor</h1>',
            f'<h1 class="names">{pair}</h1>'
        )
        content = content.replace('styles.css', '../../styles.css')
        content = content.replace('assets/processed/', '../../assets/processed/')
```
