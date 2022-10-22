""" trigger/02000311_bf/ai.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_user_value(triggerId=9999993, key='Buff_01', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='Phase_02', value=1):
            return Phase_02()


class Phase_02(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_2001')
        move_npc(spawnId=202, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Phase_02_b()


class Phase_02_b(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=201, script='$02000311_BF__AI__0$', arg4=2, arg5=2)
        set_conversation(type=1, spawnId=202, script='$02000311_BF__AI__1$', arg4=2, arg5=0)
        set_skill(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Phase_02_c()


class Phase_02_c(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20003111, textId=20003111, duration=5000)
        set_effect(triggerIds=[7001], visible=True)
        set_effect(triggerIds=[7002], visible=True)
        set_user_value(triggerId=9999994, key='Buff_01', value=1)
        set_user_value(triggerId=9999995, key='Buff_02', value=1)


