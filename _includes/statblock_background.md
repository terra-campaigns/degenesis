# {{ page.title }}

|                           |                         |
| ------------------------- | ----------------------- |
| ![]({{ page.icon_link }}) | {{ page.flavour_text }} |

![]({{ page.img_front}})

## Names

{% for entry in page.names %} {{ entry }} <br>   {% endfor %}

## Starting Gear

{% for entry in page.gear %} {{ entry }} <br>   {% endfor %}

## What is your rank? Roll a d6.

![]({{ page.img_rank }})

{% for entry in page.ranks %}
| **{{ entry.roll }}** | {{ entry.text }} | {% endfor %}

Depending on gained renown, you may be promoted to higher Ranks by your Cult.

![]({{ page.img_eqpt }})

## What is your potential? Roll a d6.

{% for entry in page.potentials %}
| **{{ entry.roll }}** | **{{ entry.name }}:** *"{{ entry.flavour }}"* <br> {{ entry.rule }} | {% endfor %}

With enough time and a mentor you can learn new potentials.
Even from other **Backgrounds**.

![]({{ page.img_sttp }})
