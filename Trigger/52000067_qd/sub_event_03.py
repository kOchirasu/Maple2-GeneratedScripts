""" trigger/52000067_qd/sub_event_03.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[591,592], animationEffect=True) # 시민

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=705, boxId=1):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[537,538,539], animationEffect=True) # 몬스터
        self.set_npc_emotion_loop(spawnId=591, sequenceName='Emotion_Failure_Idle_A', duration=600000)
        self.set_npc_emotion_loop(spawnId=592, sequenceName='Emotion_Failure_Idle_A', duration=600000)
        self.set_conversation(type=1, spawnId=591, script='$52000067_QD__SUB_EVENT_03__0$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=592, script='$52000067_QD__SUB_EVENT_03__1$', arg4=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[537,538,539]):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=591, sequenceName='Talk_A')
        self.set_npc_emotion_sequence(spawnId=592, sequenceName='Idle_A')
        self.set_conversation(type=1, spawnId=591, script='$52000067_QD__SUB_EVENT_03__2$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return ending(self.ctx)


class ending(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=591, patrolName='MS2PatrolData_5010')
        self.move_npc(spawnId=592, patrolName='MS2PatrolData_5010')


initial_state = idle
