""" trigger/02000400_bf/99_bossspawn.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if check_user():
            return 룸체크()


class 룸체크(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return 던전시작()
        if not is_dungeon_room():
            return 퀘스트던전시작()


class 던전시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[900,901], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BossBattle01()


class 퀘스트던전시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[910,911], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료체크()


class 종료체크(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[910,911]):
            return QuestClear()


class BossBattle01(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='CheckDualKill', value=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[900,901]):
            return BossBattle02()


class BossBattle02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[900,901])
        set_achievement(triggerId=9900, type='trigger', achieve='Madracan02')
        set_achievement(triggerId=9900, type='trigger', achieve='Madracan_Q02')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class QuestClear(state.State):
    def on_enter(self):
        set_achievement(triggerId=9900, type='trigger', achieve='Madracan_Q02')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        dungeon_clear()
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


