---
layout: post
title: "Rest API, python e Django Rest"
tag: django, rest, api, flask, python, programação, desenvolvimento
date: 2016-03-21 17:39
figura: /assets/images/django-rest/Django-Livre.jpg
published: true
---
<table>
  <tr>
    <td width="400">
    <p>Este post talvez se torne uma apresentação para o <a href="https://djangogirls.org/">Django Girls</a> que rolará aqui em <b>Recife</b> nos próximos meses.</p>
    </td>
    <td>
        <img style="padding: 50px;" width="150" align="center" src="https://djangogirls.org/static/img/global/logo.png" />
    </td>
  </tr>
</table>

<span class="evidence"> Antes de ler esse post pergunte-se se você entende o que é um arquivo HTML. Se entende um pouco (pode ser pouco mesmo) do que rola no desenvolvimento de aplicações Web.</span>

## Rest

<p style="text-align: left;">REST = Representative State Transfer (Transferência de Estado Representacional)</p>

O REST é um estilo arquitetural para aplicações Web, cunhado por <a href="http://roy.gbiv.com/">Roy Fielding</a>, em 2000, na sua tese <b>Architectural Styles and the Design of Network-based Software Architectures</b> [1].

Em termos gerais, uma aplicação que segue as especificações REST disponibiliza métodos (verbos), geralmente pelo protocolo <a href="http://br.ccm.net/contents/266-o-protocolo-http">HTTP</a>, que agirão no servidor, modificando ou obtendo informação.

Com o uso dos verbos teremos acesso aos resources (recursos), que são qualquer mapeamento de um conjunto de dados para uma determinada entidade.

Exemplo de um resource de uma entidade Usuário:

<script src="https://gist.github.com/roselmamendes/778e47dcba28920a480a.js"></script>

Em linhas gerais, se temos uma url `http://servidor-qualquer.com/v1/posts` que recebe um `POST` com um json definido com campos para um usuário. A url gerará uma ação do tipo "Crie um usuário" (um registro na tabela `usuario` será criado). Esta ação gera uma resposta com informações de status e a url <b>única e exclusiva</b> para acessar o registro, entre outras informações da requisição.

<script src="https://gist.github.com/roselmamendes/4e98fe440572658d49cf.js"></script>

Quando temos um serviço baseado em REST costumamos chamá-lo de um serviço <span class="evidence">Restful</span>.

### Verbos

Os verbos mais comumente usados são o GET (visualizar), POST (criar), PUT (atualizar/substituir), PATCH (atualizar/modificar) e DELETE (remover). Além desses verbos, existem outros, mas pouco usados.

No caso do GET, por exemplo, dado que uma aplicação que interage com sua API "chame" `http://servidor-qualquer.com/v1/usuario/1`, ela obterá as informações do registro 1 da tabela usuario. O método GET serve tanto para uma lista de usuários como para obter um único registro.

## API

<p style="text-align: left;">API = Application Programming Interface (Interface de Programação de Aplicação)</p>

Uma API é um conjunto de rotinas usadas pelas aplicações com o intuito de usar um serviço sem conhecer sua implementação. No caso de <span class="evidence">Rest API's</span>, estamos falando de um conjunto de operações disponibilizadas por um serviço Restful.

## Django

<div align="center" >
<img src="/assets/images/django-rest/django-unchained.gif" />
</div>

Não o [filme](http://www.imdb.com/title/tt1853728/) do Quentin Tarantino estrelado pelo Jamie Foxx.

Em se falando de Python, [Django](https://www.djangoproject.com/) é um framework para construção de aplicações Web "que encoraja o desenvolvimento rápido e um design limpo e pragramático".

Imagine que temos uma pesquisa de satisfação que possui uma questão com algumas opções para as pessoas escolherem como resposta.

Aqui abaixo temos um HTML que exibe o enunciado da questão e quantos votos cada resposta recebeu.

Django permite acessarmos, dentro de um arquivo HTML, o objeto Pergunta e com um `for` percorrer suas respostas (linha 4).

<script src="https://gist.github.com/roselmamendes/840de27ecf0ad20ed767.js"></script>

<hr>

E abaixo definimos uma classe View onde relacionamos a classe Pergunta com o resultados.html (linha 8).

<script src="https://gist.github.com/roselmamendes/e814c41b5f201870b491.js"></script>

## Django Rest

Já o Django Rest é a implementação do Django para fazermos Rest API's.

Dado que tenho uma classe herdando de `models.Model` do Django, chamada `Pergunta`, e a classe `Resposta`. Ambas relacionadas visto que uma pergunta pode ter várias respostas.

<script src="https://gist.github.com/roselmamendes/85583b5a5b8a14f035db.js"></script>

Criarei uma view (PerguntaView) que terá definido um serializer chamado PerguntaSerializer.

<script src="https://gist.github.com/roselmamendes/adb4ebdfbe9329aebe36.js"></script>

O Django Rest possui uma quantidade de classes View que já abstraem os principais verbos que um serviço Restful precisa. No exemplo acima utilizamos o `ListCreateAPIView` que possui POST e GET já implementados.

Por sua vez, o serializer faz a "conversão" dos dados de um objeto (Model) para a representação em json (ou outro formato). E vice-versa.

<script src="https://gist.github.com/roselmamendes/03fc0c08e69eb8287585.js"></script>

<table>
  <tr>
    <td>
      <p>Não necessariamente sou obrigada a retornar uma ou mais entidades da forma como elas estão representadas no banco.</p>
    </td>
    <td>
      <img src="/assets/images/django-rest/usurpa.jpg" />
    </td>
  </tr>
</table>
Pelo serializer tenho liberdade de mexer em como desejo representar uma ou mais entidades. Adicionando, removendo campos de acordo com a necessidade do projeto.

Tirando alguns outros passos não mencionados, teremos a url `http://localhost:8000/v1/perguntas` recebendo um json (método POST) e recebendo um outro json em resposta.

<img src="/assets/images/django-rest/resposta-exemplo.png" width="500" height="350" hspace="100px" />

Para facilitar a vida de quem desenvolve, o Django Rest disponibiliza uma interface web que nos permite explorar os verbos implementados.

![Resposta](/assets/images/django-rest/print-django-rest-interface.png)

### Por fim

Além do Django Rest, para a linguagem Python existem outros frameworks voltados para Rest API's como o [Flask](http://flask.pocoo.org/).

Vale dar uma olhada em outras opções e escolher a que melhor atende as necessidades do seu projeto.

Esse post foi muito mais uma visão geral do que é o Django Rest, não entrei em detalhes de como colocar a aplicação para funcionar, então se você se interessou em saber mais sobre visite a página oficial do [projeto](http://www.django-rest-framework.org/). Lá tem alguns tutoriais para aprofundar melhor no framework.

No mais deixe suas perguntas nos comentários que ficarei feliz em responder :) <a style="color: #f2f2f2">(rosto sorrindo)</a>

Claro que críticas, sugestões também são bem-vindas!

## Referências

<p style="text-align: left;">[1]<a href="http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm"> Architectural Styles and
the Design of Network-based Software Architectures - Chapter 5</a></p>

<p style="text-align: left;">[2] <a href="http://www.drdobbs.com/web-development/restful-web-services-a-tutorial/240169069"> RESTful Web Services: A Tutorial</a> </p>

<p style="text-align: left;">[3] <a href="http://www.restapitutorial.com/lessons/httpmethods.html">Using HTTP Methods for RESTful Services</a></p>
