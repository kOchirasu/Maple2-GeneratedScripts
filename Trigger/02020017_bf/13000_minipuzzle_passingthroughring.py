""" trigger/02020017_bf/13000_minipuzzle_passingthroughring.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        reset_timer(timerId='1')
        reset_timer(timerId='10')
        set_mesh(triggerIds=[13001], visible=False, arg3=0, arg4=0, arg5=0) # off_01
        set_mesh(triggerIds=[13011], visible=False, arg3=0, arg4=0, arg5=0) # on_01
        set_mesh(triggerIds=[13002], visible=False, arg3=0, arg4=0, arg5=0) # off_02
        set_mesh(triggerIds=[13012], visible=False, arg3=0, arg4=0, arg5=0) # on_02
        set_mesh(triggerIds=[13003], visible=False, arg3=0, arg4=0, arg5=0) # off_03
        set_mesh(triggerIds=[13013], visible=False, arg3=0, arg4=0, arg5=0) # on_03
        set_mesh_animation(triggerIds=[13011], visible=False, arg3=0, arg4=0) # on_01
        set_mesh_animation(triggerIds=[13012], visible=False, arg3=0, arg4=0) # on_02
        set_mesh_animation(triggerIds=[13013], visible=False, arg3=0, arg4=0) # on_03
        set_interact_object(triggerIds=[12000232], state=2) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001131 걸어서 71001031 제거
        set_interact_object(triggerIds=[12000076], state=2) # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001031 부여
        set_effect(triggerIds=[13101], visible=False) # Right Sound Effect
        set_effect(triggerIds=[13102], visible=False) # Right Sound Effect
        set_effect(triggerIds=[13103], visible=False) # Right Sound Effect
        set_effect(triggerIds=[13200], visible=False) # Success Sound Effect
        set_mesh(triggerIds=[13300], visible=False, arg3=0, arg4=0, arg5=0) # Final_FootHold

    def on_tick(self) -> state.State:
        if user_value(key='TimeEventOn', value=1):
            return SettingDelay()


class SettingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Setting()
        if user_value(key='EventStart', value=0):
            return Wait()


class Setting(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000076], state=1) # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001031 부여

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000076], arg2=0):
            set_timer(timerId='1', seconds=120, clearAtZero=True, display=False, arg5=0)
            return PassingThroughRing_Start_Delay()
        if user_value(key='TimeEventOn', value=0):
            return Wait()


class PassingThroughRing_Start_Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PassingThroughRing_Play01()


class PassingThroughRing_Play01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[13001], visible=True, arg3=0, arg4=0, arg5=1) # off_01

    def on_tick(self) -> state.State:
        if check_any_user_additional_effect(boxId=13401, additionalEffectId=71001031, level=1):
            return PassingThroughRing_Play01_Delay()
        if time_expired(timerId='1'):
            return PassingThroughRing_Fail()


class PassingThroughRing_Play01_Delay(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[13001], visible=False, arg3=1, arg4=0, arg5=1) # off_01
        set_mesh(triggerIds=[13011], visible=True, arg3=0, arg4=0, arg5=1) # on_01
        set_mesh_animation(triggerIds=[13011], visible=True, arg3=0, arg4=0) # on_01
        set_effect(triggerIds=[13101], visible=True) # Right Sound Effect

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PassingThroughRing_Play02()
        if time_expired(timerId='1'):
            return PassingThroughRing_Fail()


class PassingThroughRing_Play02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[13002], visible=True, arg3=0, arg4=0, arg5=1) # off_02

    def on_tick(self) -> state.State:
        if check_any_user_additional_effect(boxId=13402, additionalEffectId=71001031, level=1):
            return PassingThroughRing_Play02_Delay()
        if time_expired(timerId='1'):
            return PassingThroughRing_Fail()


class PassingThroughRing_Play02_Delay(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[13002], visible=False, arg3=1, arg4=0, arg5=1) # off_02
        set_mesh(triggerIds=[13012], visible=True, arg3=0, arg4=0, arg5=1) # on_02
        set_mesh_animation(triggerIds=[13012], visible=True, arg3=0, arg4=0) # on_02
        set_effect(triggerIds=[13102], visible=True) # Right Sound Effect

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PassingThroughRing_Play03()
        if time_expired(timerId='1'):
            return PassingThroughRing_Fail()


class PassingThroughRing_Play03(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[13003], visible=True, arg3=0, arg4=0, arg5=1) # off_03

    def on_tick(self) -> state.State:
        if check_any_user_additional_effect(boxId=13403, additionalEffectId=71001031, level=1):
            return PassingThroughRing_Play03_Delay()
        if time_expired(timerId='1'):
            return PassingThroughRing_Fail()


class PassingThroughRing_Play03_Delay(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[13003], visible=False, arg3=1, arg4=0, arg5=1) # off_03
        set_mesh(triggerIds=[13013], visible=True, arg3=0, arg4=0, arg5=1) # on_03
        set_mesh_animation(triggerIds=[13013], visible=True, arg3=0, arg4=0) # on_03
        set_effect(triggerIds=[13103], visible=True) # Right Sound Effect

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PassingThroughRing_Success()


#  퍼즐 성공 후 종료 
class PassingThroughRing_Success(state.State):
    def on_enter(self):
        add_buff(boxIds=[130001], skillId=71001032, level=1, arg4=False, arg5=False)
        set_timer(timerId='10', seconds=61, clearAtZero=True, display=False, arg5=0) # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001031 지속시간 동일
        set_effect(triggerIds=[13200], visible=True) # Success Sound Effect
        set_mesh(triggerIds=[13300], visible=True, arg3=0, arg4=0, arg5=0) # Final_FootHold
        set_interact_object(triggerIds=[12000232], state=1) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001131 걸어서 71001031 제거

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000232], arg2=0):
            return PassingThroughRing_SuccessDelay()
        if time_expired(timerId='10'):
            return ResetTimer()


class PassingThroughRing_SuccessDelay(state.State):
    def on_enter(self):
        set_user_value(triggerId=13000, key='TimeEventOn', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ResetTimer()


#  제한 시간 종료 
class PassingThroughRing_Fail(state.State):
    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            reset_timer(timerId='1')
            reset_timer(timerId='10')
            return Wait()


class ResetTimer(state.State):
    def on_enter(self):
        reset_timer(timerId='1')
        reset_timer(timerId='10')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


