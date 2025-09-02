import pytest
from main import age_in_years, oldest_ancestor, sort_by_birth_year #Import the functions

def test_age_calc():
    """Test if age calculation works"""
    assert age_in_years(1988, 2025) == 37
    assert age_in_years(2021, 2025) == 4


def test_oldest_ancestors():
    """Test for finding the oldest person, based on birth year"""
    test_data = {
        "Jason": 1987,
        "Hugo": 2021,
        "Sharah": 1988
    }

    name, year = oldest_ancestor(test_data)
    assert name == "Jason"
    assert year == 1987


def test_sort_by_birth_year():
    """Sorting family from oldest to youngest"""
    test_data = {
        "Ivorine Clarke": 1940,
        "Novia Joyce McLean": 1945,
        "Hugo Crispin": 2021
    }

    sorted_results = sort_by_birth_year(test_data)

    assert sorted_results[0][0] == "Ivorine Clarke"
    assert sorted_results[0][1] == 1940

    assert sorted_results[-1][0] == "Hugo Crispin"
    assert sorted_results[-1][1] == 2021


def test_handles_zero_birth_year():
    """Test what happens with Leslie Griffiths who has 0 as birth year"""
    test_data = {"Leslie": 0, "Jason": 1987}
    name, year = oldest_ancestor(test_data)
    assert name == "Leslie"
    assert year == 0