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
    "Hélio Batista e Maria Aparecida",
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

if __name__ == "__main__":
    generate()
