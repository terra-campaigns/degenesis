---
template: NPC v0.3
layout: default
title: Commando Prime Klaus
parent: Protectorate Clique
image: https://i.imgur.com/ArqQk2I.png

statblock: true
hp: 4
armour: 0
str: 9
dex: 14
wil: 13
at: Splayer (d8 or d4 *detachment*)

---

# {{ page.title }}

- Commander of the [Protectorate Clique](index.md).
- A man of vanity, but well relatable.

| "You and you, back to your posts!" and then unfolds the portrait [one of the Anabaptists](MarcusVoss.md) made of him."

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
