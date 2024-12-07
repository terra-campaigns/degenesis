{% comment %}
=======================
template: npc v0.3
=======================
{% endcomment %}

{% if page.template == "loc v0.3" %}

# {{ page.title }}

> {{ page.role }}

{% if page.image %}
![]({{ page.image }})
{% endif %}
{% for sec in page.details %} 
| {{ sec }} | {% endfor %}
{% include connected_to.md %}

{% endif %}

