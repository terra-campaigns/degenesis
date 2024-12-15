---
template: npc v0.3
layout: default
title: Prokhor
role: Leader of the Streltsys
parent: Founders' Blessed

image: https://i.imgur.com/J01Rztk.png

statblock: false
hp: 
armour: 
str: 
dex: 
wil: 
at: 

---

# {{ page.title }}

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
