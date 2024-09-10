---
layout: default
title: Terra System
parent: Systems
nav_order: 999
nav_exclude: true

---

# Terra System's Degenesis

This section details how to play **Degenesis** using a forked version of the **Terran Engine v0.5.3a**.
The **Terran Engine** is self contained in this section, and will not require reading the [SRD](https://terra-campaigns.github.io/terraSystem/) separately.

#### Taxonomy

- "You" and "Your" are used interchangeably to refer to players and their characters. For disambiguation "Player(s)" is used when referring to the player outside the context of their character.
- "Challenge" is used to represent anything that is antagonistic to you, be that an NPC, the environment, etc.
- Meta game concepts, stats and currencies are marked as *italic*.
- Book references are marked in `code`, they might be accompanied by page ranges.

#### Requirements

- **Degenesis Rebirth**, which can be obtained at no cost from the [Degenesis website](https://degenesis.com/downloads/books/degenesis-rebirth-edition):
	- **Primal Punk** `DR1`
	- **Katharsys** `DR2`
- [The Metamorphica (Classic Edition)](https://www.drivethrurpg.com/pt/product/115703/The-Metamorphica-Classic-Edition), which can be acquired as pay-what-you-want `MORPH`
- **Light** and **Dark Dice**

## Characters

1. With the other players, define a cohesive group concept.
2. Always start with a Name and *Archetype*.
3. Roll for *Attributes* and assign points.
4. Roll for *Grit* and *Ego.*
5. Choose one *Advancement.*

A character sheet is available [here](assets/TerranSheet.pdf).

### Archetypes

You are defined by your **Culture**, **Clan** and **Concept**.
Together they define your *Archetype*.
The *Archetype* encapsulates your background, concept, role and community within the narrative.
It should offer an immediate grasp of your identity and behaviours.
It is expected you will evolve beyond your initial *Archetype*, towards unique narratives.
`DR2 34-41`

#### Example: Who is Scuff

![](https://i.imgur.com/736ZRi8.png)

Meet **Scuff**, our example character.
Because the group is playing in the **Balkan** region, **Scuff** took that as a **Culture**.
The group also agreed to play as a scouting detachment, and most of them are **Clanners**, although one is a **Scraper** - but not **Scuff**.
**Scuff** is intended to be a believer in spirits, so their concept is that of a **Zealot**.

### Attributes

There are $6$ *Attributes* that you can use to overcome obstacles.

- **Intuition**: track targets, understand creatures, care, survive.
- **Reason**: concentrate, think abstractly, build knowledge.
- **Finesse**: dextrous manipulation, precision, subtle misdirection.
- **Exertion**: apply physical force and power, melee.
- **Attunement**: get in the flow and tune the arcane or technology.
- **Influence**: compel obedience, socialise, influence.

Each *Attribute* has a rating (from $0$ to $4$) that determine how many dice to roll when performing *Risky Actions.*
On the character sheet, their ratings are read horizontally.

*Saves* are groupings of two *Attributes* each.

- **Insight/Reflexes** *Save* groups **Intuition** and **Reason** *Attributes*
- **Prowess/Fortitude** *Save* groups **Finesse** and **Exertion** *Attributes*
- **Resolve/Willpower** *Save* groups **Attunement** and **Influence** *Attributes*

*Saves* also have ratings (from $0$ to $2$) that determine how many dice to roll in a *Reaction* situation.
On the character sheet, their ratings are read vertically.

#### Determine ratings

For each *Save* grouping (**Insight**, **Prowess**, and **Resolve**) roll $1d$ and consult the table below to determine how many rating points you have to distribute for each.

|               | $1:3$ | $4:5$ | $6$ |
| :------------ | :---: | :---: | :-: |
| Rating points |  $1$  |  $2$  | $3$ |

In certain conditions, you might permanently lose ratings, this is discussed in other sections.

#### Example: Scuff's ratings

![](https://i.imgur.com/bnKfumi.png)


Scuff has an **Attunement** *Attribute* rating of $3$ (read horizontally).
They roll $3d$ when performing a Risky Action related to **Attunement**.
They also have **Influence** $0$ (horizontally), so they roll $0d$ (i.e. no chance if no advantage is found).
If their **Resolve** is challenged, they may roll a *Reaction* with $1d$, based on their **Resolve/Willpower** *Save* rating (read vertically).

### Grit & Ego

> *"It's about how hard you can get hit and keep moving forward"*
> (Rocky Balboa)

While *Grit* represents your disposition, *Ego* represents your resilience to keep pushing.
Roll $1d$ to determine your *Grit* and *Ego.*
Advancements and conditions may change the number of dice you roll.

#### Wounds

You lose *Grit* when you are harmed.
When your *Grit* reaches $0$ you start marking *Wound* tracks.
You have $3$ *Wound* tracks: Stressed ($-1d$ **Insight**), Broken ($-1d$ **Prowess**) and Weary ($-1d$ **Resolve**).
When all three *Wound* tracks are marked, you become *Mortally Wounded*.

While *Mortally Wounded* you cannot gather *Light Die* for your *Risky Actions*.
You will die instantly if harmed further, or in minutes if not attended to.
If you survive being *Mortally Wounded*, you develop a *Malaise*.
Roll $1d$ and consult the table below.
With the GM, describe it narratively.

|     | *Malaises*                                                                         |
| :-: | ---------------------------------------------------------------------------------- |
| $1$ | No *Malaise*.                                                                      |
| $2$ | $-1$ **Prowess**, you die if it goes below $0d$.                                   |
| $3$ | $-1$ **Insight**, you die if it goes below $0d$.                                   |
| $4$ | $-1$ **Resolve**, you die if it goes below $0d$.                                   |
| $5$ | When you re-roll your *Ego,* use $-1d$ from now on. You die if it goes below $0d$. |
| $6$ | Re-roll your *Grit* with $-1d$ from now on. You die if it goes below $0d$.         |

After a well fed and rested night, you roll and reset your *Grit* ($1d$).
If you did not rest well you have $-1d$ to roll for *Grit*.
Each *Wound* track recovers through appropriate care and a week of rest.
A *Malaise* never recovers.

#### Pushing yourself

You spend *Ego* when you push beyond yourself in *Risky Actions* or use some character *Advancements.*
When your *Ego* reaches $0$ you are lost somehow.
With the GM determine how your last scene goes.

You may choose to consume **Primer** spores (or drugs based on these spores) to roll and reset your *Ego* ($1d$).
Consult the highest value of your roll on the table below.

|       | Outcome                                                                     |
| :---: | --------------------------------------------------------------------------- |
| $1:3$ | Reset your *Ego* to $1:3$. You gain a Stigma. `DR2`                         |
| $4:5$ | Reset your *Ego* to $4:5$, and roll a detrimental mutation. `MORPH 127-129` |
|  $6$  | Reset your *Ego* to $6$, and roll a random mutation. `MORPH 124-129`        |

These are the **Primer** slowly developing you into a [Homo Degenesis](https://degenesis.com/world/stories/essential-reads/homo-degenesis).
With the GM, determine the mechanical effects and how to introduce your mutation into the narrative.

#### Example: Scuff's scuffs

![](https://i.imgur.com/IYdZoZh.png)


Scuff has $1d$ for both *Grit* and *Ego* (usual for early characters).
They have seen some harm, having lost $3$ *Grit* (from $5$ to $2$) and taken a **Hazed** wound.
This means that any time they roll related to **Insight** (**Intuition** or **Reason** for *Risky Actions*, or **Evasion** *Reaction*), they take $-1d$.

Scuff also risked their *Ego* a few times, and took **Spores** to reset it (from 2 to 4).
They have taken a mutation, which is detailed as a *Condition*.
Finally, they have gotten a malaise at some point, having reduced their **Exertion** *Attribute* rating because of a weakened lower back.

### Advancements

As you become more seasoned, you gain *Advancements*.
You start the game with $1$ *Advancement*.
Many *Advancements* in this section are adaptations of **Degenesis**' Potentials.
These will be accompanied by book reference tags.

For every session you play (and survive) you gain $+2$ *Experience*.
You also gain $+1$ *Experience* for each new *Condition* you develop.

Whenever it is narratively coherent, you may spend *Experience* equal to $2\times$ your current number of *Advancements* to gain a new one.
As you do that, you may reset your *Grit* maximum.
Roll your dice and keep the maximum between the current and the new *Grit*.

Until you have $5$ *Advancements*, you can only choose from your own **Cult** or from the common list.

#### Common

|                 |                                                                                                                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Asceticism      | You do not take $-1d$ when rolling for *Grit* while poorly fed. `DR2 98`                                                                                                                       |
| Bodyguard       | You can choose to take damage instead of one of your allies.                                                                                                                                   |
| Brainwave       | Roll **Attunement**. It you *Succeed*, you gain $+1d$ when you try to find a solution to a problem, until the end of the scene. If you *Fail*, you become **Hazed**. `DR2 98`                  |
| Could be worse  | When **Broken** you do not take the penalty of $-1d$. `DR2 99`                                                                                                                                 |
| Danger sense    | $+1d$ whenever you use a **Insight/Evasion** *Save*. `DR2 98-99`                                                                                                                               |
| Developed       | Gain $1$ in an *Attribute*. The maximum you can have in all *Attributes* together is $10$.                                                                                                     |
| Die Hard        | When you reset your *Grit*, roll $+1d$ and sum all the dice you rolled.                                                                                                                        |
| Eager           | When you reset your *Ego*, roll $+1d$ and keep the highest.                                                                                                                                    |
| Elephant skin   | When unarmored your **Armour** is $1$. `DR2 98`                                                                                                                                                |
| Ether call      | $+1d$ when interacting with other mutants (including combat). You must have at least $5$ mutations to take this *Advancement*. `DR2 98`                                                        |
| Fast            | When you roll, your *Effect* is always applied first.                                                                                                                                          |
| Marathon        | $+1d$ when running. `DR2 99`                                                                                                                                                                   |
| Number cruncher | $+1d$ when using mathematics or logic. `DR2 99`                                                                                                                                                |
| Sensory acuity  | You have $+1d$ on noticing things through a chosen sense.                                                                                                                                      |
| Sleek           | $+1d$ whenever you contort yourself to to break free. `DR2 99`                                                                                                                                 |
| Specialist      | Choose a specific type of action. When you *Fail* it in a *Risky Actions* you still succeed, with Reduced *Effect*. For a list of specialisations, use **Degenesis**' skills list. `DR2 17-23` |
| Unyielding      | When **Weary** you do not take the penalty of $-1d$. `DR2 99`                                                                                                                                  |
| Whirlwind       | In combat, when you are successful, select an additional die as a second hit.                                                                                                                  |

#### Chroniclers

|                |                                                                                                                                                                   |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dead End       | $+1d$ when attacking someone cornered. `DR2 53`                                                                                                                   |
| Download       | $+1d$ when questioning a prisoner NPC. `DR2 53`                                                                                                                   |
| Fractal Memory | $+1d$ on memory related actions. `DR2 53`                                                                                                                         |
| Nova           | Roll **Attunement**. It you *Succeed*, cause blindness until the end of the scene. If you *Fail*, the suit power is depleted until the end of the scene. `DR2 53` |
| Tesla          | $+1d$ when in close contact conflict. If you *Fail*, roll $2d$ effect as you electrocute yourself. `DR2 53`                                                       |
| Upload         | $+1d$ when trying to incept an idea on an NPC. `DR2 53`                                                                                                           |

### Equipment

With the GM define which tags, ranges and *Effect* are appropriate for your weapons.
Weapons used outside their expected ranges roll with $-1d$.

The following short list of tags may be expanded with the GM.

- **Versatile**: $+1e$ when held two-handed.
- **Nimble**: *Effect* is applied first.
- **Slaughter**: *Effect* die explode on $5+$.
- **Improvised**: $-1d$, $1e$.
- **Unhandy**: $-1d$ if used at **Contact** or **Reach** ranges.

| Weapon        | Effect | Ranges           | Tags      | Notes |
| ------------- | ------ | ---------------- | --------- | ----- |
| Knife         | $2e$   | Contact          | Nimble    |       |
| Staff         | $2e$   | Contact; Reach   | -         |       |
| Primitive bow | $3e$   | Nearby           | Unhandy   |       |
| Short sword   | $3e$   | Contact          | Versatile |       |
| Long sword    | $4e$   | Contact          | Versatile |       |
| Hunting rifle | $5e$   | Nearby; Far Away | -         |       |

Armours act as buffers when you take damage from *Challenges*.
Subtract the armour modifier from the *Effect* before reducing your *Grit*

| Armour     | Modifier | Details                                            |
| ---------- | :------: | -------------------------------------------------- |
| **Light**  |   $-1e$  |                                                    |
| **Heavy**  |   $-2e$  | $-1d$ to run, observe, sneak, swim, etc.           |
| **Shield** |   $-1e$  | Can be sacrificed to completely avoid an *Effect*. |

## Rules

### Risky Actions

When you are trying your chances at a *Risky Action*, say what you intend to do.
With the GM determine your appropriate *Attribute* or *Save*.
Then gather 6-sided dice.

|                                | Dice Pool                                                                                                                                                                                                                     |
| :----------------------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](../imgs/dice-light-6-sml.png) | Take a number of **Light Dice** equal to your applicable *Attribute* or *Save*. If you are in an advantageous or precarious position, the GM may give you $\pm d$. You must always roll between $0d$ and $4d$ **Light Dice**. |
| ![](../imgs/dice-dark-6-sml.png)  | Take as many **Dark Dice** as you wish to risk *Ego* for pushing yourself for a success. For each **Dark Die** that rolls equal or lower than your current *Ego*, decrease your *Ego* in one.                                 |

Roll the dice and choose one die to be your *Precision* (generally the highest, but you might choose differently if you wish) and consult the table.

|       | Outcome                                                                                                                                                     |
| :---: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $1:3$ | You *Fail*, and things get worse. With the GM describe the consequences. The GM may also allow you to succeed, but things will get worse in some other way. |
| $4:5$ | You *Succeed*, but there’s some consequences. With the GM describe the complication and how you succeed.                                                    |
|  $6$  | You *Succeed*. With the GM describe what happens.                                                                                                           |

Evaluate *Effects* as appropriate, if the *Risky Action* is part of a *Challenge*.

#### Effects

*Effects* determines the quantitative result of your *Risky Actions* towards overcoming *Challenges*.
Examples of *Effects* are:

- Damage given,
- Convincing done,
- Distance covered,
- Weakness learned.

When you roll your *Risky Actions*, choose one die to be your *Effect* (generally the second highest, if the highest was used as *Precision*).
The *Effect* die is an exploding die (i.e. if the result is a $6$, keep rolling and accumulating the result).
The *Effect* you apply is never lower than the *Effect* *Tier* of your approach, regardless of the die outcome.
Your *Effect* is subtracted from the *Challenge* *Disposition*.

| Tier                   | Minimum Effect for                                                                   |
| :--------------------- | ------------------------------------------------------------------------------------ |
| $1e$<br>**Improvised** | Makeshift tool;<br>Rock, pipe, punch.                                                |
| $2e$<br>**Reduced**    | Primitive tool;<br>Weak argument<br>Knife, staff                                     |
| $3e$<br>**Standard**   | Fit for purpose tool;<br>Good argument; <br>Revolver, short sword                    |
| $4e$<br>**Increased**  | Expert grade tool;<br>Strong rationale;<br>Autofire pistol, SMG, shotgun, long sword |
| $5e$<br>**Extreme**    | Tech augmented expert grade tool;<br>Rifle, axe, halberd                             |

#### Challenges

Sometimes, multiple actions are required to overcome *Challenges*.
Examples of *Challenges* are

- fighting an enemy,
- duelling rhetorically,
- negotiating an environment,
- crawling a location,
- journeying.

*Challenges* have Disposition, which measures how much *Effect* they take to be overcame.
*Challenges* also have *Effect* dice that are applied to you as consequences of your *Risky Actions*.

| Tier                   | Disposition | Effect | Examples                                                             |
| ---------------------- | :---------: | :----: | -------------------------------------------------------------------- |
| $0$<br>**Trivial**     |     $5$     | $d/2$  | Unskilled adversaries, low height climb, known journey               |
| $1$<br>**Dangerous**   |    $10$     |  $1d$  | Skilled adversaries, small predator, large prey, troublesome journey |
| $2$<br>**Serious**     |    $20$     |  $2d$  | Expert adversaries, large predator, traverse fire or acid            |
| $3$<br>**Formidable**  |    $30$     |  $3d$  | Human prime, apex predator, climbing the Everest                     |
| $4$<br>**Exceptional** |    $40+$    | $4d+$  | Transhuman, often fatal environments, heroic journeys                |

Some challenges might be multifaceted.
A bulky rival might be a Dangerous *Challenge* to fight against, but a Trivial *Challenge* to be convinced to ignore you.

When *Challenge Effects* are applied to you narratively, use the table.

|       | Consequence                    |
| :---: | ------------------------------ |
| $1:3$ | Something annoying happens.    |
| $4:5$ | Something troublesome happens. |
|  $6$  | Something devastating happens. |

When *Challenge* *Effects* are applied to you as damage your *Grit* might be reduced.
Subtract the armour rating from the *Effect*, and then reduce the remainder from your *Grit*.

### Fortune die 

When the GM wants to leave some decision to the dice, determine the chances and roll $1d$.

### Sayonara 

At any moment you can decide it is your last scene.
When you do that, re-roll your *Ego* and *Grit*, and keep the highest values.
For this scene, you only expend *Ego* if you roll a $1$.
By the end of the scene, you have to figure out how you depart (death, madness, mission, etc.).
You can create a new character with half (rounded up) the number of *Advances* the previous character had.

## Social contract

Define a social contract on the first session, and review it anytime a new player joins the table.

## Copyright 

*This work is based on [Blades in the Dark](http://www.bladesinthedark.com/), product of One Seven Design, developed and authored by John Harper, and licensed for our use under the [Creative Commons Attribution 3.0 Unported license](http://creativecommons.org/licenses/by/3.0/).*

*Blades in the Dark™ is a trademark of One Seven Design. The Forged in the Dark Logo is © One Seven Design, and is used with permission.*

![](https://bladesinthedark.com/sites/default/files/inline-images/forged_in_the_dark_logo2_0.png)

### Credit Due

This work is also inspired in several other games for it's sub-systems. Namely:

- The simplicity is inspired by [*World of Dungeons*](https://johnharper.itch.io/world-of-dungeons) by John Harper.
- *Ego* usage is inspired by [Trophy](https://trophyrpg.com/), product of Jesse Ross and Hedgemaze Press.
- *Precision* and *Effect* of a *Risky Action* evaluated with one single roll is inspired by [*Best Left Buried Zine Edition*](https://soulmuppet-store.co.uk/products/best-left-buried-zini-edition) by Zachary Cox and Nicholas Spence.
