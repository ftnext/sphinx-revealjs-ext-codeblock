import pytest


@pytest.mark.sphinx("revealjs", testroot="default")
def test_normal_code_block(app):
    app.build()

    assert (app.outdir / "index.html").exists()
