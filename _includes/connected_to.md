
---
#### Connected to
{: .no_toc }

{% comment %}
connected_to v0.4
{% endcomment %}

{% for entry in site.data.markdown_links.file[page.path] %} {% if entry.is_internal %} {% assign target = site.pages | where: 'path', entry.url %} {% assign prettylink = entry.url | split: "." | first %} |![]({{ target[0].icon_link }}){: width="50" } &ensp; &ensp; [{{ target[0].title }}]({{ site.url }}/{{ prettylink }}) | 
{% else %} |![]({{ entry.favicon }}){: width="50"} &ensp; &ensp; [{{ entry.text }}]({{ entry.url }}) | 
{% endif %} {% endfor %}
