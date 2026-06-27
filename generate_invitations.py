import os
import re
import unicodedata

# List of godparents (padrinhos)
# Each guest can be a couple ("casal"), a single godmother ("madrinha"), or a single godfather ("padrinho").
padrinhos = [
    # Luana's side
    {"names": "Sueleny e Valter", "type": "casal"},
    {"names": "Jéssica e Welligton", "type": "casal"},
    {"names": "Rosângela e Diogo", "type": "casal"},
    {"names": "Josimara e Gustavo", "type": "casal"},
    {"names": "Roseny", "type": "madrinha"},
    {"names": "João Otávio", "type": "padrinho"},
    {"names": "Solange e Júnior", "type": "casal"},
    {"names": "Hélio Batista e Maria Aparecida", "type": "casal"},
    {"names": "Daniela e Mateus", "type": "casal"},
    {"names": "Kátia e Wallington", "type": "casal"},
    {"names": "Felipe e Vanessa", "type": "casal"},
    
    # Nauto's side
    {"names": "Leonardo e Valdirene", "type": "casal"},
    {"names": "Vilmar e Luciane", "type": "casal"},
    {"names": "Rosânia e Adilson", "type": "casal"},
    {"names": "Priscila e Anderson", "type": "casal"},
    {"names": "Otaviano e Patrícia", "type": "casal"},
    {"names": "Elizabete e Honório", "type": "casal"},
    {"names": "Laldete e Maria Aparecida", "type": "casal"},
    {"names": "Werlei e Danielle", "type": "casal"},
    {"names": "Maria e Thiago", "type": "casal"},
    {"names": "Felipe e Poliana", "type": "casal"},
    {"names": "Sandro e Ana Paula", "type": "casal"},
    {"names": "Ernando e Maria das Graças", "type": "casal"}
]

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

def generate():
    template_path = "index.html"
    output_dir = "LuanaeNauto"
    
    if not os.path.exists(template_path):
        print("Error: index.html template not found.")
        return
        
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()
        
    # Standardize newlines to \n for clean and reliable replacements
    template_content = template_content.replace("\r\n", "\n")
    print(f"Loaded template from {template_path} (normalized newlines).")
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    print(f"Ensured output directory '{output_dir}' exists.")
    
    # Define text replacements for singular madrinha
    intro_casal_p = (
        '            <p class="description">\n'
        '                Vocês são pessoas muito importantes na<br>\n'
        '                nossa história. Por isso, não poderíamos<br>\n'
        '                dizer \'sim\' sem vocês ao nosso lado.<br>\n'
        '                Aceitam ser nossos padrinhos e fazer parte<br>\n'
        '                deste momento único?\n'
        '            </p>'
    )
    btn_casal_a = (
        '            <a href="https://wa.me/553198396857?text=Ol%C3%A1%21%20Confirmamos%20com%20muita%20alegria%20que%20seremos%20padrinhos%20deste%20momento%20%C3%BAnico%21" target="_blank" class="btn primary-btn">Vocês aceitam?</a>'
    )
    
    intro_madrinha_p = (
        '            <p class="description">\n'
        '                Você é uma pessoa muito importante na<br>\n'
        '                nossa história. Por isso, não poderíamos<br>\n'
        '                dizer \'sim\' sem você ao nosso lado.<br>\n'
        '                Aceita ser nossa madrinha e fazer parte<br>\n'
        '                deste momento único?\n'
        '            </p>'
    )
    btn_madrinha_a = (
        '            <a href="https://wa.me/553198396857?text=Ol%C3%A1%21%20Confirmo%20com%20muita%20alegria%20que%20serei%20madrinha%20deste%20momento%20%C3%BAnico%21" target="_blank" class="btn primary-btn">Você aceita?</a>'
    )
    
    # Define text replacements for singular padrinho
    intro_padrinho_p = (
        '            <p class="description">\n'
        '                Você é uma pessoa muito importante na<br>\n'
        '                nossa história. Por isso, não poderíamos<br>\n'
        '                dizer \'sim\' sem você ao nosso lado.<br>\n'
        '                Aceita ser nosso padrinho e fazer parte<br>\n'
        '                deste momento único?\n'
        '            </p>'
    )
    btn_padrinho_a = (
        '            <a href="https://wa.me/553198396857?text=Ol%C3%A1%21%20Confirmo%20com%20muita%20alegria%20que%20serei%20padrinho%20deste%20momento%20%C3%BAnico%21" target="_blank" class="btn primary-btn">Você aceita?</a>'
    )
    
    generated_files = []
    
    for guest in padrinhos:
        pair = guest["names"]
        g_type = guest["type"]
        
        foldername = sanitize_foldername(pair)
        guest_dir = os.path.join(output_dir, foldername)
        os.makedirs(guest_dir, exist_ok=True)
        filepath = os.path.join(guest_dir, "index.html")
        
        content = template_content
        
        # 1. Replace title and header names
        content = content.replace(
            "<title>Convite Especial - Bruna e Vitor</title>",
            f"<title>Convite Especial - {pair}</title>"
        )
        
        # For the header, if it's a couple, put a line break after " e "
        header_names = pair
        if g_type == "casal" and " e " in pair:
            header_names = pair.replace(" e ", " e<br>")
            
        content = content.replace(
            '<h1 class="names">Bruna e Vitor</h1>',
            f'<h1 class="names">{header_names}</h1>'
        )
        
        # 2. Adjust content based on guest type
        if g_type == "madrinha":
            # Change intro wording to singular female
            content = content.replace(intro_casal_p, intro_madrinha_p)
            content = content.replace(btn_casal_a, btn_madrinha_a)
            
            # Remove Godfather section completely
            pattern_godfather = r"<!--\s*Godfather Section\s*-->\s*<section class=\"section godparents-section\">.*?</section>"
            content = re.sub(pattern_godfather, "", content, flags=re.DOTALL)
            
        elif g_type == "padrinho":
            # Change intro wording to singular male
            content = content.replace(intro_casal_p, intro_padrinho_p)
            content = content.replace(btn_casal_a, btn_padrinho_a)
            
            # Remove Godmother section completely
            pattern_godmother = r"<!--\s*Godmother Section\s*-->\s*<section class=\"section godparents-section section-relative\">.*?</section>"
            content = re.sub(pattern_godmother, "", content, flags=re.DOTALL)
            
            # Add side decorations (flowers) to Godfather section since Godmother section was removed
            godfather_replacement = (
                '<section class="section godparents-section section-relative">\n'
                '            <img src="assets/processed/lateral_mais_curto.svg" alt="" class="floral floral-side-left">\n'
                '            <img src="assets/processed/lateral_mais_longo.svg" alt="" class="floral floral-side-right">'
            )
            content = content.replace('<section class="section godparents-section">', godfather_replacement)
            
        # 3. Adjust asset paths for the subdirectory structure (two levels deep)
        content = content.replace('styles.css', '../../styles.css')
        content = content.replace('assets/processed/', '../../assets/processed/')
        
        # Write the customized HTML file
        with open(filepath, "w", encoding="utf-8") as f_out:
            f_out.write(content)
            
        generated_files.append(filepath)
        print(f"Generated: {filepath} for {pair} ({g_type})")
        
    print(f"\nSuccessfully generated {len(generated_files)} invitation files under '{output_dir}'.")

if __name__ == "__main__":
    generate()
