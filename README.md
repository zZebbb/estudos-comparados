# Estudos Comparados · ambiente virtual

Site público do projeto Estudos Comparados (Laboratório ECoS, UnB): mapa dos países, entrevistas por município e categoria profissional, publicações, galeria e materiais educativos.

**Situação:** protótipo. Todos os números, trechos e fotos são exemplos fictícios.

## Estrutura

- `index.html`: o site inteiro (HTML, CSS e JS, sem dependências). Navegação por `#` (`#inicio`, `#mapa`, `#pais-peru`, `#comparativo`, `#publicacoes`, `#galeria`, `#materiais`, `#equipe`).
- `data/mapa.json`: contornos dos países já projetados (Natural Earth, a partir do pacote `world-atlas`, domínio público).
- Os dados de exemplo estão no topo do `<script>` em `index.html` (`COUNTRIES`, `PUBS`, `TEAM`). No site real eles virão de um arquivo de dados gerado a partir das planilhas por país.

## Ver localmente

```
python3 -m http.server 8000
```

e abra http://localhost:8000 (o mapa é carregado por `fetch`, então abrir o arquivo direto pelo navegador não funciona).

## Regra de dados

Antes da publicação dos artigos, só dados descritivos e anonimizados: número de entrevistas por país, município e categoria profissional, e no máximo 3 trechos curtos aprovados por país.
