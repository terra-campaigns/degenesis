{% comment %}
=======================
template: npc v0.3
=======================
{% endcomment %}

{% if page.template == "npc v0.3" %}

# {{ page.title }}

| {{ page.role }}

{% if page.image %}
![]({{ page.image }})
{% endif %}
{% if page.statblock %}
| {{ page.hp }} HP, {{ page.armour }} Armour, {{ page.str }} STR, {{ page.dex }} DEX, {{ page.wil }} WIL, {{ page.at }} |
{% endif %}
{% for sec in page.details %} 
- {{ sec }}  {% endfor %}
{% include connected_to.md %}

{% endif %}


{% comment %}
=======================
template: npc v0.3.1
=======================
{% endcomment %}

{% if page.template == "npc v0.3.1" %}

# {{ page.title }}

| ***{{ page.role }}***
| {{ page.archetype }}

{% if page.image %}
![]({{ page.image }})
{% endif %}
{% if page.statblock %}
| {{ page.hp }} HP, {{ page.armour }} Armour, {{ page.str }} STR, {{ page.dex }} DEX, {{ page.wil }} WIL, {{ page.at }} |
{% endif %}
{% for sec in page.details %} 
- {{ sec }}  {% endfor %}
{% include connected_to.md %}

{% endif %}