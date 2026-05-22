# Changelog [22/05/2026 - 17:10] - Aumento do Espaçamento Superior (Testa) da Página

Este changelog documenta o aumento do espaçamento no topo do convite ("testa" da página) para reduzir a densidade visual e posicionar as flores e os textos do cabeçalho de forma mais elegante e harmônica.

## Prompt Motivador
"Coloca mais espaço na testa da página, tá com um aspecto visual ruim tudo muito pra cima"

## Funcionamento Anterior vs. Funcionamento Atual
- **Antes:**
  - O container principal (`.invitation-container`) possuía um preenchimento superior (`padding-top`) de apenas `40px`.
  - O cartão de cabeçalho (`header.section`) não possuía espaçamento interno superior específico (herdava os `20px` padrão de `.section`), fazendo com que o texto da logo (`L e N`) ficasse muito espremido no topo do cartão, sob a ilustração floral.
  - A ilustração floral (`.floral-header`) estava com posicionamento de `top: -60px`, fazendo com que ficasse ligeiramente cortada pelo overflow.
- **Agora:**
  - O preenchimento superior do container (`.invitation-container`) foi aumentado para `80px`, empurrando toda a página para baixo e dando mais respiro visual.
  - O cartão de cabeçalho (`header.section`) recebeu um preenchimento superior de `90px` (`padding-top: 90px`), empurrando os textos internos ("L e N", "Convite Especial", "Bruna e Vitor") para baixo e criando uma área de respiro ("testa") generosa onde as flores se posicionam sem esmagar o texto.
  - O posicionamento vertical da ilustração floral (`.floral-header`) foi ajustado para `top: -95px`, garantindo que ela se estenda até a borda absoluta do topo da página (surgindo exatamente junto com a delimitação da página) mesmo com o novo recuo de 80px do container.

## Backups Criados
- `styles_backup_11_20260522.css` (criado antes da modificação em `styles.css`)

## Código Antigo vs. Código Novo

### Código Antigo (Diferenças em `styles.css`):
```css
.invitation-container {
    max-width: 480px;
    margin: 0 auto;
    background: transparent;
    position: relative;
    z-index: 2;
    padding: 40px 20px;
    display: flex;
    flex-direction: column;
    gap: 40px;
    min-height: 100vh;
    overflow: hidden;
}
...
.floral-header {
    top: -60px;
    left: -40px;
    width: 280px;
}
...
/* Header */
.monogram {
```

### Código Novo (Diferenças em `styles.css`):
```css
.invitation-container {
    max-width: 480px;
    margin: 0 auto;
    background: transparent;
    position: relative;
    z-index: 2;
    padding: 80px 20px 40px;
    display: flex;
    flex-direction: column;
    gap: 40px;
    min-height: 100vh;
    overflow: hidden;
}
...
.floral-header {
    top: -95px;
    left: -40px;
    width: 280px;
}
...
/* Header */
header.section {
    padding-top: 90px;
}

.monogram {
```
