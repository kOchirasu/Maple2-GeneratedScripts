""" trigger/52010001_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000871], state=1)
        set_interact_object(triggerIds=[10000910], state=1)
        set_actor(triggerId=1001, visible=True, initialSequence='Down_Idle_A')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000871,10000910], arg2=0):
            return Event_02()

    def on_exit(self):
        set_achievement(triggerId=701, type='trigger', achieve='Firepotoff') # Firepotoff


class Event_02(state.State):
    def on_enter(self):
        set_actor(triggerId=1001, visible=False, initialSequence='Down_Idle_A')
        create_monster(spawnIds=[101], arg2=False) # 노인 생성
        move_npc(spawnId=101, patrolName='MS2PatrolData_1001')
        set_conversation(type=1, spawnId=101, script='$52010001_QD__MAIN__0$', arg4=3, arg5=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=702, spawnIds=[101]):
            return Event_03()


class Event_03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$52010001_QD__MAIN__1$', arg4=3, arg5=0)
        move_npc(spawnId=101, patrolName='MS2PatrolData_1002')
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_04()


class Event_04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$52010001_QD__MAIN__2$', arg4=3, arg5=0)
        set_interact_object(triggerIds=[10000871], state=1)
        move_npc(spawnId=101, patrolName='MS2PatrolData_1003')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=703, spawnIds=[101]):
            return Event_04_02()


class Event_04_02(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return Event_05()


class Event_05(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_1004')
        set_conversation(type=1, spawnId=101, script='$52010001_QD__MAIN__3$', arg4=3, arg5=0)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_06()


class Event_06(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$52010001_QD__MAIN__4$', arg4=3, arg5=3)
        set_interact_object(triggerIds=[10000910], state=1)
        move_npc(spawnId=101, patrolName='MS2PatrolData_1005')
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=704, spawnIds=[101]):
            return End()


class End(state.State):
    def on_enter(self):
        set_actor(triggerId=1001, visible=True, initialSequence='Down_Idle_A')
        destroy_monster(spawnIds=[101])


