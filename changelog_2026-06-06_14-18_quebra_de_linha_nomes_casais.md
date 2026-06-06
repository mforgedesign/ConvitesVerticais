# Changelog - 06/06/2026 14:18

## Prompts Motivadores
"Ficou descentralizado o 'Ana Paula'"
"Coloca quebra de linha após o 'e'"

## Funcionamento Anterior vs. Funcionamento Atual
- **Antes:** Os nomes dos casais eram substituídos diretamente na tag `<h1>` do cabeçalho sem quebras de linha controladas, o que podia causar quebras e desalinhamentos inadequados em telas menores para nomes mais longos (ex: "Sandro e Ana Paula").
- **Agora:** O script `generate_invitations.py` identifica convites do tipo "casal" e que contêm " e " no nome, inserindo automaticamente uma quebra de linha HTML (`<br>`) logo após o conectivo "e". Isso garante um alinhamento perfeitamente centralizado e balanceado em dispositivos móveis.

## Código Antigo
```python
        # 1. Replace title and header names
        content = content.replace(
            "<title>Convite Especial - Bruna e Vitor</title>",
            f"<title>Convite Especial - {pair}</title>"
        )
        content = content.replace(
            '<h1 class="names">Bruna e Vitor</h1>',
            f'<h1 class="names">{pair}</h1>'
        )
```

## Código Novo
```python
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
```
