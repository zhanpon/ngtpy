import pytest

import ngtpy


def new_index(path, dimension):
    path_str = str(path)
    index = ngtpy.create(path_str, dimension)
    return ngtpy.Index(path_str)


def test_insert(tmp_path):
    index = new_index(tmp_path, dimension=3)

    v = [2, 3, 5]
    v_id = index.insert(v)

    result = index.get_object(v_id)

    assert result == v
