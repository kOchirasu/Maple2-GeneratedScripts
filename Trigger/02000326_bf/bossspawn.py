""" trigger/02000326_bf/bossspawn.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1099])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1099]):
            return 종료딜레이()


class 종료딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            dungeon_clear()
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_achievement(triggerId=99999, type='trigger', achieve='ClearDeborak') # ClearDeborak 퀘스트
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True)


