import os
import numpy as np

import pandas as pd

OPPPONENT_MAP = {"A": 1, "B": 2, "C": 3}
LOSS_MAP = {1: 2, 2: 3, 3: 1}


def _rock_paper_scissors(strategy: pd.DataFrame) -> int:
    you_map = {"X": 1, "Y": 2, "Z": 3}
    strategy["opponent_value"] = strategy["opponent"].map(OPPPONENT_MAP)
    strategy["you_value"] = strategy["you"].map(you_map)
    strategy["opponent_loss"] = strategy["opponent_value"].map(LOSS_MAP)
    strategy["score"] = strategy["you_value"]
    strategy["score"] = strategy["score"].where(
        strategy["opponent_value"] != strategy["you_value"], strategy["score"] + 3
    )
    return (
        strategy["score"]
        .where(
            strategy["opponent_loss"] != strategy["you_value"], strategy["score"] + 6
        )
        .sum()
    )


def rock_paper_scissors(input_fp: os.PathLike) -> int:
    strategy = pd.read_csv(input_fp, header=None, names=["opponent", "you"], sep=" ")
    return _rock_paper_scissors(strategy)


def rock_paper_scissors_2(input_fp: os.PathLike) -> int:
    opp_lose = {"A": "Y", "B": "Z", "C": "X"}
    opp_win = {"A": "Z", "B": "X", "C": "Y"}
    opp_draw = {"A": "X", "B": "Y", "C": "Z"}
    strategy = pd.read_csv(input_fp, header=None, names=["opponent", "you"], sep=" ")
    strategy["opp_draw"] = strategy["opponent"].map(opp_draw)
    strategy["opp_win"] = strategy["opponent"].map(opp_win)
    strategy["opp_lose"] = strategy["opponent"].map(opp_lose)
    strategy["new_strat"] = np.where(strategy["you"] == "Y", strategy["opp_draw"], None)
    strategy["new_strat"] = np.where(
        strategy["you"] == "X", strategy["opp_win"], strategy["new_strat"]
    )
    strategy["new_strat"] = np.where(
        strategy["you"] == "Z", strategy["opp_lose"], strategy["new_strat"]
    )
    return _rock_paper_scissors(
        strategy.drop("you", axis=1).rename({"new_strat": "you"}, axis=1)
    )
