# Changelog - 06/06/2026 14:15

## Prompt Motivador
"Sandro e Ana Paula, corrige pra mim"

## Funcionamento Anterior vs. Funcionamento Atual
- **Antes:** O script `generate_invitations.py` continha o casal de padrinhos cadastrado sob o nome "Sandro e Paula", o que gerava o convite no diretório `LuanaeNauto/SandroePaula/`.
- **Agora:** O script `generate_invitations.py` foi corrigido para conter "Sandro e Ana Paula", o que gera o convite no diretório `LuanaeNauto/SandroeAnaPaula/`. O diretório antigo e obsoleto foi removido do controle de versão.

## Código Antigo
```python
    {"names": "Sandro e Paula", "type": "casal"}
```

## Código Novo
```python
    {"names": "Sandro e Ana Paula", "type": "casal"}
```
