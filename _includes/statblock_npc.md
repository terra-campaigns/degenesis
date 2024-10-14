# {{ page.title }}

| {{ page.hp }} HP, {{ page.ar }} Armour, {{ page.str }} STR, {{ page.dex }} DEX, {{ page.wil }} WIL, {{ page.at }} |

{% for sec in page.bullets %} 
| {{ sec }} | {% endfor %}
