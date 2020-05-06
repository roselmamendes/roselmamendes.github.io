Title:  Entrega Contínua, o que aprendi - parte 2
date: 2017-10-07
categories: programacao
tags: automacao, segurança, CI/CD, Tecnologia, Implantação
cover: images/entrega-continua/riri-williams.jpg
summary: Já ouviu sobre Entrega Contínua? Seu time implementa essa prática?

Continuando do post [capítulo 1](/entrega-continua-o-que-aprendi-parte-1.html). Vou continuar falando de práticas que aprendi sobre Entrega Contínua.

Estou construindo um blog e usando essa construção como exemplo para o assunto.

Esta é a segunda parte. Se você não leu a primeira parte, aqui: [capítulo 1](/entrega-continua-o-que-aprendi-parte-1.html).

(Antes de voltarmos a esse papo de Entrega Contínua. Um ponto. Houve alguns termos que são minhas traduções livres. Se você conhece traduções melhores comenta logo abaixo. Obrigada!)

#### Integração Contínua

![https://circleci.com/gh/roselmamendes/continuous-delivery-blog/14]({static}/images/entrega-continua/unit-tests-on-circle.png)

Com testes bem escritos e com boa cobertura, nós garantimos que os requisitos do sistema estão satisfeitos.

Testes nos dão a segurança que novos códigos no fonte não mudarão funcionalidades já existentes ou garantir que novas funcionalidades façam o que se espera delas. Os testes precisam traduzir como o sistema deve funcionar.

"Falhe rápido, falhe frequentemente" (tradução livre-“Fail fast, fail often”)

Como desenvolvedoras precisamos fazer commits/pushes (Git) frequentes e pequenos, executar sempre os testes localmente antes de puxar código, executar verificações de segurança (próxima seção).

Um commit é uma peça de código onde todos os testes (novos e velhos) passam e <b>o código está pronto para ser usado em produção</b>.

Tenha uma suite de testes consistente. Como desenvolvedora pense nos possíveis cenários, de sucesso e erro, que você consegue elaborar.

Como time, tenham estórias consistentes, pequenas, com valor e com critérios de aceitação (acceptance criteria). Aqui um texto sobre usar [I.N.V.E.S.T](http://ihd.net.br/blog/invest-estorias-dos-usuarios-metodos-ageis-gestao-projetos), uma técnica para escrever estórias.

Use uma ferramenta de Entrega e Implantação Contínua (CI/CD em inglês-Continuous Integration e Continuous Deployment). Existem muitas opções no mercado: [Circle CI](https://circleci.com/), [Go CD](https://www.gocd.org/), [Travis CI](https://travis-ci.org/), [Concourse CI](https://concourse-ci.org/), etc. Elas ajudam a ter um lugar centralizado onde seu time pode seguir a situação do código: testes, análises de qualidade, implantação entre os ambientes, e por aí vai.

![Circle CI builds]({static}/images/entrega-continua/circle-ci-builds.png)

Com a prática da [Integração Contínua](http://blog.caelum.com.br/integracao-continua/), você garante a junção dos códigos vindos dos pares ou pessoas no seu time e que o código integrado está ideal para uso. Vá além dos testes unitários. Há outros tipos de testes, mais alto nível, que podem ajudar a fazer a entrega mais confiável. Alguns exemplos de tipos de testes: End to end (preferir não traduzir), Funcionais, Integração.

Ainda sobre testes, pesquise sobre [Pirâmide de Testes e o anti padrão Ice Cream Cone](https://www.thoughtworks.com/insights/blog/introducing-software-testing-cupcake-anti-pattern).

#### Testes de segurança

Como garantir que o que entregamos é seguro?

Três coisas que vem a minha mente: evite o [security sandwich](https://www.thoughtworks.com/radar/techniques/security-sandwich) (infelizmente não encontrei fontes em pt-br), use a ferramenta de Entrega e Implantação Contínua para rodar os testes de segurança e [faça o ambiente para executar seus builds seguro](http://blog.rivendel.com.br/2016/10/13/5-praticas-devops-para-aprimorar-a-seguranca-na-engenharia-de-software/).

No projeto do Blog ([capítulo 1](/tec/entrega-continua-1)), eu adicionei uma verificação nas dependências, procurando por dependências vulneráveis ([nsp](https://www.npmjs.com/package/nsp)) e também um teste de segurança estático ([eslint](https://eslint.org/)-não só para verificações lint, scanjs, no-unsafe-innerhtml).

Já que consigo usar estas verificações por linha de comando, eu posso adicioná-las junto com outras verificações em uma ferramenta de Entrega e/ou Implantação contínua. Com isso posso monitorar se um novo código não está seguro. E isso não só para mim, mas também para as pessoas que estão contribuindo/usando meu projeto.

![console no circleci built para o repositório continuous-delivery-blog]({static}/images/entrega-continua/circle-erro-dependency-check.png) 

Pense em análise de dependências, análise de segurança [estática](https://before-you-ship.18f.gov/security/static-analysis/) (infelizmente fontes em inglês) e [dinâmica](https://before-you-ship.18f.gov/security/dynamic-scanning/) para seu projeto. Alguns destas análises podem ser integradas na ferramenta de Integração/Implantação Contínua.

Uma boa fonte sobre o assunto de segurança é o site do [OWASP](https://www.owasp.org/index.php/Main_Page) (inglês) onde você encontra o [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project#tab=OWASP_Top_10_for_2017_Release_Candidate_1) além de vários textos sobre o tema. O Top 10 consiste de uma lista das vulnerabilidades mais encontradas em sistemas pelo mundo.

Outras fontes em inglês: https://devops.com/automated-security-testing-continuous-delivery-pipeline/.

(complicado achar conteúdo em português sobre o assunto)

#### A tal da implantação

![console no circleci built para o repositório continuous-delivery-blog]({static}/images/entrega-continua/entrega-continua-1.png)

Lembra do processo de implantação (ou deployment pipeline)?

Nas seções/[posts](/tec/entrega-continua-1) anteriores lemos sobre CI, tests e análises de segurança. Isto cobre desde estágio de commit (Commit Stage) até os testes manuais (Manual Testing).

Agora vamos ler sobre a Entrega (Release).

<b>Ambientes (Environments)</b>

Também é parte de uma entrega contínua usar ferramentas como o Docker para ajudar a manter a consistência entre os vários ambientes que você implantará sua aplicação.

Por exemplo, ter o ambiente das desenvolvedoras idêntico ao ambiente onde são executados testes de aceitação automatizados. Isso diminui o trabalho na investigação de erros otimizando o tempo do seu time para focar no que importa: a funcionalidade. Esta não é uma boa prática somente para ambientes de testes, mas também para o de produção.

[Heroku](https://devcenter.heroku.com/articles/container-registry-and-runtime), Google Cloud Platform ([opção 1](https://cloud.google.com/compute/docs/containers/deploying-containers) e [opção 2](https://cloud.google.com/kubernetes-engine/)) e [AWS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html) provêem implantação usando Docker. (Fontes em inglês)

(Pretendo escrever um texto sobre Heroku com Docker. Logo mais. ;) )

[Aqui](https://braziljs.org/blog/uma-breve-introducao-ao-docker-com-nodejs/) um texto explicando o uso do Docker com uma aplicação NodeJS. E se for mesmo usar a ferramenta, procure por melhores práticas usando-a.

Muitas ferramentas por aí estão suportando Docker. Mesmo que você não a use, tenha em mente manter a consistência entre seus ambientes de implantação. <b>Eles devem ser espelhos de um e outro</b>. Talvez você se interesse por [infraestrutura como código](https://churrops.io/2017/09/30/ansible-por-que-ansible-e-nao-outras-ferramentas-de-gerencia-de-configuracao/) (infrastructure as code).

#### Implantando o blog

Eu escolhi Heroku por ser a ferramenta que tenho mais contexto.

Heroku tem uma funcionalidade chamada Pipeline. Diferente de uma ferramenta como Circle, uma pipeline no Heroku é exclusivo para monitorar/disparar as implantações para uma aplicação, e não rodar verificações tipo testes.

![Uma pipeline para o repositório continuous-delivery-blog]({static}/images/entrega-continua/entrega-continua-2.png)

É possível começar uma [implantação (deploy) no Heroku usando commandos Git](https://devcenter.heroku.com/articles/git) (inglês). Mas <b>falando em Entrega Contínua, nós precisamos pensar em automação</b>.

O Circle 2.0 usa o arquivo .circleci/config.yml. Então…

Abaixo .circleci/config.yml no repositório continuous-delivery-blog para usar o Circle.
<script src="https://gist.github.com/roselmamendes/286d8686c69b4426752bff2756acd461.js"></script>

<b>Eu não vou fazer [Implantação Contínua](https://www.infoq.com/br/news/2011/05/implantacao-continua) (Continuous Deployment), isso significa que minha implantação em produção será manual</b>. Eu tenho um botão "On Hold" no Circle para começar a implantação no ambiente de produção.

![Funcionalidade Workflow do Circle: https://circleci.com/workflow-run/eb07571a-eab7-48cf-a705-ae4bc56fe6a7]({static}/images/entrega-continua/circleci-workflow.png)

É isso. Eu naveguei pelos conceitos que sou exposta no meu dia-a-dia:

* Integração Contínua: faça pushes ao master, commits pequenos, não puxe sem rodar os testes localmente, seu time deve usar uma ferramenta para Integração e Entrega Contínua;
* Segurança: além de testes funcionais, de unidade, etc, é necessário integrar a Segurança no desenvolvimento de software. Isso significa termos verificações de segurança do sistema que estamos entregando em nossas builds/pipelines;
Onboarding: quando alguém entra no seu time, para essa pessoa já começar a contribuir, deve existir uma boa documentação e automação de como testar e executar o sistema.
* Ambientes: é estritamente importante ter todos os ambientes com as mesmas configurações, desde do ambiente de quem desenvolve até produção. Isso evita o “funciona na minha máquina”.
* Deploy (Implantação): a implantação do seu sistema tem que ser simples como o apertar de um botão, e você deve confiar que tudo vai ficar bem quando você aperta o botão.

#### Outros assuntos para ficar "ligada"

[Trunk Based Development](https://www.slideshare.net/anapauladaros/adeus-trunk-based-development-trabalhando-com-shortlived-branches-pull-requests-e-code-review-75736869)

[Database](https://www.linkedin.com/pulse/continuous-delivery-database-krzysztof-ziomek?articleId=8641378527989497278) (em Inglês)

[Logging](https://medium.com/@roselmamendes/logs-85e35fe386c7) e Monitoramento

Repositório do blog: https://github.com/roselmamendes/continuous-delivery-blog

<hr>

Você usa alguma das coisas que mencionei aqui?

Gostaria de pedi ajuda sobre fontes em português sobre os assuntos aqui abordados. Você conhece algum? Comenta no twitter e me marca @roselmamendes :) (rosto sorrindo)
