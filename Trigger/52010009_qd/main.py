""" trigger/52010009_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000866], state=0) # 컨테이너를 반응 가능한 상태로 변경
        self.set_interact_object(triggerIds=[10000880], state=0) # 컨테이너를 반응 가능한 상태로 변경
        self.set_interact_object(triggerIds=[10000915], state=0) # 컨테이너를 반응 가능한 상태로 변경

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[20002091], questStates=[1]):
            return Event_01_Idle(self.ctx)


class Event_01_Idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return Event_02(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=110)
        self.set_interact_object(triggerIds=[10000866], state=1) # 컨테이너를 반응 가능한 상태로 변경


class Event_02(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=111, textId=25201901) # 수리공이 숨어있는 컨테이너를 찾으세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000866], stateValue=0):
            return Event_03(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=111)
        self.create_monster(spawnIds=[111], animationEffect=False) # 그 안에 숨어있던 수리공 NPC들이 리젠
        self.set_conversation(type=1, spawnId=111, script='$52010009_QD__MAIN__0$', arg4=3, arg5=1)
        self.move_npc(spawnId=111, patrolName='MS2PatrolData0_1001')


class Event_03(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[102]):
            return Event_04(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=110)
        self.set_interact_object(triggerIds=[10000880], state=1) # 컨테이너를 반응 가능한 상태로 변경


class Event_04(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=111, textId=25201901) # 수리공이 숨어있는 컨테이너를 찾으세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000880], stateValue=0):
            return Event_05(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=111)
        self.create_monster(spawnIds=[112], animationEffect=False) # 그 안에 숨어있던 수리공 NPC들이 리젠
        self.set_conversation(type=1, spawnId=112, script='$52010009_QD__MAIN__1$', arg4=3, arg5=1)
        self.move_npc(spawnId=112, patrolName='MS2PatrolData0_1001')


class Event_05(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[103], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[103]):
            return Event_06(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=110)
        self.set_interact_object(triggerIds=[10000915], state=1) # 컨테이너를 반응 가능한 상태로 변경


class Event_06(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=111, textId=25201901) # 수리공이 숨어있는 컨테이너를 찾으세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000915], stateValue=0):
            return End(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=111)
        self.create_monster(spawnIds=[113], animationEffect=False) # 그 안에 숨어있던 수리공 NPC들이 리젠
        self.set_conversation(type=1, spawnId=113, script='$52010009_QD__MAIN__2$', arg4=3, arg5=1)
        self.move_npc(spawnId=113, patrolName='MS2PatrolData0_1001')


class End(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=701, type='trigger', achieve='findrepairman') # findrepairman


initial_state = idle
