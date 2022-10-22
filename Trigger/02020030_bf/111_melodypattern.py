""" trigger/02020030_bf/111_melodypattern.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=0)
        set_user_value(key='Reset', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='PatternPick', value=1):
            return MelodyPlay01_Start()

    def on_exit(self):
        set_user_value(key='Reset', value=0)


#  퀴즈시작 / 파-솔-라-시-도` 
class MelodyPlay01_Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[11204], visible=True) # Bell F
        set_actor(triggerId=11004, visible=True, initialSequence='ks_quest_musical_B01_green') # Bell F

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MelodyPlay01_End()


class MelodyPlay01_End(state.State):
    def on_enter(self):
        set_actor(triggerId=11004, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell F

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MelodyPlay02_Start()


class MelodyPlay02_Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[11205], visible=True) # Bell D
        set_actor(triggerId=11005, visible=True, initialSequence='ks_quest_musical_B01_blue') # Bell D

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MelodyPlay02_End()


class MelodyPlay02_End(state.State):
    def on_enter(self):
        set_actor(triggerId=11005, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell D

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MelodyPlay03_Start()


class MelodyPlay03_Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[11206], visible=True) # Bell A
        set_actor(triggerId=11006, visible=True, initialSequence='ks_quest_musical_B01_navy') # Bell A

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MelodyPlay03_End()


class MelodyPlay03_End(state.State):
    def on_enter(self):
        set_actor(triggerId=11006, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell A

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MelodyPlay04_Start()


class MelodyPlay04_Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[11207], visible=True) # Bell B
        set_actor(triggerId=11007, visible=True, initialSequence='ks_quest_musical_B01_purple') # Bell B

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MelodyPlay04_End()


class MelodyPlay04_End(state.State):
    def on_enter(self):
        set_actor(triggerId=11007, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell B

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MelodyPlay05_Start()


class MelodyPlay05_Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[11208], visible=True) # Bell HighC
        set_actor(triggerId=11008, visible=True, initialSequence='ks_quest_musical_B01_pink') # Bell HighC

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MelodyPlay05_End()


class MelodyPlay05_End(state.State):
    def on_enter(self):
        set_actor(triggerId=11008, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell HighC

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CheckAnswer01_Start()


#  정답체크 / 파-솔-라-시-도` 
class CheckAnswer01_Start(state.State):
    def on_enter(self):
        set_actor(triggerId=11101, visible=False, initialSequence='ks_quest_musical_A01_off') # Dummy Lever C
        set_actor(triggerId=11102, visible=False, initialSequence='ks_quest_musical_A01_off') # Dummy Lever D
        set_actor(triggerId=11103, visible=False, initialSequence='ks_quest_musical_A01_off') # Dummy Lever E
        set_actor(triggerId=11104, visible=False, initialSequence='ks_quest_musical_A01_off') # Dummy Lever F
        set_actor(triggerId=11105, visible=False, initialSequence='ks_quest_musical_A01_off') # Dummy Lever G
        set_actor(triggerId=11106, visible=False, initialSequence='ks_quest_musical_A01_off') # Dummy Lever A
        set_actor(triggerId=11107, visible=False, initialSequence='ks_quest_musical_A01_off') # Dummy Lever B
        set_actor(triggerId=11108, visible=False, initialSequence='ks_quest_musical_A01_off') # Dummy Lever HighC
        set_interact_object(triggerIds=[12000058], state=1) # Lever C
        set_interact_object(triggerIds=[12000059], state=1) # Lever D
        set_interact_object(triggerIds=[12000060], state=1) # Lever E
        set_interact_object(triggerIds=[12000061], state=1) # Lever F
        set_interact_object(triggerIds=[12000062], state=1) # Lever G
        set_interact_object(triggerIds=[12000063], state=1) # Lever A
        set_interact_object(triggerIds=[12000064], state=1) # Lever B
        set_interact_object(triggerIds=[12000065], state=1) # Lever HighC
        set_user_value(triggerId=11001, key='PlayC', value=1)
        set_user_value(triggerId=11002, key='PlayD', value=1)
        set_user_value(triggerId=11003, key='PlayE', value=1)
        set_user_value(triggerId=11004, key='PlayF', value=1)
        set_user_value(triggerId=11005, key='PlayG', value=1)
        set_user_value(triggerId=11006, key='PlayA', value=1)
        set_user_value(triggerId=11007, key='PlayB', value=1)
        set_user_value(triggerId=11008, key='PlayHighC', value=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000058], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000059], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000060], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000061], arg2=0):
            return CheckAnswer01_Delay()
        if object_interacted(interactIds=[12000062], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000063], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000064], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000065], arg2=0):
            return AnswerIsWrong_Delay()
        if user_value(key='Reset', value=1):
            return ResetDelay()


class CheckAnswer01_Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CheckAnswer02_Start()
        if user_value(key='Reset', value=1):
            return ResetDelay()

    def on_exit(self):
        set_interact_object(triggerIds=[12000061], state=1) # Lever F


class CheckAnswer02_Start(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000058], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000059], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000060], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000061], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000062], arg2=0):
            return CheckAnswer02_Delay()
        if object_interacted(interactIds=[12000063], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000064], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000065], arg2=0):
            return AnswerIsWrong_Delay()
        if user_value(key='Reset', value=1):
            return ResetDelay()


class CheckAnswer02_Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CheckAnswer03_Start()
        if user_value(key='Reset', value=1):
            return ResetDelay()

    def on_exit(self):
        set_interact_object(triggerIds=[12000062], state=1) # Lever D


class CheckAnswer03_Start(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000058], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000059], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000060], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000061], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000062], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000063], arg2=0):
            return CheckAnswer03_Delay()
        if object_interacted(interactIds=[12000064], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000065], arg2=0):
            return AnswerIsWrong_Delay()
        if user_value(key='Reset', value=1):
            return ResetDelay()


class CheckAnswer03_Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CheckAnswer04_Start()
        if user_value(key='Reset', value=1):
            return ResetDelay()

    def on_exit(self):
        set_interact_object(triggerIds=[12000063], state=1) # Lever A


class CheckAnswer04_Start(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000058], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000059], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000060], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000061], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000062], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000063], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000064], arg2=0):
            return CheckAnswer04_Delay()
        if object_interacted(interactIds=[12000065], arg2=0):
            return AnswerIsWrong_Delay()
        if user_value(key='Reset', value=1):
            return ResetDelay()


class CheckAnswer04_Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CheckAnswer05_Start()
        if user_value(key='Reset', value=1):
            return ResetDelay()

    def on_exit(self):
        set_interact_object(triggerIds=[12000064], state=1) # Lever B


class CheckAnswer05_Start(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000058], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000059], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000060], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000061], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000062], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000063], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000064], arg2=0):
            return AnswerIsWrong_Delay()
        if object_interacted(interactIds=[12000065], arg2=0):
            return CheckAnswer05_Delay()
        if user_value(key='Reset', value=1):
            return ResetDelay()


class CheckAnswer05_Delay(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Reset', value=1):
            return ResetDelay()
        if wait_tick(waitTick=500):
            return AnswerIsRight()

    def on_exit(self):
        set_interact_object(triggerIds=[12000065], state=1) # Lever B


#  정답 
class AnswerIsRight(state.State):
    def on_enter(self):
        set_user_value(triggerId=11001, key='PlayC', value=0)
        set_user_value(triggerId=11002, key='PlayD', value=0)
        set_user_value(triggerId=11003, key='PlayE', value=0)
        set_user_value(triggerId=11004, key='PlayF', value=0)
        set_user_value(triggerId=11005, key='PlayG', value=0)
        set_user_value(triggerId=11006, key='PlayA', value=0)
        set_user_value(triggerId=11007, key='PlayB', value=0)
        set_user_value(triggerId=11008, key='PlayHighC', value=0)
        set_user_value(triggerId=11000, key='AnswerIsRight', value=1)
        set_interact_object(triggerIds=[12000058], state=0) # Lever C
        set_interact_object(triggerIds=[12000059], state=0) # Lever D
        set_interact_object(triggerIds=[12000060], state=0) # Lever E
        set_interact_object(triggerIds=[12000061], state=0) # Lever F
        set_interact_object(triggerIds=[12000062], state=0) # Lever G
        set_interact_object(triggerIds=[12000063], state=0) # Lever A
        set_interact_object(triggerIds=[12000064], state=0) # Lever B
        set_interact_object(triggerIds=[12000065], state=0) # Lever HighC

    def on_tick(self) -> state.State:
        if user_value(key='Reset', value=1):
            return ResetDelay()


#  오답 
class AnswerIsWrong_Delay(state.State):
    def on_enter(self):
        set_user_value(triggerId=11001, key='PlayC', value=0)
        set_user_value(triggerId=11001, key='PlayC', value=0)
        set_user_value(triggerId=11002, key='PlayD', value=0)
        set_user_value(triggerId=11003, key='PlayE', value=0)
        set_user_value(triggerId=11004, key='PlayF', value=0)
        set_user_value(triggerId=11005, key='PlayG', value=0)
        set_user_value(triggerId=11006, key='PlayA', value=0)
        set_user_value(triggerId=11007, key='PlayB', value=0)
        set_user_value(triggerId=11008, key='PlayHighC', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return AnswerIsWrong()
        if user_value(key='Reset', value=1):
            return ResetDelay()


class AnswerIsWrong(state.State):
    def on_enter(self):
        set_user_value(triggerId=11000, key='AnswerIsWrong', value=1)
        set_interact_object(triggerIds=[12000058], state=0) # Lever C
        set_interact_object(triggerIds=[12000059], state=0) # Lever D
        set_interact_object(triggerIds=[12000060], state=0) # Lever E
        set_interact_object(triggerIds=[12000061], state=0) # Lever F
        set_interact_object(triggerIds=[12000062], state=0) # Lever G
        set_interact_object(triggerIds=[12000063], state=0) # Lever A
        set_interact_object(triggerIds=[12000064], state=0) # Lever B
        set_interact_object(triggerIds=[12000065], state=0) # Lever HighC

    def on_tick(self) -> state.State:
        if user_value(key='Reset', value=1):
            return ResetDelay()
        if user_value(key='Reset', value=0):
            return MelodyPlay01_ReStartDelay01()


#  재도전 딜레이 
class MelodyPlay01_ReStartDelay01(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Reset', value=1):
            return ResetDelay()
        if wait_tick(waitTick=1000):
            return MelodyPlay01_ReStartDelay02()


class MelodyPlay01_ReStartDelay02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[4301], visible=True) # Right Sound Effect
        set_actor(triggerId=11001, visible=True, initialSequence='ks_quest_musical_B01_red') # Bell C
        set_actor(triggerId=11002, visible=True, initialSequence='ks_quest_musical_B01_orange') # Bell D
        set_actor(triggerId=11003, visible=True, initialSequence='ks_quest_musical_B01_yellow') # Bell E
        set_actor(triggerId=11004, visible=True, initialSequence='ks_quest_musical_B01_green') # Bell F
        set_actor(triggerId=11005, visible=True, initialSequence='ks_quest_musical_B01_blue') # Bell G
        set_actor(triggerId=11006, visible=True, initialSequence='ks_quest_musical_B01_navy') # Bell A
        set_actor(triggerId=11007, visible=True, initialSequence='ks_quest_musical_B01_purple') # Bell B
        set_actor(triggerId=11008, visible=True, initialSequence='ks_quest_musical_B01_pink') # Bell HighC

    def on_tick(self) -> state.State:
        if user_value(key='Reset', value=1):
            return ResetDelay()
        if wait_tick(waitTick=1000):
            return StartMelodyQuiz_Delay03()


class StartMelodyQuiz_Delay03(state.State):
    def on_enter(self):
        set_actor(triggerId=11001, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell C
        set_actor(triggerId=11002, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell D
        set_actor(triggerId=11003, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell E
        set_actor(triggerId=11004, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell F
        set_actor(triggerId=11005, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell G
        set_actor(triggerId=11006, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell A
        set_actor(triggerId=11007, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell B
        set_actor(triggerId=11008, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell HighC

    def on_tick(self) -> state.State:
        if user_value(key='Reset', value=1):
            return ResetDelay()
        if wait_tick(waitTick=1000):
            return MelodyPlay01_Start()


#  리셋 
class ResetDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


