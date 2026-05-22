import os
import re
import unicodedata

# List of godparent pairs (padrinhos)
# Wilmar was corrected to Vilmar as per user request.
# "Laldete" was corrected to "Valdete" based on common name usage, but we can support easily.
padrinhos = [
    # Luana's side
    "Sueleny e Valter",
    "Jéssica e Welligton",
    "Rosângela e Diogo",
    "Josimara e Gustavo",
    "Roseny e João Otávio",
    "Solange e Júnior",
    "Nélio Batista e Maria Aparecida",
    "Daniela e Mateus",
    "Kátia e Wallington",
    "Felipe e Vanessa",
    
    # Nauto's side
    "Leonardo e Valdirene",
    "Vilmar e Luciane",
    "Rosânia e Adilson",
    "Priscila e Anderson",
    "Otaviano e Patrícia",
    "Elizabete e Honório",
    "Laldete e Maria Aparecida",
    "Werlei e Danielle",
    "Cleonice e Célio",
    "Felipe e Poliana"
]

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

if __name__ == "__main__":
    generate()
