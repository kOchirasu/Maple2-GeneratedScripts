""" trigger/99999884/scene01.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[401], visible=False)
        self.set_effect(triggerIds=[402], visible=False)
        self.set_effect(triggerIds=[403], visible=False)
        self.set_effect(triggerIds=[404], visible=False)
        self.set_actor(triggerId=405, visible=False)
        self.set_effect(triggerIds=[406], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라등장(self.ctx)


class 벨라등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[202])
        self.set_effect(triggerIds=[401], visible=True)
        self.set_timer(timerId='1', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사1(self.ctx)


class 벨라대사1(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[401], visible=False)
        self.set_timer(timerId='1', seconds=2)
        self.set_conversation(type=2, spawnId=11000057, script='$99999884__SCENE01__0$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사2(self.ctx)


class 벨라대사2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.set_conversation(type=1, spawnId=202, script='$99999884__SCENE01__1$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 프레이와오스칼등장(self.ctx)


class 프레이와오스칼등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[203])
        self.create_monster(spawnIds=[204])
        self.set_effect(triggerIds=[402], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 프레이대사1(self.ctx)


class 프레이대사1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.set_conversation(type=2, spawnId=11000119, script='$99999884__SCENE01__2$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사3(self.ctx)


class 벨라대사3(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.set_effect(triggerIds=[402], visible=False)
        self.move_npc(spawnId=202, patrolName='202_MS2PatrolData_Bella_TurnToFrey')
        self.set_conversation(type=1, spawnId=202, script='$99999884__SCENE01__3$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사4(self.ctx)


class 벨라대사4(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.move_npc(spawnId=202, patrolName='202_MS2PatrolData_Bella_TurnToDevorak')
        self.set_conversation(type=1, spawnId=202, script='$99999884__SCENE01__4$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 이펙트지연(self.ctx)


class 이펙트지연(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_effect(triggerIds=[402], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 프레이대사2(self.ctx)


class 프레이대사2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.move_npc(spawnId=203, patrolName='203_MS2PatrolData_Frey_MoveToBella')
        self.set_conversation(type=1, spawnId=203, script='$99999884__SCENE01__5$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사5(self.ctx)


class 벨라대사5(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_effect(triggerIds=[402], visible=False)
        self.set_effect(triggerIds=[403], visible=True)
        self.move_npc(spawnId=202, patrolName='202_MS2PatrolData_Bella_TurnToFrey')
        self.set_conversation(type=1, spawnId=202, script='$99999884__SCENE01__6$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 프레이피격(self.ctx)


class 프레이피격(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.move_npc(spawnId=203, patrolName='203_MS2PatrolData_Frey_HitByBella')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 오스칼대사1(self.ctx)


class 오스칼대사1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.destroy_monster(spawnIds=[203])
        self.set_effect(triggerIds=[403], visible=False)
        self.set_effect(triggerIds=[406], visible=True)
        self.set_actor(triggerId=405, visible=True, initialSequence='Down_Idle_A')
        self.move_npc(spawnId=204, patrolName='204_MS2PatrolData_Oskhal_MoveToFrey')
        self.set_conversation(type=2, spawnId=11000015, script='$99999884__SCENE01__7$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 오스칼대사2(self.ctx)


class 오스칼대사2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_conversation(type=1, spawnId=204, script='$99999884__SCENE01__8$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 오스칼돌격(self.ctx)


class 오스칼돌격(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.move_npc(spawnId=204, patrolName='204_MS2PatrolData_Oskhal_MoveToBella')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 연출끝(self.ctx)


class 연출끝(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera_path(pathIds=[302], returnView=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    pass


initial_state = 시작대기중
