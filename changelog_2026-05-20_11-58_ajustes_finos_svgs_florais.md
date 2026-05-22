# Changelog: Ajustes Finos nos SVGs Florais

**Data:** 20/05/2026
**Hora:** 11:58
**Prompt Motivador:** "O de canto não está no canto suficientemente, tem uma distância. Arrume. O lateral está escondido, e tem que ser de um lado e do outro. E também precisa estar corretamente junto a borda, invés de ter um espaço. O bottom também está afastado e está com as letras sobrepondo. Arrume o espaço."

## Funcionamento Anterior
- O canto floral (`canto.svg`) estava com um recuo perceptível de cerca de 20px das bordas superior e esquerda.
- Os ramos laterais estavam cortados (escondidos) quase por completo porque estavam muito para fora da seção e havia apenas um ramo por seção (um na direita da data e um na esquerda da madrinha).
- O floral inferior (`bottom.svg`) estava afastado da borda inferior da caixa e os nomes "Bruna e Vitor" estavam sendo renderizados diretamente sobre a arte, gerando sobreposição que prejudicava a leitura.

## Funcionamento Atual
- **Ajuste de Canto (`.floral-header`):** Puxado mais para a borda superior esquerda (`top: -45px`, `left: -45px`) e levemente ampliado (`width: 250px`). Isso compensou o whitespace do próprio SVG e eliminou o gap de 20px.
- **Flores Duplas e Posicionamento Lateral (`.floral-side-left`, `.floral-side-right`):**
  - Agora, tanto a seção de Data (`.date-section`) quanto a seção de Madrinhas (`.godparents-section`) possuem ramos em **ambos os lados** (esquerdo e direito).
  - O posicionamento foi aproximado das margens internas (`right: -10px` e `left: -10px`) e a largura foi ligeiramente aumentada. Isso garante que eles fiquem visíveis rente às bordas da seção sem sumirem.
- **Ajuste de Base e Respiro do Texto (`.floral-footer`, `.footer-section`):**
  - O `bottom.svg` foi puxado mais para baixo (`bottom: -35px`) para eliminar qualquer fresta branca inferior.
  - Criada a classe `.footer-section` com um padding-bottom reforçado (`160px !important`). Isso empurra os nomes dos noivos e a assinatura para cima, criando uma área livre e limpa onde as flores do rodapé assentam sem encostar ou sobrepor as letras.
