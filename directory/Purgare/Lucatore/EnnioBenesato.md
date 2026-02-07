---
layout: default
template: 0.4
type: people
nav_exclude: false
has_children: true
has_toc: true

parent: House Benesato
title: Ennio Benesato
role: 
status: 
footer_content: 

images:
- ../../../imgs/gallery/Pasted%20image%2020260204194616.png


---

{% include header_directories.md %}
{% comment %}
`=map(this.images, (x) => "![im|200](" + x + ")")`
```dataview
LIST without ID "["+ title + "](" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE file.path != this.file.path SORT file.folder DESC
```
---

{% endcomment %}
