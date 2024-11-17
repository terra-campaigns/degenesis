---
title: Spitalians
layout: default
parent: Backgrounds

icon_link: ../../../imgs/icons/01-CULT-SPITALIANS-WHITE-ON-BLACK-320x320.webp
flavour_text: Mankind’s last line of defense against the Primer and its spawn. [Spitalians](https://degenesis.com/world/cults/spitalians) explore the spore fields, dissect dead Psychonauts, and develop poisons and weapons. With their fungicides they cut swathes into the Sepsis, and carry spore covered muscles in glass tubes to lead them to the Aberrants’ breeding grounds.

img_front: https://a.storyblok.com/f/72501/2715x3840/8900dcd07d/001-spitalians-archetype.jpg
img_rank: https://i.imgur.com/LKEOuPq.png
img_eqpt: https://i.imgur.com/n83TXJi.png
img_sttp: https://i.imgur.com/boJTIow.png
img_back: https://img2.storyblok.com/3420x2162/filters:quality(90)/f/72501/4570x2887/fdff41381a/opener-spitalian.jpg

names:
- Dr. Aurelia Voss
- Sergeant Roderick Stein
- Chief Surgeon Octavius Grey
- Pathologist Lena Krieger
- Field Operative Marik Holt
- Purifier Harlan Dray
- Erasmus Kline
- Liora Kaestner

gear:
- 2d6 x 50 Chronicler Drafts
- Scalpel (d6)
- Tranquilizer (3 uses)
- Sterile Gloves

ranks:
  - roll: "1"
    text:
      - "**RECRUIT:** Take **The Manual** and a **Mask** (1 Armour against Spore Infestation). <br>"
  - roll: "2:3"
    text:
      - "**ORDERLY**: Take a **Spitalian Suit** (2 Armour against Spore Infestation). You have strengthened your immune system, re-roll 1d6 HP and keep the highest. <br>"
  - roll: "4:5"
    text:
      - "**FAMULANCER**: Take a **Splayer with Mollusk** (d8) and a **Spitalian Suit** (2 Armour against Spore Infestation). You are appreciated and always get food for free in the Protectorate. <br>"
  - roll: "6"
    text:
      - (choose one) All take a **Spitalian Suit** (2 Armour against Spore Infestation). <br>
      - "**PRESERVIST**: Take a **Preservalis Sword** (d10), a **Pistol** (d6) and a **Horse**. In the Protectorate, you have access to armories. <br>"
      - "**FIELD MEDIC**: take a **Field Kit**, you are well regarded in the Protectorate. <br>"
      - "**SURGEON**: Take **Surgical Equipment**. You are well regarded by the Anabaptists. <br>"
      - "**HYGIENIST**: take a **Hygienist bodysuit** (3 Armour against Spore Infestation). you are well regarded by the Judges. <br>"
      - "**ANAESTHESIOLOGIST**: Take a **Burn injections** (3 uses). You can use **Burn** unpunished. <br>"
      - "**PHARMACIST**: Take an **Apothecarium**. You gain free access to pharmacies and hospitals. <br>"
      - "**EPIGENETICIST**: take a **Sequencer**, you are well regarded by the Chroniclers. <br>"
      - "**HIPPOCRAT**: take a **Revolver** (d6), you have access to secret facilities. <br>"

potentials:
  - roll: 1
    name: SPLAYING
    flavour:
      - "The Spitalian expertly manoeuvres the Splayer, sliding the blades open and closed with precise, deadly efficiency. With a swift motion, he strikes, forcing the mechanism to snap open, and prepares for another strike, each movement adding to his defence and control of battlefield. "
    rule:
      - "Requires a **Splayer**. Engaged opponents have their next attacks impaired. Your attacks are impaired (d4) but they have the Blast property."
  - roll: 2
    name: PHALANX
    flavour:
      - "A wall of spears forms a nearly impenetrable defence, with each point aimed at the enemy. Standing shoulder to shoulder, the Spitalian joins the line, ready to draw attacks toward himself to protect his comrades. As the phalanx strengthens, any foe foolish enough to charge risks impaling themselves on their deadly formation."
    rule:
      - Requires 2+ close allies. Your opponent is impaired if they try to attack the formation in melee.
  - roll: 3
    name: PRESERVALIS
    flavour:
      - "Preservists are relentless, never giving their enemies a chance to surrender. Trained in a brutal technique known as Preservalis, they strike with their sword to create an opening, then follow up with a point-blank pistol shot to ensure the kill. The recoil propels them out of reach, leaving their foes defenceless."
    rule:
      - Requires dual wielding a **Sword** and a **Pistol**. You may disengage after a melee attack.
  - roll: 4
    name: LAST BASTION
    flavour:
      - "The Spitalian's knowledge of his enemy runs deep—flesh torn, bones exposed, even the most hidden vulnerabilities laid bare. He knows precisely where to strike and how to inflict maximum pain. When facing Psychonauts, this intimate understanding grants him an edge, allowing him to strike with devastating accuracy."
    rule:
      - Requires a melee weapon. When you roll 6+ damage, your attack against Psychonaults ignores armour.
  - roll: 5
    name: KRANZLER'S TEACHINGS
    flavour:
      - "Kranzler's soul is unyielding, impervious even to the eerie chants of the Dushani. Famulancers study his techniques, but only the most dedicated can truly master them. Those who succeed become temporarily immune to Psychonautic mental influences, standing firm when others would falter."
    rule:
      - Gain **Fatigue**. You are immune to Dushani chants for the scene.
  - roll: 6
    name: THE LAST FAREWELL
    flavour:
      - "The battlefield is littered with the fallen, and the Spitalian stands alone, the last beacon of hope. In this desperate hour, a destructive madness fuels him, his humanity burning away as he fights on. For a brief time, his attacks, defences, and resilience surge with unmatched fury, but if an ally stirs and rejoins the fight, the flame of his rage extinguishes."
    rule:
      - Your attacks are enhanced until someone rejoins the fight.
---

{% include statblock_background.md %}

---
#### Connected to
{: .no_toc }

<!-- QueryToSerialize: LIST without ID "["+ title + "](https://terra-campaigns.github.io/" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE (file.path != this.file.path AND title != null) SORT file.folder DESC -->
<!-- SerializedQuery: LIST without ID "["+ title + "](https://terra-campaigns.github.io/" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE (file.path != this.file.path AND title != null) SORT file.folder DESC -->
- [Backgrounds](https://terra-campaigns.github.io/degenesis/systems/backgrounds/index), from systems/backgrounds
- [Protectorate Clique](https://terra-campaigns.github.io/degenesis/people/ProtectorateClique/index), from people/ProtectorateClique
- [Return Geteli](https://terra-campaigns.github.io/degenesis/campaigns/ConnectNikopol/ReturnGeteli), from campaigns/ConnectNikopol
<!-- SerializedQuery END -->

{% comment %}
connected_to v0.3
{% endcomment %}

{% if page.img_back %}
![]({{ page.img_back }})
{% endif %}
