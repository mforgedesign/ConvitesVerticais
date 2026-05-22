# Changelog: Remoção das Flores CSS/HTML (Preparação para Blocos Canva)

**Data:** 19/05/2026
**Hora:** 15:32

## Motivação
**Prompt:** "Faz o seguinte, tira fora essas flores. Eu vou no canva pegar as partes em que elas deveriam aparecer e criar como imagem, pra tu substituir a sessão."
O usuário optou por uma abordagem mais prática (e muito comum em convites estáticos de alta fidelidade): ao invés de codificar a sobreposição de dezenas de PNGs florais soltos com CSS (`position: absolute`, `mix-blend-mode`), ele criará no Canva os blocos inteiros das seções já com o design (textos, fontes e flores achatadas juntos) ou assets específicos e fechados. Meu papel é limpar a estrutura CSS de posicionamento floral.

## Explicação
- Removi todas as tags `<img class="floral ...">` do arquivo `index.html`.
- Removi a classe `.section-relative` que havia sido criada para ancorar as flores dentro de cada seção.
- No `styles.css`, deletei todo o bloco pertencente às classes florais (`.floral`, `.floral-header`, `.floral-side-right`, `.floral-side-left`, `.floral-footer`, `.section-relative`), limpando o código morto.

O projeto agora está "limpo" de elementos decorativos florais via código, aguardando as imagens/seções que serão fornecidas pelo usuário vindas do Canva.
