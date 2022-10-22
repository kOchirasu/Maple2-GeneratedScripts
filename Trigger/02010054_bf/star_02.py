""" trigger/02010054_bf/star_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000860], state=2)
        set_effect(triggerIds=[605], visible=False)
        set_mesh(triggerIds=[3306,3307,3308,3309], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3125], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 생성()


class 생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3306,3307,3308,3309], visible=True, arg3=0, arg4=500, arg5=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 몬스터생성()


class 몬스터생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3306,3307,3308,3309], visible=False, arg3=0, arg4=900, arg5=3)
        set_mesh(triggerIds=[3125], visible=False, arg3=0, arg4=0, arg5=5)
        set_effect(triggerIds=[605], visible=True)
        create_monster(spawnIds=[2004], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2004]):
            set_interact_object(triggerIds=[10000860], state=1)
            return 종료()


class 종료(state.State):
    pass


