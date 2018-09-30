---
layout: post
title:  "Docker no desenvolvimento web (nodejs)"
modified:   2018-02-01
categories: tec
tags: [docker, node, contêineres]
image:
  feature: docker-dev-web/group_5622_0.png
excerpt: "Como utilizar conteinerização para aplicações web e qual a vantagem disso."
published: true
---
## Conteinerização

Assim como as máquinas virtuais, os contêineres possibilitam o isolamento de um ambiente de execução para uma aplicação.
Esse isolamento compreende as dependências e componentes da sua aplicação. 

Em outras palavras, se chamarmos container de pacote então: temos um pacote com as configurações necessárias para executar seu programa, e esse pacote é facilmente distribuído entre seu time e/ou ambientes (implantação e desenvolvimento local).

O processo de implantação pode ser otimizado com a ajuda de contêineres no que diz respeito às práticas de Entrega e Implantação Contínua, quando se pensa na propagação da configuração de mais um ambiente ao longo de uma pipeline. Ou pensando simples, na garantia de que a mesma configuração do ambiente da desenvolvedora vai ser replicado para o ambiente de produção.

Diferente de uma máquina virtual, os contêineres são mais "leves". Contêineres se utilizam dos recursos do sistema operacional do "computador host" para execução dos processos. Enquanto as máquinas virtuais "levantam" um sistema operacional completo dentro do "computador host".

<figure>
	<a href="#"><img src="/images/docker-dev-web/Container-Overview.png" alt="image"></a>
	<figcaption>visão geral de um container</figcaption>
</figure>

O uso de contêineres não é só para sistemas distribuídos ou microsserviços. A conteinerização é uma vantagem também para arquiteturas simples com componentes como frontend, backend/api, etc. No final a intenção é manter uma implantação segura e fácil de distribuir.

## Vantagens da Conteinerização

Do [post](https://www.digitalocean.com/community/tutorials/o-ecossistema-do-docker-uma-introducao-aos-componentes-comuns-pt) do Digital Ocean:

* Utilização leve de recursos: Em vez da virtualização de um sistema operacional inteiro, os contêineres isolam no nível de processos e utilizam o kernel do host.
* Portabilidade: Todas as dependências para uma aplicação conteinerizada são empacotadas dentro do contêiner, permitindo-a executar em qualquer host Docker.
* Previsibilidade: O host não se importa com o que está sendo executado dentro do contêiner e o contêiner não se importa em qual host ele está executando. As interfaces são padronizadas e as interações são previsíveis.


Estes pontos significam que é possível ter um onboarding no time (pessoas novas no seu time) mais rápido e simples; um processo de implantação rápido e seguro (AWS e Heroku são exemplos de serviços que permitem o deploy de aplicações usando Docker); garantia de que “se na minha máquina funciona na sua também é para funcionar” (desenvolvedora, testadora e ambiente de produção usando a mesma configuração de ambiente).


## Docker
<figure>
	<a href="#"><img src="/images/docker-dev-web/dados-docker.png" alt="image"></a>
	<figcaption><a href="https://www.docker.com/company" title="">https://www.docker.com/company</a></figcaption>
</figure>

[Docker](https://www.docker.com/) é uma plataforma open source para a construção e execução de contêineres. Em 2013, a plataforma começou sua história que revolucionou o uso de contêineres no desenvolvimento de software. 

<img src="/images/docker-dev-web/docker-logo.png" />
Hoje falar em dockerizar uma aplicação já é um termo na comunidade de TI.

## Imagem e contêiner

Uma imagem, [como no próprio site do Docker relata](https://docs.docker.com/get-started/#a-brief-explanation-of-containers), é um pacote executável com tudo necessário para rodar um componente de software. Um dockerfile terá as instruções para montar uma imagem, mas ela precisa ser construída para termos um contêiner.

Já um contêiner é uma instância da imagem. Como falamos mais acima sobre o que é um contêiner, um ambiente isolado no "computador host" que acessa arquivos e portas, se configurado para a tal.

## Dockerizando uma aplicação web
A primeira coisa que você precisa é ter um arquivo Dockerfile na pasta do seu repositório.

Como minha aplicação vai usar pacotes Node, vou utilizar uma imagem pronta de Node. No [Docker Hub](https://hub.docker.com/) eu encontrei [essa](https://hub.docker.com/_/node/) imagem e no meu Dockerfile vou colocar:

{% highlight python linenos %}
FROM node:8.7.0
{% endhighlight %}

Node possui imagens para várias versões. Isso acontece com outras imagens no Docker Hub, como por exemplo, [essa](https://hub.docker.com/_/postgres/) imagem para Postgres.

Para construir uma imagem para minha aplicação posso executar o comando `docker build -t docker-apresentacao .`, e então eu obtenho mais ou menos essa saída no meu terminal:

<figure>
	<img src="/images/docker-dev-web/saida-docker-build-from.png" />
</figure>

Dentro do arquivo Dockerfile, a palavra reservada `FROM` seguida de `node:8.7.0`, diz ao Docker para montar minha imagem "herdando" da imagem `node:8.7.0` (linha 1). A imagem do node copia o arquivo `package.json` para a pasta do container (linha 8) e executa o `npm install` dentro do próprio container (linha 9).

<figure><img src="/images/docker-dev-web/dockerfile-node-onbuild.png" />
<figcaption><a href="https://github.com/nodejs/docker-node/blob/15d780e932fc8cd4a145a36cff405610c8c71b0c/8.7/onbuild/Dockerfile">Veja mais no Github</a></figcaption>
</figure>

<figure><img src="/images/docker-dev-web/docker-build-image-diagram.png" />
<figcaption>construindo uma imagem</figcaption></figure>

Executando `docker images` veremos a imagem para `docker-apresentacao` na lista de imagens.

<figure><img src="/images/docker-dev-web/saida-docker-images.png" /></figure>

Após construir a imagem, executo o `docker run -p 3000:3000 -t docker-apresentacao npm start`. Isto deve permiti que eu acesse em <i>http://localhost:3000</i> a aplicação.

<b>package.json</b>

Com node, para otimizar a construção de uma imagem você precisa separar o momento de instalar os pacotes da cópia do código fonte para o container. Isto facilita quando você modifica um arquivo em específico e isso não dispara a instalação das dependências desnecessariamente.

<figure><img src="/images/docker-dev-web/dockerfile-packagejson.png"/></figure>

<b>Montando volumes</b>

Para que você possa editar os arquivos e isto reflita no container o comando `docker run` precisa ter `-v <pasta-host>:<pasta-container>` e definido o diretório de trabalho com o parâmetro `-w <pasta-container>`.


`docker run --rm -p 3000:3000 <b>-v "$PWD":/usr/src/app</b> -w /usr/src/app -it nome-container yarn test`

<b>Como acessar uma aplicação localmente</b>

Para que seja possível eu acessar na minha máquina o endereço http://localhost:3000, é necessário usar `-p <porta-host>:<port-container>`. No Dockerfile colocar o `EXPOSE <porta-container>`.

`docker run --rm <b>-p 3000:3000</b> -v "$PWD":/usr/src/app -w /usr/src/app -it nome-projeto yarn test`

Use o parâmetro --rm para garantir que ao "fechar" o container, ele seja destruído. 
 
<b>node_modules<b>

Quando docker, na construção da imagem, chama o npm install, o node_modules é criado e a pasta fica na raiz do repositório. Porém isto traz problemas se você executa o comando docker run com -v. O -v diz para "sincronizar" sua pasta do repositório (sem node_modules) para a pasta do container. Então o comando quebra dizendo que o mesmo não existe, porque o node_modules já não está lá.

O truque que uso é que ao construir a imagem, no Dockerfile, especifico que o npm install execute dentro de uma pasta acima da pasta onde ficará o código fonte.

```
+-- /usr/src
	+-- node_modules
	+-- app
```

No Dockerfile fica como nas linhas 7 a 13:

{% gist 51c1b0b6ca1f786c9c3d5e018e7316e4 %}

Perceba que primeiro a construção da imagem começa com o workdir apontando para `usr/src` e depois o workdir passa a ser `usr/src/app`. O último para que o código fonte seja copiado em app em vez de usr.

## Comandos básicos do Docker

docker build: constrói a imagem

docker run: executa o container

docker ps / docker ps -a: mostra os contêineres em execução / mostra os contêineres parados e executando

docker images: lista as imagens construídas

docker system prune: para remoção de artefatos do Docker (imagens, contêineres, volumes, redes) 

## Conclusão

Conteiner não é um termo novo, mas seu uso tem se tornado mais aparente dentro da comunidade recentemente.
É um movimento muito defendido no DevOps, e quando se fala de ter uma entrega (release) confiável muitos estão adotando-a, assim como Infraestrutura como código.


## Referências
[Docker… da teoria ao Hands on](https://www.mundotibrasil.com.br/docker-da-teoria-ao-hands-on/)

[O Ecossistema do Docker: Uma Introdução aos Componentes Comuns](https://www.digitalocean.com/community/tutorials/o-ecossistema-do-docker-uma-introducao-aos-componentes-comuns-pt)

[A Survival Guide for Containerizing your Infrastructure — Part 1: Why switch?](https://medium.com/google-cloud/a-survival-guide-for-containerizing-your-infrastructure-part-1-why-switch-8e8dee9fc66)

[A Brief History of Containers: From 1970s chroot to Docker 2016](http://blog.aquasec.com/a-brief-history-of-containers-from-1970s-chroot-to-docker-2016)

[Docker Inc](https://www.sdxcentral.com/listings/docker-inc/)

[Get Started, Part 1: Orientation and setup](https://docs.docker.com/get-started/#a-brief-explanation-of-containers)

[Get Started, Part 2: Containers](https://docs.docker.com/get-started/part2/)

