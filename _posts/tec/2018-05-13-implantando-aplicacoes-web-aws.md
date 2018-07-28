---
layout: post
title:  "[Tutorial] Infra na web - AWS e conhecendo o personagem DNS"
modified:   2018-05-13
categories: tec
tags: [implantacao, DEVOPS, AWS, DNS]
image:
  feature: /implantacao-web-app-aws/janelle-monae-afroturismo-1.png
excerpt: "Implantar uma aplicação web envolve certos conceitos que aproveito nesse artigo para aprender e compartilhar."
published: false
---
No início a intenção com esse post era aprender sobre AWS, mas acabei percebendo que o valor desse texto vem dos conceitos por volta do uso dos serviços da AWS. Este post relata minha aventura aprendendo um pouco do uso das ferramentas da AWS e explico sobre DNS nesse contexto. 

A [AWS]() (Amazon Web Service) é a maior empresa que tenho conhecimento no mercado de infraestrura de software ([IaaS - Infrastructure as Service - Infraestrutura como Serviço]()), além dela existem outros serviços como o [GCP]() do Google. [Existe um vasto número de serviços que a AWS fornece](). Neste post vou colocar um site estático "no ar" o que **não cobre boa parte dos serviços da Amazon**.

## Qual a primeira coisa a fazer colocando um site no ar na AWS?

Encontrei esse [link](https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html) da própria AWS que explica como colocar um site no ar. Nele são mencionados os seguintes passos:

1. Obter seu domínio por uma empresa Registrar (palavra em Inglês) - para esse passo eu escolhi a ?;

2. Criar buckets no serviço S3 (vê [Serviços da AWS utlizados neste post](#servicos-da-aws-utilizados-neste-post));

3. Importar os arquivos do site para esses buckets criados no passo anterior;

> info ""
> Enquanto escrevia esse texto, onde houve uma pausa de 1 mês mais ou menos, a AWS mudou o conteúdo do tutorial onde mencionava sobre Registrar.
> AWS oferece o registro de domínio com o Route53.

## Antes de falarmos de DNS, vamos criar buckets e importar os arquivos do site

Para o conteúdo do site estático tudo gira em torno do S3 (Simple Storage Service - serviço básico de armazenamento) da AWS, você manda os arquivos para um bucket, configura a permissão de acesso (AWS policies) e diz que esse bucket irá servir como um site estático.

Eu criei dois buckets na minha conta da AWS: um chamado `roselmamendes.com` e outro `www.roselmamendes.com`. A intenção com esses dois buckets é que seja possível acessar o site se digitado `roselmamendes.com` ou `www.roselmamendes.com`.

Para o bucket `roselmamendes.com` eu carrego um arquivo `index.html`.

Também para o `roselmamendes.com` configuro um bucket policy para ter acesso publico.

<figure>
	<img src="/images/implantacao-web-app-aws/bucket-policy.png" alt="image">
	<figcaption>no <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html">link de tutorial sobre implantar site estatico</a> tem um exemplo de um bucket policy.</figcaption>
</figure>

[É possível depois abrir o arquivo no bucket para acessar seu link](https://s3.us-east-2.amazonaws.com/roselmamendes.com/index.html). Se você clica nele é aberto o arquivo como uma página. Afinal estamos acessando um arquivo .html pelo navegador, e o bucket age como se fosse uma pasta na internet que possui nosso arquivo.

Mas como não pretendo usar a url padrão do bucket, é necessário configurar os buckets como site estático. Para o `roselmamendes.com`, em Properties eu escolho Static Web hosting, escolho a primeira opção e coloco o nome do arquivo index.html. Para o `www.roselmamendes.com`, em Properties eu escolho também Static Web hosting, escolho Redirect requests e coloco o nome do bucket roselmamendes.com.

## Nessa história toda onde entra esse danado de DNS?

DNS vem de Domain Name System (Sistema de Nome de Domínio - tradução livre). DNS faz a tradução de toda url que conhecemos para um endereço de IP. Isso quer dizer que existe alguem que traduz toda vez que você acessa [o `google.com` para `http://74.125.224.72/`](https://www.lifewire.com/what-is-the-ip-address-of-google-818153), por exemplo.

Dito isso, todo o site na Internet aponta para um endereço de IP. Para o seu site não será diferente. Por isso você precisa registrar um domínio.

Com toda a configuração acima feita no S3, eu já tenho a url `http://roselmamendes.com.s3-website.us-east-2.amazonaws.com`. Mas esta não é uma url muito amigável de ler e escrever. Eu gostaria de usar somente `roselmamendes.com`. Aí é que entra o DNS.

Para uma leiga como eu, que não sabe nada de configuração de DNS, achei bem difícil compreender o que fazer se não quero usar o Route53 da AWS como meu serviço de DNS. Depois de várias tentativas com palavras-chave no Google, achei [esse stackoverflow](https://stackoverflow.com/a/8357318).

**DNS record**

Name server

CNAME

A

## Serviços/termos da AWS utilizados neste post

[S3]()

[Route53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-dns-service.html)

[AWS policies]()

## Referências

**Em Inglês**

[DNS](https://en.wikipedia.org/wiki/Domain_Name_System)

[Registrar para DNS](https://en.wikipedia.org/wiki/Domain_name_registrar)

[Domain Registration vs DNS Service vs Web-Hosting](https://fusion.easydns.com/Knowledgebase/Article/View/159/17/domain-registration-vs-dns-service-vs-web-hosting)

[List de Registrars](https://www.icann.org/resources/pages/registrars-0d-2012-02-25-en)

[Tutorial da AWS para uma aplicação web estática](https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html)

[Os 10 melhores provedores de DNS](https://www.keycdn.com/blog/best-free-dns-hosting-providers/)
