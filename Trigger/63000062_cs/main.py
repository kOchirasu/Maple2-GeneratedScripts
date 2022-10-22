""" trigger/63000062_cs/main.xml """
from common import *
import state


class 날짜체크(state.State):
    def on_tick(self) -> state.State:
        if day_of_week(dayOfWeeks=[4], desc='1(일)-7(토)'):
            return 만남()
        if day_of_week(dayOfWeeks=[1,2,3,5,6,7], desc='1(일)-7(토)'):
            return 헤어짐()


class 만남(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[111,112])
        create_monster(spawnIds=[121,122], arg2=False)

    def on_tick(self) -> state.State:
        if day_of_week(dayOfWeeks=[1,2,3,5,6,7], desc='1(일)-7(토)'):
            return 헤어짐()


class 헤어짐(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[121,122])
        create_monster(spawnIds=[111,112], arg2=False)

    def on_tick(self) -> state.State:
        if day_of_week(dayOfWeeks=[4], desc='1(일)-7(토)'):
            return 만남()


