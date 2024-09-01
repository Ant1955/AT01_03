import pytest

from main_at02 import vowels

@pytest.mark.parametrize("s, expected", [
   ("hello from Cicago", 6),
   ("привет из Сочи", 5),
   ("и вот так possible", 6),
   ("", 0),
])
def test_count_vowels(s, expected):
   assert vowels(s) == expected

