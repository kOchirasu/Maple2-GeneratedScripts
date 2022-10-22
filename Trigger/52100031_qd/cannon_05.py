""" trigger/52100031_qd/cannon_05.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[695], visible=False)
        set_mesh(triggerIds=[3905], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_value(key='cannon05', value=1):
            return 생성()


class 생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2905], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2905]):
            set_effect(triggerIds=[695], visible=True)
            set_mesh(triggerIds=[3905], visible=False, arg3=0, arg4=0, arg5=5)
            return 종료()


class 종료(state.State):
    pass


