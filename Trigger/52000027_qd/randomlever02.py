""" trigger/52000027_qd/randomlever02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000475], state=0)
        set_interact_object(triggerIds=[10000476], state=0)
        set_interact_object(triggerIds=[10000477], state=0)

    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return 번패턴1()
        if random_condition(rate=30):
            return 번패턴2()
        if random_condition(rate=30):
            return 번패턴3()


#  첫 번째 레버 정답 패턴 
class 번패턴1(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='SetLever', value=1):
            return 번패턴_모든레버켜기1()


class 번패턴_모든레버켜기1(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000475], state=1) # Correct
        set_interact_object(triggerIds=[10000476], state=1) # Wrong
        set_interact_object(triggerIds=[10000477], state=1) # Wrong

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000475], arg2=0):
            return 번패턴_정답1()
        if object_interacted(interactIds=[10000476], arg2=0):
            return 번패턴_2번레버_오답01_1()
        if object_interacted(interactIds=[10000477], arg2=0):
            return 번패턴_3번레버_오답01_1()


#  첫 번째 레버 정답 맞춤 
class 번패턴_정답1(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000476], state=0) # Wrong
        set_interact_object(triggerIds=[10000477], state=0) # Wrong
        set_user_value(triggerId=1, key='TrapOpen', value=1)
        set_user_value(triggerId=3, key='TrapOpen', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 종료()


#  첫 번째 레버 정답 패턴에서 두 번째 레버 오답 
class 번패턴_2번레버_오답01_1(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__0$', arg4=3, arg5=0)
        set_interact_object(triggerIds=[10000475], state=0) # Correct
        set_interact_object(triggerIds=[10000477], state=0) # Wrong
        create_monster(spawnIds=[921], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[921]):
            return 번패턴_2번레버_재도전1()


class 번패턴_2번레버_재도전1(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000475], state=1) # Correct
        set_interact_object(triggerIds=[10000477], state=1) # Wrong

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000475], arg2=0):
            return 번패턴_정답1()
        if object_interacted(interactIds=[10000477], arg2=0):
            return 번패턴_2번레버_오답02_1()


class 번패턴_2번레버_오답02_1(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__1$', arg4=3, arg5=0)
        set_interact_object(triggerIds=[10000475], state=0) # Correct
        create_monster(spawnIds=[922], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[921]):
            return 번패턴_2번레버_마지막도전1()


class 번패턴_2번레버_마지막도전1(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000475], state=1) # Correct

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000475], arg2=0):
            return 번패턴_정답1()


#  첫 번째 레버 정답 패턴에서 세 번째 레버 오답 
class 번패턴_3번레버_오답01_1(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__0$', arg4=3, arg5=0)
        set_interact_object(triggerIds=[10000475], state=0) # Correct
        set_interact_object(triggerIds=[10000476], state=0) # Wrong
        create_monster(spawnIds=[921], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[921]):
            return 번패턴_3번레버_재도전1()


class 번패턴_3번레버_재도전1(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000475], state=1) # Correct
        set_interact_object(triggerIds=[10000476], state=1) # Wrong

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000475], arg2=0):
            return 번패턴_정답1()
        if object_interacted(interactIds=[10000476], arg2=0):
            return 번패턴_3번레버_오답02_1()


class 번패턴_3번레버_오답02_1(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__1$', arg4=3, arg5=0)
        set_interact_object(triggerIds=[10000475], state=0) # Correct
        create_monster(spawnIds=[922], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[921]):
            return 번패턴_3번레버_마지막도전1()


class 번패턴_3번레버_마지막도전1(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000475], state=1) # Correct

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000475], arg2=0):
            return 번패턴_정답1()


#  두 번째 레버 정답 패턴 
class 번패턴2(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='SetLever', value=1):
            return 번패턴_모든레버켜기2()


class 번패턴_모든레버켜기2(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000475], state=1) # Wrong
        set_interact_object(triggerIds=[10000476], state=1) # Correct
        set_interact_object(triggerIds=[10000477], state=1) # Wrong

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000475], arg2=0):
            return 번패턴_1번레버_오답01_2()
        if object_interacted(interactIds=[10000476], arg2=0):
            return 번패턴_정답2()
        if object_interacted(interactIds=[10000477], arg2=0):
            return 번패턴_3번레버_오답01_2()


#  두 번째 레버 정답 맞춤 
class 번패턴_정답2(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000475], state=0) # Wrong
        set_interact_object(triggerIds=[10000477], state=0) # Wrong
        set_user_value(triggerId=1, key='TrapOpen', value=1)
        set_user_value(triggerId=3, key='TrapOpen', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 종료()


#  두 번째 레버 정답 패턴에서 두 번째 레버 오답 
class 번패턴_1번레버_오답01_2(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__0$', arg4=3, arg5=0)
        set_interact_object(triggerIds=[10000476], state=0) # Correct
        set_interact_object(triggerIds=[10000477], state=0) # Wrong
        create_monster(spawnIds=[921], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[921]):
            return 번패턴_1번레버_재도전2()


class 번패턴_1번레버_재도전2(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000476], state=1) # Correct
        set_interact_object(triggerIds=[10000477], state=1) # Wrong

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000476], arg2=0):
            return 번패턴_정답2()
        if object_interacted(interactIds=[10000477], arg2=0):
            return 번패턴_1번레버_오답02_2()


class 번패턴_1번레버_오답02_2(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__1$', arg4=3, arg5=0)
        set_interact_object(triggerIds=[10000476], state=0) # Correct
        create_monster(spawnIds=[922], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[921]):
            return 번패턴_1번레버_마지막도전2()


class 번패턴_1번레버_마지막도전2(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000476], state=1) # Correct

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000476], arg2=0):
            return 번패턴_정답2()


#  두 번째 레버 정답 패턴에서 세 번째 레버 오답 
class 번패턴_3번레버_오답01_2(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__0$', arg4=3, arg5=0)
        set_interact_object(triggerIds=[10000476], state=0) # Correct
        set_interact_object(triggerIds=[10000477], state=0) # Wrong
        create_monster(spawnIds=[921], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[921]):
            return 번패턴_3번레버_재도전2()


class 번패턴_3번레버_재도전2(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000476], state=1) # Correct
        set_interact_object(triggerIds=[10000477], state=1) # Wrong

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000476], arg2=0):
            return 번패턴_정답2()
        if object_interacted(interactIds=[10000477], arg2=0):
            return 번패턴_3번레버_오답02_2()


class 번패턴_3번레버_오답02_2(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__1$', arg4=3, arg5=0)
        set_interact_object(triggerIds=[10000476], state=0) # Correct
        create_monster(spawnIds=[922], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[921]):
            return 번패턴_3번레버_마지막도전2()


class 번패턴_3번레버_마지막도전2(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000476], state=1) # Correct

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000476], arg2=0):
            return 번패턴_정답2()


#  세 번째 레버 정답 패턴 
class 번패턴3(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='SetLever', value=1):
            return 번패턴_모든레버켜기3()


class 번패턴_모든레버켜기3(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000475], state=1) # Wrong
        set_interact_object(triggerIds=[10000476], state=1) # Wrong
        set_interact_object(triggerIds=[10000477], state=1) # Correct

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000475], arg2=0):
            return 번패턴_1번레버_오답01_3()
        if object_interacted(interactIds=[10000476], arg2=0):
            return 번패턴_2번레버_오답01_3()
        if object_interacted(interactIds=[10000477], arg2=0):
            return 번패턴_정답3()


#  세 번째 레버 정답 맞춤 
class 번패턴_정답3(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000475], state=0) # Wrong
        set_interact_object(triggerIds=[10000476], state=0) # Wrong
        set_user_value(triggerId=1, key='TrapOpen', value=1)
        set_user_value(triggerId=3, key='TrapOpen', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 종료()


#  세 번째 레버 정답 패턴에서 두 번째 레버 오답 
class 번패턴_1번레버_오답01_3(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__0$', arg4=3, arg5=0)
        set_interact_object(triggerIds=[10000476], state=0) # Wrong
        set_interact_object(triggerIds=[10000477], state=0) # Correct
        create_monster(spawnIds=[921], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[921]):
            return 번패턴_1번레버_재도전3()


class 번패턴_1번레버_재도전3(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000476], state=1) # Wrong
        set_interact_object(triggerIds=[10000477], state=1) # Correct

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000476], arg2=0):
            return 번패턴_1번레버_오답02_3()
        if object_interacted(interactIds=[10000477], arg2=0):
            return 번패턴_정답3()


class 번패턴_1번레버_오답02_3(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__1$', arg4=3, arg5=0)
        set_interact_object(triggerIds=[10000477], state=0) # Correct
        create_monster(spawnIds=[922], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[921]):
            return 번패턴_1번레버_마지막도전3()


class 번패턴_1번레버_마지막도전3(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000477], state=1) # Correct

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000477], arg2=0):
            return 번패턴_정답3()


#  세 번째 레버 정답 패턴에서 세 번째 레버 오답 
class 번패턴_2번레버_오답01_3(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__0$', arg4=3, arg5=0)
        set_interact_object(triggerIds=[10000475], state=0) # Wrong
        set_interact_object(triggerIds=[10000477], state=0) # Correct
        create_monster(spawnIds=[921], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[921]):
            return 번패턴_2번레버_재도전3()


class 번패턴_2번레버_재도전3(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000475], state=1) # Wrong
        set_interact_object(triggerIds=[10000477], state=1) # Correct

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000475], arg2=0):
            return 번패턴_2번레버_오답02_3()
        if object_interacted(interactIds=[10000477], arg2=0):
            return 번패턴_정답3()


class 번패턴_2번레버_오답02_3(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__1$', arg4=3, arg5=0)
        set_interact_object(triggerIds=[10000477], state=0) # Correct
        create_monster(spawnIds=[922], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[921]):
            return 번패턴_2번레버_마지막도전3()


class 번패턴_2번레버_마지막도전3(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000477], state=1) # Correct

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000477], arg2=0):
            return 번패턴_정답3()


class 종료(state.State):
    pass


