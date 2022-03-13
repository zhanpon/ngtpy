import pytest

import ngtpy


def new_index(path, dimension):
    path_str = str(path)
    ngtpy.create(path_str, dimension)
    return ngtpy.Index(path_str)


def test_insert(tmp_path):
    index = new_index(tmp_path, dimension=3)

    v = [2, 3, 5]
    v_id = index.insert(v)

    result = index.get_object(v_id)

    assert result == v


def test_batch_insert(tmp_path):
    index = new_index(tmp_path, dimension=2)

    v0 = [0, -1]
    v1 = [0, 0]
    v2 = [0, 1]
    index.batch_insert([v0, v1, v2])

    result = index.linear_search([0, 0.1], size=3)
    result_ids = [i for i, _ in result]

    assert result_ids == [1, 2, 0]
