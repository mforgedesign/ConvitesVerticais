# Documentação: Convite Digital Rosé Gold

**Data de Criação:** 19/05/2026

## Índice Semântico / Tópicos do Código

1. **Visão Geral do Projeto**
2. **Estrutura de Arquivos**
3. **Dependências**
4. **Detalhes da Implementação (HTML/CSS)**
5. **Automação de Assets (Python)**
6. **Configurações de Deploy e Ambiente**
7. **Workflow de Replicação Técnica**

## 1. Visão Geral do Projeto
Este projeto consiste na criação de um convite digital interativo para casamento (Bruna e Vitor), no formato de uma página web responsiva com rolagem vertical. O layout segue uma estética refinada com paleta "Rosé Gold", detalhes em dourado e decoração floral lateral.
Para permitir a replicação e criação de novos convites semelhantes no futuro por outras I.A.s, criamos um guia central de referência técnica em [workflow_geracao_convites.md](file:///c:/Users/Acer/Documents/VerticalBuilder/Testes/ConviteRoseGold/workflow_geracao_convites.md).

## 2. Estrutura de Arquivos
- `index.html`: Arquivo principal contendo a marcação semântica e a estrutura do convite (funciona como template para geração em lote).
- `styles.css`: Folha de estilos para o design e responsividade.
- `fetch_images.py`: Script Python autônomo para baixar e remover o fundo de imagens florais da web.
- `generate_invitations.py`: Script de geração em lote que lê `index.html` e gera convites personalizados para cada casal de padrinhos.
- `workflow_geracao_convites.md`: Guia e manual técnico de referência para replicação do projeto de convites por I.A.s ou desenvolvedores futuramente.
- `LuanaeNauto/`: Diretório contendo os convites individuais dos padrinhos (ex: `CleoniceeCelio.html`) estruturados no padrão CamelCase sem espaços ou hifens.
- `.gitignore`: Configuração para ignorar ambiente virtual Python e cache de scripts.
- `CNAME`: Configuração do domínio personalizado cliqueparaabrir.mforge.com para o GitHub Pages.
- `assets/`: Diretório contendo os recursos de imagem:
  - `raw/`: Imagens originais baixadas da web.
  - `processed/`: Imagens com fundo transparente (processadas via `rembg`).

## 3. Dependências
- **Google Fonts:** Cinzel, Great Vibes, Montserrat, Pinyon Script.
- **FontAwesome:** Ícones vetoriais.
- **Python Libraries (para o gerador de imagens):** `duckduckgo-search`, `requests`, `rembg`, `onnxruntime-gpu`, `Pillow`.

## 4. Detalhes da Implementação (HTML/CSS)
- **Cabeçalho (`.monogram`):** O selo com as iniciais "IM" foi criado via CSS puro com `radial-gradient` e pseudoelementos `::before` / `::after` para as linhas laterais simulando o barbante/fita.
- **Botões (`.primary-btn`, `.icon-btn`):** Desenvolvidos com flexbox para alinhamento e efeitos de hover para interatividade.
- **Paleta de Cores (`.color-palette`):** Demonstração da cartela da madrinha utilizando `div`s circulares com as variáveis de cor CSS `--rose-gold`, `--rose-gold-light`, etc.
- **Flores (`.floral`):** Elementos posicionados com `position: absolute` e rotação para preencher os cantos do convite sem atrapalhar a leitura.

## 5. Automação de Assets (Python)
O script `fetch_images.py` busca automaticamente na DuckDuckGo por "rose gold watercolor flowers corner border white background png", salva na pasta `assets/raw/` e utiliza o modelo de inteligência artificial u2net (`rembg`) para extrair os elementos principais, resultando em PNGs transparentes gravados em `assets/processed/`.

## 6. Configurações de Deploy e Ambiente
- **Nome do Arquivo:** `.gitignore`
  - **Funcionamento:** Configurado para ignorar o diretório de ambiente virtual Python (`venv/`), arquivos de bytecode compilados (`*.pyc`, `__pycache__/`), arquivos de sistema (`.DS_Store`) e pastas de configuração de IDEs (`.vscode/`, `.idea/`).
  - **Dependências:** Controla quais arquivos locais não devem ser sincronizados com o repositório remoto do Git.
- **Nome do Arquivo:** `CNAME`
  - **Funcionamento:** Define o domínio personalizado `cliqueparaabrir.mforge.com` para a hospedagem do GitHub Pages. Ao receber requisições HTTP neste domínio, o GitHub as direciona para a raiz do repositório.
  - **Dependências:** Depende da configuração do DNS externa (HostGator) apontando os registros apropriados para os servidores de IP do GitHub Pages.

## Histórico de Modificações (Changelogs)
- **[19/05/2026]** `changelog_2026-05-19_14-46_flores_em_frente_nos_cantos.md`: Alteração no CSS (`styles.css`) para corrigir a posição das flores para `position: fixed` e `z-index: 10`, trazendo-as à frente dos conteúdos e fixando-as nos quatro cantos da tela perfeitamente durante o scroll.
- **[19/05/2026]** `changelog_2026-05-19_14-48_flores_scroll_interno.md`: Alteração no HTML e CSS para mover as imagens `.floral` para dentro da `.invitation-container` com `position: absolute` e `z-index: 5`. As flores agora acompanham o scroll do usuário e aparecem de forma intercalada ao longo do layout longo, idêntico à imagem de referência anexada originalmente.
- **[19/05/2026]** `changelog_2026-05-19_14-50_reasoning_design_flores.md`: Execução de protocolo de design para substituir imagens recortadas pela GPU por imagens puras processadas com a propriedade CSS `mix-blend-mode: multiply`, corrigindo completamente contornos escuros e melhorando o respiro do texto.
- **[19/05/2026]** `changelog_2026-05-19_14-53_correcao_flores_em_secoes.md`: Refinamento do CSS (`filter: brightness`) para corrigir quadros visíveis (bounding box off-white) causados pelo blend-mode e realocação das tags `<img>` para dentro de cada `.section` específica, evitando sobreposição com o texto na arquitetura responsiva.
- **[19/05/2026]** `changelog_2026-05-19_15-02_curadoria_assets_organicos.md`: Substituição do PNG único espelhado por 4 artes independentes geradas por IA (`flower_header`, `flower_side_right`, `flower_side_left`, `flower_footer`) para conferir formato orgânico em aquarela à anatomia do convite.
- **[19/05/2026]** `changelog_2026-05-19_15-32_remocao_flores_para_canva.md`: Remoção completa de todo o HTML e CSS (`.floral`, `.section-relative`) que gerenciava as flores via código, preparando o terreno para receber assets finais unificados estáticos que serão produzidos no Canva pelo usuário.
- **[19/05/2026]** `changelog_2026-05-19_15-39_insercao_dados_reais.md`: Aplicação de todos os dados reais do evento fornecidos pelos noivos: data, hora, endereços consolidados, linkagem dos botões de ação (Google Maps, Forms de RSVP, Lista de Presentes no Canva), botão de confirmação configurado via URI scheme do WhatsApp e exclusão do bloco social "moldura do instagram".
- **[20/05/2026]** `changelog_2026-05-20_11-53_posicionamento_svgs_florais.md`: Posicionamento e dimensionamento dos 4 novos arquivos SVG florais criados pelo usuário no Canva. Adicionada a lógica CSS para manter os SVGs atrás do texto de forma segura e responsiva.
- **[20/05/2026]** `changelog_2026-05-20_11-58_ajustes_finos_svgs_florais.md`: Ajustes finos de margem, espaçamento e escala dos SVGs. Implementação de flores bilaterais (laterais duplas) nas seções de Data e Madrinha, correção do recuo do cabeçalho e adição de padding-bottom expressivo no rodapé para evitar que as letras sobreponham as flores de base.
- **[20/05/2026]** `changelog_2026-05-20_12-04_alinhamento_florais_bordas_finais.md`: Remoção do overflow restrito dos cartões de seção, fazendo com que as flores sangrem além das caixas de texto e alcancem as bordas absolutas de visualização da página, eliminando qualquer margem branca entre as flores e a margem de delimitação lateral do layout.
- **[22/05/2026]** `changelog_2026-05-22_03-10_atualizacao_imagens_padrinhos_madrinhas.md`: Atualização da imagem de inspiração do terno dos padrinhos com a nova foto do usuário e inserção do bloco correspondente de inspiração para o tom de vestido das madrinhas.
- **[22/05/2026]** `changelog_2026-05-22_16-50_imagem_madrinha_tom_vestido.md`: Substituição do placeholder transparente pela imagem real do tom de vestido das madrinhas (`baixados (7).jpg`) e ajuste de extensão no HTML.
- **[22/05/2026]** `changelog_2026-05-22_16-55_remocao_logo_redonda_iniciais_cabeçalho.md`: Remoção do monograma redondo (iniciais "IM") e suas linhas decorativas laterais no cabeçalho do convite.
- **[22/05/2026]** `changelog_2026-05-22_17-00_substituicao_nomes_iniciais_l_n.md`: Substituição do nome "Bruna e Vitor" pelas iniciais "L e N" no título, cabeçalho e rodapé do convite.
- **[22/05/2026]** `changelog_2026-05-22_17-05_logo_iniciais_cabeçalho_nomes_padrinhos.md`: Inserção da logo com as iniciais dos noivos "L e N" no topo do cabeçalho e restauração dos nomes dos padrinhos convidados ("Bruna e Vitor").
- **[22/05/2026]** `changelog_2026-05-22_17-10_espaco_testa_cabeçalho_convite.md`: Aumento do espaçamento superior no container principal e no cartão de cabeçalho para criar mais espaço ("testa") e respiro visual no topo da página.
- **[22/05/2026]** `changelog_2026-05-22_17-15_assinatura_luana_nauto_correcao_sobreposicao.md`: Substituição da assinatura final por "Luana e Nauto", adição de `flex-shrink: 0` nas seções para evitar cortes de texto e correção de colisão/sobreposição na assinatura.
- **[22/05/2026]** `changelog_2026-05-22_17-20_geracao_lote_convites_padrinhos.md`: Criação de script Python para geração automática de 20 convites personalizados de padrinhos em lote, e adição da documentação dos novos arquivos.
- **[22/05/2026]** `changelog_2026-05-22_17-25_correcao_nome_padrinho_laldete.md`: Ajuste no script gerador e substituição do convite Valdete pelo correto Laldete de acordo com a grafia literal solicitada pelo usuário.
- **[22/05/2026]** `changelog_2026-05-22_17-30_publicacao_github_pages_custom_domain.md`: Inicialização do repositório Git, criação de arquivos .gitignore e CNAME, e deploy/ativação do GitHub Pages no repositório remoto mforgedesign/ConvitesVerticais sob o domínio personalizado cliqueparaabrir.mforge.com.
- **[22/05/2026]** `changelog_2026-05-22_17-35_organizando_convites_em_subdiretorios.md`: Reestruturação do script gerador para criar convites dentro da subpasta slug `Luana&Nauto` com padrão de nomenclatura CamelCase (ex: `CleoniceeCelio.html`) e ajuste correspondente de caminhos relativos de assets e estilos.
- **[22/05/2026]** `changelog_2026-05-22_17-55_movendo_arquivos_backup_para_pasta.md`: Remoção de todos os arquivos de backup da raiz do repositório no controle de versão Git, movendo-os localmente para o diretório `backups/` e configurando o `.gitignore` para desconsiderá-los.
- **[22/05/2026]** `changelog_2026-05-22_18-05_correcao_nome_padrinho_helio.md`: Correção do nome do padrinho Nélio Batista para Hélio Batista no script gerador e regeneração em lote das páginas HTML de convite.
- **[22/05/2026]** `changelog_2026-05-22_18-04_troca_slug_para_luanaenauto.md`: Alteração do diretório de saída do lote de convites de Luana&Nauto para LuanaeNauto para corrigir erros de carregamento e URL amigável no GitHub Pages.
- **[22/05/2026]** `changelog_2026-05-22_18-15_slugs_de_convites_como_pastas.md`: Reestruturação dos convites individuais para serem gerados como pastas com `index.html` (ex: `LuanaeNauto/CleoniceeCelio/index.html`) para permitir que o GitHub Pages resolva as URLs limpas sem extensão `.html` (ex: `LuanaeNauto/CleoniceeCelio`).
- **[22/05/2026]** `changelog_2026-05-22_18-35_correcao_do_dominio_customizado_cname.md`: Correção do domínio customizado no arquivo CNAME de `.com` para `.com.br` para coincidir com o apontamento de DNS ativo na zona de DNS do usuário.
- **[22/05/2026]** `changelog_2026-05-22_18-40_separacao_de_convites_individuais_padrinhos.md`: Separação do casal Roseny e João Otávio em dois convites individuais (madrinha e padrinho) com linguagem no singular e ocultação das seções opostas.
- **[25/05/2026]** `changelog_2026-05-25_10-45_alteracao_de_nome_do_casal.md`: Alteração do nome do casal de padrinhos Cleonice e Célio para Maria e Thiago, com regeneração das páginas de convite correspondentes.
- **[06/06/2026]** `changelog_2026-06-06_14-12_adicao_de_sandro_e_paula_como_padrinhos.md`: Adição de Sandro e Paula como casal de padrinhos na lista de geração em lote e regeneração dos arquivos HTML correspondentes.
- **[06/06/2026]** `changelog_2026-06-06_14-15_correcao_nome_sandro_e_ana_paula.md`: Correção do nome do casal de padrinhos Sandro e Paula para Sandro e Ana Paula, com a exclusão do diretório de convite antigo.
- **[06/06/2026]** `changelog_2026-06-06_14-18_quebra_de_linha_nomes_casais.md`: Implementação de quebra de linha dinâmica no cabeçalho após o conectivo "e" para todos os convidados do tipo casal, melhorando o alinhamento em viewports mobile.
- **[06/06/2026]** `changelog_2026-06-06_14-19_correcao_sobreposicao_de_flores_no_rodape.md`: Correção de sobreposição visual na seção social (`.social-section`) causada por elementos florais absolutos do rodapé que transbordavam para cima, adicionando posicionamento relativo e z-index.
- **[27/06/2026]** `changelog_2026-06-27_12-26_adicao_de_ernando_e_maria_das_gracas.md`: Adição do casal de padrinhos Ernando e Maria das Graças e geração em lote dos convites correspondentes.

## 7. Workflow de Replicação Técnica
Para recriar um projeto de convite digital responsivo com a mesma arquitetura de geração em lote de páginas estáticas e deploy, consulte o arquivo [workflow_geracao_convites.md](file:///c:/Users/Acer/Documents/VerticalBuilder/Testes/ConviteRoseGold/workflow_geracao_convites.md). Ele contém detalhes de design, comportamento estrutural do código Python e o passo a passo para publicação no GitHub Pages.
