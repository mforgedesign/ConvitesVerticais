# Changelog - 22/05/2026 17:25

**Prompt Motivador:**
> Laldete mesmo

---

## Explicação do Funcionamento

### Como funcionava antes:
O script gerador `generate_invitations.py` continha o nome "Valdete e Maria Aparecida" baseado em uma normalização preliminar do texto manuscrito. Como resultado, o arquivo gerado correspondente chamava-se `valdete-e-maria-aparecida.html` e exibia o nome "Valdete" no título e no cabeçalho do convite.

### Como funciona agora:
- O script `generate_invitations.py` foi atualizado para conter a grafia literal solicitada pelo usuário: "Laldete e Maria Aparecida".
- O script foi reexecutado e gerou o convite correto no arquivo [laldete-e-maria-aparecida.html](file:///c:/Users/Acer/Documents/VerticalBuilder/Testes/ConviteRoseGold/laldete-e-maria-aparecida.html).
- O arquivo obsoleto `valdete-e-maria-aparecida.html` foi removido do sistema.
- A documentação `docs.md` e o `walkthrough.md` foram devidamente atualizados.

---

## Código Antigo

### `generate_invitations.py` (linhas 27-29)
```python
    "Elizabete e Honório",
    "Valdete e Maria Aparecida",
    "Werlei e Danielle",
```

---

## Código Novo

### `generate_invitations.py` (linhas 27-29)
```python
    "Elizabete e Honório",
    "Laldete e Maria Aparecida",
    "Werlei e Danielle",
```
