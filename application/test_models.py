import pytest, sys
from .models import Team

@pytest.fixture
def team_test_data():
  return Team("Luton", "England", 1)


def test_init(team_test_data):
  team = team_test_data
  assert isinstance(team, Team)
  assert team.name == "Luton"

def test_repr(team_test_data, capsys):
  team = team_test_data
  print(team.__repr__())
  out, err = capsys.readouterr()
  sys.stdout.write(out)
  assert "Luton" in out
  assert out == "Team(id: None, name: Luton)\n"

def test_json_prop(team_test_data, capsys):
  team = team_test_data
  print(team.json)
  out, err = capsys.readouterr()
  sys.stdout.write(out)
  assert "Luton" in out
  assert out == "{'id': None, 'name': 'Luton', 'nation': 'England', 'tier': 1}\n"