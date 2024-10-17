# {{ page.title }}

| {{ page.hp }} HP, {{ page.ar }} Armour, {{ page.s }} STR, {{ page.d }} DEX, {{ page.w }} WIL |

{% for sec in page.bullets %} 
| {{ sec }} | {% endfor %}

|**Gear:** {% for sec in page.gear %} {{ sec }}, {% endfor %}
