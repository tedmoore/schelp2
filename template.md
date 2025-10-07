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

---

{% macro render_inline(inline_content) -%}
{%- for item in inline_content -%}
{%- if item.type == 'text' -%}
{{ item.content }}
{%- elif item.type == 'link' -%}
[{{ item.text }}](#{{ item.target | replace('Classes/', '') | replace('/', '-') }})
{%- elif item.type == 'inline_code' -%}
`{{ item.content }}`
{%- elif item.type == 'emphasis' -%}
*{{ item.content }}*
{%- elif item.type == 'strong' -%}
**{{ item.content }}**
{%- endif -%}
{%- endfor -%}
{%- endmacro %}

{% macro render_content(content_list) %}
{%- for item in content_list -%}

{%- if item.type == 'paragraph' -%}
{{ render_inline(item.content) }}

{%- elif item.type == 'code_block' -%}
```
{{ item.content }}
```

{%- elif item.type == 'section' -%}
## {{ item.title }}

{{ render_content(item.content) }}

{%- elif item.type == 'subsection' -%}
### {{ item.title }}

{{ render_content(item.content) }}

{%- elif item.type == 'method' -%}
### `{{ item.name }}`

{%- if item.arguments %}

**Arguments:**

| Argument | Description |
|----------|-------------|
{%- for arg in item.arguments %}
| `{{ arg.name }}` | {% for desc in arg.description %}{{ render_inline(desc) }}{% endfor %} |
{%- endfor %}
{%- endif %}

{%- if item.returns %}

**Returns:** {% for ret in item.returns %}{{ render_inline(ret) }}{% endfor %}
{%- endif %}

{%- if item.content %}
{{ render_content(item.content) }}
{%- endif %}

{%- elif item.type == 'argument' -%}
- `{{ item.name }}` - {{ render_content(item.content) }}

{%- elif item.type == 'admonition' -%}
{% if item.admonition_type == 'note' %}
> **Note:** {{ render_content(item.content) }}
{% elif item.admonition_type == 'warning' %}
> **⚠️ Warning:** {{ render_content(item.content) }}
{% endif %}

{%- elif item.type == 'definition_list' -%}
{%- for def_item in item['items'] %}
- **{{ render_inline(def_item.term) }}** - {{ render_inline(def_item.definition) }}
{%- endfor %}

{%- elif item.type == 'list' or item.type == 'numbered_list' -%}
{%- for list_item in item['items'] %}
{% if item.type == 'numbered_list' %}{{ loop.index }}.{% else %}-{% endif %} {{ render_inline(list_item) }}
{%- endfor %}

{%- elif item.type == 'list_item' -%}
- {{ render_inline(item.content) }}

{%- elif item.type == 'image' -%}
![{{ item.caption }}]({{ item.path }})
{% if item.caption %}*{{ item.caption }}*{% endif %}

{%- elif item.type == 'blank_line' -%}

{%- endif -%}

{%- endfor -%}
{%- endmacro %}

{% for block in doc.content %}
{{ render_content([block]) }}
{% endfor %}

---

*Generated from SuperCollider documentation*
