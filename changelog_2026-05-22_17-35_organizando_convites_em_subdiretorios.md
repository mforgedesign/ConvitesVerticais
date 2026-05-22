# Changelog - 22/05/2026 17:35

**Prompt Motivador:**
> Você enviou todos os arquivos para o repositório? Deveria enviar apenas os convites dentro dos respectivos slugs, pra ficar, por exemplo, assim o url de cada um: cliqueparaabrir.mforge.com/Luana&Nauto/CleoniceeCelio

---

## Explicação do Funcionamento

### Como funcionava antes:
Os convites individuais de padrinhos eram gerados diretamente no diretório raiz do projeto com o padrão de nome de arquivo `slug-com-hifens.html` (por exemplo, `cleonice-e-celio.html`). Isso poluía o diretório raiz e produzia URLs longas sem separação por casamento.

### Como funciona agora:
- O script gerador `generate_invitations.py` foi modificado para gerar os arquivos HTML dentro do subdiretório de slug de casamento `Luana&Nauto/`.
- O padrão de nomenclatura dos arquivos de convite mudou de `slug-com-hifens.html` para `CamelCase` sem hifens nem espaços (ex: `CleoniceeCelio.html`), permitindo que a URL final seja acessada em `cliqueparaabrir.mforge.com/Luana&Nauto/CleoniceeCelio` (aproveitando o recurso de URLs amigáveis do GitHub Pages).
- O script altera dinamicamente os caminhos relativos dos assets e folha de estilos (`styles.css` vira `../styles.css` e `assets/processed/` vira `../assets/processed/`) ao gravar cada convite personalizado.
- Todos os arquivos HTML antigos na raiz do repositório foram removidos.

---

## Código Antigo

### `generate_invitations.py` (linhas 34-89)
```python
def sanitize_filename(name):
    # Convert to lowercase
    name = name.lower()
    # Normalize unicode characters to decompose them into letters and diacritics
    name = unicodedata.normalize('NFKD', name)
    # Remove diacritics
    name = "".join([c for c in name if not unicodedata.combining(c)])
    # Replace anything that isn't a letter or space with empty string
    name = re.sub(r'[^a-z0-9\s-]', '', name)
    # Replace spaces with hyphens
    name = re.sub(r'\s+', '-', name)
    # Return sanitized name with .html extension
    return f"{name}.html"

def generate():
    template_path = "index.html"
    
    if not os.path.exists(template_path):
        print("Error: index.html template not found.")
        return
        
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()
        
    print(f"Loaded template from {template_path}.")
    
    generated_files = []
    
    for pair in padrinhos:
        filename = sanitize_filename(pair)
        
        # Replace the placeholders in the template
        # 1. Title tag: <title>Convite Especial - Bruna e Vitor</title>
        content = template_content.replace(
            "<title>Convite Especial - Bruna e Vitor</title>",
            f"<title>Convite Especial - {pair}</title>"
        )
        
        # 2. Header heading: <h1 class="names">Bruna e Vitor</h1>
        content = content.replace(
            '<h1 class="names">Bruna e Vitor</h1>',
            f'<h1 class="names">{pair}</h1>'
        )
        
        # Write the customized HTML file
        with open(filename, "w", encoding="utf-8") as f_out:
            f_out.write(content)
            
        generated_files.append(filename)
        print(f"Generated: {filename} for {pair}")
        
    print(f"\nSuccessfully generated {len(generated_files)} invitation files.")
```

---

## Código Novo

### `generate_invitations.py` (linhas 34-89)
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

def generate():
    template_path = "index.html"
    output_dir = "Luana&Nauto"
    
    if not os.path.exists(template_path):
        print("Error: index.html template not found.")
        return
        
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()
        
    print(f"Loaded template from {template_path}.")
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    print(f"Ensured output directory '{output_dir}' exists.")
    
    generated_files = []
    
    for pair in padrinhos:
        filename = sanitize_filename(pair)
        filepath = os.path.join(output_dir, filename)
        
        # Replace the placeholders in the template
        # 1. Title tag: <title>Convite Especial - Bruna e Vitor</title>
        content = template_content.replace(
            "<title>Convite Especial - Bruna e Vitor</title>",
            f"<title>Convite Especial - {pair}</title>"
        )
        
        # 2. Header heading: <h1 class="names">Bruna e Vitor</h1>
        content = content.replace(
            '<h1 class="names">Bruna e Vitor</h1>',
            f'<h1 class="names">{pair}</h1>'
        )
        
        # 3. Adjust asset paths for the subdirectory structure
        content = content.replace('styles.css', '../styles.css')
        content = content.replace('assets/processed/', '../assets/processed/')
        
        # Write the customized HTML file
        with open(filepath, "w", encoding="utf-8") as f_out:
            f_out.write(content)
            
        generated_files.append(filepath)
        print(f"Generated: {filepath} for {pair}")
        
    print(f"\nSuccessfully generated {len(generated_files)} invitation files under '{output_dir}'.")
```
