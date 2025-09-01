from datetime import datetime as dt

current_year = dt.now().year

# List of family names
family = [
    "Hugo Crispin", "Sharah Crispin", "Carmen Briscoe", "Junior Griffiths",
    "Ivorine Clarke", "Leslie Griffiths", "Steadlyn Briscoe","Novia Joyce McLean",
    "Martha Hall", "Samuel Briscoe", "Vivian McLean", "Myrtle Williams", 
    "Mazie Poole", "Herbert Clarke", "Alfred Griffiths", "Alice May Robinson"
    ]

ancestors = {
    "Hugo Crispin": 2021,
    "Sharah Crispin": 1988,
    "Carmen Briscoe": 1968,
    "Junior Griffiths": 1957,
    "Ivorine Clarke": 1940,
    "Leslie Griffiths": "unknown",
    "Steadlyn Briscoe": 1941,
    "Novia Joyce McLean": 1945,
    "Martha Hall": 1900,
    "Samuel Briscoe": 1884,
    "Vivian McLean": 1916,
    "Myrtle Williams": 1919,
    "Mazie Poole": 1919,
    "Herbert Clarke": 1912,
    "Alfred Griffiths": 1903,
    "Alice May Robinson": 1910 
}

# print(len(ancestors))
# print(ancestors)

def oldest_ancestor(data: dict[str, int]) -> tuple[str, int]:
    return min (data.items(), key=lambda kv: kv[1])

def sort_by_birth_year(data: dict[str, int]):
    return sorted(data.items(), key=lambda kv: kv[1])

def age_in_years(birth_year: int = ancestors.values(), year: int = current_year) -> int:
    return year - birth_year

if __name__ == "__main__":
    print(f"Youngest Relative: {family[0]}  Oldest Relative: {family[-1]}")
    ages = {n: age_in_years(y) for n, y in ancestors.items()}
    for n, a in ages.items():
        print(f"{n}: {a}")
    name, by = oldest_ancestor(ancestors)
    print(f"Oldest: {name} (b. {by})")
    print("Oldest → Youngest:")
    for n, y in sort_by_birth_year(ancestors):
        print(f"{n} — {y}")
