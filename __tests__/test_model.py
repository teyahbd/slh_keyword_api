import pytest
from model.model import find_keywords

# find_keywords() functionality testing:

def test_returns_list():
    liked_keywords = ["king", "woman"]
    disliked_keywords = ["man"]
    assert type(find_keywords(liked_keywords, disliked_keywords)) is list

def test_returns_two_results():
    liked_keywords = ["king", "woman"]
    disliked_keywords = ["man"]
    assert len(find_keywords(liked_keywords, disliked_keywords)) == 2


def test_returns_list_of_tuples():
    liked_keywords = ["king", "woman"]
    disliked_keywords = ["man"]
    output = find_keywords(liked_keywords, disliked_keywords)
    for i in output:
        assert type(i) is tuple

def test_returns_list_of_correctly_formatted_tuples():
    liked_keywords = ["king", "woman"]
    disliked_keywords = ["man"]
    output = find_keywords(liked_keywords, disliked_keywords)
    for i in output:
        assert type(i[0]) is str
        assert type(i[1]) is float

def test_returns_correct_result():
    liked_keywords = ["king", "woman"]
    disliked_keywords = ["man"]
    expected_result = [("queen", 0.8523604273796082), ("throne", 0.7664334177970886)]
    assert find_keywords(liked_keywords, disliked_keywords) == expected_result

# find_keywords() error handling testing:

def test_raises_error_all_missing_args():
    with pytest.raises(TypeError):
      find_keywords()

def test_raises__error_one_missing_arg():
    liked_keywords = ["heart"]
    with pytest.raises(TypeError):
      find_keywords(liked_keywords)

def test_raises_error_empty_arrays():
    with pytest.raises(ValueError):
      find_keywords([],[])

def test_raises_error_unknown_word():
    liked_keywords = ["heart"]
    unknown_keyword = ["mansjk"]
    with pytest.raises(KeyError):
        find_keywords(liked_keywords, unknown_keyword)
