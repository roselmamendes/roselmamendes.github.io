---
layout: post
title:  "Monitoring applications"
modified:   2018-11-02
categories: tec
tags: [monitoring, logging, alerts, delivery, deploy] 
excerpt: ""
published: false
---
On the project I am working on, we were facing instability in our automated flows. Basically, we have flows to provide access to some cloud services helping people to get most common assets to deploy their application. These flows are automated using Celery and Rabbitmq, so they are composed by tasks that run in a determined order.

At the time we didn't have any clue what was causing the instability. So we start to log, and then create alerts for some specific logs. From that point we noticed alerts about certain data inconsistencies that were causing errors during the flow. All those alerts helped us to identify patterns around the instability and established how to fix it.

Log and alerts are practices in Monitoring.

## Observability or Monitoring?

Some concepts I found on the internet:

"Monitoring tells you whether a system is working, observability lets you ask why it isn't working." [Source on 2017](https://www.vividcortex.com/blog/monitoring-isnt-observability)

"Monitoring is most often used for alerting, troubleshooting, capacity planning, and other traditional IT Ops functions, usually not too deeply.

Observability elements, on the other hand, are often much detailed, more diverse, and used more for debugging, complex troubleshooting, performance analyses, and generally going ‘deeper’." [Source on 2017](https://medium.com/@steve.mushero/observability-vs-monitoring-is-it-about-active-vs-passive-or-dev-vs-ops-14b24ddf182f)

Also, both posts above mention about the [Cindy' post](https://medium.com/@copyconstruct/monitoring-and-observability-8417d1952e1c) where she elaborates the differences between Observability and Monitoring.

What each one stand for is still confusing for me. Maybe it is something that come with experience. However, reading them gave me the feeling that what I experienced with my team, identifying the instability on our flows, was Observability. Why? Because of the debug process involved to find out what was happening. We were not looking if the system was up or down, but why it was not working as expected. Monitoring is about availability (is it up?) and healthy (monitor known failures), and observability about debugging (unknown scenarios) for an application.

Based on the Cindy' post, seems the evolution of the monitoring tools brought to us the Observability practices. More detailed information can be extracted from these tools and more assertive decision taken. 

As it is still not clear on my mind, I will keep using the word monitoring.

## Availability

I agree with Susan Fowler that at the end, for any practices we apply to manage the deliver of our application, the goal of them will be the application availability.

That word is very stressed by Susan in her book <Microservices in production>. In that context what availability means for an application is 

* saber do estado -> prevenção -> maiores danos

* sem monitoramento, a disponibilidade já esta prejudicada
<elaborate about how important is to deign systems considering how "monitorable" it is. See Monitoring is for symptom based Alerting on Cindy' post>

KPI - Key Performance Metric

https://medium.com/@copyconstruct/health-checks-in-distributed-systems-aa8a0e8c1672

https://medium.com/@copyconstruct/monitoring-in-the-time-of-cloud-native-c87c7a5bfa3e

Monitoring doesn't avoid failure, it helps us to be aware and take action in a it as fast as possible. We should not perceive a system completely without failure, but try to define as accurate as possible the known scenarios and have a process to respond fast and reliable to a failure.

## Levels of Aplication monitoring

1. Logs in the application
https://medium.com/@copyconstruct/logs-and-metrics-6d34d3026e38

2. Alerts

3. Dashboard

## What to monitor?

elaborate on key metrics and how useful they are to the availability

Key metrics need to be actionable, that means useful for the availability and healthy of the application.

## Links

[Observability to Better Serverless Apps por Erica Windisch](https://www.infoq.com/presentations/serverless-observability-2018)

[Monitoring and Observability](https://medium.com/@copyconstruct/monitoring-and-observability-8417d1952e1c)

[Monitoring Isn't Observability](https://www.vividcortex.com/blog/monitoring-isnt-observability)

[Observability vs. Monitoring, is it about Active vs. Passive or Dev vs. Ops ?](https://medium.com/@steve.mushero/observability-vs-monitoring-is-it-about-active-vs-passive-or-dev-vs-ops-14b24ddf182f)

[Observability by Wikipedia - Math perspective](https://en.wikipedia.org/wiki/Observability)