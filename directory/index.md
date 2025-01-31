---
layout: default
title: Directory
has_children: true
nav_order: 51

---

# Directory

![](https://img2.storyblok.com/0x0/filters:quality(99):format(webp)/f/72501/5031x3579/fdaa067ccc/wp-36-desktop-5031x3579.jpg)

### In Memoriam

<table style="width:100%">
  <tr>
    <td align="left">
    <p>
    {% for my_page in site.pages %}
    {% if my_page.deceased %}
    <a href="{{ site.url }}{{ my_page.url }}">{{ my_page.title }}</a><br>
    {% endif %}
    {% endfor %}
    </p>
    <p> ... and others we don't remember their names </p>
    </td>
  </tr>
</table>

### World Map

<iframe style="border: 0; width:100%; height: 800px; overflow: auto;" src="https://degenesis.com/world/map/"></iframe>
