Title: Aventura da vez criando uma API com Spring
Date: 2021-03-03 10:20
Modified: 2021-03-03 10:20
Category: Java
Tags: spring, rest, api
Slug: tec/api-com-spring
Authors: Roselma Mendes
Summary: O básico para implementar uma API REST com Spring
Image: sem.jpg
Status: draft

## Spring

[Spring](https://spring.io/why-spring) é um framework para aplicações na linguagem Java. Utilizando de Inversão de Controle e Injeção de Dependência, Spring promete facilitar o ciclo de desenvolvimento dos times tanto no aspecto de implantar bem como implementar um código Java.

----------------------

Aqui vão alguns aprendizados que achei útil registrar tanto para o meu do futuro, quanto para outras pessoas que estão aprendendo Spring.

Para criar um projeto Spring, podemos utilizar o https://start.spring.io/. Com esse inicializador, já podemos definir as dependências, escolher entre Maven e Gradle e outras configurações para o projeto.

Com o inicializador nós criamos um projeto com o [*Spring Boot*](https://spring.io/projects/spring-boot), que é um ator frequente em projetos Spring. Ele define algumas pre-configurações para que uma aplicação Java esteja pronta para ser executada, mas também nos possibilita customizar estas e outras configurações para execução da app.

-------------------------------

Tudo em Spring tem anotações (annotations)...

Quem está acostumado com Java, sabe que toda app precisa de um método main. É onde tudo começa. No Spring, o método main vem acompanhado da primeira anotação na nossa aventura: @SpringBootApplication`.

<exemplo>

Não vou aprofundar na SpringBootApplication. O mais importante agora é sabermos que ela define o ponto de partida da aplicação, e também é importante que pacotes e classes criados estejam dentro do mesmo pacote que ela.

<Diagrama>
Boot > Scan
</Diagrama>

Para saber mais sobre Spring Boot: https://tanzu.vmware.com/content/springone-platform-2017/its-a-kind-of-magic-under-the-covers-of-spring-boot-brian-clozel-st%C3%A9phane-nicoll

## Testando

<exemplo>

Com a anotação `@WebMvcTest` informamos que vamos testar a camada Web da aplicação. No meu caso, `CalendarResource`, onde tenho definido  o meu endpoint `\calendar`.

`@AutoWired` para a variável mockMvc informa que precisamos de um objeto da classe MockMvc. Estamos usando injeção de dependência. Assim, poderemos chamar `this.mockMvc` ao longo dessa classe teste.

Todo método que define um teste precisa da `@Test`.

Objeto MockMvc. Vem com metodos `perform`, `andExpect`


- Achei muito complicado achar como mostrar no terminal a causa de um teste falhando.

- Configuração para mostrar causa de teste falhando. build.gradle > Test > TestLogging.

## Conteinerizando

Utilizei a imagem [gradle:jdk8](https://hub.docker.com/_/gradle). Você também pode utilizar a imagem padrão do [JDK](https://hub.docker.com/_/openjdk/).

O comando que utilizei para executar a aplicação foi esse `docker run -p 8080:8080 -v ${PWD}:/home/gradle/project -w /home/gradle/project -it gradle:jdk8 ./gradlew bootRun`

Ainda não descobri como evitar que o gradle baixe tudo de novo toda vez que é executado. Por enquanto, o paleativo tem sido rodar os comandos de dentro do container (abrir o terminal do container).

E por fim, no site do Spring existe um tutorial de como usar o Spring com Docker: https://spring.io/guides/gs/spring-boot-docker/. Apesar de que nesse tutorial você não "builda" a aplicação, esse tutorial já assume que o build será feito sem o Docker. E no meu caso, eu uso o Docker para "buildar" e executar a aplicação localmente.

## Referências

[Spring Component Scan](https://springframework.guru/spring-component-scan/)
[Building REST services with Spring](https://spring.io/guides/tutorials/rest/)
[Testing the Web Layer](https://spring.io/guides/gs/testing-web/)
[How to collect and print out tests summary in Gradle](https://medium.com/@wasyl/pretty-tests-summary-in-gradle-744804dd676c)