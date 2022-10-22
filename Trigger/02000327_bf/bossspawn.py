""" trigger/02000327_bf/bossspawn.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[99], arg2=False) # arg2="0" 을 넣으면 보스 등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99]):
            return 종료체크()


class 종료체크(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[99])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        dungeon_clear()
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


