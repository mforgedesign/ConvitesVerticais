# Changelog - 22/05/2026 18:05

**Prompt Motivador:**
> Corrije Nélio Batista para Hélio Batista, e faça deploy.

---

## Explicação do Funcionamento

### Como funcionava antes:
O script `generate_invitations.py` continha na lista de padrinhos o nome "Nélio Batista e Maria Aparecida", o que resultava na geração do arquivo `Luana&Nauto/NelioBatistaeMariaAparecida.html`.

### Como funciona agora:
- O nome no script `generate_invitations.py` foi corrigido para "Hélio Batista e Maria Aparecida".
- O arquivo antigo `Luana&Nauto/NelioBatistaeMariaAparecida.html` foi excluído do repositório.
- Foi gerado o novo arquivo `Luana&Nauto/HelioBatistaeMariaAparecida.html` correspondente à grafia correta solicitada pelo usuário.

---

## Código Antigo

### `generate_invitations.py` (linha 16)
```python
    "Nélio Batista e Maria Aparecida",
```

---

## Código Novo

### `generate_invitations.py` (linha 16)
```python
    "Hélio Batista e Maria Aparecida",
```
