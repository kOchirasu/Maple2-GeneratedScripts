""" trigger/02000244_bf/trigger_01_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[701,702], visible=True)
        set_mesh(triggerIds=[709,710], visible=True)
        destroy_monster(spawnIds=[631,632,633,634,635,636,637,638,639])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[201]):
            return 몹생성()


class 몹생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[631,632,633,634,635,636,637,638,639], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[631,632,633,634,635,636,637,638,639]):
            return 통과()
        if object_interacted(interactIds=[10000303], arg2=0):
            return 통과()


class 통과(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[701,702], visible=False)
        set_mesh(triggerIds=[709,710], visible=False)
        set_timer(timerId='1', seconds=180)


