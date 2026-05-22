# Changelog: Correção do Ponderamento e Limite Visível das Flores

**Data:** 19/05/2026
**Hora:** 14:53

## Motivação
**Prompt:** "Você não tá ponderando corretamente... O recorte tá mal feito (tá com um contorno escuro), o posicionamento delas tá horrível."
A imagem gerada pela IA, apesar de ter um fundo claro, não possuía um fundo 100% branco puro (`#ffffff`), o que tornava a caixa delimitadora (bounding box) da imagem visível como um quadrado bege/cinza com a aplicação do `mix-blend-mode: multiply`. Além disso, o posicionamento absoluto pelo container principal fazia as imagens atropelarem os textos dependendo do tamanho da tela.

## Explicação
Para corrigir definitivamente o design (reasoning design protocol implementado):
1. **Limpeza do Fundo Off-White:** Ao invés de tentar recortes em scripts, apliquei o CSS `filter: brightness(1.05) contrast(1.2);` junto ao `mix-blend-mode`. Isso "estoura" o fundo quase branco da imagem para branco puro invisível, eliminando instantaneamente o efeito de quadrado escuro ao redor das flores sem destruir a aquarela.
2. **Nova Arquitetura de Posicionamento:** Abandonei o `position: absolute` baseado em `top` arbitrários (`top: 1350px`) no container gigante. Agora as flores estão injetadas **dentro de cada `.section`** específica que elas devem decorar (cabeçalho, data, madrinha e rodapé). A classe `.section-relative` força as imagens a respeitarem a área da seção com `z-index: -1`, mantendo-as delicadamente atrás do texto como um verdadeiro e elegante background de aquarela que espreita pelas margens, sem causar atropelamentos visuais de leitura.

## Código Novo (Trecho CSS)
```css
.section-relative {
    position: relative;
    overflow: hidden; /* Corta o excesso da flor que vaza da seção */
}

.floral {
    position: absolute;
    z-index: -1; /* Fica atrás do texto, mas dentro da seção */
    pointer-events: none;
    opacity: 0.8;
    max-width: 180px;
    mix-blend-mode: multiply;
    filter: brightness(1.05) contrast(1.2); /* Força o off-white para branco puro */
}
```
