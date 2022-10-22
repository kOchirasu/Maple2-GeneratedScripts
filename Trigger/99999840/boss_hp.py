""" trigger/99999840/boss_hp.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if dungeon_variable(varID='100', value=1):
            return 시작()


class 시작(state.State):
    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=70, spawnId=901, isRelative=True):
            return 프로70()


class 프로70(state.State):
    def on_enter(self):
        dungeon_variable(varId=110, value=1)

    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=50, spawnId=901, isRelative=True):
            return 프로50()


class 프로50(state.State):
    def on_enter(self):
        dungeon_variable(varId=120, value=1)

    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=30, spawnId=901, isRelative=True):
            return 프로30()


class 프로30(state.State):
    def on_enter(self):
        dungeon_variable(varId=130, value=1)

    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=10, spawnId=901, isRelative=True):
            return 프로10()


class 프로10(state.State):
    def on_enter(self):
        dungeon_variable(varId=140, value=1)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    pass


