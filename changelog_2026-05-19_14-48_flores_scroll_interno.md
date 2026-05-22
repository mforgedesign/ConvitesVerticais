# Changelog: Flores acompanhando o scroll interno

**Data:** 19/05/2026
**Hora:** 14:48

## Motivação
**Prompt:** "As imagens das flores agora ficaram emolduradas fixas. Analise como as flores eram posicionadas no convite exemplo que anexei como imagem, como é feito lá?"

## Explicação
Antes, as flores estavam configuradas como `position: fixed` em relação à tela, o que criava uma "moldura" estática. No entanto, analisando o convite de referência (que é longo e *scrollável*), as flores são dispostas ao longo do conteúdo e acompanham a rolagem do usuário (scroll).
Para corrigir isso, as imagens `<img class="floral">` foram movidas para dentro da `.invitation-container`. Com isso, a propriedade `position: absolute` voltou a ser utilizada, mas agora ela é relativa ao contêiner principal e não à tela. As flores foram posicionadas ao longo de diferentes alturas (`top: 600px`, `top: 1300px`, etc.) para aparecerem esporadicamente enquanto o usuário faz a rolagem. Além disso, aplicou-se `overflow: hidden` ao container para que as flores fiquem embutidas e não quebrem a responsividade no celular.

## Código Antigo (Trecho)
`index.html`:
```html
<body>
    <div class="invitation-container">...</div>
    <img src="..." class="floral floral-bottom-left">
</body>
```
`styles.css`:
```css
.floral { position: fixed; z-index: 10; }
.floral-top-left { top: -10px; left: -10px; }
```

## Código Novo (Trecho)
`index.html`:
```html
<body>
    <div class="invitation-container">
        <img src="..." class="floral floral-1">
        ...
    </div>
</body>
```
`styles.css`:
```css
.floral { position: absolute; z-index: 5; }
.floral-1 { top: -20px; left: -20px; }
.floral-2 { top: 600px; right: -40px; }
```
