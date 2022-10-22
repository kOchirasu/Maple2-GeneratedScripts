""" trigger/63000038_cs/guide_mob.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[2101]):
            return 가이드출력()
        if monster_in_combat(boxIds=[2102]):
            return 가이드출력()


class 가이드출력(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26300383, textId=26300383)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 가이드삭제대기()


class 가이드삭제대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 가이드삭제()


class 가이드삭제(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2103]):
            hide_guide_summary(entityId=26300383)
            return 종료()


class 종료(state.State):
    pass


