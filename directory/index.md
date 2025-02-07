---
layout: default
title: Directory
has_children: true
nav_order: 51
has_toc: false

---

# Directory

![](https://img2.storyblok.com/0x0/filters:quality(99):format(webp)/f/72501/5031x3579/fdaa067ccc/wp-36-desktop-5031x3579.jpg)

## People

<table style="width:100%">
  <tr>
    <td align="left">
    <p>
    {% for my_page in site.pages %}
        {% if my_page.type == 'people' %}
            {% if my_page.status %}
                <a href="{{ site.url }}{{ my_page.url }}">{{ my_page.title }}</a>, {{ my_page.status }}<br>
            {% else %}
                <a href="{{ site.url }}{{ my_page.url }}">{{ my_page.title }}</a><br>
            {% endif %}
        {% endif %}
    {% endfor %}
    </p>
    </td>
  </tr>
</table>

## Factions

<table style="width:100%">
  <tr>
    <td align="left">
    <p>
    {% for my_page in site.pages %}
        {% if my_page.type == 'faction' %}
            <a href="{{ site.url }}{{ my_page.url }}">{{ my_page.title }}</a><br>
        {% endif %}
    {% endfor %}
    </p>
    </td>
  </tr>
</table>


## Locations

<table style="width:100%">
  <tr>
    <td align="left">
    <p>
    {% for my_page in site.pages %}
        {% if my_page.type == 'location' %}
            <a href="{{ site.url }}{{ my_page.url }}">{{ my_page.title }}</a><br>
        {% endif %}
    {% endfor %}
    </p>
    </td>
  </tr>
</table>

### World Map

<iframe style="border: 0; width:100%; height: 800px; overflow: auto;" src="https://degenesis.com/world/map/"></iframe>
