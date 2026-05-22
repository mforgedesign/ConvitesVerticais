# Changelog [22/05/2026 - 16:55] - Remoção da Logo Redonda com Iniciais

Este changelog documenta a remoção do monograma redondo (iniciais "IM") localizado no cabeçalho do convite.

## Prompt Motivador
"Remove essa logo redonda com as iniciais"

## Funcionamento Anterior vs. Funcionamento Atual
- **Antes:**
  - O cabeçalho continha um círculo gradiente rosé gold/dourado (`.monogram`) com as iniciais "IM" e duas linhas pontilhadas de barbante saindo para os lados, simulando um lacre de convite físico.
- **Agora:**
  - O monograma redondo e suas marcações foram completamente removidos da estrutura HTML. O cabeçalho agora exibe de forma limpa a imagem floral do topo, o subtítulo "Convite Especial" e os nomes dos noivos ("Bruna e Vitor").

## Backups Criados
- `index_backup_11_20260522.html` (criado antes da modificação em `index.html`)

## Código Antigo vs. Código Novo (Diferenças em `index.html`)

### Código Antigo:
```html
        <!-- Header Section -->
        <header class="section section-relative">
            <img src="assets/processed/canto.svg" alt="" class="floral floral-header">
            <div class="monogram">
                <span>IM</span>
            </div>
            <h2 class="subtitle">Convite Especial</h2>
            <h1 class="names">Bruna e Vitor</h1>
        </header>
```

### Código Novo:
```html
        <!-- Header Section -->
        <header class="section section-relative">
            <img src="assets/processed/canto.svg" alt="" class="floral floral-header">
            <h2 class="subtitle">Convite Especial</h2>
            <h1 class="names">Bruna e Vitor</h1>
        </header>
```
