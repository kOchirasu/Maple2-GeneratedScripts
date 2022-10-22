""" trigger/99999871/12000_minipuzzle_tracingfoothold.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000082], state=2) # Flower01
        set_interact_object(triggerIds=[12000083], state=2) # Flower02
        set_interact_object(triggerIds=[12000067], state=2) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001121 걸어서 71001021 제거
        set_interact_object(triggerIds=[12000075], state=2) # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001021 부여
        set_mesh(triggerIds=[12001], visible=False, arg3=0, arg4=0, arg5=0) # FootHold01
        set_mesh(triggerIds=[12002], visible=False, arg3=0, arg4=0, arg5=0) # FootHold02
        set_mesh(triggerIds=[12003], visible=False, arg3=0, arg4=0, arg5=0) # FootHold03
        set_actor(triggerId=12201, visible=False, initialSequence='Interaction_luminous_A01_on') # Actor_FlowerOn01
        set_actor(triggerId=12202, visible=False, initialSequence='Interaction_luminous_A01_on') # Actor_FlowerOn02
        set_effect(triggerIds=[12100], visible=False) # Success Sound Effect

    def on_tick(self) -> state.State:
        if user_value(key='TimeEventOn', value=1):
            return SettingDelay()


class SettingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Setting()


class Setting(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000075], state=1) # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001021 부여

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000075], arg2=0):
            set_timer(timerId='1', seconds=90, clearAtZero=True, display=False, arg5=0)
            return TracingFootHold_Start_Delay()


class TracingFootHold_Start_Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TracingFootHold_Play01()


class TracingFootHold_Play01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[12001], visible=True, arg3=0, arg4=0, arg5=1) # FootHold01
        set_interact_object(triggerIds=[12000082], state=1) # Flower01

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000082], arg2=0):
            return TracingFootHold_Play01_Delay()
        if time_expired(timerId='1'):
            return TracingFootHold_Fail()


class TracingFootHold_Play01_Delay(state.State):
    def on_enter(self):
        set_actor(triggerId=12201, visible=True, initialSequence='Interaction_luminous_A01_on') # Actor_FlowerOn01
        set_interact_object(triggerIds=[12000082], state=2) # Flower01

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TracingFootHold_Play02()
        if time_expired(timerId='1'):
            return TracingFootHold_Fail()


class TracingFootHold_Play02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[12002], visible=True, arg3=0, arg4=0, arg5=1) # FootHold02
        set_interact_object(triggerIds=[12000083], state=1) # Flower02

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000083], arg2=0):
            return TracingFootHold_Play02_Delay()
        if time_expired(timerId='1'):
            return TracingFootHold_Fail()


class TracingFootHold_Play02_Delay(state.State):
    def on_enter(self):
        set_actor(triggerId=12202, visible=True, initialSequence='Interaction_luminous_A01_on') # Actor_FlowerOn02
        set_interact_object(triggerIds=[12000083], state=2) # Flower02

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TracingFootHold_Success()


#  퍼즐 성공 후 종료 
class TracingFootHold_Success(state.State):
    def on_enter(self):
        add_buff(boxIds=[120001], skillId=71001022, level=1, arg4=False, arg5=False)
        set_effect(triggerIds=[12100], visible=True) # Success Sound Effect
        set_mesh(triggerIds=[12003], visible=True, arg3=0, arg4=0, arg5=1) # FootHold03
        set_interact_object(triggerIds=[12000067], state=1) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001121 걸어서 71001021 제거
        set_timer(timerId='2', seconds=60, clearAtZero=True, display=False, arg5=0)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000067], arg2=0):
            return TracingFootHold_SuccessDelay()
        if time_expired(timerId='2'):
            set_interact_object(triggerIds=[12000067], state=2)
            return ResetTimer()


class TracingFootHold_SuccessDelay(state.State):
    def on_enter(self):
        set_user_value(triggerId=12000, key='TimeEventOn', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ResetTimer()


#  제한 시간 종료 
class TracingFootHold_Fail(state.State):
    def on_enter(self):
        set_actor(triggerId=12201, visible=False, initialSequence='Interaction_luminous_A01_on') # Actor_FlowerOn01
        set_actor(triggerId=12202, visible=False, initialSequence='Interaction_luminous_A01_on') # Actor_FlowerOn02

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ResetTimer()


class ResetTimer(state.State):
    def on_enter(self):
        reset_timer(timerId='1')
        reset_timer(timerId='2')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


