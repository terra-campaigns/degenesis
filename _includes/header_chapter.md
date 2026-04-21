{% comment %}
terra-jekyll tools v0.7.0
{% endcomment %}

# {{ page.title }}
{: .text-right}

#### {{ page.nav_order | date: "%-d %B %Y" }}, {% if page.location %} in {{ page.location }} {% elsif page.region %} in {{ page.region }} {% endif %}
{: .text-right}

{% if page.narration %}

{% assign filename = page.path | split: '/' | last | replace: '.md', ''%}
{% for entry in page.narration %}
{% assign to_include = filename | append: "_" | append: entry | append: ".md" %}
<details close markdown="block">
  <summary id="accounts">
    <b>{{ entry }}'s accounts</b><br> 
  </summary>
{: .text-delta}
{% include_relative {{ to_include }} %}
</details>
{% endfor %}
{% endif %}

{% include connected_to.html %}

