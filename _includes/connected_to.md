#### Connected to
{: .no_toc .text-right}

{% comment %}
connected_to v0.4.1
{% endcomment %}

{% for entry in site.data.markdown_links.file[page.path] %} {% if entry.is_internal %} {% assign target = site.pages | where: 'path', entry.url %} {% assign prettylink = entry.url | split: "." | first %} [{{ target[0].title }}]({{ site.url }}/{{ prettylink }})  
{% else %} [{{ entry.text }}]({{ entry.url }})  
{% endif %} {% endfor %} {: .fs-3 .text-right }
