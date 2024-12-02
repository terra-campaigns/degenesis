---
template: NPC v0.3
layout: default
title: Purifier Harlem
parent: Protectorate Clique
image: 

statblock: true
hp: 
armour: 
str: 
dex: 
wil: 
at: 

---

# {{ page.title }}

- Spitalian Femulancer?
- Is on the pocket of [Dexter](Dexter.md)

{% comment %} =========================== TEMPLATE CODE =========================== {% endcomment %}
{% comment %} ===================== DO NOT EDIT BELOW THIS LINE ===================== {% endcomment %}

{% if page.image %}
![]({{ page.image }})
{% endif %}
{% if page.statblock %}
| {{ page.hp }} HP, {{ page.armour }} Armour, {{ page.str }} STR, {{ page.dex }} DEX, {{ page.wil }} WIL, {{ page.at }} |
{% endif %}
{% include connected_to.md %}

{% comment %} =========================== TEMPLATE ENDS =========================== {% endcomment %}
