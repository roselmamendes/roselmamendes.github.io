---
layout: post
title: "Um dia, Roselma conheceu o Jekyll no Github, então viu que era bom"
date:             2016-03-27T13:04:19+05:45 # XML Schema Date/Time
last_modified_at: 2016-03-27T05:20:00+05:45 # last page modified date/time
excerpt:          "" # Optional for overwriting content excerpt
categories:       framework # ["category1"] - best is to have one category in a post
tags:             ["frontend"] # ["tag1", "tag2", "tag3"] - you can have several post tags
image:
  feature: jekyll-github/jesus.jpg # image.jpg, suggested size:  2000x700px
  topPosition: 0px # top position for featured image if needed
bgContrast: dark
bgGradientOpacity: darker
---

Nada como escrever um post no blog com um texto descrevendo como eu criei o próprio blog.
<div align="center">
  <img src="/assets/images/jekyll-github/amazingly-funny.gif" width="230px" height="200px"/>
</div>

## Conteúdo

1. [Jekyll](#jekyll)
2. [Github Pages](#github-pages)
3. [O que você precisa para começar](#o-que-voc-precisa-para-comear)
  - [Ferramentas Necessárias](#ferramentas-necessrias)
4. [Começando nosso site](#comeando-nosso-site)
  - [Instalação do Jekyll](#instalaao-do-jekyll)  
  - [Principais Comandos](#principais-comandos)
  - [Executando o site](#executando-o-site)
  - [Escrevendo um post](#escrevendo-um-post)
    1. [Font Matter](#font-matter)
  - [Básico de Markdown](#bsico-de-markdown)
    1. [Imagens/Arquivos](#imagens-arquivos)
  - [Estrutura de um projeto Jekyll](#estrutura-de-um-projeto-jekyll)
  - [Visual do seu site](#visual-do-seu-site)
5. [No Github](#no-github)
  - [Arquivos a serem ignorados](#arquivos-a-serem-ignorados)
  - [Site do seu usuáro e site para organizações](#site-do-seu-usuario-e-site-para-organizaes)
6. [Links Úteis](#links-teis)


## Jekyll

Jekyll é um gerador de páginas estáticas geralmente usado para a criação de blogs pessoais bem como empresariais.

Tem uma proposta simples, onde usa um conversor <span class="evidence">(Markdown)</span> e um renderizador <span class="evidence">(Liquid)</span> para ajudar a criadora ou criador a produzir informação e o visual que desejam, e que por sua vez podem ficar hospedados em um servidor web de sua preferência.

## Github Pages

O Github Pages é uma proposta do Github para hospedar sites, geralmente blogs pessoais ou sites de projetos também versionados no próprio.

Você pode ter um site por conta no Github. Além disso, para cada organização e/ou projeto que você tenha, é possível criar um site para tal.

Os sites pessoais (por conta) geralmente estão disponíveis na url no formato a seguir:

```
http://username.github.io
```

Para sites de organização será o formato ```http://organizacao.github.io```.

E finalmente para projetos serão ```http://username.github.io/project-name``` ou ```http://organizacao.github.io/project-name```.

A diferença entre os tipos de sites é que para os de projeto, o contéudo deve ser colocado na branch <span class="evidence">gh-pages</span>. Para os outros tipos, a branch <span class="evidence">master</span> é que irá conter tudo que será publicado.

## O que você precisa para começar

Há alguns termos que achei necessário ter uma breve explicação e serão coisas que trabalharemos nesse post.

<b>Gemfile</b>,
como mencionado no site oficial do [Bundle](http://bundler.io/), um arquivo nomeado Gemfile, sem extensão, descreverá todas as dependências necessárias para o funcionamento de um programa na linguagem [Ruby](https://www.ruby-lang.org/pt/).

<b>Markdown</b>

No site do criador, [John Gruber](https://daringfireball.net/projects/markdown/), diz que:

> Markdown é um ferramenta de conversão texto-para-HTML com foco em escritores da web. Markdown permite que você escreva usando um simples formato de texto, fácil de ler e fácil de escrever, e então converte estruturalmente para um formato válido de XHTML (ou HTML). (Tradução livre)

Além disso, vale dizer que a criação do Markdown deve e muito a [Aaron Swartz](https://pt.wikipedia.org/wiki/Aaron_Swartz) que colaborou bastante na confecção da sintaxe.

Markdown está muito presente nos famosos README dos repositórios Github.
<hr>
# Dica
Enquanto escrevia esse post me deparei com esse site: [http://markdowntutorial.com/](http://markdowntutorial.com/). Um tutorial bem legal (em inglês) para quem quer aprender mais sobre como escrever arquivos .markdown.
<hr>

<b>Liquid</b>

Liquid é uma linguagem de template que permite a interação de dados e páginas HTML. Em outras palavras você consegue acessar os seus dados armazenados e mostrá-los facilmente em seu HTML.
O Liquid é quem nos permite acessar nossos posts dentro de um projeto Jekyll, por exemplo.

Em um projeto Jekyll, recém criado, um arquivo index.html possuirá o comando <span class="evidence">{% raw %} {% for post in site.posts %} {% endraw %}</span>. Esse código faz com que todos os posts sejam mostrados usando as tags definidas dentro desse loop.

<script src="https://gist.github.com/roselmamendes/7c2bfee4ead0c7dd9e30.js"></script>

### Ferramentas necessárias

<b>Editor de texto</b>

Quando comecei a escrever esse post usava o [Brackets](http://brackets.io/), mas terminei usando o [Atom](https://atom.io/), só para experimentar mesmo.
Existem outras opções como [Sublime Text](https://www.sublimetext.com/), [Vim](http://www.vim.org/), [Emacs](https://www.gnu.org/software/emacs/), e assim vai.

Escolha o que mais lhe agradar.

<div align="center">
<img src="/assets/images/jekyll-github/choose-wisely.gif" />
</div>

<b>Ruby</b>

No Windows você pode usar o [RubyInstaller](http://rubyinstaller.org/).

Para Mac ou Linux existem as opções [rbenv](https://github.com/rbenv/rbenv) ou [RVM](https://rvm.io/).

Nessa [página](https://www.ruby-lang.org/pt/documentation/installation/) você pode encontrar mais informações.

<b>RubyGem</b>

É necessário instalar o [RubyGem](https://rubygems.org/) para usar a ferramenta <span class="evidence">gem</span> no terminal. Usaremos o gem para instalar o Bundler (a seguir) e outros pacotes.

<b>Bundler</b>

Apenas execute no terminal ```gem install bundler``` e tudo estará pronto para começar a usar.

<hr>
# Dica
Acabei atualizando meu Mac OS para o El Capitan, e tive alguns problemas com o Bundler. Tipo, ele não estava mais instalado :S <a style="color: #f2f2f2">(rosto fazendo muxoxo com os lábios)</a>

Para resolver isso tive que instalar o bundle usando esse comando ```sudo gem install bundler -n /usr/local/bin```.

Tudo isso porque aparentemente o El Capitan passou a usar um tal de SIP (System Integrity Protection) restrigindo a escrita em algumas pastas do sistema.

Links que podem te ajudar na resolução desse problema:
https://talk.jekyllrb.com/t/cant-run-jekyll-on-mac-os-x-10-11-el-capitan/1284/9

http://blog.kapilsharma.info/solving-jekyll-issue-with-mac-os-x-el-capitan-10-11/
<hr>

## Começando nosso site

### Instalação do jekyll
Com todos os itens acima mencionados instalados no seu computador, crie uma pasta para o seu projeto/site.

Dentro da pasta crie um arquivo Gemfile. O nome deve ser Gemfile, sem extensão mesmo.

Com o arquivo Gemfile criado, adicione dentro dele os seguintes comandos:


> source 'https://rubygems.org'

> gem 'github-pages'


Salve o arquivo Gemfile.
Execute no terminal o comando:

```
bundle install
```

Isto instalará o Jekyll, bem como suas dependências necessárias para o projeto.

<div class="img img--fullContainer"><img src="/assets/images/jekyll-github/mensagem-bundle-sucesso.png"/>
</div>
<a style="color: #f2f2f2">Na imagem: Your bundle is complete! Use bundle show [gemname] to see where a bundled gem is installed.</a>

### Principais comandos
```
jekyll new nome-site
```
cria um novo site Jekyll, onde uma pasta com o nome definido por você na parte `nome-site` é criada.


```
bundle exec jekyll serve --watch
```
roda um servidor local disponiblizando a aplicação no endereço `http://localhost:4000`.
O parâmetro `--watch` permite que a cada mudança feita nos arquivos do projeto, elas possam ser vistas imediatamente após atualizar a página no navegador.
Isto economiza a necessidade de ter que reiniciar o servidor. Assim você não precisa executar o comando várias vezes.

### Executando o site

Vamos começar nosso projeto para o site executando o comando:

```
jekyll new nome-site
```

Surgirá uma pasta com o nome dado em `nome-site`.

IMPORTANTE: passe o arquivo `Gemfile.lock` para a pasta do projeto criada acima. Se não você verá um erro de execução como abaixo quando formos executar o próximo comando.

<div align="center" class="img img--fullContainer"><img src="/assets/images/jekyll-github/mensagem-erro-jekyll-sass.png"/>
</div>
<p style="color: #f2f2f2">Na imagem são mostradas, em inglês, algumas mensagens de aviso em amarelo e mais duas mensagens de erro em vermelho. Sobre as mensagens em vermelho elas falam de um erro que ocorre na execução do arquivo main.scss.</p>

Agora execute o comando ``` bundle exec jekyll serve --watch```.

<p style="align-text: left;">Isso acontecerá:</p>
<div align="center" class="img img--fullContainer"><img src="/assets/images/jekyll-github/executando-jekyll-serve.png"/>
</div>
<p style="color: #f2f2f2">Na imagem são mostradas mensagens em inglês que indicam alguns caminhos de pasta e arquivos e informa qual a url local do site</p>

Perceba que a penúltima mensagem diz `Server address: http://0.0.0.0:4000/`. Isso significa que se formos no navegador e digitarmos `http://localhost:4000` um site padrão do Jekyl será carregado.

<div align="center" class="img img--fullContainer"><img src="/assets/images/jekyll-github/pagina-inicial.png"/>
</div>
<p style="color: #f2f2f2">A imagem mostra a página padrão de um site Jekyll. Existem três seções. No título está escrito "Your Awesome Title". Na segunda seção temos os posts. Na terceira seção informações de contato e uma pequena descrição do site.</p>

### Escrevendo um post

Vou dar uma passada no que me parece ser o básico para você escrever um artigo no seu site.

Para adicionar um post em seu site/blog crie um arquivo nomeando-o no seguinte formato:

`YYYY-MM-DD-titulo-do-artigo.markdown`

**YYYY** - ano da publicação;

**MM** - mês da publicação;

**DD** - dia da publicação;

**titulo-do-artigo** - aqui geralmente é um nome para identicar seu post. O Jekyll usa esse nome para formar a url para esta postagem. Para mais de uma palavra use o hífen (-) para separá-las.

E por fim o arquivo deve ter a extensão `.markdown` ou `.md` representando um documento escrito usando a sintaxe Markdown. O arquivo deve ser colocado dentro da pasta `_post` do seu site.

Note que já existe um post criado pelo Jekyll quando criamos o projeto. Se quiser pode removê-lo. Assim ele não aparecerá mais na página principal do seu site.

#### Front Matter

Dentro do arquivo de post é necessário definir certas varíaveis no ínicio. O Jekyll chama essas definições de *Front Matter*.
Essas definições são cercadas de três hífens acima e abaixo.


`---`

title: Este é meu título

layout: post

`---`

Entre esses hífens você pode definir variáveis customizadas e/ou usar as variáveis pré-definidas do Jekyll, tais como:

- layout: defini qual arquivo .html, definido na pasta `_layouts`, a página do post irá usar. São nesses arquivos que podemos brincar com o visual das postagens e página inicial.

- title: o título do post. O que você definir aqui será usado como Título na página do post, bem como na página inicial na lista de posts do seu site.

Tem várias outras variáveis que podem ser definidas. [Aqui](http://jekyllrb.com/docs/frontmatter/) você encontra mais sobre.

Após esse bloco de definições (Front Matter) todo o texto colocado é tratado como o corpo do post.

<hr>
# Lembre-se ...
... de atualizar a página no seu navegador para que possa visualizar as modificações feitas.
<hr>


### Básico de Markdown

Para textos em negrito use dois asteriscos na frente e atrás da palavra.

`**texto**`
**texto**

Para textos em itálico use um asterisco na frente e atrás da palavra.

`*texto*`
*texto*

Títulos e subtítulos são definidos com o uso de um ou mais jogos da velha (#) a frente do texto desejado.

`# Titulo nível 1`

# Título nível 1

`## Titulo nível 2`

## Título nível 2

Listas são criadas usando um hífen (-) ou um asterisco (*) antes das linhas pertencentes a lista.
Para criar subníveis use a tecla tab na frente das linhas desejadas também usando o hífen ou o asterisco.

- linha 1
	- linha 1.1

#### Imagens/Arquivos

Para adicionar imagens ou colocar links para arquivos no seu post você pode usar essa notação:

`![descrição para o recurso](caminho do arquivo na pasta do site)`

Por exemplo, possuo uma imagem mensagem-bundle-sucesso.png na pasta images dentro da pasta do site. Logo poderia colocá-la no post fazendo assim:

`![Mensagem do bundle de sucesso](/images/mensagem-bundle-sucesso.png)`

Minha imagem aparecerá no mesmo lugar que foi colocado esse código.
<hr>
#Dica.
Gosto de usar o [dillinger.io](http://dillinger.io). Um editor online para arquivos markdown. Ele permite que escrevamos o texto e visualizar ao mesmo tempo como ficará em um leitor de markdown.
<hr>
### Estrutura de um projeto Jekyll

<div align="center">
<img src="/assets/images/jekyll-github/jekyll-estrutura-pasta.png"  width="350px" height="300px"/>
</div>

Não vou falar de todas as pastas e arquivos mostrados na imagem acima. Somente as que acredito que valem a explicação para um ínicio com Jekyll.

<b>_config.yml</b> guarda as informações de configuração. Aqui definimos, por exemplo, o nome do site, contatos, e com isso acessá-los em qualquer lugar que quisermos no site.

<b>_includes</b>, nessa pasta encontramos arquivos .html que servem para definir partes de nosso site que podemos replicar em várias páginas, por exemplo, cabeçalho e rodapé das páginas de um site que geralmente são os mesmos em todas páginas.

<b>css</b> é a pasta onde fica o arquivo principal com as definições de estilo do site. Se você abrir esse arquivo percebe um monte de variáveis definidas. Estas são usadas nos arquivos .scss na pasta `_sass`. Alguns temas colocam o css usam a pasta `assets`.

<b>_site</b> é onde o site gerado é armazenado pelo jekyll após as devidas transformações aplicadas. Não é necessário se preocupar com essa pasta, e ela pode ser ignorada quando versionando os arquivos com o Github.

<b>about.md</b> é onde temos a seção Sobre do site. Aqui você pode colocar uma descrição sobre você ou outra coisa que ache pertinente.

<b>_posts</b>, os posts do seu site ficarão nessa pasta. O legal também é que o Jekyll permite o acesso de todos os posts dentro dessa pasta usando a sintaxe do [Liquid](#o-que-voc-precisa-para-comear) nos arquivos .markdown e .html.

Aí dá pra usar a imaginação nos arquivos .html de como mostrar os posts.

### Visual do seu site

Bem, essa parte talvez seja a que mais complique ou não. Pelo menos complicou um pouco comigo, ou melhor, demandou um tempo a mais. Eu não tenho tanto domínio de CSS e HTML e fui "catando" a melhor maneira de fazer o que queria para o visual do site.

Eu enxerguei dois caminhos. Pelo menos foram os que me deparei construindo esse blog.

1. Você pode botar a mão na massa com o CSS e HTML. Manuseando e/ou adicionando os arquivos nas pastas _includes, css, _layouts e o arquivo index.html.

...ou...

2. ...você pode procurar por temas prontos na rede mundial de computadores. Para os íntimos, Google (ou DuckDuckGo, ou outro site de busca de sua preferência. Seja feliz).

Eu fui pelo caminho dos temas.

É o caminho mais fácil? Sim.
<div align="center">
<img src="/assets/images/jekyll-github/will.gif" />
</div>

Procurar temas me ajudou a encontrar visuais que me agradacem, sem que eu tivesse que defini um do zero.
Eu já sei que gosto de coisas com cores, mas ao mesmo tempo o mais clean possível. Assim encontrava os temas nessa categoria e via o que mais se adequava ao meu gosto.

Encontrei o site <a href="http://jekyllthemes.org/">http://jekyllthemes.org/</a>. Lá tem uma variedade de templates para você escolher.

Escolhido o tema, baixe as pastas e arquivos e substitua na sua pasta do projeto.

Se você já tiver escrito algum post. Lembre-se de mantê-los na pasta _posts.

Geralmente os temas vem com alguns posts de exemplo, é legal da uma olhada neles para ver quais variáveis (a parte do [Front Matter](#front-matter)) que o tema está usando para mostrar as informações nas páginas. Por exemplo, imagem oficial do post para ser exibida na página oficial.

Outra coisa, alguns temas vem com algumas configurações a mais no arquivo _config. Por exemplo, teve um tema que baixei que colocava o endereço local do site como http://localhost:4000/DropeAlgumaCoisa, em vez do padrão que é http://localhost:4000. Ou com uma variável para apontar a foto da pessoa autora do site.

Além disso atentar que muitos temas **não vem com o arquivo Gemfile** ou um [rakefile](http://www.akitaonrails.com/2009/02/16/automatizando-tarefas-com-ruby-e-rake/) para executar as dependências do site na máquina. Teve um tema que tive que colocar um arquivo Gemfile e repetir o processo que mencionamos na seção [`Instalação do Jekyll`](#instalao-do-jekyll).

## No Github

A partir do momento que você possui um projeto Jekyll configurado ou não, você pode realizar `push` a um repositório no Github.

### Arquivos a serem ignorados

É interessante que você ignore alguns arquivos e pastas no git, no meu caso eu coloquei em meu arquivo `.gitignore` os seguintes arquivos:

- _drafts
- _site
- .sass-cache
- node_modules

A pasta <span class="evidence">_site</span> realmente não faz sentido nenhum de ir para o Github, já que é uma pasta gerada no momento de compilação dos arquivos. Com ela você só terá arquivos duplicados em seu repositório do Github.

### Site do seu usuario e site para organizações

Como mencionei na seção [`Github Pages`](#github-pages), o Github vai assumir que seu repositório é um site para o domínio `github.io` dependendo se o repo está em uma conta pessoal ou uma organização.

Para as contas pessoais e organizações, o repo do site deve ter o seguinte formato no nome: `username.github.io`.

Este blog, por exemplo, é o repositório `roselmamendes.github.io`.

Com isso em mente atente para o que mencionei na seçao `Github Pages` para ver seu site realmente publicado na web.

E sempre se sinta a vontade para perguntar nos comentários :D <a style="color: #f2f2f2">(rosto sorrindo)</a>

## Links úteis

[Página do Github usando o Jekyll](https://help.github.com/articles/using-jekyll-with-pages/)

[Bundler](http://bundler.io/v1.11/man/bundle.1.html)

[Gemfile](http://bundler.io/v1.11/man/gemfile.5.html)

[Posts no Jekyll](http://jekyllrb.com/docs/posts/)

[Jekyll estrura do diretório](http://jekyllrb.com/docs/structure/)

[Yaml Front Matter](http://jekyllrb.com/docs/frontmatter/)

[Jekyll](http://jekyllrb.com/docs/home/)

[Github Pages](https://help.github.com/articles/user-organization-and-project-pages/)

[Getting Started With Liquid; Shopify’s Template Language](http://webdesign.tutsplus.com/tutorials/getting-started-with-liquid-shopifys-template-language--cms-19747)
