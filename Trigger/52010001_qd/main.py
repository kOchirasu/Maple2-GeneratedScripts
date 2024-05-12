""" trigger/52010001_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000871], state=1)
        self.set_interact_object(triggerIds=[10000910], state=1)
        self.set_actor(triggerId=1001, visible=True, initialSequence='Down_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000871,10000910], stateValue=0):
            return Event_02(self.ctx)

    def on_exit(self) -> None:
        self.set_achievement(triggerId=701, type='trigger', achieve='Firepotoff')
        # Firepotoff


class Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=1001, visible=False, initialSequence='Down_Idle_A')
        self.create_monster(spawnIds=[101], animationEffect=False) # 노인 생성
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1001')
        self.set_conversation(type=1, spawnId=101, script='$52010001_QD__MAIN__0$', arg4=3, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=702, spawnIds=[101]):
            return Event_03(self.ctx)


class Event_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=101, script='$52010001_QD__MAIN__1$', arg4=3, arg5=0)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1002')
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return Event_04(self.ctx)


class Event_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=101, script='$52010001_QD__MAIN__2$', arg4=3, arg5=0)
        self.set_interact_object(triggerIds=[10000871], state=1)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=703, spawnIds=[101]):
            return Event_04_02(self.ctx)


class Event_04_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return Event_05(self.ctx)


class Event_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1004')
        self.set_conversation(type=1, spawnId=101, script='$52010001_QD__MAIN__3$', arg4=3, arg5=0)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return Event_06(self.ctx)


class Event_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=101, script='$52010001_QD__MAIN__4$', arg4=3, arg5=3)
        self.set_interact_object(triggerIds=[10000910], state=1)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1005')
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=704, spawnIds=[101]):
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=1001, visible=True, initialSequence='Down_Idle_A')
        self.destroy_monster(spawnIds=[101])


initial_state = idle
