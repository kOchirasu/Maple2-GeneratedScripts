""" trigger/02000242_bf/trigger_04_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[707,708], visible=True)
        destroy_monster(spawnIds=[607,608])


class 차웨이브1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[607,608], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[607,608]):
            return 차딜레이1()


class 차딜레이1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 차웨이브2()


class 차웨이브2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[607,608], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[607,608]):
            return 차딜레이2()


class 차딜레이2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 차웨이브3()


class 차웨이브3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[607,608], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[607,608]):
            return 차딜레이3()


class 차딜레이3(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=180)


