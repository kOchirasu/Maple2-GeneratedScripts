""" trigger/02010054_bf/spawn_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000885], state=2)
        set_effect(triggerIds=[611], visible=False)
        set_mesh(triggerIds=[3128], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[106]):
            return 몬스터생성()


class 몬스터생성(state.State):
    def on_enter(self):
        set_effect(triggerIds=[611], visible=True)
        set_mesh(triggerIds=[3128], visible=False, arg3=0, arg4=0, arg5=5)
        create_monster(spawnIds=[2023], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2023]):
            set_interact_object(triggerIds=[10000885], state=1)
            return 종료()


class 종료(state.State):
    pass


