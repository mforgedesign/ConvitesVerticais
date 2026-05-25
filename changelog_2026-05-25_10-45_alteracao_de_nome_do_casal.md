# Changelog - 25/05/2026 10:45

## Prompt Motivador
> O convite Célio e Cleonice, muda pra Maria e thiago

## O que mudou
- **Antes**: Havia um convite estruturado para o casal "Cleonice e Célio" na lista de convidados padrinhos sob a pasta `LuanaeNauto/CleoniceeCelio/`.
- **Agora**: A entrada correspondente em `generate_invitations.py` foi atualizada de `"Cleonice e Célio"` para `"Maria e Thiago"`. O script gerou um novo convite personalizado sob a pasta `LuanaeNauto/MariaeThiago/` e a pasta antiga foi removida do repositório para evitar arquivos órfãos.

## Código Antigo (`generate_invitations.py` - trecho)
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
    {"names": "Cleonice e Célio", "type": "casal"},
    {"names": "Felipe e Poliana", "type": "casal"}
```

## Código Novo (`generate_invitations.py` - trecho)
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
```
*(Para ver o arquivo completo modificado, consulte [generate_invitations.py](file:///c:/Users/Acer/Documents/VerticalBuilder/Testes/ConviteRoseGold/generate_invitations.py))*
