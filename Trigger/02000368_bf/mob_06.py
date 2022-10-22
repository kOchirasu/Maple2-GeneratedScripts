""" trigger/02000368_bf/mob_06.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1001]):
            return 전투01()
        if user_detected(boxIds=[1002]):
            return 전투01()


class 전투01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[601,611], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[601,611]):
            return 전투02()


class 전투02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[602], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[602]):
            return 종료()


class 종료(state.State):
    pass


