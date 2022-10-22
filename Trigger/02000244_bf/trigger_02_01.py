""" trigger/02000244_bf/trigger_02_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[703,704], visible=True)
        destroy_monster(spawnIds=[622,623,624,625,626,627,628,629,630])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[202]):
            return 몹생성()


class 몹생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[622,623,624,625,626,627,628,629,630], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[622,623,624,625,626,627,628,629,630]):
            return 통과()
        if object_interacted(interactIds=[10000302], arg2=0):
            return 통과()


class 통과(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[703,704], visible=False)
        set_timer(timerId='1', seconds=180)


