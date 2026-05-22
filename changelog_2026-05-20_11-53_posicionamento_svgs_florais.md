# Changelog: Posicionamento dos SVGs Florais no Convite

**Data:** 20/05/2026
**Hora:** 11:53
**Prompt Motivador:** "Joguei 4 svgs na pasta C:\Users\Acer\Documents\Testes. Analise e posicione eles no convite."

## Funcionamento Anterior
- O convite estava sem os elementos decorativos de flores, mantendo apenas a estrutura padrão de texto e caixas de seções. As classes de posições florais antigas haviam sido removidas.

## Funcionamento Atual
- **Importação:** Os arquivos `canto.svg`, `bottom.svg`, `Lateral mais longo.svg` e `lateral mais curto.svg` foram copiados para `assets/processed/` com nomes limpos.
- **Posicionamento no HTML:**
  - `canto.svg` foi inserido no topo da seção `<header>`.
  - `lateral_mais_longo.svg` foi posicionado na lateral direita da seção de Data e Local (`.date-section`).
  - `lateral_mais_curto.svg` foi colocado na lateral esquerda da seção de Madrinhas (`.godparents-section`).
  - `bottom.svg` foi inserido na base do rodapé (`<footer>`).
- **Lógica de CSS:**
  - A classe `.section-relative` foi reativada com `position: relative` e `overflow: hidden`.
  - Para garantir que os SVGs fiquem perfeitamente atrás do texto, mas à frente do fundo da seção, a classe `.floral` foi definida com `z-index: 1`. 
  - Um seletor de herança `.section-relative > *:not(.floral)` foi criado, atribuindo `position: relative; z-index: 2;` para todos os outros filhos. Isso garante de forma robusta que nenhum texto fique por baixo das flores.
  - Como SVGs possuem transparência nativa perfeita, não foi necessário usar blend-mode ou filtros de brilho, mantendo os tons rosé gold totalmente fiéis.
