---
layout: post
title: Um dia, Roselma conheceu o Jekyll no Github, então viu que era bom
categories: frontend
published: false
---

Nada como começar um blog com um texto descrevendo como eu criei o próprio blog.

*Para entendimento desse artigo é necessária uma noção de programação e conhecer certos termos utilizados no desenvolvimento de software.
Eu tento explicar algumas coisas, mas abordar tudo fica inviável, acredito.
Tem dúvida? Pergunta aí nos comentários que eu tento responder dentro do possível.
:) (rosto sorrindo)*


## Jekyll

## Github Pages
Github

Github Pages

## O que você precisa para começar

Há alguns termos que achei necessário ter uma breve explicação e serão coisas que trabalharemos nesse post.

**Bundler**
é uma ferramenta que com a ajuda de um arquivo *Gemfile* instala e gerencia as dependências de uma aplicação na linguagem Ruby.
Muito usado para o compartilhamento entre equipes que programam em Ruby, onde cada desenvolvedora ou desenvolvedor pode ter as mesmas dependências que as outras pessoas do time possuem.
Esta prática elimina problemas de incompatibilidades no ambiente de desenvolvimento bem como no lançamento das aplicações aos usuários, evitando que o programa não funcione por falta de alguma dependência que não está instalada.

**Gemfile**,
como mencionado no site oficial do [Bundle](http://bundler.io/), um arquivo nomeado Gemfile sem extensão descreverá todas as dependências necessárias para o funcionamento de um programa na linguagem [Ruby](https://en.wikipedia.org/wiki/Ruby_(programming_language)).

**Markdown**
Tutorial sobre Markdown http://markdowntutorial.com/

**HTML**

**Liquid**

**CSS e SASS**

#Atente... 
...que quando coloco os comandos para serem executados no terminal, eles aparecerão com as letras `sh` na frente.
Ao copiar ou digitar os comandos em seu computador, esqueça o `sh`. Ele só serve para identificar em um texto demonstrado que se trata de uma linha de comando a ser executada no terminal (Windows -> MS-DOS/Mac -> terminal).

### Ferramentas necessárias
{Windows/Mac
Editor de texto
Ruby
Bundler
Jekyll}

## Na sua máquina

### Instalação do jekyll
Com todos os itens acima mencionados instalados no seu computador, crie uma pasta para o seu projeto/site.

Dentro da pasta crie um arquivo Gemfile. O nome deve ser Gemfile, sem extensão mesmo.

Com o arquivo Gemfile criado, adicione dentro dele os seguintes comandos:


> source 'https://rubygems.org'

> gem 'github-pages'


Salve o arquivo Gemfile.
Execute no terminal o comando:

```sh
bundle install
```

Isto instalará o Jekyll, bem como suas dependências necessárias para o projeto.

![Sucesso](/assets/images/mensagem-bundle-sucesso.png)

**github-pages**

### Principais comandos
```
jekyll new nome-site
```
cria um novo site Jekyll, onde uma pasta com o nome definido por você na parte `nome-site` é criada.


```
bundle exec jekyll serve --watch
```
roda um servidor local disponiblizando a aplicação no endereço *http://localhost:4000*.
O parâmetro `--watch` permite que a cada mudança feita nos arquivos do projeto, elas possam ser vistas imediatamente após atualizar a página no navegador. 
Isto economiza a necessidade de ter que reiniciar o servidor. Assim você não precisa executar o comando acima várias vezes.

Porém, o `--watch--` é opcional.
Se escolher não usar o `--watch` (como demonstrado abaixo), a cada alteração que fizer, você precisará usar o Ctrl+C/CMD+C (Windows/Mac) para parar o servidor e depois chamar novamente o comando de iniciar o servidor. Dessa forma:

```sh
bundle exec jekyll serve
```

Fica a seu critério.

### Executando o site

Vamos começar nosso projeto para o site executando o comando:

```sh
jekyll new nome-site
```

Surgirá uma pasta com o nome dado em `nome-site`.

IMPORTANTE: passe o arquivo `Gemfile.lock` para a pasta do projeto criada acima. Se não você verá um erro de execução como abaixo quando formos executar o próximo comando.

![Erro](/assets/images/mensagem-erro-jekyll-sass.png)

Agora execute o comando ```sh bundle exec jekyll serve --watch```.

Isso acontecerá:
![Executando o servidor do jekyll](/assets/images/executando-jekyll-serve.png)

Perceba que a penúltima mensagem diz `Server address: http://0.0.0.0:4000/`. Isso significa que se formos no navegador e digitarmos `http://localhost:4000` um site padrão do Jekyl será carregado.

![Página inicial](/assets/images/pagina-inicial.png)

### Escrevendo um post

Vou dar uma passada no que me parece ser o básico para você escrever um artigo no seu site.

Para adicionar um post em seu site/blog crie um arquivo no seguinte formato em seu nome:

`YYYY-MM-DD-titulo-do-artigo.markdown`

**YYYY** - ano da publicação;

**MM** - mês da publicação;

**DD** - dia da publicação;

**titulo-do-artigo** - aqui geralmente é um nome para identicar seu post. O Jekyll usa esse nome para formar a url para esta postagem. Para mais de uma palavra use o hífen `-` para separá-las.

E por fim o arquivo deve ter a extensão `.markdown` ou `.md` representando um documento escrito usando a sintaxe Markdown. O arquivo deve ser colocado dentro da pasta `_post` do seu site.

Note que já existe um criado pelo Jekyll quando criamos o projeto. Se quiser pode removê-lo. Assim ele não aparecerá mais na página principal do seu site.

Dentro do arquivo de post é necessário definir certas varíaveis no ínicio. O Jekyll chama essas definições de *Front Matter*.
Essas definições são cercadas de três hífens acima e abaixo.


`---` 

title: Este é meu título

layout: post

`---`

Entre esses hífens você pode definir variáveis suas e/ou usar as variáveis pré-definidas do Jekyll, tais como:

- layout: defini qual arquivo .html, definido na pasta `_layouts` a página do post irá usar. São nesses arquivos que podemos brincar com o visual das postagens e página inicial.

- title: o título do post. O que você definir aqui será usado como Título na página do post, bem como na página inicial na lista de posts do seu site.

Tem várias outras que podem ser definidas. [Aqui](http://jekyllrb.com/docs/frontmatter/) você encontra mais sobre.

Após esse bloco de definições todo o texto colocado é tratado como o corpo do post.

# Lembre-se ...
... de atualizar a página no seu navegador para que possa visualizar as modificações feitas.

#### Básico de Markdown
	
Para textos em negrito use dois astericos na frente e atrás da palavra. 

`**texto**`
**texto**

Para textos em itálico use um asterisco na frente e atrás da palavra. 

`*texto*`
*texto*

Títulos e subtítulos são definidos com o uso de um ou mais jogos da velha `#` a frente do texto desejado.

`# Titulo nível 1`
	
# Título nível 1
	
`## Titulo nível 2`

## Título nível 2
	
Listas são criadas usando um hífen `-` ou um asterisco `*` antes das linhas pertencentes a lista.
Para criar subníveis use a tecla tab na frente das linhas desejadas também usando o hífen ou o asterisco.

- linha 1
	- linha 1.1

	
#### Imagens/Arquivos

Para adicionar imagens ou colocar links para arquivos no seu post você pode usar essa notação:

`![descrição para o recurso](caminho do arquivo na pasta do site)`

Por exemplo, possuo uma imagem mensagem-bundle-sucesso.png na pasta images dentro da pasta do site. Logo poderia colocá-la no post fazendo assim:

`![Mensagem do bundle de sucesso](/images/mensagem-bundle-sucesso.png)`

Minha imagem aparecerá no mesmo lugar que foi colocado esse código.

### Estrutura de um projeto Jekyll

![Estrutura da pasta](/assets/images/jekyll-estrutura-pasta.png)

Não vou falar de todas as pastas e arquivos mostrados na imagem acima. Somente as que acredito que valem a explicação para um ínicio com Jekyll.

**_config.yml** guarda as informações de configuração. Aqui definimos, por exemplo, o nome do site, contatos, e com isso acessá-los em qualquer lugar que quisermos no site.

**_includes**, nessa pasta encontramos arquivos .html que servem para definir partes de nosso site que podemos replicar em várias páginas, por exemplo, cabeçalho e rodapé das páginas de um site que geralmente são os mesmos em todas páginas.

**css** é a pasta onde fica o arquivo principal com as definições de estilo do site. Se você abri esse arquivo percebe um monte de variáveis definidas. Estas são usadas nos arquivos .scss na pasta `_sass`.

**_site** é onde o site gerado é armazenado pelo jekyll após as devidas transformações aplicadas. Não é necessário se preocupar com essa pasta, e ela pode ser ignorada quando versionando os arquivos com o Github.

**about.md** é onde temos a seção Sobre do site. Aqui você pode colocar uma descrição sobre você ou outra coisa que ache pertinente.

**_posts**, como já falamos na seção `Escrevendo um post`, os posts do seu site ficarão nessa pasta. O legal também é que o Jekyll permite o acesso de todos os posts dentro dessa pasta usando a sintaxe do Liquid nos arquivos .markdown e .html. 

Aí dá pra usar a imaginação nos arquivos .html de como mostrar os posts.

### Visual do seu site

Bem, essa parte talvez seja a que mais pegue ou não. Pelo menos pegou um pouco, ou melhor, demandou um tempo a mais. Eu não tenho tanto domínio de CSS e HTML assim e fui catando a melhor maneira de fazer o que queria para o visual do site.

Eu enxerguei dois caminhos. Pelo menos foram os que me deparei construindo esse blog.

1. Você pode bota a mão na massa com o CSS e HTML. Manuseando e/ou adicionando os arquivos nas pastas _includes, css, _layouts e o arquivo index.html.

...ou...

2. ...você pode procurar por temas prontos na rede mundial de computadores. Para os íntimos, Google (ou DuckDuckGo, ou outro site de busca de sua preferência. Seja feliz).

Eu fui pelo caminho dos temas.

É o caminho mais fácil? Sim.

Procurar temas me ajudou a encontrar visuais que me agradacem, sem que eu tivesse que defini um antes.
Eu já sei que gosto de coisas com cores, mas ao mesmo tempo o mais clean possível. Assim encontrava os temas nessa categoria e via o que mais se adequava ao meu gosto.

Encontrei o site http://jekyllthemes.org/. Lá tem uma variedade de templates para você escolher.

Escolhido o tema, baixe as pastas e arquivos e substitua na sua pasta do projeto.

Se você já tiver escrito algum post. Lembre-se de mantê-los na pasta _posts. 

Geralmente os temas vem com alguns posts de exemplo, é legal da uma olhada neles para ver quais variáveis (a parte do Front Matter) a pessoa criadora está usando para mostrar as informações nas páginas. Por exemplo, imagem oficial do post para ser exibida na página oficial.

Outra coisa, alguns temas vem com algumas configurações a mais no arquivo _config. Por exemplo, teve um tema que baixei que colocava o endereço local do site como http://localhost:4000/DropeAlgumaCoisa, em vez do padrão que é http://localhost:4000. Ou com uma variável para apontar a foto da pessoa autora do site.

Além disso atentar que muitos temas **não vem com o arquivo Gemfile** ou um [rakefile](http://stackoverflow.com/questions/2881482/what-is-a-rakefile) para executar as dependências do site na máquina. Teve um tema que tive que colocar um arquivo Gemfile e repetir o processo que mencionamos na seção `Instalação do Jekyll`.

## No Github
Arquivos a serem ignorados
Diferença entre o site do seu usuario e site para organizações
Nome do repositório

## Referências (infelizmente em inglês)
[Página do Github sobre o Jekyll](https://help.github.com/articles/using-jekyll-with-pages/)

[Bundler](http://bundler.io/v1.11/man/bundle.1.html)

[Gemfile](http://bundler.io/v1.11/man/gemfile.5.html)

[Posts no Jekyll](http://jekyllrb.com/docs/posts/)

[Jekyll estrura do diretório](http://jekyllrb.com/docs/structure/)

[Yaml Front Matter](http://jekyllrb.com/docs/frontmatter/)