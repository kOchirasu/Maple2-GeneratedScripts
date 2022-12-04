""" trigger/52000019_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2002], animationEffect=False)
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[603], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[100]):
            return 시작대기(self.ctx)


class 시작대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[100], questIds=[60001012], questStates=[1]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2002])
        self.create_monster(spawnIds=[2001], animationEffect=False)
        self.set_timer(timerId='5', seconds=5)
        self.set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__0$', arg4=5)
        self.move_npc(spawnId=2001, patrolName='MS2PatrolData_2001A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=101, spawnIds=[2001]):
            return 첫번째구덩이도착(self.ctx)


class 첫번째구덩이도착(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[601], visible=True)
        self.set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__1$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 첫번째구덩이(self.ctx)


class 첫번째구덩이(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__2$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 첫번째꿈틀이(self.ctx)


class 첫번째꿈틀이(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__3$', arg4=3)
        self.move_npc(spawnId=2001, patrolName='MS2PatrolData_2001B')
        self.create_monster(spawnIds=[1001], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1001]):
            return 첫번째구덩이완료(self.ctx)


class 첫번째구덩이완료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__4$', arg4=3)
        self.move_npc(spawnId=2001, patrolName='MS2PatrolData_2001C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[2001]):
            return 두번째구덩이시작(self.ctx)


class 두번째구덩이시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__5$', arg4=5)
        self.move_npc(spawnId=2001, patrolName='MS2PatrolData_2001D')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=103, spawnIds=[2001]):
            return 두번째구덩이도착(self.ctx)


class 두번째구덩이도착(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[602], visible=True)
        self.set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__6$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 두번째구덩이(self.ctx)


class 두번째구덩이(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__7$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 두번째꿈틀이(self.ctx)


class 두번째꿈틀이(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__8$', arg4=3)
        self.move_npc(spawnId=2001, patrolName='MS2PatrolData_2001E')
        self.create_monster(spawnIds=[1002], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1002]):
            return 두번째구덩이완료(self.ctx)


class 두번째구덩이완료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__9$', arg4=3)
        self.move_npc(spawnId=2001, patrolName='MS2PatrolData_2001F')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=104, spawnIds=[2001]):
            return 세번째구덩이시작(self.ctx)


class 세번째구덩이시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__10$', arg4=5)
        self.move_npc(spawnId=2001, patrolName='MS2PatrolData_2001G')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=105, spawnIds=[2001]):
            return 세번째구덩이도착(self.ctx)


class 세번째구덩이도착(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4', seconds=4)
        self.set_effect(triggerIds=[603], visible=True)
        self.set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__11$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 세번째구덩이(self.ctx)


class 세번째구덩이(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__12$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 세번째꿈틀이(self.ctx)


class 세번째꿈틀이(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2001, patrolName='MS2PatrolData_2001H')
        self.create_monster(spawnIds=[1003], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1003]):
            return 세번째구덩이완료(self.ctx)


class 세번째구덩이완료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__13$', arg4=5)
        self.move_npc(spawnId=2001, patrolName='MS2PatrolData_2001G')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.create_monster(spawnIds=[2003], animationEffect=False)
            self.destroy_monster(spawnIds=[2001])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
