---
layout: post
title:  "Deploying an application with Google App Engine"
modified:   2019-02-06
categories: tec
tags: [] 
excerpt: ""
published: false
---

## Google App Engine - GAE

The App Engine is  part of the Google Cloud Platform (GCP) ecosystem to host Web applications. As it says in its [page](https://cloud.google.com/appengine/) *"Focus just on writing code, without the worry of managing the underlying infrastructure."*. Besides to deploy your app, it provides a lot of monitoring tools over it.

Other Google Cloud products can be checked [here](https://cloud.google.com/products/).

## Deploying an application

I am going to use my repository [conteudo-negro-tech](https://github.com/NegraTec/conteudo-tech-negro). It is a Python project using [Flask](http://flask.pocoo.org/).

**Create an app.yaml in the repository**

First of all, the project needs to have an [app.yaml](https://cloud.google.com/appengine/docs/standard/go/config/appref). This file is responsible to describe how the deploy will be configured and started.

For conteudo-negro-tech I have the follow:

```yaml
runtime: python37
entrypoint: gunicorn app:app && flask db migrate && flask db upgrade
```

**On Google Console create a project**

When logged on cloud.google.com, you can access the [Console](https://cloud.google.com/cloud-console/) where you can manage, create the Cloud products of Google using an UI. To go to the Console, usually it is placed at the right up, beside your photo.

Along all the functionalities the Console brings, you can use the [CLI gcloud](https://cloud.google.com/sdk/gcloud/). But if you prefer use it locally, it is possible install the CLI in your machine as well.

In this post, I use the Google Console UI.

To create a new project, go to the name of the project beside the title "Google Cloud Platform" and click in the arrow. It will show a window with the list of projects and a button "New project".

<figure>
	<img src="/images/google-app-engine/google-console-new-project.png" alt="image">
	<figcaption>Google Console - list of projects</figcaption>
</figure>

**Create an app on the Google App Engine**

With the project selected, on the Cloud Shell use the command `glcoud app create` or on App Engine page click on "Create an app". You need to choose a region, the language and [the environment](https://cloud.google.com/appengine/docs/the-appengine-environments). I am using the standard environment.

<figure>
	<img src="/images/google-app-engine/google-cloud-shell-button.png" alt="image">
	<figcaption>Cloud Shell button, it is on the right up of the screen</figcaption>
</figure>

<figure>
	<img src="/images/google-app-engine/google-shell.png" alt="image">
	<figcaption>Google Cloud Shell</figcaption>
</figure>

**Clone the project to the environment of Cloud shell**

As I am using the Google Console UI, I need to clone the repository to this.

Open the Cloud shell and run the git clone of the project. On the project folder, run `gcloud app deploy`. Now the app is available on project-name.appspot.com

But my app got errors...

<figure>
	<img src="/images/google-app-engine/app-engine-chart-summary.png" alt="image">
	<figcaption>Summary Chart on App Engine Painel</figcaption>
</figure>

<figure>
	<img src="/images/google-app-engine/app-engine-found-errors.png" alt="image">
	<figcaption>App Errors on App Engine Painel</figcaption>
</figure>

## Monitoring tools

Not only host your application in the infrastructure, Google Cloud allows to use monitoring tools to follow the health of those services deployed.

In the Google world, who takes care of Monitoring is the [Stackdriver](https://cloud.google.com/stackdriver/). To use with Google Cloud and AWS, Stackdriver is a platform to manage  techniques in monitoring for your applications and/or infrastructure.

**Logs**

To see the logs of the app, on the Google Console UI, on the menu at left side, go to StackDriver, then Logs.

As the page is splitted in two sections (up and down). At the down section click on Logs. It will show all the last logs.

<figure>
	<img src="/images/google-app-engine/stackdriver-logs.png" alt="image">
	<figcaption>Logs on Stackdriver painel</figcaption>
</figure>


**Error Reporting**

Other Stackdriver tool is the Error reporting. It shows the identified errors in the logs.

If I clicked in one of those, it opens a page with more details about the error log.

<figure>
	<img src="/images/google-app-engine/stackdriver-error-reporting-detail.png" alt="image">
	<figcaption>Detailed error log on Error Reporting painel</figcaption>
</figure>

It is possible to link an error log with an issue in your repository.

**Alerts**

<figure>
	<img src="/images/google-app-engine/stackdriver-policy.png" alt="image">
	<figcaption>Policy creation page</figcaption>
</figure>

To create alerts on GCP it is necessary to create a workspace for the project. There you need to create policies where you can define conditions, notifications and any type of documentation you want to send with the alert.

To create a workspace, on Google Console UI at the left menu, go to Stackdriver, then Monitoring. It will trigger the creation of a workspace for the project. More info about creating policies on Stackdriver Monitoring [here](https://cloud.google.com/monitoring/alerts/ui-conditions-ga).

Other interesting tools on Alerts are the [UpTime Checks](https://cloud.google.com/monitoring/uptime-checks/).

## Secrets in the code

It was difficult to understand how to deal with sensible information on GCP. Basically my application needs to read the database uri which has sensible information including the password. The good practice is to read it from an environment variable to avoid secrets on the code. But the thing is how to load environment variable while deploying and keep the secrets safe on GCP?

In the app.yaml, you can use the keyword `env_variables` to set environment variables for your app. However, as I mentioned before, having secrets in this file, commited in a Github repository, is definitely not a good thing to do.

After reading many times the Google documentation and stackoverflow, I got this approach:

1. Have a encrypted file called env.yaml in the repository. It is encrypted using the [KMS (Key Management Service)](https://cloud.google.com/kms/), other Google Cloud product;

2. [Include the env.yaml file in the app.yaml to "import" the needed environment variables](https://github.com/NegraTec/conteudo-tech-negro/blob/master/app.yaml);

3. When deploying it to app engine:
 
 > a. I need to decrypt the env.yaml;
 
 > b. call the command `gcloud app deploy` which will use the env.yaml to load the environment variables.
 
 This approach would be used locally in your machine or from a CI/CD tool.

Other approaches I found on the Internet:

- [Datastore: need changes on the code to use the Google library.](https://stackoverflow.com/questions/22669528/securely-storing-environment-variables-in-gae-with-app-yaml)

- [Metadata](https://medium.com/google-cloud/google-compute-engine-metadata-service-de9d71ea44e0)

## Downsides

It was an adventurous make the database works. I have to change the original code that worked very well on Heroku: 

- I needed to understand how to connect to the socket connections with psycopg2 library. Outdated information in the App Engine standard environment documentation;

- I struggled to get an approach to run the migrations on the database. At the end I added the migration command on the initialization of the server, programatically. Before I could use `flask db upgrade` while deploying in Heroku but App Engine doesn't allow run more than one command on the entrypoint for the deploy. Also, I couldn't find a ["easy"](https://stackoverflow.com/questions/36698070/how-to-use-flask-migrate-with-google-app-engine) way to run commands on the application machine;

It is possible to access the app on https://conteudo-negro-tech.appspot.com/.

## References

[Best practices for securing your Google Cloud databases](https://cloud.google.com/blog/products/gcp/best-practices-for-securing-your-google-cloud-databases)

[Google App Engine and Python: a correct way to store configuration variables](https://www.andreafortuna.org/programming/google-app-engine-and-python-a-correct-way-to-store-configuration-variables/)

[Secrets Management](https://cloud.google.com/kms/docs/secret-management)

[Google Cloud SDK with Docker](https://hub.docker.com/r/google/cloud-sdk)

[Using psycopg2 directly on Google AppEngine](https://stackoverflow.com/questions/51061722/using-psycopg2-directly-on-google-appengine)




