{% for block in doc.content %}
{{ macros.render_content([block]) }}
{% endfor %}
