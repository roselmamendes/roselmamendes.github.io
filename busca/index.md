---
layout: page
title: "Busca"
date: 
modified:
excerpt:
image:
  feature:
search_omit: true
sitemap: false
---
  
<!-- Search form -->
<form method="get" action="{{ site.url }}/search/" data-search-form class="simple-search">
  <label for="q">Busca {{ site.title }} por:</label>
  <input type="search" name="q" id="q" placeholder="O que você está procurando?" data-search-input id="goog-wm-qt" autofocus />
  <input type="submit" value="Buscar" id="goog-wm-sb" />
</form>

<!-- Search results placeholder -->
<h6 data-search-found>
  <span data-search-found-count></span> resultados(s) encontrados para &ldquo;<span data-search-found-term></span>&rdquo;.
</h6>
<ul class="post-list" data-search-results></ul>

<!-- Search result template -->
<script type="text/x-template" id="search-result">
<li>
	<article>
		<a href="##Url##">##Title##<span class="entry-date"><time datetime="##Date##">##Date##</time></span></a>
	</article>
	<footer>
		<span><i class="fa fa-edit"></i>&nbsp;##Category##</span>
		<span><i class="fa fa-tags"></i>&nbsp;##Tags##</span>
		<span class="excerpt">##Excerpt##</span>				
	</footer>
</li>
</script>
