# {{ doc.metadata.title }}

{% if doc.metadata.summary %}
> {{ macros.render_inline(doc.metadata.summary) }}
{% endif %}

{% if doc.metadata.categories %}
**Categories:** {{ doc.metadata.categories | join(', ') }}
{% endif %}

{% if doc.metadata.related %}
**Related:** {% for item in doc.metadata.related %}{{ macros.render_inline([item]) }}{% if not loop.last %}, {% endif %}{% endfor %}
{% endif %}


{% if doc.metadata.description %}
**Description:** {{ macros.render_inline(doc.metadata.description) }}
{% endif %}
