""" trigger/02010054_bf/spawn_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000884], state=2)
        set_effect(triggerIds=[610], visible=False)
        set_mesh(triggerIds=[3127], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[105]):
            return 몬스터생성()


class 몬스터생성(state.State):
    def on_enter(self):
        set_effect(triggerIds=[610], visible=True)
        create_monster(spawnIds=[2022], arg2=False)
        set_mesh(triggerIds=[3127], visible=False, arg3=0, arg4=0, arg5=5)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2022]):
            set_interact_object(triggerIds=[10000884], state=1)
            return 종료()


class 종료(state.State):
    pass


