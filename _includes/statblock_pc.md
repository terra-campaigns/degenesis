{% comment %}
=======================
template: pc v0.3
=======================
{% endcomment %}

{% if page.template == "pc v0.3" %}

# {{ page.title }}

| {{ page.role }}

{% if page.image %}
![]({{ page.image }})
{% endif %}
{% if page.statblock %}
| {{ page.hp }} HP, {{ page.armour }} Armour, {{ page.str }} STR, {{ page.dex }} DEX, {{ page.wil }} WIL |
{% endif %}
{% for sec in page.details %} 
- {{ sec }}  {% endfor %}

|**Gear:** {% for sec in page.gear %} {{ sec }}, {% endfor %}
{% include connected_to.md %}
{% endif %}
