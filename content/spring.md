Title: Construindo uma API com Spring
Date: 2021-03-03 10:20
Modified: 2021-03-03 10:20
Category: Java
Tags: spring, rest, api
Slug: tec/api-com-spring
Authors: Roselma Mendes
Summary: o básico para implementar uma API REST com Spring
Image: sem.jpg
Status: draft

## Conteinerizando

- Usei a imagem gradle:jdk8, mas posso usar as imagens do próprio jdk

- o Dockerfile não tem muito código. pode-se pensar em só utilizar direto `docker run` usando a imagem do gradle ou jdk. Por exemplo: `docker run -p 8080:8080 -v ${PWD}:/home/gradle/project -w /home/gradle/project -it gradle:jdk8 ./gradlew bootRun`

- Ainda não descobri como evitar que o gradle baixe tudo de novo toda vez que é executado. Por enquando, paleativo é rodar dentro do container.

## Testando

Quais anotações usar: WebMvcTest, AutoWired, Test

Objeto MockMvc. Vem com metodos `perform`, `andExpect`
<exemplo>

- Achei muito complicado achar como mostrar no terminal a causa de um teste falhando.

- Configuração para mostrar causa de teste falhando. build.gradle > Test > TestLogging.

## Referências

[Testing the Web Layer](https://spring.io/guides/gs/testing-web/)
[How to collect and print out tests summary in Gradle](https://medium.com/@wasyl/pretty-tests-summary-in-gradle-744804dd676c)