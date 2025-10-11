# {{ doc.metadata.title }}

{% if doc.metadata.summary %}
> {{ doc.metadata.summary }}
{% endif %}

{% if doc.metadata.categories %}
**Categories:** {{ doc.metadata.categories | join(', ') }}
{% endif %}

{% if doc.metadata.related %}
**Related:** {% for item in doc.metadata.related %}[{{ item }}]({{ item }}){% if not loop.last %}, {% endif %}{% endfor %}
{% endif %}

{% if doc.metadata.keywords %}
**Keywords:** {{ doc.metadata.keywords | join(', ') }}
{% endif %}
