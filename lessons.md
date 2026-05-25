# Lições Aprendidas

Neste arquivo, registraremos as lições aprendidas durante o desenvolvimento do Convite Digital Rosé Gold, conforme a regra R5 do projeto.

## 19/05/2026 - Uso de GPU Local para Tratamento de Imagem
- **Desafio:** A remoção de fundo com ferramentas automáticas pode ser pesada para CPU. A utilização da `rembg` localmente precisava ser otimizada.
- **Solução:** A instalação e uso do pacote `rembg[gpu]` juntamente com `onnxruntime-gpu` garante que a placa de vídeo (RTX 4060) seja utilizada para a remoção de fundo, acelerando muito a renderização em lote das imagens de flores coletadas da DuckDuckGo.
- **Atenção Futura:** Quando provisionar scripts python em Windows PowerShell, assegurar o uso do ambiente virtual correto ativado (ex: `.\venv\Scripts\Activate.ps1`) para que o contexto de dependências não contamine o ambiente global.

## 19/05/2026 - Paleta Rosé Gold no CSS
- **Desafio:** Adaptar uma imagem baseada em azul para uma paleta visualmente coerente em Rosé Gold, mantendo o contraste das fontes legível.
- **Solução:** Utilizamos tons variando de `#b76e79` a `#f2e3e5` (criando um *gradiente* natural nas paletas de vestidos da madrinha), e mudamos o acento de texto para tons levemente amarronzados/acinzentados (`#5a5a5a`) que harmonizam muito melhor com o rosé do que o preto puro ou azul escuro da referência original.

## 19/05/2026 - Posição das Imagens de Decoração
- **Desafio:** Ao configurar os arranjos florais com `position: absolute` na página longa, os enfeites ficavam atrás do conteúdo embaçado e acabavam "soltos" com a rolagem ou restritos a coordenadas perdidas na página longa. Quando trocados para `fixed`, eles perdiam a naturalidade do convite longo, ficando grudados na tela.
- **Solução:** A solução final e correta para convites no estilo *long-scroll* foi mover as imagens (`img.floral`) para **dentro** do `.invitation-container` e manter o container como `position: relative` (com `overflow: hidden` para não gerar barra de rolagem lateral com as bordas das flores). As flores voltaram a usar `position: absolute` com `z-index: 5` (maior que o fundo transparente do container, mas sem tapar botões) e seus `top`s e `bottom`s espalhados pelo tamanho do container (`top: -20px`, `top: 600px`, `top: 1300px`, `bottom: -20px`). Isso recriou o efeito perfeito da imagem de referência, onde as flores surgem gradualmente enquanto o usuário desce a página.

## 19/05/2026 - Alpha Matting vs CSS Blend Modes
- **Desafio:** Remover fundo branco de pinturas em aquarela usando algoritmos tradicionais (como `rembg`) geralmente resulta em contornos escuros ao redor das bordas semitransparentes (halos).
- **Solução:** Em projetos web onde o fundo é branco ou claro, é uma péssima prática tentar recortar aquarelas. A solução definitiva de design é utilizar a imagem original (com o fundo branco intacto) e aplicar `mix-blend-mode: multiply;` no CSS. O algoritmo do navegador processa os pixels brancos como 100% transparentes e mescla a aquarela perfeitamente na página sem qualquer artefato, preservando toda a suavidade da pintura original.

## 20/05/2026 - Uso de SVGs com Transparência Nativa
- **Desafio:** Evitar problemas de recorte, halos escuros e perda de definição visual ao redimensionar elementos florais decorativos em layouts responsivos.
- **Solução:** O uso de arquivos SVG contendo os vetores das flores com transparência nativa elimina a necessidade de recortar imagens rasterizadas (PNG/JPG) e evita o uso de `mix-blend-mode: multiply`. Os SVGs escalam perfeitamente sem perda de qualidade e não exibem halos escuros.
- **Atenção no Z-Index:** Para garantir que os SVGs (inseridos como `<img>` com `position: absolute`) fiquem localizados precisamente entre o plano de fundo da seção e as informações de texto sem obstruir interações do usuário ou a leitura, utilizamos o seletor universal `.section-relative > *:not(.floral) { position: relative; z-index: 2; }` e `.floral { z-index: 1; }`. Isso blinda o layout contra sobreposições indesejadas de texto.

## 22/05/2026 - Gestão de Assets Locais de Usuário e Alinhamento de Seções
- **Desafio:** Garantir a coerência estética entre as seções de "Querida Madrinha" e "Querido Padrinho" quando novos assets locais são fornecidos pelo usuário, mesmo se um dos arquivos vier como placeholder transparente.
- **Solução:** Copiar sistematicamente os arquivos temporários fornecidos pelo usuário para os diretórios estruturados do projeto (`assets/processed/`) e espelhar a estrutura visual. No caso da madrinha, implementamos o bloco de inspiração ("Inspire-se") idêntico ao do padrinho. Desta forma, a imagem do vestido (mesmo sendo um arquivo transparent) fica mapeada e posicionada no local exato para quando for atualizada com o arquivo final.

## 22/05/2026 - Resolução de Arquivos Locais Fora do Workspace e Extensões
- **Desafio:** Lidar com arquivos que o usuário aponta em diretórios do sistema (como a pasta de Downloads) e garantir que a extensão do arquivo coincida exatamente no HTML.
- **Solução:** Copiar os arquivos para o repositório com o nome estruturado apropriado e adaptar a extensão no `index.html` (de `.png` para `.jpg`, por exemplo). Sempre validar o caminho de origem usando comandos do sistema (como `Test-Path` no Windows) para certificar a existência física do arquivo antes de realizar o deploy/copy.

## 22/05/2026 - Simplificação de Cabeçalhos e Redução de Complexidade Visual
- **Desafio:** Remover elementos visuais redundantes ou que poluem o cabeçalho (como o monograma redondo) garantindo que o restante dos elementos (subtítulo, nomes e flores) se reajustem de forma harmoniosa no layout flexbox.
- **Solução:** Remover a marcação HTML obsoleta e certificar que as regras CSS globais ou da seção de cabeçalho continuem funcionando perfeitamente sem quebras de layout. Em designs modernos e minimalistas, a remoção de elementos pesados como monogramas com bordas gradientes limpa consideravelmente a primeira dobra da página, direcionando a atenção diretamente para os nomes principais.

## 22/05/2026 - Substituição de Textos Principais e Iniciais
- **Desafio:** Substituir strings principais de nomes do casal em múltiplos pontos do HTML sem quebrar a consistência das tags de título, cabeçalho e rodapé.
- **Solução:** Mapear todas as ocorrências do nome ("Bruna e Vitor") e aplicar a substituição para as iniciais ("L e N") em locais semânticos apropriados (incluindo o título da aba no navegador, título do cabeçalho e assinatura final), garantindo que as classes de estilo e a tipografia cursiva permaneçam inalteradas.

## 22/05/2026 - Hierarquia de Identidade Visual em Convites Personalizados
- **Desafio:** Diferenciar de forma limpa e harmônica no cabeçalho os nomes dos destinatários do convite (os convidados padrinhos) da logo dos remetentes (as iniciais dos noivos), evitando poluição visual após a remoção de elementos pesados.
- **Solução:** Criar uma classe `.logo` com estilização cursiva elegante e minimalista e posicioná-la no topo do cabeçalho, mantendo os nomes dos convidados padrinhos com o maior peso visual logo abaixo. Isso preserva a experiência de personalização do convite digital de maneira limpa.

## 22/05/2026 - Controle de Densidade Visual e Espaçamento de Topo (Testa) em Telas Mobile
- **Desafio:** Evitar que os elementos do topo da primeira dobra fiquem aglomerados ou empurrados contra as bordas do viewport em layouts de convites digitais móveis, especialmente quando há sobreposição de ilustrações decorativas absolutas (como arranjos florais).
- **Solução:** Aumentar o preenchimento superior do container principal (`padding-top` do `.invitation-container`) para empurrar toda a página para baixo e criar um recuo confortável. Em paralelo, aplicar um `padding-top` específico e generoso na primeira seção do layout (o cabeçalho) para criar a "testa" do cartão, assegurando que o texto principal não dispute espaço ou fique sob os elementos gráficos. Por fim, sincronizar o `top` negativo do SVG decorativo absoluto com o novo padding do container para que ele continue surgindo diretamente da borda de delimitação da página, sem criar gaps vazios.

## 22/05/2026 - Prevenção de Encolhimento de Cards Flexbox e Colisão Tipográfica
- **Desafio:** Corrigir cortes de texto em cartões informativos causados por encolhimento no layout flexbox e resolver sobreposições verticais em assinaturas com fontes cursivas.
- **Solução:** 
  1. Adicionar `flex-shrink: 0;` nos cartões de seção (`.section`). Isso impede o navegador de espremer as dimensões verticais dos cartões quando o conteúdo é maior que a altura inicial calculada, evitando vazamentos e sobreposição de seções vizinhas.
  2. Ajustar margens negativas para positivas (`margin-bottom: 5px` no separador da assinatura) e declarar `line-height: 1.3;` na tipografia cursiva (`.final-names`). Fontes caligráficas/cursivas costumam possuir hastes muito longas (ascendentes/descendentes) que colidem facilmente com textos em caixa alta ou caixa baixa se o line-height for muito baixo ou se houver deslocamentos negativos severos.

## 22/05/2026 - Automação de Geração em Lote e Codificação de Caracteres no Windows
- **Desafio:** Gerar múltiplos convites HTML personalizados a partir de uma lista de nomes fornecida pelo usuário, lidando com caracteres especiais/acentos e evitando inconsistências de codificação (encoding) e nomes de arquivos inválidos.
- **Solução:**
  1. Utilizar normalização Unicode (decomposição de caracteres com `unicodedata.normalize('NFKD', ...)` e remoção de diacritics via `unicodedata.combining`) para limpar os nomes ao gerar os nomes de arquivos (ex: `rosângela` se torna `rosangela.html`). Isso previne problemas com caracteres especiais nas URLs.
  2. Forçar explicitamente a codificação UTF-8 ao ler o template e ao gravar cada arquivo gerado (`encoding="utf-8"`). No Windows, o padrão do Python pode variar dependendo do terminal/sistema (como CP-1252), o que corrompe acentos em português.
  3. Preprocessar e corrigir manualmente erros de digitação e acentuação nos dados brutos de entrada (como o pedido de corrigir 'Wilmar' para 'Vilmar' e acentuar 'Jéssica', 'Célio' etc.) para assegurar que a renderização visual final seja de altíssima qualidade.

## 22/05/2026 - Validação de Grafia Manuscrita e Limpeza de Arquivos Obsoletos em Lotes
- **Desafio:** Lidar com caligrafia de difícil leitura (ex: "Laldete") sem realizar adivinhações arbitrárias definitivas e manter o repositório livre de arquivos gerados erroneamente.
- **Solução:**
  1. Utilizar a abordagem de normalização provisória e solicitar explicitamente a confirmação ao usuário (Regra R4 - nunca adivinhar).
  2. Ao receber a correção ou confirmação, atualizar o script gerador base, reexecutar a automação para criar o novo arquivo (ex: `laldete-e-maria-aparecida.html`) e deletar ativamente os arquivos HTML órfãos do lote anterior (ex: `valdete-e-maria-aparecida.html`), garantindo que o diretório contenha estritamente os convites válidos.

## 22/05/2026 - Deploy e Configuração de Domínio Personalizado no GitHub Pages
- **Desafio:** Configurar domínio customizado em hospedagem GitHub Pages garantindo que a resolução de DNS e o arquivo CNAME estejam alinhados sem causar loops de redirecionamento ou quebra do link seguro (HTTPS).
- **Solução:**
  1. Criar o arquivo `CNAME` na raiz do repositório contendo exatamente o domínio (`cliqueparaabrir.mforge.com`) sem prefixos de protocolo (como `http://`).
  2. Inicializar o repositório local e fazer o push para o branch padrão (`main`).
  3. Ativar o recurso GitHub Pages via API do GitHub apontando para a pasta raiz (`/`) do branch `main`, o que automaticamente detecta o arquivo `CNAME` e realiza a requisição de certificado SSL/TLS (processo que pode levar alguns minutos para ser finalizado).
  4. Utilizar tokens de acesso pessoal clássicos com escopo `repo` para autenticação HTTPS via git remotes com URL formatada (`https://<token>@github.com/...`).

## 22/05/2026 - Estrutura de Slugs em Subdiretórios e Caminhos Relativos no GitHub Pages
- **Desafio:** Organizar os convites gerados em lote dentro de um subdiretório correspondente ao slug do casal (ex: `Luana&Nauto/`) para criar URLs personalizadas sem quebrar o carregamento dos assets e estilos (CSS, imagens) que permanecem na raiz.
- **Solução:**
  1. Modificar o script de geração em lote para salvar os arquivos gerados no diretório do slug do casal (usando `os.makedirs` para garantir sua criação).
  2. Ajustar dinamicamente as referências de arquivos e caminhos no HTML gerado, alterando caminhos locais como `styles.css` e `assets/processed/` para caminhos relativos superiores (`../styles.css` e `../assets/processed/`).
  3. Utilizar o padrão de nomenclatura `CamelCase` sem hifens nem espaços nos arquivos do subdiretório (ex: `CleoniceeCelio.html`) permitindo que o GitHub Pages os sirva em URLs limpas como `cliqueparaabrir.mforge.com/Luana&Nauto/CleoniceeCelio`.

## 22/05/2026 - Caractere de Ampersand (&) no Windows PowerShell
- **Desafio:** Ao executar comandos do Git ou do sistema no Windows PowerShell passando caminhos que contêm o caractere de ampersand `&` (ex: `git add Luana&Nauto/`), o terminal falha interpretando o ampersand como um operador reservado inválido.
- **Solução:** Sempre encapsular caminhos ou strings que contêm caracteres especiais ou reservados do PowerShell em aspas duplas (ex: `git add "Luana&Nauto/"`), garantindo a correta interpretação da string literal.

## 22/05/2026 - Organização e Exclusão de Backups do Controle de Versão (Git)
- **Desafio:** Manter o histórico e a conformidade de backups locais exigidos pela regra R6 sem poluir a raiz do repositório ou expor centenas de arquivos de backup na interface pública do GitHub.
- **Solução:** 
  1. Centralizar todos os backups locais em um subdiretório dedicado (`backups/`).
  2. Adicionar o subdiretório `backups/` ao arquivo `.gitignore` para blindar o repositório contra o envio acidental de arquivos temporários.
  3. Para arquivos que já estavam sendo rastreados, utilizar `git rm --cached <arquivos>` para removê-los do índice de commits (desrastreá-los) mantendo a cópia local intacta no disco antes de movê-la para a pasta ignorada.

## 22/05/2026 - Propagação de Correções e Limpeza de Arquivos Órfãos Gerados em Lote
- **Desafio:** Ao corrigir dados de entrada de um script de geração em lote (ex: alterar o nome do padrinho Nélio para Hélio), o script passa a gerar um arquivo novo com o nome correto, porém o arquivo gerado com o nome anterior torna-se "órfão" na pasta de saída.
- **Solução:**
  1. Corrigir o dado de entrada na lista do script.
  2. Executar o script para criar a nova página corrigida.
  3. Fazer a exclusão manual e explícita do arquivo órfão no Git (usando `git rm`) para garantir que links quebrados ou incorretos não continuem sendo servidos no ambiente de produção do GitHub Pages.

## 22/05/2026 - Evitar Caracteres Especiais Reservados em Slugs de URLs
- **Desafio:** Pasta de saída de convites usando o caractere `&` (ex: `Luana&Nauto`) apresentava falhas intermitentes de navegação e resolução 404 ao ser hospedada no GitHub Pages com domínio customizado, já que o caractere `&` possui significado especial em protocolos web (como delimitador de parâmetros de busca).
- **Solução:** Substituir o caractere especial `&` por um caractere alfanumérico limpo (ex: alterar o slug para `LuanaeNauto`). Isso garante que os servidores estáticos de hospedagem resolvam a rota perfeitamente sem decodificações corrompidas de URL (evitando `%26` ou interpretação como query parameters).

## 22/05/2026 - URLs Sem Extensão (.html) no GitHub Pages via Diretórios
- **Desafio:** URLs amigáveis e limpas sem `.html` (ex: `/LuanaeNauto/CleoniceeCelio`) não abrem nativamente no GitHub Pages se os arquivos forem gerados diretamente como arquivos `.html` avulsos no subdiretório (resultando em 404).
- **Solução:** Gerar cada convite em seu próprio subdiretório contendo um arquivo `index.html` (ex: `LuanaeNauto/CleoniceeCelio/index.html`). O GitHub Pages serve automaticamente arquivos `index.html` quando o diretório pai é acessado sem barra ou extensão. Os caminhos de assets e estilos no HTML devem ser adaptados com `../../` para subir os dois níveis de subpasta gerados.

## 22/05/2026 - Diagnóstico de DNS e Resolução de NXDOMAIN para Domínio Personalizado
- **Desafio:** Resolver problemas de carregamento de páginas após a vinculação correta do CNAME ao repositório no GitHub Pages.
- **Solução:** Verificar através de ferramentas de terminal (como `nslookup`) e APIs do GitHub se a configuração do lado do repositório foi bem-sucedida e onde reside o gargalo. Quando o domínio retorna NXDOMAIN globalmente e as requisições diretas ao domínio do GitHub Pages (`mforgedesign.github.io`) realizam o redirecionamento (301) correto para o domínio customizado, fica comprovado que a configuração no GitHub está 100% perfeita. O problema está exclusivamente na falta do apontamento de DNS (registro CNAME para `mforgedesign.github.io` ou registros A para os IPs do GitHub) no gerenciador de DNS do domínio pai (neste caso, sob os nameservers `mysecurecloudhost.com`).

## 22/05/2026 - Geração em Lote Condicional para Convidados Individuais (Madrinha e Padrinho)
- **Desafio:** Separar um casal cadastrado conjuntamente em convites individuais específicos, removendo os blocos de conteúdo visual irrelevantes de cada gênero (madrinha/padrinho), alterando a linguagem do plural para o singular gramatical adequado e preservando o plano de fundo decorativo lateral.
- **Solução:**
  1. Modificar a estrutura de dados de convidados em `generate_invitations.py` para mapear o tipo do convidado (`casal`, `madrinha`, `padrinho`).
  2. Implementar substituições dinâmicas de texto multilistas normalizadas em `\n` para adequar as introduções e links de retorno do WhatsApp ao singular feminino ou masculino.
  3. Utilizar expressões regulares não-gulosas (`re.DOTALL` e `.*?`) para capturar e remover a seção indesejada por completo a partir do seu comentário HTML demarcador (ex: remover a seção de madrinha inteira no convite do padrinho).
  4. Para padrinhos individuais, reinserir dinamicamente a classe `.section-relative` e as tags `<img>` dos SVGs florais no cabeçalho da seção de padrinho, visto que a seção de madrinha (que as continha originalmente) foi excluída, restaurando a simetria estética do convite.

## 25/05/2026 - Alteração de Dados de Entrada e Limpeza de Diretórios no Controle de Versão
- **Desafio:** Quando o usuário solicita a alteração do nome de um convidado/casal (ex: de "Cleonice e Célio" para "Maria e Thiago"), o script de geração cria uma pasta com a nova slug sanitizada, mas a pasta gerada anteriormente torna-se órfã e permanece no repositório.
- **Solução:**
  1. Atualizar a lista de convidados em `generate_invitations.py`.
  2. Executar o gerador de lote para criar o novo diretório com o arquivo `index.html` correspondente.
  3. Excluir a pasta antiga manualmente do sistema de arquivos e encenar a exclusão no controle de versão do Git (usando `git rm -r` ou `git add .` pós-deleção local), garantindo que caminhos antigos e órfãos não continuem versionados ou servidos no ambiente de deploy.
