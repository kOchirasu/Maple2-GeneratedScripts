""" trigger/02000553_bf/main.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 기본셋팅()


class 기본셋팅(state.State):
    def on_enter(self):
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False) # 나가기 포탈 최초에는 감추기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False) # arg2="0" 을 넣으면 보스 등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 클리어처리()


class 클리어처리(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 종료처리()


class 종료처리(state.State):
    def on_enter(self):
        dungeon_clear()
        destroy_monster(spawnIds=[-1])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=True) # 나가기 포탈 등장


