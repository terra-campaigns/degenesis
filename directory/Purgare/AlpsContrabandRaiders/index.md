---
layout: default
template: 0.4
type: faction
nav_exclude: false
has_children: true
has_toc: false

parent: Directory
title: Hellvetics Contrabandists
role: 
status: 
footer_content: 

images:

---

{% include header_directories.md %}
{% comment %}
`=map(this.images, (x) => "![im|200](" + x + ")")`
```dataview
LIST without ID "["+ title + "](" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE file.path != this.file.path SORT file.folder DESC
```
---

{% endcomment %}
