""" trigger/03000039_bf/elite.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[11000008], state=2)
        set_interact_object(triggerIds=[11000009], state=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            create_monster(spawnIds=[1001,1002,1003], arg2=False)
            return 엘리트등장()


class 엘리트등장(state.State):
    def on_enter(self):
        show_guide_summary(entityId=23000002, textId=23000002, duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 엘리트등장()
        if monster_dead(boxIds=[1001,1002,1003]):
            hide_guide_summary(entityId=23000002)
            set_event_ui(type=7, arg3='2000', arg4='0')
            return 상자확률()


class 상자확률(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=90):
            set_interact_object(triggerIds=[11000008], state=1)
            return 종료()
        if random_condition(rate=10):
            set_interact_object(triggerIds=[11000009], state=1)
            return 종료()


class 종료(state.State):
    pass


