""" trigger/99999873/14000_minipuzzle_touchinginorder.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000069], state=2) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001141 걸어서 71001041 제거
        set_interact_object(triggerIds=[12000077], state=2) # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001041 부여
        set_interact_object(triggerIds=[12000088], state=0) # CheckPosition_Tree01
        set_interact_object(triggerIds=[12000089], state=0) # CheckPosition_Tree02
        set_interact_object(triggerIds=[12000090], state=0) # CheckPosition_Tree03
        set_interact_object(triggerIds=[12000091], state=0) # CheckPosition_Tree04
        set_interact_object(triggerIds=[12000092], state=0) # CheckPosition_Tree05
        set_actor(triggerId=14011, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree01
        set_actor(triggerId=14021, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree02
        set_actor(triggerId=14022, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree02
        set_actor(triggerId=14031, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree03
        set_actor(triggerId=14032, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree03
        set_actor(triggerId=14033, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree03
        set_actor(triggerId=14041, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree04
        set_actor(triggerId=14042, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree04
        set_actor(triggerId=14043, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree04
        set_actor(triggerId=14044, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree04
        set_actor(triggerId=14051, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree05
        set_actor(triggerId=14052, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree05
        set_actor(triggerId=14053, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree05
        set_actor(triggerId=14054, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower04_Of_Tree05
        set_actor(triggerId=14055, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower05_Of_Tree05
        set_effect(triggerIds=[14200], visible=False) # Success Sound Effect
        set_effect(triggerIds=[14201], visible=False) # Right Sound Effect
        set_effect(triggerIds=[14202], visible=False) # Wrong Sound Effect

    def on_tick(self) -> state.State:
        if user_value(key='TimeEventOn', value=1):
            return SettingDelay()


class SettingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Setting()
        if user_value(key='TimeEventOn', value=0):
            return Wait()


class Setting(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000077], state=1) # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001041 부여

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000077], arg2=0):
            set_timer(timerId='1', seconds=90, clearAtZero=True, display=False, arg5=0)
            return TouchingInNumericalOrder_Start_Delay()
        if user_value(key='TimeEventOn', value=0):
            return Wait()


class TouchingInNumericalOrder_Start_Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TouchingInNumericalOrder_Play01()


class TouchingInNumericalOrder_Play01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[14201], visible=True) # Right Sound Effect
        set_interact_object(triggerIds=[12000088], state=1) # CheckPosition_Tree01
        set_interact_object(triggerIds=[12000089], state=1) # CheckPosition_Tree02
        set_interact_object(triggerIds=[12000090], state=1) # CheckPosition_Tree03
        set_interact_object(triggerIds=[12000091], state=1) # CheckPosition_Tree04
        set_interact_object(triggerIds=[12000092], state=1) # CheckPosition_Tree05
        set_actor(triggerId=14011, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree01
        set_actor(triggerId=14021, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree02
        set_actor(triggerId=14022, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree02
        set_actor(triggerId=14031, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree03
        set_actor(triggerId=14032, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree03
        set_actor(triggerId=14033, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree03
        set_actor(triggerId=14041, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree04
        set_actor(triggerId=14042, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree04
        set_actor(triggerId=14043, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree04
        set_actor(triggerId=14044, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree04
        set_actor(triggerId=14051, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree05
        set_actor(triggerId=14052, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree05
        set_actor(triggerId=14053, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree05
        set_actor(triggerId=14054, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower04_Of_Tree05
        set_actor(triggerId=14055, visible=True, initialSequence='Interaction_luminous_A02_off') # Flower05_Of_Tree05

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return ResetTimer()
        if object_interacted(interactIds=[12000088], arg2=0):
            return TouchingInNumericalOrder_Play02()
        if object_interacted(interactIds=[12000089], arg2=0):
            return TouchingInNumericalOrder_FailDelay()
        if object_interacted(interactIds=[12000090], arg2=0):
            return TouchingInNumericalOrder_FailDelay()
        if object_interacted(interactIds=[12000091], arg2=0):
            return TouchingInNumericalOrder_FailDelay()
        if object_interacted(interactIds=[12000092], arg2=0):
            return TouchingInNumericalOrder_FailDelay()


class TouchingInNumericalOrder_Play02(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000088], state=0) # CheckPosition_Tree01
        set_effect(triggerIds=[14201], visible=True) # Right Sound Effect
        set_actor(triggerId=14011, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower01_Of_Tree01

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return ResetTimer()
        if object_interacted(interactIds=[12000089], arg2=0):
            return TouchingInNumericalOrder_Play03()
        if object_interacted(interactIds=[12000090], arg2=0):
            return TouchingInNumericalOrder_FailDelay()
        if object_interacted(interactIds=[12000091], arg2=0):
            return TouchingInNumericalOrder_FailDelay()
        if object_interacted(interactIds=[12000092], arg2=0):
            return TouchingInNumericalOrder_FailDelay()


class TouchingInNumericalOrder_Play03(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000089], state=0) # CheckPosition_Tree02
        set_effect(triggerIds=[14201], visible=True) # Right Sound Effect
        set_actor(triggerId=14021, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower01_Of_Tree02
        set_actor(triggerId=14022, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower02_Of_Tree02

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return ResetTimer()
        if object_interacted(interactIds=[12000090], arg2=0):
            return TouchingInNumericalOrder_Play04()
        if object_interacted(interactIds=[12000091], arg2=0):
            return TouchingInNumericalOrder_FailDelay()
        if object_interacted(interactIds=[12000092], arg2=0):
            return TouchingInNumericalOrder_FailDelay()


class TouchingInNumericalOrder_Play04(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000090], state=0) # CheckPosition_Tree03
        set_effect(triggerIds=[14201], visible=True) # Right Sound Effect
        set_actor(triggerId=14031, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower01_Of_Tree03
        set_actor(triggerId=14032, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower02_Of_Tree03
        set_actor(triggerId=14033, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower03_Of_Tree03

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return ResetTimer()
        if object_interacted(interactIds=[12000091], arg2=0):
            return TouchingInNumericalOrder_Play05()
        if object_interacted(interactIds=[12000092], arg2=0):
            return TouchingInNumericalOrder_FailDelay()


class TouchingInNumericalOrder_Play05(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000091], state=0) # CheckPosition_Tree04
        set_effect(triggerIds=[14201], visible=True) # Right Sound Effect
        set_actor(triggerId=14041, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower01_Of_Tree04
        set_actor(triggerId=14042, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower02_Of_Tree04
        set_actor(triggerId=14043, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower03_Of_Tree04
        set_actor(triggerId=14044, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower03_Of_Tree04

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return ResetTimer()
        if object_interacted(interactIds=[12000092], arg2=0):
            return TouchingInNumericalOrder_End()


class TouchingInNumericalOrder_End(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000092], state=0) # CheckPosition_Tree05
        set_effect(triggerIds=[14201], visible=True) # Right Sound Effect
        set_actor(triggerId=14051, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower01_Of_Tree05
        set_actor(triggerId=14052, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower02_Of_Tree05
        set_actor(triggerId=14053, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower03_Of_Tree05
        set_actor(triggerId=14054, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower04_Of_Tree05
        set_actor(triggerId=14055, visible=True, initialSequence='Interaction_luminous_A02_on') # Flower05_Of_Tree05

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TouchingInNumericalOrder_Success()


#  퍼즐 성공 후 종료 
class TouchingInNumericalOrder_Success(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=61, clearAtZero=True, display=False, arg5=0)
        add_buff(boxIds=[140001], skillId=71001042, level=1, arg4=False, arg5=False)
        set_effect(triggerIds=[14200], visible=True) # Success Sound Effect
        set_interact_object(triggerIds=[12000069], state=1) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001141 걸어서 71001041 제거

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000069], arg2=0):
            return TouchingInNumericalOrder_SuccessDelay()
        if time_expired(timerId='10'):
            return ResetTimer()


class TouchingInNumericalOrder_SuccessDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return TouchingInNumericalOrder_Quit()


class TouchingInNumericalOrder_Quit(state.State):
    def on_enter(self):
        set_user_value(triggerId=14000, key='TimeEventOn', value=0)
        reset_timer(timerId='1')
        reset_timer(timerId='10')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


#  오답 터치 
class TouchingInNumericalOrder_FailDelay(state.State):
    def on_enter(self):
        set_effect(triggerIds=[14202], visible=True) # Wrong Sound Effect

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TouchingInNumericalOrder_Fail()
        if time_expired(timerId='1'):
            return ResetTimer()
        if user_value(key='TimeEventOn', value=0):
            return ResetTimer()


class TouchingInNumericalOrder_Fail(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000088], state=0) # CheckPosition_Tree01
        set_interact_object(triggerIds=[12000089], state=0) # CheckPosition_Tree02
        set_interact_object(triggerIds=[12000090], state=0) # CheckPosition_Tree03
        set_interact_object(triggerIds=[12000091], state=0) # CheckPosition_Tree04
        set_interact_object(triggerIds=[12000092], state=0) # CheckPosition_Tree05
        set_actor(triggerId=14011, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree01
        set_actor(triggerId=14021, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree02
        set_actor(triggerId=14022, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree02
        set_actor(triggerId=14031, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree03
        set_actor(triggerId=14032, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree03
        set_actor(triggerId=14033, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree03
        set_actor(triggerId=14041, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree04
        set_actor(triggerId=14042, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree04
        set_actor(triggerId=14043, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree04
        set_actor(triggerId=14044, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree04
        set_actor(triggerId=14051, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower01_Of_Tree05
        set_actor(triggerId=14052, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower02_Of_Tree05
        set_actor(triggerId=14053, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower03_Of_Tree05
        set_actor(triggerId=14054, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower04_Of_Tree05
        set_actor(triggerId=14055, visible=False, initialSequence='Interaction_luminous_A02_off') # Flower05_Of_Tree05

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return TouchingInNumericalOrder_Play01()
        if time_expired(timerId='1'):
            return ResetTimer()
        if user_value(key='TimeEventOn', value=0):
            return ResetTimer()


class ResetTimer(state.State):
    def on_enter(self):
        reset_timer(timerId='1')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


