---
template: npc v0.3
layout: default
title: Yelena
parent: Protectorate Clique

image: https://i.imgur.com/AJau74H.png

statblock: false
hp: 
armour: 
str: 
dex: 
wil: 
at: 

---

# {{ page.title }}

- Cossack Tribal Warrior
- Fond of [Isolde Pax](IsoldePax.md)
- Daughter had Psychonaut signs and was killed horribly in [Nikopol](../../campaigns/ConnectNikopol/InNikopol01.md), Yelena became broken after the fact.

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
