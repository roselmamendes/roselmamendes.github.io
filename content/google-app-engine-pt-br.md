Title:  Implantando aplicações com Google App Engine
Date: 2019-02-06
Category: DevOps
Tags: GCP, GAE, Monitoring, KMS
Summary: Aprenda como implantar uma aplicação Flask no Google App Engine.
Image: /google-app-engine/print-conteudo-tech-negro.png
Status: draft
Slug: tec/google-app-engine
Lang: pt-br

[English](/tec/google-app-engine-en.html)

## Google App Engine - GAE

O App Engine é parte do ecossistema do Google Cloud Platform (GCP) para hospedar aplicações web. Como na própria [página](https://cloud.google.com/appengine/) diz *"Foco apenas em escrever código, sem a preocupação de gerenciar a infraestrutura por baixo."*. Além de implantar sua aplicação, o serviço também prover algumas ferramentas para monitoramento.

Os produtos do Google Cloud podem ser encontradas [aqui](https://cloud.google.com/products/).

## Implantando uma aplicação

Eu vou usar o meu repositorio [conteudo-tech-negro](https://github.com/NegraTec/conteudo-tech-negro). Ele é um projeto Python usando [Flask](http://flask.pocoo.org/).

**Crie um app.yaml no repositório**

Primeiramente, o projeto precisa ter um  [app.yaml](https://cloud.google.com/appengine/docs/standard/go/config/appref). Este arquivo contém a descrição de como a implantação é configurada.

Para conteudo-tech-negro teremos o seguinte:

	:::yaml
	runtime: python37
	entrypoint: gunicorn app:app && flask db migrate && flask db upgrade

**No Google Console crie um projeto**

Quando você loga em cloud.google.com, você pode acessar o [Console](https://cloud.google.com/cloud-console/). Nele é possível gerenciar os produtos para Cloud do Google usando o navegador. Para acessar o Console, geralmente isto está localizado na parte direita da tela, ao lado da sua foto.

Entre todas as funcionalidades que o Console traz, você pode usar o [CLI gcloud](https://cloud.google.com/sdk/gcloud/). Contudo, se você prefere usar localmente, é possível instalar o CLI em sua máquina local.

Neste post, eu uso o Google Console no navegador.

Para criar um novo projeto, ao lado do título "Google Cloud Platform" existe uma seta que abre uma janela com a lista dos projetos e o botão "Novo projeto".

![Google Console - list of projects](../theme/images/google-app-engine/google-console-new-project.png)

**Crie um app no Google App Engine**

Com o projeto selecionado, no Cloud Shell use o comando `glcoud app create` ou na seção App Engine clique em "Crie um app". Você precisa escolher uma região, a linguagem e o [the environment (ambiente)](https://cloud.google.com/appengine/docs/the-appengine-environments). Estou usando o ambiente standard (padrão).

![Cloud Shell button, it is on the right up of the screen](../theme/images/google-app-engine/google-cloud-shell-button.png)

![Google Cloud Shell](../theme/images/google-app-engine/google-shell.png)

**Clone o projeto para o ambiente do Cloud Shell**

Como estou usando o Google Console no navegador, eu preciso clonar o repositório no Cloud Shell.

Abra o Cloud Shell e rode o git clone do projeto. Na pasta do projeto, rode `gcloud app deploy`. Agora o app está disponível em nome-do-projeto.appspot.com

Mas meu app tem erros...

![App Errors on App Engine Painel](../theme/images/google-app-engine/app-engine-found-errors.png)

## Ferramentas de Monitoramento

Não só infraestrutura na Cloud, o Google Cloud oferece ferramentas de monitoração para entender a saúde das aplicações.

No ambiente google, quem cuida de Monitoramento é o [Stackdriver](https://cloud.google.com/stackdriver/). Esta ferramenta funciona com Google Cloud e AWS. 

**Logs**

Para vê os logs do app, no Google Console, no menu ao lado esquerdo da tela, vá para Stackdriver, e escolha Logs.

Como a página é dividida em duas seções (superior e inferior), na seção de baixo clique em Logs. Isto mostrará todos os últimos logs.

![Logs on Stackdriver painel](../theme/images/google-app-engine/stackdriver-logs.png)

**Error Reporting**

Outra ferramenta do StackDriver é o Error Reporting. Isto mostra os erros identificados nos logs.

Se eu clico em um desses erros, isto mostra uma página com mais detalhes.

![Detailed error log on Error Reporting painel](../theme/images/google-app-engine/stackdriver-error-reporting-detail.png)

É possível associar um erro a uma "issue" no seu repositório.

**Alertas**

![Policy creation page](../theme/images/google-app-engine/stackdriver-policy.png)

Para criar alertas no GCP é necessário criar um "workspace" para o projeto. Então, você criará políticas para definir condições, notificações e qualquer tipo de documento que você queira enviar com o alerta.

Para criar um "workspace", no Google Console, no menu esquerdo, vá para StackDriver e então Monitoring. Isto fará com que se crie um "workspace" para o projeto. Mais informações sobre criar políticas no StackDriver Monitoring[aqui](https://cloud.google.com/monitoring/alerts/ui-conditions-ga).

Outras ferramentas de alertas interessantes são o [UpTime Checks (Verificação de Tempo de Atividade - tradução do própria documentação em português)](https://cloud.google.com/monitoring/uptime-checks/).

## Dados sensíveis no código

Foi difícil entender como lidar com dados sensíveis (senhas, tokens, etc) no GCP. 

Basicamente minha aplicação precisa ler a URI do banco de dados que por sua vez tem a senha em sua composição. A boa prática é ler isto de uma variável de ambiente que evita ter esta senha exposta no código. Contudo como configurar variáveis de ambiente enquanto implantando e ao mesmo tempo manter esses dados sensíveis seguros no GCP?

In the app.yaml, you can use the keyword `env_variables` to set environment variables for your app. However, as I mentioned before, having secrets in this file, commited in a Github repository, is definitely not a good thing to do.

After reading many times the Google documentation and stackoverflow, I got this approach:

1. Have an encrypted file called env.yaml in the repository. It is encrypted using the [KMS (Key Management Service)](https://cloud.google.com/kms/), other Google Cloud product;

2. [Include the env.yaml file in the app.yaml to "import" the needed environment variables](https://github.com/NegraTec/conteudo-tech-negro/blob/master/app.yaml);

When deploying it to app engine:
 
* a. I need to decrypt the env.yaml;
 
* b. call the command `gcloud app deploy` which will use the env.yaml to load the environment variables.

Other approaches I found on the Internet:

- [Datastore: it is necessary to make changes on the code to use the Google library.](https://stackoverflow.com/questions/22669528/securely-storing-environment-variables-in-gae-with-app-yaml)

- [Metadata](https://medium.com/google-cloud/google-compute-engine-metadata-service-de9d71ea44e0)

## Downsides

It was an adventure make the database works. I have to change the original code that worked already on Heroku: 

* I needed to understand how to connect to the socket connections with psycopg2 library. At the time I was writing this post there was outdated information in the App Engine standard environment documentation;

* I struggled to get an approach to run the migrations on the database with [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/). At the end I added the migration command on the initialization of the server, programatically. Before I could use `flask db upgrade` deploying in Heroku but App Engine doesn't allow run more than one command on the entrypoint for the deploy. Also, I couldn't find an ["easy"](https://stackoverflow.com/questions/36698070/how-to-use-flask-migrate-with-google-app-engine) way to run commands on the application machine;

* I shut down the app since I was charged. It was not simple to understand what is going to be billed or not. I decided to remove all the resources configured there...

## And that is all...

To check the code: https://github.com/NegraTec/conteudo-tech-negro

Also I have another example of application on GAE: https://github.com/roselmamendes/vamos-fazer-compras

## References

[Best practices for securing your Google Cloud databases](https://cloud.google.com/blog/products/gcp/best-practices-for-securing-your-google-cloud-databases)

[Google App Engine and Python: a correct way to store configuration variables](https://www.andreafortuna.org/programming/google-app-engine-and-python-a-correct-way-to-store-configuration-variables/)

[Secrets Management](https://cloud.google.com/kms/docs/secret-management)

[Google Cloud SDK with Docker](https://hub.docker.com/r/google/cloud-sdk)

[Using psycopg2 directly on Google App Engine](https://stackoverflow.com/questions/51061722/using-psycopg2-directly-on-google-appengine)




