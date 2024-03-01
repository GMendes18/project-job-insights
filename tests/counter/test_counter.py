from src.pre_built.counter import count_ocurrences


def test_counter():

    path = "data/jobs.csv"
    javascript_counter = count_ocurrences(path, "javascript")
    assert javascript_counter == 122

    python_counter = count_ocurrences(path, "python")
    assert python_counter == 1639
