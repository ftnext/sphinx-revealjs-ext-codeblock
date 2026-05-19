# SPDX-FileCopyrightText: 2025-present ftnext <takuyafjp+develop@gmail.com>
#
# SPDX-License-Identifier: MIT
from docutils.nodes import literal_block, section
from sphinx.util.typing import ExtensionMetadata
from sphinxcontrib.kasane import TranslatorSetUp
from sphinxcontrib.kasane.conditions import BuilderNameCondition
from sphinxcontrib.kasane.inheritance import MixinDynamicInheritance

from sphinx_revealjs_ext_codeblock.__about__ import __version__


class ExtendedLiteralRevealjsSlideTranslatorMixin:
    def visit_literal_block(self, node: literal_block):
        lang = node["language"]
        # add section id as data-id if it is exists
        if "data-id" in node:
            self.body.append(f"<pre data-id=\"{node['data-id']}\">")
        elif isinstance(node.parent, section) and len(node.parent["ids"]):
            self.body.append(f"<pre data-id=\"{node.parent['ids'][0]}\">")
        else:
            self.body.append("<pre>")
        self.body.append(f'<code data-trim data-noescape class="{lang}"')
        highlight_args = node.get("highlight_args", {})
        line_numbers_emitted = False
        # Map standard Sphinx code options to reveal.js line number attributes.
        if "data-line-numbers" in node:
            self.body.append(f" data-line-numbers=\"{node['data-line-numbers']}\"")
            line_numbers_emitted = True
        elif "hl_lines" in highlight_args:
            highlight_lines = ",".join(str(num) for num in highlight_args["hl_lines"])
            self.body.append(f' data-line-numbers="{highlight_lines}"')
            line_numbers_emitted = True
        elif node["linenos"]:
            self.body.append(" data-line-numbers")
            line_numbers_emitted = True
        if "data-ln-start-from" in node:
            lineno_start = node["data-ln-start-from"]
            self.body.append(f' data-ln-start-from="{lineno_start}"')
            if not line_numbers_emitted:
                self.body.append(" data-line-numbers")
        else:
            lineno_start = highlight_args.get("linenostart")
            if lineno_start is not None and node["linenos"]:
                self.body.append(f' data-ln-start-from="{lineno_start}"')
        self.body.append(">")


def setup(app) -> ExtensionMetadata:
    condition = BuilderNameCondition("revealjs")
    inheritance = MixinDynamicInheritance(
        ExtendedLiteralRevealjsSlideTranslatorMixin,
        "ExtendedLiteralRevealjsSlideTranslator",
    )
    app.connect("builder-inited", TranslatorSetUp(inheritance, condition))

    return ExtensionMetadata(version=__version__)
