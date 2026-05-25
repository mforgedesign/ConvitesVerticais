# Workflow de Criação e Geração de Convites Digitais Interativos

Este documento serve como um guia técnico passo a passo e manual de referência para que qualquer desenvolvedor ou Inteligência Artificial (I.A.) possa recriar, manter ou gerar novos convites digitais em lote utilizando esta mesma arquitetura.

---

## 1. Visão Geral da Arquitetura
O projeto é um gerador de páginas estáticas baseado em um arquivo de template (`index.html`), uma folha de estilos centralizada (`styles.css`), ativos visuais compartilhados (imagens e SVGs) e um script Python (`generate_invitations.py`) que processa os dados dos convidados e exporta as páginas finais estruturadas em diretórios para suporte a URLs limpas.

### Estrutura de Diretórios Recomendada
```text
/
├── index.html                    # Template HTML base
├── styles.css                    # Estilo CSS centralizado
├── generate_invitations.py       # Script de geração em lote
├── CNAME                         # Configuração de domínio do GitHub Pages
├── docs.md                       # Documentação principal do projeto
├── lessons.md                    # Histórico de lições aprendidas
├── assets/                       # Recursos de mídia
│   └── processed/                # Imagens finais (vestido, terno, SVGs decorativos)
└── LuanaeNauto/                  # Pasta gerada pelo script (slug do casal)
    ├── ConvidadoA/               # Subpasta do convidado A
    │   └── index.html            # Arquivo gerado
    └── ConvidadoB/               # Subpasta do convidado B
        └── index.html            # Arquivo gerado
```

---

## 2. Decisões de Design e UX Cruciais
Para preservar a altíssima qualidade visual do convite, as seguintes técnicas devem ser mantidas:

1. **Responsividade em Tela Inteira (Mobile First):** O container principal `.invitation-container` possui largura máxima de `480px` e margem automática para centralizar em computadores, simulando a tela de um smartphone.
2. **Padding Superior ("Testa"):** O container do cabeçalho exige um preenchimento confortável (`padding-top: 130px`) para evitar que as fotos dos noivos ou as ilustrações decorativas absolutas colidam com o topo da tela do celular.
3. **SVG Floral nas Bordas (Sem Margem Branca):** Os arquivos SVG florais bilaterais (`lateral_mais_curto.svg` e `lateral_mais_longo.svg`) usam posicionamento absoluto (`position: absolute; top: 0; left: 0; right: 0;`) com margens calculadas para "sangrar" até o limite físico da tela, cobrindo qualquer espaço em branco.
4. **Z-Index Blindado:** Para impedir que as decorações fiquem por cima do texto e bloqueiem botões ou leitura, todo elemento de texto dentro de seções relativas deve receber uma declaração explícita de `position: relative` e `z-index: 2`, enquanto os SVGs decorativos (`.floral`) usam `z-index: 1`.
5. **Prevenção de Encolhimento Flexbox:** Os cartões de seção devem usar `flex-shrink: 0;` no CSS para que o navegador nunca aperte ou corte o texto quando a tela do dispositivo for menor.
6. **Legibilidade das Fontes Caligráficas:** Tipografias cursivas (como *Great Vibes* ou *Pinyon Script*) usam hastes longas que exigem um `line-height` mínimo de `1.3` e margens de afastamento adequadas para que suas letras não colidam verticalmente com as linhas vizinhas.

---

## 3. Funcionamento Detalhado do Gerador Python
O script `generate_invitations.py` lê o template `index.html` e itera sobre uma lista estruturada de dicionários contendo os dados dos convidados. Ele suporta três modalidades de convidados:

1. **casal:** Exibe ambas as seções de dicas ("Querida Madrinha" e "Querido Padrinho"). Usa plural no convite e no botão.
2. **madrinha:** Exclui a seção de Padrinho do HTML usando expressões regulares e altera o texto do cabeçalho e link do WhatsApp para o singular feminino (*"Você é uma pessoa muito importante..."*, *"Aceita ser nossa madrinha..."*, *"Você aceita?"*).
3. **padrinho:** Exclui a seção de Madrinha do HTML. Ajusta o texto e link do WhatsApp para o singular masculino (*"Aceita ser nosso padrinho..."*, *"Você aceita?"*). Como a seção de Madrinha continha os SVGs florais decorativos de fundo, o script reinserte a classe `section-relative` e os elementos `<img>` correspondentes de forma dinâmica na seção de Padrinho para manter a simetria de design das flores.

### Trecho de Código de Geração Condicional:
```python
# Lógica de processamento condicional no generate_invitations.py
if g_type == "madrinha":
    # Linguagem no singular feminino
    content = content.replace(intro_casal_p, intro_madrinha_p)
    content = content.replace(btn_casal_a, btn_madrinha_a)
    # Remoção da seção de Padrinho
    pattern_godfather = r"<!--\s*Godfather Section\s*-->\s*<section class=\"section godparents-section\">.*?</section>"
    content = re.sub(pattern_godfather, "", content, flags=re.DOTALL)
    
elif g_type == "padrinho":
    # Linguagem no singular masculino
    content = content.replace(intro_casal_p, intro_padrinho_p)
    content = content.replace(btn_casal_a, btn_padrinho_a)
    # Remoção da seção de Madrinha
    pattern_godmother = r"<!--\s*Godmother Section\s*-->\s*<section class=\"section godparents-section section-relative\">.*?</section>"
    content = re.sub(pattern_godmother, "", content, flags=re.DOTALL)
    # Inserção das flores na seção de Padrinho
    godfather_replacement = (
        '<section class="section godparents-section section-relative">\n'
        '            <img src="assets/processed/lateral_mais_curto.svg" alt="" class="floral floral-side-left">\n'
        '            <img src="assets/processed/lateral_mais_longo.svg" alt="" class="floral floral-side-right">'
    )
    content = content.replace('<section class="section godparents-section">', godfather_replacement)
```

---

## 4. Workflow de Deploy e Publicação
Toda a hospedagem é mantida de forma estática no **GitHub Pages** sob um domínio customizado.

### Passos de Deploy para I.A.s e Desenvolvedores:
1. **Configuração do Repositório Git:**
   - O projeto deve possuir um arquivo `CNAME` localizado estritamente na raiz do repositório, contendo apenas o domínio a ser utilizado (ex: `cliqueparaabrir.mforge.com.br`).
   - O arquivo `.gitignore` deve ignorar pastas locais de sistema, caches do python e o diretório de backups (`backups/`).
2. **Execução Local:**
   - Faça as alterações cadastrais ou de estilos desejadas.
   - Execute o script de geração: `python generate_invitations.py`
   - Exclua eventuais pastas antigas que tornaram-se obsoletas devido à mudança de nome de convidados usando: `git rm -r LuanaeNauto/NomeAntigo`.
3. **Commit e Push:**
   - Envie as modificações para a branch padrão do repositório remoto:
     ```powershell
     git add .
     git commit -m "feat: atualiza convidados"
     git push origin main
     ```
4. **Resolução de URLs no GitHub Pages:**
   - Graças à estrutura de pastas do gerador (`LuanaeNauto/NomeDoConvidado/index.html`), o GitHub Pages interpretará o acesso à URL `https://cliqueparaabrir.mforge.com.br/LuanaeNauto/NomeDoConvidado` e servirá o arquivo HTML de forma transparente e sem a necessidade de exibir extensões `.html` na barra do navegador.
   - *Nota Importante:* Como as páginas geradas estão em subpastas de nível 2, as referências de arquivos no HTML (como `styles.css` e caminhos de imagens) precisam ser substituídas dinamicamente pelo script para conter o prefixo `../../` (ex: `../../styles.css`).
