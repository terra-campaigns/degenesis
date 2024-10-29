# {{ page.title }}

| {{ page.hp }} HP, {{ page.ar }} Armour, {{ page.str }} STR, {{ page.dex }} DEX, {{ page.wil }} WIL, {{ page.at }} |

{% for sec in page.bullets %} 
- {{ sec }}  {% endfor %}

![]({{ page.image}})

| {% for sec in page.flavour %} {{ sec }} {% endfor %} |

{% comment %}
statblock_npc v0.2
{% endcomment %}
