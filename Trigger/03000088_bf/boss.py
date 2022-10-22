""" trigger/03000088_bf/boss.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[11000009], state=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            create_monster(spawnIds=[2001], arg2=False)
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        show_guide_summary(entityId=23000001, textId=23000001, duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 보스등장()
        if monster_dead(boxIds=[2001]):
            hide_guide_summary(entityId=23000001)
            set_interact_object(triggerIds=[11000009], state=1)
            set_event_ui(type=7, arg3='2000', arg4='0')
            return 종료()


class 종료(state.State):
    pass


