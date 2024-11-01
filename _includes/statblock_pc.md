# {{ page.title }}

| {{ page.hp }} HP, {{ page.armour }} Armour, {{ page.str }} STR, {{ page.dex }} DEX, {{ page.wil }} WIL |

{% for sec in page.details %} 
- {{ sec }}  {% endfor %}

![]({{ page.image}})

|**Gear:** {% for sec in page.gear %} {{ sec }}, {% endfor %}

{% comment %}
statblock_pc v0.2
{% endcomment %}
