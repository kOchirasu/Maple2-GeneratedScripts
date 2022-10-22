""" trigger/02020070_bf/16000_minipuzzle_timetrial.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        reset_timer(timerId='1')
        reset_timer(timerId='10')
        reset_timer(timerId='100')
        set_mesh(triggerIds=[16001], visible=False, arg3=0, arg4=0, arg5=0) # Destination_FootHold
        set_interact_object(triggerIds=[12000265], state=0) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001161 걸어서 71001061 제거
        set_interact_object(triggerIds=[12000079], state=0) # Start_FootHold / 기믹 시작 오브젝트 / Additional Effect 71001061 71001271 71001281 부여
        set_interact_object(triggerIds=[12000098], state=0) # ReStart_FootHold / 제한 시간 리셋용 오브젝트 / Additional Effect 71001061 71001271 71001281 부여  / 71001061 버프 소유자만 반응 가능
        set_effect(triggerIds=[16200], visible=False) # Success Sound Effect
        set_effect(triggerIds=[16201], visible=False) # Right Sound Effect

    def on_tick(self) -> state.State:
        if user_value(key='TimeEventOn', value=1):
            return SettingDelay()


class SettingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Setting()


class Setting(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000079], state=1) # Start_FootHold / 기믹 시작 오브젝트 / Additional Effect 71001061 71001271 71001281 부여

    def on_tick(self) -> state.State:
        if user_value(key='TimeEventOn', value=0):
            return Wait()
        if object_interacted(interactIds=[12000079], arg2=0):
            set_timer(timerId='10', seconds=120, clearAtZero=True, display=False, arg5=0)
            set_timer(timerId='1', seconds=15, clearAtZero=True, display=False, arg5=0)
            return TimeTrial_StartDelay()


class TimeTrial_StartDelay(state.State):
    def on_enter(self):
        set_effect(triggerIds=[16201], visible=True) # Right Sound Effect
        set_mesh(triggerIds=[16001], visible=True, arg3=0, arg4=0, arg5=0) # Destination_FootHold

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return TimeTrial_Start()


class TimeTrial_Start(state.State):
    def on_tick(self) -> state.State:
        if check_any_user_additional_effect(boxId=16100, additionalEffectId=71001271, level=1):
            add_buff(boxIds=[160001], skillId=71001062, level=1, arg4=False, arg5=False)
            set_timer(timerId='100', seconds=60, clearAtZero=True, display=False, arg5=0)
            return TimeTrial_Success()
        if time_expired(timerId='1'):
            return TimeTrial_Fail()


class TimeTrial_Reset(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000098], state=1) # ReStart_FootHold / 제한 시간 리셋용 오브젝트 / Additional Effect 71001061 71001271 71001281 부여  / 71001061 버프 소유자만 반응 가능

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000098], arg2=0):
            return TimeTrial_TimerReset01()
        if time_expired(timerId='10'):
            set_interact_object(triggerIds=[12000098], state=0)
            reset_timer(timerId='10')
            return Setting()


#  타이머 리셋 시퀀스 
class TimeTrial_TimerReset01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[16201], visible=True) # Right Sound Effect
        set_timer(timerId='1', seconds=15, clearAtZero=True, display=False, arg5=0) # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001061 지속시간 동일
        set_interact_object(triggerIds=[12000098], state=0) # ReStart_FootHold / 제한 시간 리셋용 오브젝트 / Additional Effect 71001061 71001271 71001281 부여  / 71001061 버프 소유자만 반응 가능

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TimeTrial_Start()


#  목표 지점에 도착 성공 
class TimeTrial_Success(state.State):
    def on_enter(self):
        reset_timer(timerId='1')
        set_effect(triggerIds=[16200], visible=True) # Success Sound Effect
        set_interact_object(triggerIds=[12000265], state=1) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001161 걸어서 71001061 제거

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000265], arg2=0):
            set_interact_object(triggerIds=[12000265], state=2)
            set_user_value(triggerId=16000, key='TimeEventOn', value=0)
            return TimeTrial_SuccessDelay()
        if time_expired(timerId='100'):
            set_interact_object(triggerIds=[12000265], state=0)
            reset_timer(timerId='100')
            return TimeTrial_Quit()


class TimeTrial_SuccessDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return TimeTrial_Quit()


class TimeTrial_Quit(state.State):
    def on_enter(self):
        reset_timer(timerId='1')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


#  타임 아웃 실패 
class TimeTrial_Fail(state.State):
    def on_enter(self):
        reset_timer(timerId='1')

    def on_tick(self) -> state.State:
        if user_value(key='TimeEventOn', value=0):
            return Wait()
        if time_expired(timerId='10'):
            set_interact_object(triggerIds=[12000098], state=0)
            reset_timer(timerId='10')
            return Setting()
        if wait_tick(waitTick=2000):
            return TimeTrial_Reset()


