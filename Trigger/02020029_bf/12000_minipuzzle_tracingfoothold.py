""" trigger/02020029_bf/12000_minipuzzle_tracingfoothold.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='2')
        self.set_interact_object(triggerIds=[12000082], state=2) # Flower01
        self.set_interact_object(triggerIds=[12000083], state=2) # Flower02
        self.set_interact_object(triggerIds=[12000224], state=2) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001121 걸어서 71001021 제거
        self.set_interact_object(triggerIds=[12000075], state=2) # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001021 부여
        self.set_mesh(triggerIds=[12001], visible=False, arg3=0, delay=0, scale=0) # FootHold01
        self.set_mesh(triggerIds=[12002], visible=False, arg3=0, delay=0, scale=0) # FootHold02
        self.set_mesh(triggerIds=[12003], visible=False, arg3=0, delay=0, scale=0) # FootHold03
        self.set_actor(triggerId=12201, visible=False, initialSequence='Interaction_luminous_A01_on') # Actor_FlowerOn01
        self.set_actor(triggerId=12202, visible=False, initialSequence='Interaction_luminous_A01_on') # Actor_FlowerOn02
        self.set_effect(triggerIds=[12100], visible=False) # Success Sound Effect

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimeEventOn', value=1):
            return SettingDelay(self.ctx)


class SettingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Setting(self.ctx)


class Setting(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000075], state=1) # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001021 부여

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000075], stateValue=0):
            self.set_timer(timerId='1', seconds=120, startDelay=1, interval=0, vOffset=0)
            return TracingFootHold_Start_Delay(self.ctx)


class TracingFootHold_Start_Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TracingFootHold_Play01(self.ctx)


class TracingFootHold_Play01(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[12001], visible=True, arg3=0, delay=0, scale=1) # FootHold01
        self.set_interact_object(triggerIds=[12000082], state=1) # Flower01

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000082], stateValue=0):
            return TracingFootHold_Play01_Delay(self.ctx)
        if self.time_expired(timerId='1'):
            return TracingFootHold_Fail(self.ctx)


class TracingFootHold_Play01_Delay(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=12201, visible=True, initialSequence='Interaction_luminous_A01_on') # Actor_FlowerOn01
        self.set_interact_object(triggerIds=[12000082], state=2) # Flower01

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TracingFootHold_Play02(self.ctx)
        if self.time_expired(timerId='1'):
            return TracingFootHold_Fail(self.ctx)


class TracingFootHold_Play02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[12002], visible=True, arg3=0, delay=0, scale=1) # FootHold02
        self.set_interact_object(triggerIds=[12000083], state=1) # Flower02

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000083], stateValue=0):
            return TracingFootHold_Play02_Delay(self.ctx)
        if self.time_expired(timerId='1'):
            return TracingFootHold_Fail(self.ctx)


class TracingFootHold_Play02_Delay(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=12202, visible=True, initialSequence='Interaction_luminous_A01_on') # Actor_FlowerOn02
        self.set_interact_object(triggerIds=[12000083], state=2) # Flower02

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TracingFootHold_Success(self.ctx)


# 퍼즐 성공 후 종료
class TracingFootHold_Success(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[120001], skillId=71001022, level=1, isPlayer=False, isSkillSet=False)
        self.set_effect(triggerIds=[12100], visible=True) # Success Sound Effect
        self.set_mesh(triggerIds=[12003], visible=True, arg3=0, delay=0, scale=1) # FootHold03
        self.set_interact_object(triggerIds=[12000224], state=1) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001121 걸어서 71001021 제거
        self.set_timer(timerId='2', seconds=60, startDelay=1, interval=0, vOffset=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000224], stateValue=0):
            return TracingFootHold_SuccessDelay(self.ctx)
        if self.time_expired(timerId='2'):
            self.set_interact_object(triggerIds=[12000224], state=2)
            return ResetTimer(self.ctx)


class TracingFootHold_SuccessDelay(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=12000, key='TimeEventOn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ResetTimer(self.ctx)


# 제한 시간 종료
class TracingFootHold_Fail(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=12201, visible=False, initialSequence='Interaction_luminous_A01_on') # Actor_FlowerOn01
        self.set_actor(triggerId=12202, visible=False, initialSequence='Interaction_luminous_A01_on') # Actor_FlowerOn02

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ResetTimer(self.ctx)


class ResetTimer(trigger_api.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
