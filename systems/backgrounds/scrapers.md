---
title: Scrapers
layout: default
parent: Backgrounds

potentials:
  one:
    name: The Mob
    flavour:
      The Apocalyptics swindle them, Judges hound them, Chroniclers deceive them, and the Clans drive them away.
      But when their anger finally erupts, it spreads like wildfire, igniting a shared fury among the crowd.
      The Scrapper seizes the moment, rallying the mob to action with a few well-chosen words.
    rule:
      A person or a small detachment develops a deep hatred of someone of your choice from another Cult.
  two:
    name: Rat
    flavour:
      Scrappers survive by avoiding trouble, but Rats among them seek it out while seamlessly blending into the crowd.
      They can pull off daring acts like robbing a merchant and skilfully shifting the blame to an unsuspecting bystander, disappearing into the throng with their loot unnoticed.
      No matter what they do, Rats always seem innocent, or at least, no one can ever prove otherwise.
    rule:
      You can pull roguish acts and never be caught.
  three:
    name: Tough Dog
    flavour:
      People kick and torment the Tough Dogs, but they just bite back, taunting, "Is that all you've got?" They endure the abuse, waiting for their enemies to tire, knowing they can take more punishment than most.
    rule:
      Gain +1 Armour (to the limit of 3).
  four:
    name: Nitro 
    flavour:
      Deep beneath layers of fear and survival instincts, a buried rage simmers within, fuelled by the contempt of those who see them as mere dirt diggers.
      This hidden fury, unearthed through years of digging, waits to erupt and consume anyone who dares look down on them.
      When unleashed, this anger turns the Scrapper into a force of devastation, striking with unmatched ferocity.
    rule:
      Gain **Fatigue**. Your attacks are enhanced and non-Blast attacks are impaired against you, until you take damage.
  five:
    name: Truffle Pig
    flavour:
      Skilled Scrappers uncover artefacts that make Chroniclers uneasy as they reluctantly part with their Drafts, while less fortunate Scrappers barely earn more than the scrap’s worth.
      The best Scrappers possess an instinct, a sixth sense for finding hidden treasures and avoiding dangers in the ruins.
    rule:
      Choose one kind of object (key, arrow, gold, etc.). You can sense the nearest example.
  six:
    name: Darwin
    flavour:
      In the harsh depths of the ruins, only the strongest emerge.
      The Darwins, through luck or sheer strength, consistently escape the most desperate situations.
      These masters of survival gain renown with each narrow escape.
    rule:
      You see a place where you can rest safely, and hidden, for a **Watch** (you still have to get there safely).

  
---

# {{ page.title }}

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                            |     |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| ![06-CULT-SCRAPPERS-WHITE-ON-BLACK-320x320](../../../imgs/icons/06-CULT-SCRAPPERS-WHITE-ON-BLACK-320x320.webp) | Drawn towards the ruins, away from the humming, raucous cities, [Scrappers](https://degenesis.com/world/cults/scrappers) dig in the dust and dirt. Every cut of the spade brings them closer to the era of the ancient people. They work tirelessly, digging all the way down until they can drag technical wonders caked with soot into the light of day. |     |

![](https://a.storyblok.com/f/72501/2715x3840/59d5c5c899/006-scrappers-archetype.jpg)

## Names

- Rex "Rusty" Voss
- Mara "The Rat" Quinn
- Dexter "Wrench" Hargrove
- Nina "Scav" Cole
- Jax "Grit" Turner
- Sera "Dust" Kline
- Viktor "Rubble" Nikitin
- Lena "Shiv" Goss
- Omar "Scrap" Delaney
- Tara "Gutter" Morrow

## Starting Gear

- 1d6 x 50 Chronicler Drafts
- Rope & grappling hook (d4)
- Compass
- Periscope

## What is your rank? Roll 1d6.

![](https://i.imgur.com/KFQ3EBG.png)

|         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1**   | **MOUSE**: You work for an old Scraper. He always offers you food.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **2:3** | **BADGER**: Take a **Shotgun** (d8 blast) or **Rifle** (d10), and a **Rune**. Other scrapers recognise when you scratch your **Rune** on walls.                                                                                                                                                                                                                                                                                                                                                                           |
| **4:5** | (choose one) All start with a **Rune**.<br>**FOX**: Take a **Marvel Rifle** (d6) and a carrying rig. You have a foxhole you can use for hiding, protection and storage.<br>**MECHANIST**: Take a **Toolkit**. You always scrape more raw materials when dismantling.<br>**SCAVENGER**: Take a **Crusher** (d6) that looks brutal. Scavengers always help each other out.<br>**CARTEL THUG**: Take a **Heavy Leather Apron** (1 armour). You have a Cartel tattoo in your forehead, and Appraisers always leave you alone. |
| **6**   | (choose one) All start with a **Rune**.<br>**LONE WOLF**: Take an **Upgraded Marvel Rifle** (d8). You know your territory like no one else.<br>**MANUFACTURER**: Take **Workshops Keys**. Manufacturers always give access to each other's workshops.<br>**ALPHA WOLF**: Take a **Tonfa** (d6). You are held in high regard by Judges, Spitalians, Chroniclers and Helvectics.<br>**APPRAISER**: Take a **Revolver** (d6). You have access to Judges and can negotiate with Chroniclers on behalf of other Scrapers.      |


Depending on gained renown, you may be promoted to higher Ranks by your Cult.

![](https://i.imgur.com/xcLiuvS.png)

## What is your potential? Roll a d6.

|       |                                                                                                                                                                                       |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | **{{ page.potentials.one.name }}**: *"{% for sec in page.potentials.one.flavour %} {{ sec }} {% endfor %}"*<br>{% for sec in page.potentials.one.rule %} {{ sec }} {% endfor %}       |
| **2** | **{{ page.potentials.two.name }}**: *"{% for sec in page.potentials.two.flavour %} {{ sec }} {% endfor %}"*<br>{% for sec in page.potentials.two.rule %} {{ sec }} {% endfor %}       |
| **3** | **{{ page.potentials.three.name }}**: *"{% for sec in page.potentials.three.flavour %} {{ sec }} {% endfor %}"*<br>{% for sec in page.potentials.three.rule %} {{ sec }} {% endfor %} |
| **4** | **{{ page.potentials.four.name }}**: *"{% for sec in page.potentials.four.flavour %} {{ sec }} {% endfor %}"*<br>{% for sec in page.potentials.four.rule %} {{ sec }} {% endfor %}    |
| **5** | **{{ page.potentials.five.name }}**: *"{% for sec in page.potentials.five.flavour %} {{ sec }} {% endfor %}"*<br>{% for sec in page.potentials.five.rule %} {{ sec }} {% endfor %}    |
| **6** | **{{ page.potentials.six.name }}**: *"{% for sec in page.potentials.six.flavour %} {{ sec }} {% endfor %}"*<br>{% for sec in page.potentials.six.rule %} {{ sec }} {% endfor %}       |

![](https://i.imgur.com/TA3vnRv.png)


---
#### Connected to
{: .no_toc }

<!-- QueryToSerialize: LIST without ID "["+ title + "](https://terra-campaigns.github.io/" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE (file.path != this.file.path AND title != null) SORT file.folder DESC -->
<!-- SerializedQuery: LIST without ID "["+ title + "](https://terra-campaigns.github.io/" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE (file.path != this.file.path AND title != null) SORT file.folder DESC -->
- [Backgrounds](https://terra-campaigns.github.io/degenesis/systems/backgrounds/index), from systems/backgrounds
- [Vorons](https://terra-campaigns.github.io/degenesis/people/Vorons/index), from people/Vorons
<!-- SerializedQuery END -->


{% comment %}
connected_to v0.2
{% endcomment %}

![](https://img2.storyblok.com/3492x1964/filters:quality(90)/f/72501/3508x1973/32682ccbb9/opener-scrappers.jpg)