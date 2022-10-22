""" trigger/02000055_bf/bossspawn.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[14]):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=12, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=13, visible=False, enabled=False, minimapVisible=False)
        create_monster(spawnIds=[91], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[91]):
            return 종료체크()

    def on_exit(self):
        destroy_monster(spawnIds=[91])


class 종료체크(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=12, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=13, visible=True, enabled=True, minimapVisible=True)

