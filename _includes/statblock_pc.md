{% comment %} template: pc v0.3 {% endcomment %}

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





{% comment %} template: pc v0.3.1 {% endcomment %}

{% if page.template == "pc v0.3.1" %}

# {{ page.title }}

{% if page.role %}
{% if page.deceased %}
#### **{{ page.role }}**, [deceased]({{ site.url }}/people/#in-memoriam)
{% else %}
#### **{{ page.role }}**
{% endif %}
{% endif %}

{% if page.archetype %}
| {{ page.archetype }} | {% endif %} {% if page.statblock %} 
| {{ page.hp }} HP, {{ page.armour }} armour, {{ page.str }} STR, {{ page.dex }} DEX, {{ page.wil }} WIL |
{% endif %} 

{% if page.image %}
![]({{ page.image }})
{% endif %}

{% if page.details %}
{% for sec in page.details %}
| {{ sec }} {% endfor %} |
{% endif %} | GEAR: {% for sec in page.gear %} {{ sec }}, {% endfor %}

{% include connected_to.md %}
{% endif %}
