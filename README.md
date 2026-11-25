# Estudos Comparados · ambiente virtual

Site do projeto Estudos Comparados (Laboratório ECoS, UnB): um globo com os países do estudo, diários de campo por país e uma parte de consulta com mapa, comparativo e publicações.

**Situação:** protótipo. Números, trechos de entrevista e textos dos países são exemplos fictícios. As fotos são reais, do trabalho de campo da equipe.

Endereço: https://zzebbb.github.io/estudos-comparados/ (GitHub Pages, publicado a partir da `main`, pasta raiz)

## Estrutura

| Caminho | O que é |
|---|---|
| `index.html` | Página inicial: a história contada pela rolagem, com o globo de pontos ao fundo. Um capítulo por país; os países com diário têm o botão "Abrir o diário". |
| `dados.html` | Parte de consulta (versão 1): mapa, páginas por país, comparativo, publicações. |
| `diarios/sao-tome/` | Diário de campo de São Tomé e Príncipe ("cartão-postal × como a informação de saúde circula ali"). Fotos em `fotos/sao-tome/`. |
| `diarios/peru/` | Diário de campo do Peru (Iquitos): efeito de água, globo de pontos Brasília → Iquitos, "uma gota no rio". Fotos em `fotos/peru/`. |
| `data/dots.json` | Pontos de terra do globo (latitude, longitude e país do estudo). Gerado por `scripts/gen_dots.py`. |
| `data/globo.json` | Contornos dos países em longitude/latitude (Natural Earth, domínio público). Fonte para o `gen_dots.py`. |
| `data/mapa.json` | Contornos já projetados, usados pelo mapa do `dados.html`. |
| `.nojekyll` | Diz ao GitHub Pages para servir os arquivos como estão. |

Cada página é um único arquivo HTML com CSS e JS dentro. Não há etapa de build. Bibliotecas externas, todas por CDN:
- fontes do Google Fonts;
- no diário do Peru: jQuery 3.5.1 e `jquery.ripples` 0.6.3 (efeito de água). O arquivo certo no jsDelivr é `dist/jquery.ripples-min.js`.

## Ver localmente

```
python3 -m http.server 8000
```

e abra http://localhost:8000. Os dados são carregados por `fetch`, então abrir o arquivo direto pelo navegador não funciona.

## Publicar no GitHub Pages

1. O repositório precisa ser **público** (no plano gratuito, o Pages não funciona em repositório privado). Em **Settings → General → Danger Zone → Change repository visibility → Make public**.
2. Em **Settings → Pages**: *Source* = **Deploy from a branch**, *Branch* = **main**, pasta **/ (root)**. Salvar.
3. Em 1 a 2 minutos o site aparece no endereço acima. Cada novo commit na `main` publica de novo sozinho.

Atenção: o site no Pages é público e pode ser indexado por buscadores, mesmo que o repositório volte a ser privado depois (aí o Pages para de funcionar). Para tirar uma foto do ar, apague o arquivo e faça commit; cópias em cache podem levar alguns dias para sumir.

## Como as páginas se ligam

- Na página inicial, o topo tem links fixos para os diários, e o capítulo de cada país com diário tem o botão "Abrir o diário". A lista fica em `DIARIOS`, no começo do `<script>` do `index.html`.
- Os diários voltam para o globo com `../../` e apontam um para o outro com `../<pais>/`.

### Criar o diário de um país novo

1. Copie a pasta `diarios/peru/` (ou `diarios/sao-tome/`) para `diarios/<slug>/`, com o mesmo `slug` usado em `COUNTRIES` no `index.html` (ex.: `colombia`).
2. Troque as fotos em `diarios/<slug>/fotos/<slug>/` (JPG com no máximo 1600 px no lado maior, qualidade ~82) e os textos.
3. Acrescente `"<slug>":"diarios/<slug>/"` em `DIARIOS` no `index.html`.

## Modo apresentação

As três páginas têm o botão **▶ Apresentar** (ou a tecla **P**). As setas avançam e voltam por paradas, como slides; **Esc** sai. As paradas de cada página ficam na função `window.AP_STOPS`, no fim do arquivo.

## Regras de dados e de imagem

- Antes da publicação dos artigos, só dados descritivos e anonimizados: número de entrevistas por país, município e categoria profissional, e no máximo 3 trechos curtos aprovados por país. Números e falas fictícios ficam marcados como "exemplo".
- Fotos: o Gustavo autorizou, em 25/11/2026, publicar todas as fotos dos diários de São Tomé e do Peru. Fotos de pessoas fora da equipe (comunidade, crianças, profissionais de saúde) dependem da autorização de imagem registrada pelo projeto. Na dúvida, não suba a foto.
- A pasta `/fotos/` na raiz fica fora do git: é o lugar para originais e fotos ainda não liberadas.

## Globo de pontos

O globo é desenhado em canvas 2D, sem WebGL nem bibliotecas. Visual claro: esfera quase branca, pontos cinza a cada 1,2° de latitude (verso apagado), países do estudo em violeta claro e o país do capítulo em violeta escuro; os arcos saindo de Brasília são pontilhados. Dá para arrastar o globo para girar. O botão "Menos movimento" (e a preferência do sistema) desliga o giro e as animações.

Cores e ritmo ficam em dois lugares do `index.html`: as variáveis `--night`, `--ink`, `--accent`, `--sun` no começo do CSS e os valores RGB dentro de `frame()` (pontos, arcos, municípios). A câmera vai de um capítulo a outro em ~1,4 s com aceleração suave (`DUR` e `ease` em `makeGlobe`), e os itens do painel de texto entram um a um no mesmo ritmo (`.card>*` no CSS). O texto fica sempre sobre um painel branco opaco.

Para regerar os pontos depois de mudar `data/globo.json`:

```
python3 scripts/gen_dots.py
```
