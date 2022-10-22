""" trigger/99999907/12000012.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000012], state=2)

    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return 반응대기()
        if random_condition(rate=50):
            return 종료()


class 반응대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000012], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000012], arg2=0):
            return 랜덤버프()


class 랜덤버프(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            add_buff(boxIds=[199], skillId=70000008, level=1, arg4=False, arg5=False)
            return 종료()
        if random_condition(rate=30):
            add_buff(boxIds=[199], skillId=70000008, level=1, arg4=False, arg5=False)
            return 종료()
        if random_condition(rate=40):
            add_buff(boxIds=[199], skillId=70000008, level=1, arg4=False, arg5=False)
            return 종료()


class 종료(state.State):
    pass


