from algorithmic_toolbox import __version__, max_pairwise_product

def test_version():
    assert __version__ == "0.1.0"

def test_max_pairwise_product():
    assert max_pairwise_product("4 7 1 9") == 63
    assert max_pairwise_product("18 3 4 1 9") == 162