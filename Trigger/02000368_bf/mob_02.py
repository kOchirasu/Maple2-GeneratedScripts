""" trigger/02000368_bf/mob_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3002], visible=False, arg3=0, arg4=0, arg5=0)
        set_skill(triggerIds=[7201], isEnable=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1001]):
            return 전투01()
        if user_detected(boxIds=[1002]):
            return 전투01()


class 전투01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201,211], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,211]):
            return 전투02()


class 전투02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3002], visible=True, arg3=0, arg4=0, arg5=0)
        set_skill(triggerIds=[7201], isEnable=True)
        create_monster(spawnIds=[202], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[202]):
            return 종료()


class 종료(state.State):
    pass


