""" trigger/99999875/16000_minipuzzle_timetrial.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[16001], visible=False, start_delay=0, interval=0, fade=0) # Destination_FootHold
        # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001161 걸어서 71001061 제거
        self.set_interact_object(trigger_ids=[12000071], state=2)
        # Start_FootHold / 기믹 시작 오브젝트 / Additional Effect 71001061 71001271 71001281 부여
        self.set_interact_object(trigger_ids=[12000079], state=0)
        # ReStart_FootHold / 제한 시간 리셋용 오브젝트 / Additional Effect 71001061 71001271 71001281 부여  / 71001061 버프 소유자만 반응 가능
        self.set_interact_object(trigger_ids=[12000098], state=0)
        self.set_effect(trigger_ids=[16200], visible=False) # Success Sound Effect
        self.set_effect(trigger_ids=[16201], visible=False) # Right Sound Effect

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimeEventOn') >= 1:
            return SettingDelay(self.ctx)


class SettingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Setting(self.ctx)


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Start_FootHold / 기믹 시작 오브젝트 / Additional Effect 71001061 71001271 71001281 부여
        self.set_interact_object(trigger_ids=[12000079], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimeEventOn') >= 0:
            return Wait(self.ctx)
        if self.object_interacted(interact_ids=[12000079], state=0):
            self.set_timer(timer_id='10', seconds=90, start_delay=1, interval=0, v_offset=0)
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001061 지속시간 동일
            self.set_timer(timer_id='1', seconds=15, start_delay=1, interval=0, v_offset=0)
            return TimeTrial_StartDelay(self.ctx)


class TimeTrial_StartDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[16201], visible=True) # Right Sound Effect
        self.set_mesh(trigger_ids=[16001], visible=True, start_delay=0, interval=0, fade=0) # Destination_FootHold

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return TimeTrial_Start(self.ctx)


class TimeTrial_Start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_any_user_additional_effect(box_id=16100, additional_effect_id=71001271, level=1):
            # 목표 지점에 도착 성공
            self.add_buff(box_ids=[160001], skill_id=71001062, level=1, is_player=False, is_skill_set=False)
            self.set_timer(timer_id='100', seconds=60, start_delay=1, interval=0, v_offset=0)
            return TimeTrial_Success(self.ctx)
        if self.time_expired(timer_id='1'):
            # 타임 아웃 실패
            return TimeTrial_Fail(self.ctx)


class TimeTrial_Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ReStart_FootHold / 제한 시간 리셋용 오브젝트 / Additional Effect 71001061 71001271 71001281 부여  / 71001061 버프 소유자만 반응 가능
        self.set_interact_object(trigger_ids=[12000098], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000098], state=0):
            # self.reset_timer(timer_id='1')
            return TimeTrial_TimerReset01(self.ctx)
        if self.time_expired(timer_id='10'):
            self.set_interact_object(trigger_ids=[12000098], state=0)
            self.reset_timer(timer_id='10')
            return Setting(self.ctx)


# 타이머 리셋 시퀀스
class TimeTrial_TimerReset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[16201], visible=True) # Right Sound Effect
        # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001061 지속시간 동일
        self.set_timer(timer_id='1', seconds=15, start_delay=1, interval=0, v_offset=0)
        # ReStart_FootHold / 제한 시간 리셋용 오브젝트 / Additional Effect 71001061 71001271 71001281 부여  / 71001061 버프 소유자만 반응 가능
        self.set_interact_object(trigger_ids=[12000098], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TimeTrial_Start(self.ctx)


# <state name="TimeTrial_TimerReset02">
# <onEnter>
# </onEnter>
# <condition name="오브젝트가반응했으면" arg1="12000098" arg2="0">
# <transition state="TimeTrial_TimerReset01"/>
# </condition>
# <condition name="CheckAnyUserAdditionalEffect" triggerBoxID="16100" additionalEffectID="71001271" level="1">
# <transition state="TimeTrial_Success"/>
# </condition>
# <condition name="시간이경과했으면" arg1="1">
# <transition state="TimeTrial_Fail"/>
# </condition>
# <onExit>
# </onExit>
# </state>
# 목표 지점에 도착 성공
class TimeTrial_Success(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.remove_buff(box_id=16100, skill_id=71001271)
        self.reset_timer(timer_id='1')
        self.set_effect(trigger_ids=[16200], visible=True) # Success Sound Effect
        # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001161 걸어서 71001061 제거
        self.set_interact_object(trigger_ids=[12000071], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000071], state=0):
            self.set_user_value(trigger_id=16000, key='TimeEventOn', value=0)
            return TimeTrial_SuccessDelay(self.ctx)
        if self.time_expired(timer_id='100'):
            self.set_interact_object(trigger_ids=[12000071], state=0)
            self.reset_timer(timer_id='100')
            return TimeTrial_SuccessDelay(self.ctx)


class TimeTrial_SuccessDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return TimeTrial_Quit(self.ctx)


class TimeTrial_Quit(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


# 타임 아웃 실패
class TimeTrial_Fail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimeEventOn') >= 0:
            return Wait(self.ctx)
        if self.time_expired(timer_id='10'):
            self.set_interact_object(trigger_ids=[12000098], state=0)
            self.reset_timer(timer_id='10')
            return Setting(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return TimeTrial_Reset(self.ctx)


initial_state = Wait
