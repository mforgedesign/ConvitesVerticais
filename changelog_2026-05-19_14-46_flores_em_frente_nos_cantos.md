# Changelog: Flores posicionadas à frente nos cantos

**Data:** 19/05/2026
**Hora:** 14:46

## Motivação
**Prompt:** "As flores estão soltas atrás, invés de estarem nos cantos vagos à frente"

## Explicação
Antes, as imagens das flores estavam com `position: absolute` referenciando o `body`, com `z-index: 1`, o que as deixava por trás das seções do convite e perdidas ao longo do scroll da página longa.
Agora, as flores utilizam `position: fixed` com `z-index: 10`, garantindo que elas fiquem perfeitamente ancoradas e visíveis nos cantos da tela (viewport) acompanhando o usuário enquanto ele faz a rolagem, e sobrepondo-se sutilmente ao fundo das seções, criando a sensação imersiva desejada de estar "à frente". Além disso, utilizei `transform: scale` para espelhar a mesma imagem perfeitamente para os quatro cantos.

## Código Antigo (`styles.css`)
```css
.floral {
    position: absolute;
    z-index: 1;
    pointer-events: none;
    opacity: 0.85;
    max-width: 250px;
}

.floral-top-left { top: -20px; left: -40px; transform: rotate(15deg); }
.floral-top-right { top: 150px; right: -60px; transform: rotate(-15deg); }
.floral-bottom-left { bottom: 200px; left: -50px; transform: rotate(45deg); }
.floral-bottom-right { bottom: -20px; right: -40px; transform: rotate(-30deg); }
```

## Código Novo (`styles.css`)
```css
.floral {
    position: fixed;
    z-index: 10;
    pointer-events: none;
    opacity: 1;
    max-width: 200px;
}

.floral-top-left { top: -10px; left: -10px; transform: none; }
.floral-top-right { top: -10px; right: -10px; transform: scaleX(-1); }
.floral-bottom-left { bottom: -10px; left: -10px; transform: scaleY(-1); }
.floral-bottom-right { bottom: -10px; right: -10px; transform: scale(-1, -1); }
```
