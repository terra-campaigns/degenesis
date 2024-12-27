{% comment %} template: npc v0.3 {% endcomment %}

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




{% comment %} template: npc v0.3.1 {% endcomment %}

{% if page.template == "npc v0.3.1" %}

# {{ page.title }}

{% if page.role %}
#### **{{ page.role }}**
{% endif %}

{% if page.archetype %}
| {{ page.archetype }} | {% endif %} {% if page.statblock %} 
| {{ page.hp }} HP, {{ page.armour }} armour, {{ page.str }} STR, {{ page.dex }} DEX, {{ page.wil }} WIL, {{ page.at }} |
{% endif %} {% if page.details %}
{% for sec in page.details %}
| {{ sec }} {% endfor %} |
{% endif %}

{% if page.image %}
![]({{ page.image }})
{% endif %}

{% include connected_to.md %}

{% endif %}
