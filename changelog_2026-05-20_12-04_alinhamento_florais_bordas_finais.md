# Changelog: Alinhamento dos Florais às Bordas Finais

**Data:** 20/05/2026
**Hora:** 12:04
**Prompt Motivador:** "Todas as flores seguem afastadas da borda, elas têm que surgir junto com a delimitação da página"

## Funcionamento Anterior
- Os cartões de seção possuíam `overflow: hidden;` habilitado através da classe `.section-relative`.
- Como a página tem margens externas de `20px` em cada lado (padding no container principal), as flores posicionadas dentro dos cartões não conseguiam alcançar as bordas reais do convite/tela (delimitação lateral cinza no desktop), gerando um visual onde flutuavam no meio do caminho ou ficavam cortadas se ultrapassassem a margem interna do card.

## Funcionamento Atual
- **Remoção de Limitações de Corte:** O `overflow: hidden;` foi removido de `.section-relative`. Agora as flores podem "sangrar" para fora das caixas brancas sem serem podadas.
- **Avanço às Bordas da Página:**
  - O topo-esquerdo (`.floral-header`) foi reposicionado para `top: -60px; left: -40px;` e redimensionado para `280px`, encaixando-se perfeitamente no limite superior da página.
  - As flores laterais (`.floral-side-left` e `.floral-side-right`) agora possuem recuos de `-35px` (esquerdo/direito), transpondo o espaçamento interno do card e da página para tocar a delimitação lateral de visualização.
  - O rodapé (`.floral-footer`) foi estendido com `width: calc(100% + 40px);` e jogado a `bottom: -60px; left: -20px;`, abraçando a base inteira do convite, de ponta a ponta.
  - O padding-bottom do rodapé foi expandido para `180px` para acomodar o novo posicionamento e escala do floral de encerramento.
- **Segurança de Rolagem Lateral:** A página mantém o comportamento responsivo limpo sem causar scroll horizontal porque o container pai absoluto (`.invitation-container`) continua com `overflow: hidden;` ativo, cortando quaisquer excessos indesejados fora da largura útil de 480px.
