# Changelog - 06/06/2026 14:12

## Prompt Motivador
"Quero que suba pra mim um convite para Sandro e Paula do mesmo casamento"

## Funcionamento Anterior vs. Funcionamento Atual
- **Antes:** O script `generate_invitations.py` continha uma lista de 21 convidados de padrinhos (casais e individuais) para o casamento de Luana e Nauto. Sandro e Paula não faziam parte dessa lista de padrinhos e não possuíam convite individual gerado.
- **Agora:** O script `generate_invitations.py` agora inclui o casal "Sandro e Paula" como convidados do tipo "casal". A regeneração em lote criou a estrutura de diretórios e o arquivo `index.html` em `LuanaeNauto/SandroePaula/index.html` com as substituições e assets relativos corretos.

## Código Antigo
```python
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
    {"names": "Felipe e Poliana", "type": "casal"}
]
```

## Código Novo
```python
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
    {"names": "Sandro e Paula", "type": "casal"}
]
```
