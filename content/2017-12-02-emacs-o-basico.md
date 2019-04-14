Title:  "Você já pensou em usar o editor de texto Emacs?"
modified:   2017-12-02
categories: tec
tags: [editor]
image: 
  feature: emacs.png
excerpt: "Conhecendo o editor GNU Emacs"
Status: draft

## Emacs

[GNU Emacs](https://www.gnu.org/software/emacs/) é um editor de texto da família Emacs. É código aberto, portável e customizável. Muito usado pela comunidade de pessoas que desenvolvem software.

O Emacs (estou suprimindo o GNU) funciona na maior parte dos sistemas operacionais conhecidos, como Mac OS, Windows e Linux. E você pode customizar seu Emacs tanto usando [major modes](https://www.gnu.org/software/emacs/manual/html_node/emacs/Major-Modes.html#Major-Modes) como criando customizações com a linguagem Lisp, na qual GNU Emacs é feito.

O seu uso é geralmente por teclado (atalhos). O uso do mouse é desencorajado. Acredito que por isso, e pela proposta de uma interface que diminui o número de interrupções ao longo da escrita, é que o GNU Emacs é amplamente usado pela comunidade de tecnologia. Assim como seu concorrente o [Vim](http://www.vim.org/).

Dá pra fazer de um tudo um pouco no Emacs: [abrir sites](https://www.emacswiki.org/emacs/CategoryWebBrowser), [usar o Spotify](https://github.com/krisajenkins/helm-spotify), [executar linha de comando](http://www.nongnu.org/emacsdoc-fr/manuel/shell.html), [escrever livros](https://www.masteringemacs.org/article/how-to-write-a-book-in-emacs), artigos, e claro escrever código, etc. Esse post eu fiz todo usando Emacs.

<figure>
	<a href="#"><img src="/images/este-post-emacs.png" alt="image"></a>
	<figcaption><a href="https://www.emacswiki.org/emacs/eww" title="">meu Emacs aberto com o eww e o arquivo markdown deste post.</a>.</figcaption>
</figure>

## Major modes

Um major mode é o modo de edição ativo no momento. Para saber qual está ativo no momento veja na parte de baixo da tela entre parenteses.

Eles dizem respeito algumas configurações específicas para o tipo de conteúdo editado no momento, por exemplo, quando eu abro um arquivo markdown, o Emacs identifica isso e carrega o major mode Markdown. Veja a figura abaixo.

<figure>
	<a href="#"><img src="/images/major-mode.png" alt="image"></a>
</figure>


Há vários major modes para customizar seu Emacs. Alguns que estou usando:

[Go](https://github.com/dominikh/go-mode.el)

[Markdown](https://jblevins.org/projects/markdown-mode/)

[SCSS](https://www.emacswiki.org/emacs/ScssMode)

[Aqui](https://www.emacswiki.org/emacs/List_Of_Major_And_Minor_Modes) uma lista dos major modes disponíveis.

## Instalando

Nesta [página](https://www.gnu.org/software/emacs/download.html) você pode encontrar as instruções especificas a seu sistema operacional.

## Comandos básicos

A ajuda do Emacs é C-h ?. Onde C significa a tecla Control: segure o Control, pressione h e depois interrogação.

Quando descrevendo os comandos, que se chamam key sequence, a documentação usa das terminologias C e M, onde o primeiro é para a tecla Control e a segunda para a tecla ESC/Alt.

Neste [gist](https://gist.github.com/roselmamendes/41c8d476b6e11712110d7549ede3e71e) coloquei os comandos que me são mais úteis no uso do Emacs.

## Referências

[Tutorial do Emacs](http://www2.lib.uchicago.edu/keith/tcl-course/emacs-tutorial.html)
