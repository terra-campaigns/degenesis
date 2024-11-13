
<table style="width:100%">
  <tr>
    <td align="right">
    <p>
    <b>CONNECTED TO</b><br>
    {% for entry in site.data.markdown_links.file[page.path] %}
    {% if entry.is_internal %}
    {% assign target = site.pages | where: 'path', entry.url %}
    {% assign prettylink = entry.url | split: "." | first %}
    <a href="{{ site.url }}/{{ prettylink }}">{{ target[0].title }}</a><br>
    {% else %}
    <a href="{{ entry.url }}" target="_blank">{{ entry.text }}</a> (external)<br>
    {% endif %}
    {% endfor %}
    </p>
    </td>
  </tr>
</table>

{% comment %}
connected_to v0.4.2
{% endcomment %}
