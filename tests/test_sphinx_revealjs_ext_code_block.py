import pytest
from bs4 import BeautifulSoup


@pytest.mark.sphinx("revealjs", testroot="default")
def test_normal_code_block(app):
    app.build()

    slide_contents = (app.outdir / "index.html").read_text()
    soup = BeautifulSoup(slide_contents, "html.parser")
    pre_tags = soup.find_all("pre")
    assert len(pre_tags) == 1
    pre_tag = pre_tags[0]
    pre_attrs = pre_tag.attrs
    assert pre_attrs["data-id"] == "code-block"
    code_tag = pre_tag.code
    code_attrs = code_tag.attrs
    assert "data-trim" in code_attrs
    assert "data-noescape" in code_attrs
    assert "python" in code_attrs["class"]
