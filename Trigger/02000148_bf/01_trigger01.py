""" trigger/02000148_bf/01_trigger01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000109], state=1)
        set_effect(triggerIds=[201,202,203,204], visible=False)
        set_mesh(triggerIds=[325,326,303,304], visible=True)
        set_mesh(triggerIds=[305,306,307,308], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000109], arg2=0):
            return 개봉박두()


class 개봉박두(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[325,326,303,304], visible=False)
        create_monster(spawnIds=[91,92,93,94], arg2=True)
        set_mesh(triggerIds=[305,306,307,308], visible=True)
        set_effect(triggerIds=[201,202,203,204], visible=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[91,92,93,94]):
            return 유저감지()


class 유저감지(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[401]):
            return 대기()


