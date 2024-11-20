---
template: NPC v0.3
layout: default
title: Migrants
parent: Creatures
image: https://img2.storyblok.com/0x0/filters:quality(99):format(webp)/f/72501/5517x3300/4675ce01f7/pollen-migrants.jpg

statblock: true
hp: 8
armour: 2
str: 14
dex: 11
wil: 4
at: weapon and claws (d8+d8)

---

# {{ page.title }}

- Shape-shifting abilities and physical prowess, blurs the line with the supernatural
- Avoid areas with methane gas and open flames
- "**Critical Damage**: A large chuck of flesh is infested with Sepsis (d6 infection)"
- "**Blossom**: Kills itself and spread Sepsis infection (d10 *blast* infection)"

| The true rulers of [Pollen](https://degenesis.com/world/cultures/pollen) are the Biokinetics. These Aberrants exhibit incredible shape-shifting abilities and display physical prowess that blurs the line with the supernatural. The most common forms are Migrants, Biokinetics breaking out across the plains to seed new spore fields and spread the Sepsis westwards, thus expanding their Chakra’s area of influence.

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
