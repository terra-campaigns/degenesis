---
layout: default
template: 0.4
type: faction
nav_exclude: false
hook_exclude: false
has_children: true
has_toc: false

parent: Directory
title: Altair Envoys
role: Loose Inter-Cult Assembly  
status:

hooks:

images: [../../imgs/gallery/Pasted%20image%2020251130175014.png]
flavour_text: IN 2595, BAPTIST ALTAIR WAS MURDERED IN PURGARE. Baptist Altair was important for your Cult. You were not told why. You have been told that Baptist Altair is important for other Cults, too. The order is to get to know them and work together. But don’t trust everyone.

---

{% include header_directories.md %}
{% comment %}
`=map(this.images, (x) => "![im|200](" + x + ")")`
```dataview
LIST without ID "["+ title + "](" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE file.path != this.file.path SORT file.folder DESC
```
---

{% endcomment %}


|                           |                         |
| ------------------------- | ----------------------- |
| ![]({{ page.images }}) | {{ page.flavour_text }} |
