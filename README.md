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

## Versão 2 (branch `v2-globo-interativo`)

- `index.html`: a história contada pela rolagem. Um globo 3D (Three.js r128, pelo cdnjs) fica ao fundo e cada passo da rolagem move a câmera: abertura, a rede saindo de Brasília, e um capítulo por país (chegada, onde, quem, uma voz), terminando na comparação lado a lado.
- `dados.html`: a versão 1, agora como a parte de consulta (mapa, páginas por país, comparativo, publicações).
- `data/globo.json`: contornos em longitude/latitude para desenhar a textura do globo.
- Botão "Menos movimento" desliga o giro e as animações; o site também respeita a preferência do sistema. Sem WebGL, os textos aparecem sem o globo.
