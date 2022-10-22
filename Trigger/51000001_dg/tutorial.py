""" trigger/51000001_dg/tutorial.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            return 몬스터소환()


class 몬스터소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1000], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1000]):
            return 대기시간()
        if not user_detected(boxIds=[100]):
            return 종료()


class 대기시간(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대기()
        if not user_detected(boxIds=[100]):
            return 종료()


class 종료(state.State):
    pass


