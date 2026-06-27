# Changelog - 27/06/2026 12:26

## Prompt Motivador
"Quero mais um, agora para Ernando e Maria das Graças"

## Funcionamento Anterior vs. Funcionamento Atual
- **Antes:** O script `generate_invitations.py` continha 22 casais/destinatários. Ernando e Maria das Graças não estavam na lista.
- **Agora:** O script `generate_invitations.py` foi atualizado para incluir o casal "Ernando e Maria das Graças" como tipo "casal". A regeneração em lote criou a estrutura `LuanaeNauto/ErnandoeMariadasGracas/index.html` com o nome do casal e a quebra de linha dinâmica automática após o "e".

## Código Antigo
```python
    {"names": "Maria e Thiago", "type": "casal"},
    {"names": "Felipe e Poliana", "type": "casal"},
    {"names": "Sandro e Ana Paula", "type": "casal"}
]
```

## Código Novo
```python
    {"names": "Maria e Thiago", "type": "casal"},
    {"names": "Felipe e Poliana", "type": "casal"},
    {"names": "Sandro e Ana Paula", "type": "casal"},
    {"names": "Ernando e Maria das Graças", "type": "casal"}
]
```
