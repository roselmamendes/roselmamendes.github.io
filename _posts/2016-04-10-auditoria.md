---
layout: post
title: "Logs"
date:   2016-06-04 13:50:00
last_modified_at:  2016-06-04 13:50:00
excerpt: "Se você é uma desenvolvedora ou desenvolvedor, e reparar, logs fazem parte do nosso dia-a-dia, desde aqueles que geramos em nossos sistemas, desde aqueles que **interpretamos** de sistemas de terceiros."
categories: arquitetura
tags:  ["auditoria", "logs", "log estruturado"]
image:
  feature: /auditoria/carta-pero-vaz-de-caminha.jpg
  topPosition: 0px
bgContrast: dark
bgGradientOpacity: lighter
syntaxHighlighter: no
---

No projeto que trabalhava, desenvolvemos uma **auditoria** para registrar a comunicação com os serviços externos, alertas sobre inconsistências nos dados e erros.

Queríamos prover qualidade na investigação de erros. Nós deveríamos fazer o sistema "falar" sobre esses erros de maneira **rastreável** para que encontrássemos a raiz dos problemas o mais rápido possível e resolvêssemos quando fosse a hora.


## Logging

Foi um pouco complicado pesquisar sobre o assunto. Usar como palavra-chave `log`, `logfile`, até mesmo `logging`, não me trouxeram boas fontes na área.

<div align="center" class="img img--fullContainer">
  <img src="/assets/images/auditoria/logging-arvore.jpg"/>
  <p style="font-size: 14px; text-align: center;">Logging, de acordo com os primeiros resultados do Google.</p>
</div>
<p style="color: #f2f2f2">Figura mostrando uma floresta com arvores cortadas.</p>

Com ajuda, me deparei com o termo **logging estruturado**. Essa sim foi uma boa palavra-chave.

Se você é uma desenvolvedora ou desenvolvedor, e reparar, logs fazem parte do nosso dia-a-dia, desde aqueles que geramos em nossos sistemas, desde aqueles que **interpretamos** de sistemas de terceiros.

E aqui vai uma definição que acredito se aplicar, e vem de um [texto](http://gregoryszorc.com/blog/category/logging/) do [Gregory Szorc](http://gregoryszorc.com/resume.pdf ), engenheiro da Mozilla:

> "(Logs são) um fluxo de mensagens distintas geradas a partir da execução de um programa."

---------
Logs geralmente são guardados em simples arquivos de texto, como .npm-log do NPM.
e também são mostrados em terminais/consoles.
<div align="center" class="img img--fullContainer">
  <img src="/assets/images/auditoria/example.png"/>
</div>
<p style="color: #f2f2f2">Figura mostrando a tela de um terminal com mensagens de log.</p>

Linguagens de programação proveem uma maneira de criarmos log.

Em Python temos o logger, no Javascript console.log. A simples chamada de um print() do Python ou system.out.println() do Java informando o que está ocorrendo já é um log.

As linguagens e frameworks geralmente possuem módulos, libs que abstraem o trabalho de criar logs, como [log4j](http://logging.apache.org/log4j/2.x/manual/index.html) para Java.

## Logging Estruturado

### Pessoa vs Máquina

Deve-se pensar na distinção de quem irá consumir seus logs.

Um <b>pessoa</b> é capaz de ler um conjunto de palavras que lhe sejam legíveis (levando em consideração idioma, conhecimento, contexto). Mas nem sempre o que é entendível para uma pessoa, <b>um programa</b> irá entender.

De acordo com Gregory Szorc, a informação desestruturada (puramente texto) é um problema quando queremos que uma máquina leia e interprete logs.

Digamos que vamos imprimir essa mensagem de log:

<i>Roselma successfully logged in</i>

<b>Log desestruturado</b>

<pre>
<code>
logger.info(username + " successfully logged in")
</code>
</pre>

E dessa mensagem queremos pegar as informações para guardar em uma tabela de banco, por exemplo:

<pre>
<code>
for (let line of log) {
  if (line.endsWith("successfully logged in")) {
    // Find username.
    let spaceIndex = line.indexOf(" ");
    let username = line.substr(0, spaceIndex - 1);

    // Do something interesting.
  } else if (line.indexOf(...)) {
    //
  }
}
</code>
</pre>

<b>Com log estruturado</b>

Imprimindo...
<pre>
<code>
logger.info("successful_login", who=username)
</code>
</pre>

Obtendo os dados desse log:

<pre>
<code>
for (let line of log) {
  let [time, level, action, fields] = JSON.parse(line)

  if (action == "successful_login") {
    let who = fields.who;

    // Do something interesting.
  } else if (action == "XXX") {
    // ...
  }
}
</code>
</pre>

Do primeiro para o segundo código nota-se maneiras diferentes de obter as informações. Na primeira, temos que lidar com uma pura string e se utilizar de métodos que lidem com a subtração e procura de conteúdo. Já na segunda somente lidamos com uma linha formada de campos e ler o que cada um traz.

Quando falamos de logging estruturado, precisamos que os dados de uma mensagem de log sejam guardados em estruturas bem definidas. 

Eu posso ter a mensagem de log guardada da seguinte maneira:

<pre>
<code>
[1354317157.034534, "INFO", "sucessful_login", {"who": "Roselma"}]
</code>
</pre>

O logging estruturado irá ocorrer de diferentes maneiras, dependendo da linguagem e/ou framework utilizado.

<b>Ora, mas por que logging estruturado?</b>

Bem, estamos falando aqui do uso de logs para nos dar informação rápida, gerar dados de análise para nossos sistemas. E esse melhor uso da informação, que temos com o log, tem sido alcançado usando soluções que automatizam o processo de interpretação humana.

Por fim, máquinas precisam ler nossos logs para nos dar informação otimizada sobre nossos sistemas.

Imagine que é possível que a cada mensagem de erro crítico, um sistema lhe envie uma mensagem de email avisando com detalhes o que aconteceu.

Um passo muito importante para alcançar/facilitar isso é o logging estruturado.

## O que logar?

Gregory Szorc lista o que ele acredita que sejam as situações onde logs são usados:

<ol>
  <ul>1. Registro de erros da aplicação (exceções e stack traces)</ul>
  <ul>2. Informação em baixo nível para debug ou análise humana</ul>
  <ul>3. Monitoramento da aplicação (inclui métricas e alertas)</ul>
  <ul>4. Analise de negócio (uso de dados de log para tomadas de decisão)</ul>
  <ul>5. Auditoria de segurança</ul>
</ol>

Tem muita discussão na [rede](https://www.google.com.br/webhp?sourceid=chrome-instant&rlz=1C5CHFA_enBR606BR606&ion=1&espv=2&ie=UTF-8#q=logging%20lot%20of%20code) acerca do que deve ser logado ou não. [Algumas](https://blog.codinghorror.com/the-problem-with-logging/) pessoas pregam que você só deve logar exceções, [outras](http://stackify.com/smarter-errors-logs-putting-data-work-2/) que você deve logar tudo (paramêtros das funções, funcionalidade, etc), mas com moderação.

Para mim, além das dicas do Szorc, **log tem que ter contexto**. Muito mais que ter um [stack trace](http://stackoverflow.com/a/3988794), tem muito valor você colocar mais informação no seu log, como uma simples mensagem do tipo "Verificando dados do usuário 134" que mostram o que tipo de atividade o programa estava fazendo quando a exceção aconteceu e o dado a ser manipulado. 

E logs não só necessários quando o programa lança erros, mas também quando tudo vai bem no código. Afinal, tudo está bem em um momento e no outro não. Criar uma "timeline" do que acontece no seu sistema ajudará bastante na resolução de problemas, principalmente em produção. E os problemas podem se manifestar sem exceções em logs, como uma soma errada do total de uma nota em um site de e-commerce.

No final a estrutura dos seus logs dependerão da natureza do seu sistema, tecnologias/frameworks e do que você espera que será útil saber para monitorar o seu funcionamento.


E para finalizar uma lista de ferramentas que ajudam com o manuseio de logs [no Stackshare](http://stackshare.io/search/q=logging).

## Links

[Você sabe o que é Log?](http://www.tiagomatos.com/blog/voce-sabe-o-que-e-log)

[3 Ways to Make Sense of Errors & Logging](http://stackify.com/3-ways-make-sense-errors-logging/)

[Thoughts on Logging - Part 1 - Structured Logging](http://gregoryszorc.com/blog/category/logging/)

[Announcing Project Lumberjack](http://blog.gerhards.net/2012/02/announcing-project-lumberjack.html)

[Traces - sane logging for asynchronous code](http://petercipov.com/traces-sane-logging-in-async/)
