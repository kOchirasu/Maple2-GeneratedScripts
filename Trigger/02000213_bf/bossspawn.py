""" trigger/02000213_bf/bossspawn.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10000259,10000260,10000261], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000259,10000260,10000261], arg2=2):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1099])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1099]):
            return 종료체크()

    def on_exit(self):
        destroy_monster(spawnIds=[1099])


class 종료체크(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True)


