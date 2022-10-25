""" trigger/02020034_bf/13000_minipuzzle_passingthroughring.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='10')
        self.set_mesh(triggerIds=[13001], visible=False, arg3=0, delay=0, scale=0) # off_01
        self.set_mesh(triggerIds=[13011], visible=False, arg3=0, delay=0, scale=0) # on_01
        self.set_mesh(triggerIds=[13002], visible=False, arg3=0, delay=0, scale=0) # off_02
        self.set_mesh(triggerIds=[13012], visible=False, arg3=0, delay=0, scale=0) # on_02
        self.set_mesh(triggerIds=[13003], visible=False, arg3=0, delay=0, scale=0) # off_03
        self.set_mesh(triggerIds=[13013], visible=False, arg3=0, delay=0, scale=0) # on_03
        self.set_mesh_animation(triggerIds=[13011], visible=False, arg3=0, arg4=0) # on_01
        self.set_mesh_animation(triggerIds=[13012], visible=False, arg3=0, arg4=0) # on_02
        self.set_mesh_animation(triggerIds=[13013], visible=False, arg3=0, arg4=0) # on_03
        self.set_interact_object(triggerIds=[12000233], state=2) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001131 걸어서 71001031 제거
        self.set_interact_object(triggerIds=[12000076], state=2) # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001031 부여
        self.set_effect(triggerIds=[13101], visible=False) # Right Sound Effect
        self.set_effect(triggerIds=[13102], visible=False) # Right Sound Effect
        self.set_effect(triggerIds=[13103], visible=False) # Right Sound Effect
        self.set_effect(triggerIds=[13200], visible=False) # Success Sound Effect
        self.set_mesh(triggerIds=[13300], visible=False, arg3=0, delay=0, scale=0) # Final_FootHold

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='TimeEventOn', value=1):
            return SettingDelay(self.ctx)


class SettingDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Setting(self.ctx)
        if self.user_value(key='EventStart', value=0):
            return Wait(self.ctx)


class Setting(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000076], state=1) # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001031 부여

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000076], stateValue=0):
            self.set_timer(timerId='1', seconds=120, startDelay=1, interval=0, vOffset=0)
            return PassingThroughRing_Start_Delay(self.ctx)
        if self.user_value(key='TimeEventOn', value=0):
            return Wait(self.ctx)


class PassingThroughRing_Start_Delay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PassingThroughRing_Play01(self.ctx)


class PassingThroughRing_Play01(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[13001], visible=True, arg3=0, delay=0, scale=1) # off_01

    def on_tick(self) -> common.Trigger:
        if self.check_any_user_additional_effect(boxId=13401, additionalEffectId=71001031, level=1):
            return PassingThroughRing_Play01_Delay(self.ctx)
        if self.time_expired(timerId='1'):
            return PassingThroughRing_Fail(self.ctx)


class PassingThroughRing_Play01_Delay(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[13001], visible=False, arg3=1, delay=0, scale=1) # off_01
        self.set_mesh(triggerIds=[13011], visible=True, arg3=0, delay=0, scale=1) # on_01
        self.set_mesh_animation(triggerIds=[13011], visible=True, arg3=0, arg4=0) # on_01
        self.set_effect(triggerIds=[13101], visible=True) # Right Sound Effect

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PassingThroughRing_Play02(self.ctx)
        if self.time_expired(timerId='1'):
            return PassingThroughRing_Fail(self.ctx)


class PassingThroughRing_Play02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[13002], visible=True, arg3=0, delay=0, scale=1) # off_02

    def on_tick(self) -> common.Trigger:
        if self.check_any_user_additional_effect(boxId=13402, additionalEffectId=71001031, level=1):
            return PassingThroughRing_Play02_Delay(self.ctx)
        if self.time_expired(timerId='1'):
            return PassingThroughRing_Fail(self.ctx)


class PassingThroughRing_Play02_Delay(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[13002], visible=False, arg3=1, delay=0, scale=1) # off_02
        self.set_mesh(triggerIds=[13012], visible=True, arg3=0, delay=0, scale=1) # on_02
        self.set_mesh_animation(triggerIds=[13012], visible=True, arg3=0, arg4=0) # on_02
        self.set_effect(triggerIds=[13102], visible=True) # Right Sound Effect

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PassingThroughRing_Play03(self.ctx)
        if self.time_expired(timerId='1'):
            return PassingThroughRing_Fail(self.ctx)


class PassingThroughRing_Play03(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[13003], visible=True, arg3=0, delay=0, scale=1) # off_03

    def on_tick(self) -> common.Trigger:
        if self.check_any_user_additional_effect(boxId=13403, additionalEffectId=71001031, level=1):
            return PassingThroughRing_Play03_Delay(self.ctx)
        if self.time_expired(timerId='1'):
            return PassingThroughRing_Fail(self.ctx)


class PassingThroughRing_Play03_Delay(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[13003], visible=False, arg3=1, delay=0, scale=1) # off_03
        self.set_mesh(triggerIds=[13013], visible=True, arg3=0, delay=0, scale=1) # on_03
        self.set_mesh_animation(triggerIds=[13013], visible=True, arg3=0, arg4=0) # on_03
        self.set_effect(triggerIds=[13103], visible=True) # Right Sound Effect

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PassingThroughRing_Success(self.ctx)


# 퍼즐 성공 후 종료
class PassingThroughRing_Success(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[130001], skillId=71001032, level=1, isPlayer=False, isSkillSet=False)
        self.set_timer(timerId='10', seconds=61, startDelay=1, interval=0, vOffset=0) # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001031 지속시간 동일
        self.set_effect(triggerIds=[13200], visible=True) # Success Sound Effect
        self.set_mesh(triggerIds=[13300], visible=True, arg3=0, delay=0, scale=0) # Final_FootHold
        self.set_interact_object(triggerIds=[12000233], state=1) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001131 걸어서 71001031 제거

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000233], stateValue=0):
            return PassingThroughRing_SuccessDelay(self.ctx)
        if self.time_expired(timerId='10'):
            return ResetTimer(self.ctx)


class PassingThroughRing_SuccessDelay(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=13000, key='TimeEventOn', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return ResetTimer(self.ctx)


# 제한 시간 종료
class PassingThroughRing_Fail(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            self.reset_timer(timerId='1')
            self.reset_timer(timerId='10')
            return Wait(self.ctx)


class ResetTimer(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='10')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
