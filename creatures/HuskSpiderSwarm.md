---
template: NPC v0.3
layout: default
title: Husk Spider (Swarm)
parent: Creatures
image: https://i.imgur.com/QmIQOph.png

statblock: true
hp: 6
armour: 0
str: 6
dex: 14
wil: 8
at: sting (d6), *detachment*

---

# {{ page.title }}

- The stench of ammonia lingers, accompanied by faint, greasy traces left by their skittering legs.
- "**Critical Damage**: Cocoons threats in silk that hardens, suffocating the target under layers of interwoven fibers (d4 infection per round)."
- "**Chakra Calls**: Swarm when spore fields or Psychonauts feel threatened."
- Nearby clicking and rustling sounds grow louder as Husk Spiders approach.

| Husk Spiders have been seen in the Stukov Desert, sometimes even in Borca. However, their home is Pollen. There, they are the vanguard when the ground thaws and a Fractal Forest comes to the surface. They attack this oasis by the hundreds of thousands, and other spiders and centipedes follow the pheromone contained in their silk.

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
