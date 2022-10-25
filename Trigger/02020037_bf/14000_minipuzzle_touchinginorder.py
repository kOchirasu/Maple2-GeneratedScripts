""" trigger/02020037_bf/14000_minipuzzle_touchinginorder.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='10')
        self.set_interact_object(triggerIds=[12000244], state=2) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001141 걸어서 71001041 제거
        self.set_interact_object(triggerIds=[12000077], state=2) # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001041 부여
        self.set_interact_object(triggerIds=[12000088], state=0) # CheckPosition_Tree01
        self.set_interact_object(triggerIds=[12000089], state=0) # CheckPosition_Tree02
        self.set_interact_object(triggerIds=[12000090], state=0) # CheckPosition_Tree03
        self.set_interact_object(triggerIds=[12000091], state=0) # CheckPosition_Tree04
        self.set_interact_object(triggerIds=[12000092], state=0) # CheckPosition_Tree05
        self.set_actor(triggerId=14011, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree01
        self.set_actor(triggerId=14021, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree02
        self.set_actor(triggerId=14022, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree02
        self.set_actor(triggerId=14031, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree03
        self.set_actor(triggerId=14032, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree03
        self.set_actor(triggerId=14033, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree03
        self.set_actor(triggerId=14041, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree04
        self.set_actor(triggerId=14042, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree04
        self.set_actor(triggerId=14043, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree04
        self.set_actor(triggerId=14044, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree04
        self.set_actor(triggerId=14051, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree05
        self.set_actor(triggerId=14052, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree05
        self.set_actor(triggerId=14053, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree05
        self.set_actor(triggerId=14054, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower04_Of_Tree05
        self.set_actor(triggerId=14055, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower05_Of_Tree05
        self.set_effect(triggerIds=[14200], visible=False) # Success Sound Effect
        self.set_effect(triggerIds=[14201], visible=False) # Right Sound Effect
        self.set_effect(triggerIds=[14202], visible=False) # Wrong Sound Effect

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='TimeEventOn', value=1):
            return SettingDelay(self.ctx)


class SettingDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Setting(self.ctx)
        if self.user_value(key='TimeEventOn', value=0):
            return Wait(self.ctx)


class Setting(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000077], state=1) # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001041 부여

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000077], stateValue=0):
            self.set_timer(timerId='1', seconds=120, startDelay=1, interval=0, vOffset=0)
            return TouchingInNumericalOrder_Start_Delay(self.ctx)
        if self.user_value(key='TimeEventOn', value=0):
            return Wait(self.ctx)


class TouchingInNumericalOrder_Start_Delay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return TouchingInNumericalOrder_Play01(self.ctx)


class TouchingInNumericalOrder_Play01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[14201], visible=True) # Right Sound Effect
        self.set_interact_object(triggerIds=[12000088], state=1) # CheckPosition_Tree01
        self.set_interact_object(triggerIds=[12000089], state=1) # CheckPosition_Tree02
        self.set_interact_object(triggerIds=[12000090], state=1) # CheckPosition_Tree03
        self.set_interact_object(triggerIds=[12000091], state=1) # CheckPosition_Tree04
        self.set_interact_object(triggerIds=[12000092], state=1) # CheckPosition_Tree05
        self.set_actor(triggerId=14011, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree01
        self.set_actor(triggerId=14021, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree02
        self.set_actor(triggerId=14022, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree02
        self.set_actor(triggerId=14031, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree03
        self.set_actor(triggerId=14032, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree03
        self.set_actor(triggerId=14033, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree03
        self.set_actor(triggerId=14041, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree04
        self.set_actor(triggerId=14042, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree04
        self.set_actor(triggerId=14043, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree04
        self.set_actor(triggerId=14044, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree04
        self.set_actor(triggerId=14051, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree05
        self.set_actor(triggerId=14052, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree05
        self.set_actor(triggerId=14053, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree05
        self.set_actor(triggerId=14054, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower04_Of_Tree05
        self.set_actor(triggerId=14055, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower05_Of_Tree05

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return ResetTimer(self.ctx)
        if self.object_interacted(interactIds=[12000088], stateValue=0):
            return TouchingInNumericalOrder_Play02(self.ctx)
        if self.object_interacted(interactIds=[12000089], stateValue=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)
        if self.object_interacted(interactIds=[12000090], stateValue=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)
        if self.object_interacted(interactIds=[12000091], stateValue=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)
        if self.object_interacted(interactIds=[12000092], stateValue=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)


class TouchingInNumericalOrder_Play02(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000088], state=0) # CheckPosition_Tree01
        self.set_effect(triggerIds=[14201], visible=True) # Right Sound Effect
        self.set_actor(triggerId=14011, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower01_Of_Tree01

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return ResetTimer(self.ctx)
        if self.object_interacted(interactIds=[12000089], stateValue=0):
            return TouchingInNumericalOrder_Play03(self.ctx)
        if self.object_interacted(interactIds=[12000090], stateValue=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)
        if self.object_interacted(interactIds=[12000091], stateValue=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)
        if self.object_interacted(interactIds=[12000092], stateValue=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)


class TouchingInNumericalOrder_Play03(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000089], state=0) # CheckPosition_Tree02
        self.set_effect(triggerIds=[14201], visible=True) # Right Sound Effect
        self.set_actor(triggerId=14021, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower01_Of_Tree02
        self.set_actor(triggerId=14022, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower02_Of_Tree02

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return ResetTimer(self.ctx)
        if self.object_interacted(interactIds=[12000090], stateValue=0):
            return TouchingInNumericalOrder_Play04(self.ctx)
        if self.object_interacted(interactIds=[12000091], stateValue=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)
        if self.object_interacted(interactIds=[12000092], stateValue=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)


class TouchingInNumericalOrder_Play04(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000090], state=0) # CheckPosition_Tree03
        self.set_effect(triggerIds=[14201], visible=True) # Right Sound Effect
        self.set_actor(triggerId=14031, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower01_Of_Tree03
        self.set_actor(triggerId=14032, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower02_Of_Tree03
        self.set_actor(triggerId=14033, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower03_Of_Tree03

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return ResetTimer(self.ctx)
        if self.object_interacted(interactIds=[12000091], stateValue=0):
            return TouchingInNumericalOrder_Play05(self.ctx)
        if self.object_interacted(interactIds=[12000092], stateValue=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)


class TouchingInNumericalOrder_Play05(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000091], state=0) # CheckPosition_Tree04
        self.set_effect(triggerIds=[14201], visible=True) # Right Sound Effect
        self.set_actor(triggerId=14041, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower01_Of_Tree04
        self.set_actor(triggerId=14042, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower02_Of_Tree04
        self.set_actor(triggerId=14043, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower03_Of_Tree04
        self.set_actor(triggerId=14044, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower03_Of_Tree04

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return ResetTimer(self.ctx)
        if self.object_interacted(interactIds=[12000092], stateValue=0):
            return TouchingInNumericalOrder_End(self.ctx)


class TouchingInNumericalOrder_End(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000092], state=0) # CheckPosition_Tree05
        self.set_effect(triggerIds=[14201], visible=True) # Right Sound Effect
        self.set_actor(triggerId=14051, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower01_Of_Tree05
        self.set_actor(triggerId=14052, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower02_Of_Tree05
        self.set_actor(triggerId=14053, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower03_Of_Tree05
        self.set_actor(triggerId=14054, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower04_Of_Tree05
        self.set_actor(triggerId=14055, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower05_Of_Tree05

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return TouchingInNumericalOrder_Success(self.ctx)


# 퍼즐 성공 후 종료
class TouchingInNumericalOrder_Success(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=61, startDelay=1, interval=0, vOffset=0)
        self.add_buff(boxIds=[140001], skillId=71001042, level=1, isPlayer=False, isSkillSet=False)
        self.set_effect(triggerIds=[14200], visible=True) # Success Sound Effect
        self.set_interact_object(triggerIds=[12000244], state=1) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001141 걸어서 71001041 제거

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000244], stateValue=0):
            return TouchingInNumericalOrder_SuccessDelay(self.ctx)
        if self.time_expired(timerId='10'):
            return ResetTimer(self.ctx)


class TouchingInNumericalOrder_SuccessDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return TouchingInNumericalOrder_Quit(self.ctx)


class TouchingInNumericalOrder_Quit(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=14000, key='TimeEventOn', value=0)
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='10')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


# 오답 터치
class TouchingInNumericalOrder_FailDelay(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[14202], visible=True) # Wrong Sound Effect

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return TouchingInNumericalOrder_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            return ResetTimer(self.ctx)
        if self.user_value(key='TimeEventOn', value=0):
            return ResetTimer(self.ctx)


class TouchingInNumericalOrder_Fail(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000088], state=0) # CheckPosition_Tree01
        self.set_interact_object(triggerIds=[12000089], state=0) # CheckPosition_Tree02
        self.set_interact_object(triggerIds=[12000090], state=0) # CheckPosition_Tree03
        self.set_interact_object(triggerIds=[12000091], state=0) # CheckPosition_Tree04
        self.set_interact_object(triggerIds=[12000092], state=0) # CheckPosition_Tree05
        self.set_actor(triggerId=14011, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree01
        self.set_actor(triggerId=14021, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree02
        self.set_actor(triggerId=14022, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree02
        self.set_actor(triggerId=14031, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree03
        self.set_actor(triggerId=14032, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree03
        self.set_actor(triggerId=14033, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree03
        self.set_actor(triggerId=14041, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree04
        self.set_actor(triggerId=14042, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree04
        self.set_actor(triggerId=14043, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree04
        self.set_actor(triggerId=14044, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree04
        self.set_actor(triggerId=14051, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree05
        self.set_actor(triggerId=14052, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree05
        self.set_actor(triggerId=14053, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree05
        self.set_actor(triggerId=14054, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower04_Of_Tree05
        self.set_actor(triggerId=14055, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower05_Of_Tree05

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return TouchingInNumericalOrder_Play01(self.ctx)
        if self.time_expired(timerId='1'):
            return ResetTimer(self.ctx)
        if self.user_value(key='TimeEventOn', value=0):
            return ResetTimer(self.ctx)


class ResetTimer(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
