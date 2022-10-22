""" trigger/02000177_bf/wait.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if dungeon_max_user_count(value=4):
            return MaxCount04_Wait01()
        if dungeon_max_user_count(value=3):
            return MaxCount03_Wait01()
        if dungeon_max_user_count(value=2):
            return MaxCount02_Wait01()
        if dungeon_max_user_count(value=1):
            return MaxCount01_Wait01()


#  던전 최대 인원수가 4이면 
class MaxCount04_Wait01(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=4):
            return state.DungeonStart()
        if wait_tick(waitTick=1000):
            return MaxCount04_Wait02()


class MaxCount04_Wait02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=40012, textId=40012, duration=4000)

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=4):
            return state.DungeonStart()
        if wait_tick(waitTick=5000):
            return MaxCount04_Wait03()


class MaxCount04_Wait03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=40012, textId=40012, duration=4000)

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=4):
            return state.DungeonStart()
        if wait_tick(waitTick=5000):
            return MaxCount04_Wait04()


class MaxCount04_Wait04(state.State):
    def on_enter(self):
        show_guide_summary(entityId=40012, textId=40012, duration=4000)

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=4):
            return state.DungeonStart()
        if wait_tick(waitTick=5000):
            return state.DungeonStart()


#  던전 최대 인원수가 3이면 
class MaxCount03_Wait01(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=3):
            return state.DungeonStart()
        if wait_tick(waitTick=1000):
            return MaxCount03_Wait02()


class MaxCount03_Wait02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=40012, textId=40012, duration=4000)

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=3):
            return state.DungeonStart()
        if wait_tick(waitTick=5000):
            return MaxCount03_Wait03()


class MaxCount03_Wait03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=40012, textId=40012, duration=4000)

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=3):
            return state.DungeonStart()
        if wait_tick(waitTick=5000):
            return MaxCount03_Wait04()


class MaxCount03_Wait04(state.State):
    def on_enter(self):
        show_guide_summary(entityId=40012, textId=40012, duration=4000)

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=3):
            return state.DungeonStart()
        if wait_tick(waitTick=5000):
            return state.DungeonStart()


#  던전 최대 인원수가 2이면 
class MaxCount02_Wait01(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=2):
            return state.DungeonStart()
        if wait_tick(waitTick=1000):
            return MaxCount02_Wait02()


class MaxCount02_Wait02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=40012, textId=40012, duration=4000)

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=2):
            return state.DungeonStart()
        if wait_tick(waitTick=5000):
            return MaxCount02_Wait03()


class MaxCount02_Wait03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=40012, textId=40012, duration=4000)

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=2):
            return state.DungeonStart()
        if wait_tick(waitTick=5000):
            return MaxCount02_Wait04()


class MaxCount02_Wait04(state.State):
    def on_enter(self):
        show_guide_summary(entityId=40012, textId=40012, duration=4000)

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=2):
            return state.DungeonStart()
        if wait_tick(waitTick=5000):
            return state.DungeonStart()


#  던전 최대 인원수가 1이면 바로 시작
class MaxCount01_Wait01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return state.DungeonStart()


