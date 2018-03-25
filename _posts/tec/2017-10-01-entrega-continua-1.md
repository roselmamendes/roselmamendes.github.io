---
layout: post
title:  "Entrega Contínua, o que aprendi - parte 1"
modified:   2017-10-01
categories: tec
tags: [entrega continua, automacao, dev cli, Mulher Negra, Tecnologia]
image:
  feature: entrega-continua/riri-iron-heart.jpeg
  credit: Riri Williams - IronHeart
  creditlink: en.wikipedia.org/wiki/Riri_Williams
excerpt: "Como utilizar conteinerização para aplicações web e qual a vantagem disso."
comments: true
share: true
hidelogo: true
published: true
---

Já ouviu sobre Entrega Contínua? Seu time implementa essa prática?

A idéia deste post é descrever como fui montando a infraestrutura para o desenvolvimento de um Blog. Com isso, vou tocando em pontos que aprendi no meu trabalho sobre Entrega Contínua.

Eu dividi em dois posts, pois ficou muito longo (eu não gosto de texto com mais de 5 min. Desculpa. rs)

Esta é a primeira parte.

#### Por que Entrega Contínua?

Vou chegar lá, mas primeiro o que é Entrega Contínua.

Uma boa e bem conhecida fonte sobre o assunto é o [livro Entrega Contínua do Jezz Humble e o David Farley](https://www.amazon.com.br/Entrega-Cont%C3%ADnua-Entregar-Software-Confi%C3%A1vel/dp/8582601034).

No livro há uma frase que diz "Entrega de software deve ser rápida, um processo repetitivo".

A entrega contínua é sobre a capacidade de seu sistema está pronto para ser usado. Nós podemos trazer essa definição para funcionalidades. Quão fácil, confiável é ter uma funcionalidade funcionando e disponível para as pessoas que usam sua aplicação?

A sua aplicação (um app mobile, uma API, um site, etc) deve ser fácil, rápida e confiável de ser liberada para uso.

Isto é importante para seu time e pessoas que usam seu sistema. Uma desenvolvedora está tranquila em vez de frustrada em trabalhar mais uma vez em uma nova funcionalidade ou um bug (que não seja criado pelo processo de entrega); as pessoas estão felizes em usar sua app com novas funcionalidades e têm os bugs consertados pelo seu time. Ao mesmo tempo, sua aplicação continua funcionando bem desde sua primeira entrega, em um cenário tranquilo e gerenciável (alguém pede novas funcionalidades, lidar com expectativas de cliente).

Seu time tem uma entrega simples, sem dores de cabeça. Pessoas felizes em usar um sistema que elas veem <b>valor</b> em usar/trabalhar.

Pela felicidade de todas as pessoas envolvidas com sua aplicação, você precisa de um deployment pipeline (ou na minha tradução livre, processo de implantação).

E isso é automatizado o máximo possível.

<figure>
	<a href="#"><img src="/images/entrega-continua/deployment-pipeline.png" alt="image"></a>
	<figcaption>Um processo de implantação (deployment pipeline), termo do livro Entrega Contínua.</figcaption>
</figure>

#### Ao blog

O blog terá as funcionalidades de publicar um post e mostrar a lista de posts.

Primeiro vamos criar um repositório em um controle de versão. No meu caso o [Github](https://github.com/roselmamendes/continuous-delivery-blog).

Com um controle de versão temos um histórico das mudanças. Isso permiti que mais pessoas contribuam ao projeto, e por fim isso nos ajuda com a Integração Contínua (próximo post).

Ter um controle de versão cobre os requisitos para o estágio de commit (commit stage) do processo de implantação (deployment pipeline). Antes de disparar o processo de entrega, nós precisamos saber que algo foi criado ou modificado no nosso código-fonte.

<b>Documentação e DEV CLI</b>

Onboarding=receber uma nova pessoa no time

Fazer o onboarding de alguém é uma das partes mais importantes no desenvolvimento de software. Afinal seria uma perda de tempo, custo e motivação manter por muito tempo duas ou mais desenvolvedoras tentando configurar um ambiente local e não desenvolvendo uma nova funcionalidade.

Ter um processo de onboarding bem documentado, principalmente usando automação, para mim, é uma das coisas mais espertas que seu time pode fazer.

Em alguns projetos pessoais eu uso o README (Github) para informar os comandos mais relevantes: construir a imagem ([Docker](http://brunoizidorio.com.br/blog/docker-o-que-e-docker/)), executar o container (Docker), rodar os testes dentro do container (Docker). Em outros projetos eu crio um arquivo bash para abstrair estes comandos.

Para projetos [OSS](https://canaltech.com.br/produtos/O-que-e-open-source/), é comum encontrar um contributing.md. Um arquivo para colocar tudo necessário para ter o projeto pronto para desenvolver.

Em meu time atual eu conheci sobre Dev CLI's. Os que conheço são simples programas em bash que disponibilizam os comandos para trabalhar em um projeto: rodar testes, subir o servidor, rodar lint checks, por exemplo. [Aqui](https://github.com/mavcunha/devcli) um projeto que pode ajudar você a começar um Dev CLI.

Para o projeto do Blog eu criei um simples [script bash](https://github.com/roselmamendes/continuous-delivery-blog/blob/master/cd-blog.sh).

<b>Ready to dev — pronto para desenvolver</b>

Algo que eu costumo fazer quando inicio um projeto é criar um [Dockerfile](http://flaviosilveira.com/2017/criando-seu-container-com-dockerfile/). Meu ponto é, eu começo pensando sobre o ambiente para executar a aplicação em minha máquina.

Com Docker eu tenho a oportunidade de ser mais "a mulher da infra" e ter mais controle sobre as dependências de um projeto.

Também penso o quão fácil seria para alguém que queira contribuir/usar minha app clonando do repositório.

Quando implantando (deploy), pessoalmente não estou usando o Docker, mas eu recomendo o uso ou outra solução similar a ele. Ao menos para o ambiente local para que seja tranquilo para outras pessoas que trabalhem no mesmo código-fonte que você.

Ter uma nova funcionalidade ou bug consertado significa também um onboarding tranquilo para as pessoas que começam no seu projeto. O quanto mais rápido elas tiverem prontas para entregar valor para o seu projeto, melhor.

<b>Este é só o começo</b>

No [próximo post](https://medium.com/@roselmamendes/entrega-cont%C3%ADnua-o-que-aprendi-cap%C3%ADtulo-2-2cfbcb09c8bf) escrevo sobre Integração Contínua, Segurança e Implantação.

Como é o processo para você e/ou seu time para começar um novo projeto?




