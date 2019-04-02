#!/bin/python

import json
from yahoo_fantasy_api import game, league
import os

# For testing, we don't call out to Yahoo!  We just use a sample json file.
# For that reason the OAuth2 session context can be None.
TEST_SESSION_CONTEXT = None


def league_teams_gen(sc):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/sample.league_teams.json", "r") as f:
        return json.load(f)


def test_ids():
    gm = game.Game(TEST_SESSION_CONTEXT, 'mlb')
    ids = gm.league_ids(data_gen=league_teams_gen)
    for i in ids:
        print(i)
    assert(len(ids) == 12)
    print(ids)
    assert(ids[5] == '268.l.46645')


def test_ids_for_year():
    gm = game.Game(TEST_SESSION_CONTEXT, 'mlb')
    ids = gm.league_ids(year=2017, data_gen=league_teams_gen)
    assert(len(ids) == 1)
    print(ids)
    assert(ids[0] == '370.l.56877')


def test_team_key():
    lg = league.League(TEST_SESSION_CONTEXT, '370.l.56877')
    k = lg.team_key(data_gen=league_teams_gen)
    print(k)
    assert(k == '370.l.56877.t.5')


def test_to_league():
    gm = game.Game(TEST_SESSION_CONTEXT, 'mlb')
    lg = gm.to_league('370.l.56877')
    assert(type(lg) is league.League)
