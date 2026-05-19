# sphinx-revealjs-ext-codeblock

[![PyPI - Version](https://img.shields.io/pypi/v/sphinx-revealjs-ext-codeblock.svg)](https://pypi.org/project/sphinx-revealjs-ext-codeblock)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sphinx-revealjs-ext-codeblock.svg)](https://pypi.org/project/sphinx-revealjs-ext-codeblock)

Map standard Sphinx code-block options to reveal.js code attributes for the
Sphinx `revealjs` builder.

It lets authors keep using standard directives such as `code-block`,
`literalinclude`, `:linenos:`, `:lineno-start:`, and `:emphasize-lines:`
instead of switching to reveal.js-specific directives.

-----

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

```console
pip install sphinx-revealjs-ext-codeblock
```

## Usage

conf.py

```python
extensions = [
    "sphinx_revealjs",
    "sphinx_revealjs_ext_codeblock",
]
```

Specify `revealjs_script_plugins` & `revealjs_css_files`.

* https://sphinx-revealjs.readthedocs.io/en/stable/configurations/#confval-revealjs_script_plugins
* https://sphinx-revealjs.readthedocs.io/en/stable/configurations/#confval-revealjs_css_files

### Line Numbers

```rst
.. code-block:: python
    :linenos:

    while True:
        print("Hello world!")
```

```html
<pre>
  <code class="python" data-line-numbers>
while True:
    print(&quot;Hello world!&quot;)
  </code>
</pre>
```

See https://revealjs.com/code/#line-numbers-%26-highlights

### Highlights

```rst
.. code-block:: python
    :emphasize-lines: 2

    while True:
        print("Hello world!")
```

```html
<pre>
  <code class="python" data-line-numbers="2">
while True:
    print(&quot;Hello world!&quot;)
  </code>
</pre>
```

See https://revealjs.com/code/#line-numbers-%26-highlights

### Literalinclude Line Number Start

```rst
.. literalinclude:: example.py
    :language: python
    :lines: 2-3
    :linenos:
    :lineno-start: 1
```

```html
<pre>
  <code class="python" data-line-numbers data-ln-start-from="1">
print(&quot;two&quot;)
print(&quot;three&quot;)
  </code>
</pre>
```

See https://revealjs.com/code/#line-number-offset-4.2.0

### Literalinclude Matched Line Numbers

```rst
.. literalinclude:: example.py
    :language: python
    :lines: 2-3
    :linenos:
    :lineno-match:
```

```html
<pre>
  <code class="python" data-line-numbers data-ln-start-from="2">
print(&quot;two&quot;)
print(&quot;three&quot;)
  </code>
</pre>
```

## License

`sphinx-revealjs-ext-codeblock` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
