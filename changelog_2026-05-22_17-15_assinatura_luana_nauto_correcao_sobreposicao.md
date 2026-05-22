# Changelog [22/05/2026 - 17:15] - Assinatura Luana e Nauto e Correção de Sobreposição

Este changelog documenta a substituição da assinatura do rodapé pelo nome completo dos noivos ("Luana e Nauto") e os ajustes de CSS para corrigir a sobreposição e o corte horizontal (clipping) do texto no final do convite.

## Prompt Motivador
"Ajeita isso aqui, e lá em baixo pode colocar "Luana e Nauto" invés de L N"

## Funcionamento Anterior vs. Funcionamento Atual
- **Antes:**
  - A assinatura final exibia a forma curta "L e N".
  - O texto "antecedência, ou seja, às 15h." da seção `.social-section` aparecia cortado (clipping horizontal) em telas menores porque a seção sofria encolhimento flexbox (`flex-shrink: 1` por padrão) e era sobreposta e mascarada pelo elemento vizinho `.footer-section` (que possui `position: relative`, fundo branco translúcido e `backdrop-filter`).
  - O texto introdutório da assinatura ("Com carinho,") e as iniciais cursivas se sobrepunham verticalmente devido à margem negativa de `-10px` em `.signature-intro` combinada com a falta de espaçamento/line-height adequado nos caracteres cursivos.

- **Agora:**
  - A assinatura final no rodapé foi atualizada para exibir o nome completo dos noivos: "Luana e Nauto".
  - Adicionado `flex-shrink: 0;` na regra `.section` no CSS para garantir que nenhuma seção do convite seja encolhida pelo layout flexbox, preservando a altura total das caixas e eliminando completamente qualquer vazamento e corte do texto informativo.
  - A margem inferior de `.signature-intro` foi alterada de `-10px` para `5px` e foi adicionado `line-height: 1.3;` à classe `.final-names` de rodapé, proporcionando um respiro adequado para a tipografia cursiva dos noivos e eliminando qualquer colisão com o texto "Com carinho,".

## Backups Criados
- `index_backup_15_20260522.html`
- `styles_backup_13_20260522.css`

## Código Antigo vs. Código Novo

### Código Antigo (Diferenças em `index.html`):
```html
        <!-- Footer Section -->
        <footer class="section text-center section-relative footer-section">
            <img src="assets/processed/bottom.svg" alt="" class="floral floral-footer">
            <p class="signature-intro">Com carinho,</p>
            <h1 class="names final-names">L e N</h1>
        </footer>
```

### Código Novo (Diferenças em `index.html`):
```html
        <!-- Footer Section -->
        <footer class="section text-center section-relative footer-section">
            <img src="assets/processed/bottom.svg" alt="" class="floral floral-footer">
            <p class="signature-intro">Com carinho,</p>
            <h1 class="names final-names">Luana e Nauto</h1>
        </footer>
```

### Código Antigo (Diferenças em `styles.css`):
```css
.section {
    display: flex;
    flex-direction: column;
    align-items: center;
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(5px);
    border-radius: 10px;
    padding: 20px;
}
...
.signature-intro {
    font-family: var(--font-body);
    font-size: 0.9rem;
    margin-bottom: -10px;
}

.final-names {
    font-size: 2.5rem;
}
```

### Código Novo (Diferenças em `styles.css`):
```css
.section {
    display: flex;
    flex-direction: column;
    align-items: center;
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(5px);
    border-radius: 10px;
    padding: 20px;
    flex-shrink: 0;
}
...
.signature-intro {
    font-family: var(--font-body);
    font-size: 0.9rem;
    margin-bottom: 5px;
}

.final-names {
    font-size: 2.5rem;
    line-height: 1.3;
}
```
