# Changelog - 22/05/2026 18:40

## Prompt Motivador
> O da Roseny e do João são separados. Não são casal. Faça um para cada, removendo o conteúdo respectivo (no do joão não deve ter conteúdo da madrinha, e vice versa). Corrige e deploy

## O que mudou
- **Antes**: Todos os convidados eram tratados exclusivamente como casais. O script gerava o convite "Roseny e João Otávio" de forma combinada, exibindo as seções de madrinha e padrinho juntas e usando linguagem no plural para a introdução e o botão do WhatsApp.
- **Agora**: O script de geração em lote (`generate_invitations.py`) foi reformulado para classificar cada convidado por tipo (`casal`, `madrinha` ou `padrinho`). O convite conjunto foi dividido em "Roseny" (Madrinha) e "João Otávio" (Padrinho).
  - O convite de **Roseny** (madrinha) remove a seção "Querido Padrinho" e adota texto e link do WhatsApp no singular feminino ("nossa madrinha", "Você aceita?").
  - O convite de **João Otávio** (padrinho) remove a seção "Querida Madrinha", adota texto e link do WhatsApp no singular masculino ("nosso padrinho", "Você aceita?") e transfere os SVGs florais decorativos laterais para a seção de Padrinho para manter a simetria visual do design.

## Código Antigo (`generate_invitations.py` - trecho)
```python
padrinhos = [
    # Luana's side
    "Sueleny e Valter",
    "Jéssica e Welligton",
    "Rosângela e Diogo",
    "Josimara e Gustavo",
    "Roseny e João Otávio",
    ...
]

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

## Código Novo (`generate_invitations.py` - completo)
```python
import os
import re
import unicodedata

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
    {"names": "Cleonice e Célio", "type": "casal"},
    {"names": "Felipe e Poliana", "type": "casal"}
]

# ... (normalização de quebras de linha e strings de substituição para madrinha e padrinho)
```
*(Para ver o arquivo completo modificado, consulte [generate_invitations.py](file:///c:/Users/Acer/Documents/VerticalBuilder/Testes/ConviteRoseGold/generate_invitations.py))*
