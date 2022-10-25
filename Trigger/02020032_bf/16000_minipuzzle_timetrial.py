""" trigger/02020032_bf/16000_minipuzzle_timetrial.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='10')
        self.reset_timer(timerId='100')
        self.set_mesh(triggerIds=[16001], visible=False, arg3=0, delay=0, scale=0) # Destination_FootHold
        self.set_interact_object(triggerIds=[12000261], state=0) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001161 걸어서 71001061 제거
        self.set_interact_object(triggerIds=[12000079], state=0) # Start_FootHold / 기믹 시작 오브젝트 / Additional Effect 71001061 71001271 71001281 부여
        self.set_interact_object(triggerIds=[12000098], state=0) # ReStart_FootHold / 제한 시간 리셋용 오브젝트 / Additional Effect 71001061 71001271 71001281 부여  / 71001061 버프 소유자만 반응 가능
        self.set_effect(triggerIds=[16200], visible=False) # Success Sound Effect
        self.set_effect(triggerIds=[16201], visible=False) # Right Sound Effect

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='TimeEventOn', value=1):
            return SettingDelay(self.ctx)


class SettingDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Setting(self.ctx)


class Setting(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000079], state=1) # Start_FootHold / 기믹 시작 오브젝트 / Additional Effect 71001061 71001271 71001281 부여

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='TimeEventOn', value=0):
            return Wait(self.ctx)
        if self.object_interacted(interactIds=[12000079], stateValue=0):
            self.set_timer(timerId='10', seconds=120, startDelay=1, interval=0, vOffset=0)
            self.set_timer(timerId='1', seconds=15, startDelay=1, interval=0, vOffset=0)
            return TimeTrial_StartDelay(self.ctx)


class TimeTrial_StartDelay(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[16201], visible=True) # Right Sound Effect
        self.set_mesh(triggerIds=[16001], visible=True, arg3=0, delay=0, scale=0) # Destination_FootHold

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return TimeTrial_Start(self.ctx)


class TimeTrial_Start(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_any_user_additional_effect(boxId=16100, additionalEffectId=71001271, level=1):
            self.add_buff(boxIds=[160001], skillId=71001062, level=1, isPlayer=False, isSkillSet=False)
            self.set_timer(timerId='100', seconds=60, startDelay=1, interval=0, vOffset=0)
            return TimeTrial_Success(self.ctx)
        if self.time_expired(timerId='1'):
            return TimeTrial_Fail(self.ctx)


class TimeTrial_Reset(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000098], state=1) # ReStart_FootHold / 제한 시간 리셋용 오브젝트 / Additional Effect 71001061 71001271 71001281 부여  / 71001061 버프 소유자만 반응 가능

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000098], stateValue=0):
            return TimeTrial_TimerReset01(self.ctx)
        if self.time_expired(timerId='10'):
            self.set_interact_object(triggerIds=[12000098], state=0)
            self.reset_timer(timerId='10')
            return Setting(self.ctx)


# 타이머 리셋 시퀀스
class TimeTrial_TimerReset01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[16201], visible=True) # Right Sound Effect
        self.set_timer(timerId='1', seconds=15, startDelay=1, interval=0, vOffset=0) # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001061 지속시간 동일
        self.set_interact_object(triggerIds=[12000098], state=0) # ReStart_FootHold / 제한 시간 리셋용 오브젝트 / Additional Effect 71001061 71001271 71001281 부여  / 71001061 버프 소유자만 반응 가능

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return TimeTrial_Start(self.ctx)


# 목표 지점에 도착 성공
class TimeTrial_Success(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')
        self.set_effect(triggerIds=[16200], visible=True) # Success Sound Effect
        self.set_interact_object(triggerIds=[12000261], state=1) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001161 걸어서 71001061 제거

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000261], stateValue=0):
            self.set_interact_object(triggerIds=[12000261], state=2)
            self.set_user_value(triggerId=16000, key='TimeEventOn', value=0)
            return TimeTrial_SuccessDelay(self.ctx)
        if self.time_expired(timerId='100'):
            self.set_interact_object(triggerIds=[12000261], state=0)
            self.reset_timer(timerId='100')
            return TimeTrial_Quit(self.ctx)


class TimeTrial_SuccessDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return TimeTrial_Quit(self.ctx)


class TimeTrial_Quit(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


# 타임 아웃 실패
class TimeTrial_Fail(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='TimeEventOn', value=0):
            return Wait(self.ctx)
        if self.time_expired(timerId='10'):
            self.set_interact_object(triggerIds=[12000098], state=0)
            self.reset_timer(timerId='10')
            return Setting(self.ctx)
        if self.wait_tick(waitTick=2000):
            return TimeTrial_Reset(self.ctx)


initial_state = Wait
