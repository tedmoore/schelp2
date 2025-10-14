{% import 'partials/scdoc_node_macros.jinja' as macros %}
{#- 
  Main template for rendering SCDoc parse tree from scdoc_to_json.py
  The input is a node-based structure with id, text, and children properties
-#}

{% if doc.id == "DOCUMENT" %}
{{ macros.render_node(doc) }}
{% else %}
{#- If not a document, render as-is -#}
{{ macros.render_node(doc) }}
{% endif %}
