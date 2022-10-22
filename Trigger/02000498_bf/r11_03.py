""" trigger/02000498_bf/r11_03.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=103, spawnIds=[111001]):
            return 몹스폰()


class 몹스폰(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111004], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[111001]):
            destroy_monster(spawnIds=[111004])
            return 종료()
        if monster_dead(boxIds=[111004]):
            return 몹스폰()


class 종료(state.State):
    pass


