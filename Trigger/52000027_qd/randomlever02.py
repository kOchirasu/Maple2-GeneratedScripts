""" trigger/52000027_qd/randomlever02.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000475], state=0)
        self.set_interact_object(triggerIds=[10000476], state=0)
        self.set_interact_object(triggerIds=[10000477], state=0)

    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=30):
            return 번패턴1(self.ctx)
        if self.random_condition(rate=30):
            return 번패턴2(self.ctx)
        if self.random_condition(rate=30):
            return 번패턴3(self.ctx)


# 첫 번째 레버 정답 패턴
class 번패턴1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SetLever', value=1):
            return 번패턴_모든레버켜기1(self.ctx)


class 번패턴_모든레버켜기1(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000475], state=1) # Correct
        self.set_interact_object(triggerIds=[10000476], state=1) # Wrong
        self.set_interact_object(triggerIds=[10000477], state=1) # Wrong

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000475], stateValue=0):
            return 번패턴_정답1(self.ctx)
        if self.object_interacted(interactIds=[10000476], stateValue=0):
            return 번패턴_2번레버_오답01_1(self.ctx)
        if self.object_interacted(interactIds=[10000477], stateValue=0):
            return 번패턴_3번레버_오답01_1(self.ctx)


# 첫 번째 레버 정답 맞춤
class 번패턴_정답1(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000476], state=0) # Wrong
        self.set_interact_object(triggerIds=[10000477], state=0) # Wrong
        self.set_user_value(triggerId=1, key='TrapOpen', value=1)
        self.set_user_value(triggerId=3, key='TrapOpen', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 종료(self.ctx)


# 첫 번째 레버 정답 패턴에서 두 번째 레버 오답
class 번패턴_2번레버_오답01_1(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__0$', arg4=3, arg5=0)
        self.set_interact_object(triggerIds=[10000475], state=0) # Correct
        self.set_interact_object(triggerIds=[10000477], state=0) # Wrong
        self.create_monster(spawnIds=[921], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[921]):
            return 번패턴_2번레버_재도전1(self.ctx)


class 번패턴_2번레버_재도전1(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000475], state=1) # Correct
        self.set_interact_object(triggerIds=[10000477], state=1) # Wrong

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000475], stateValue=0):
            return 번패턴_정답1(self.ctx)
        if self.object_interacted(interactIds=[10000477], stateValue=0):
            return 번패턴_2번레버_오답02_1(self.ctx)


class 번패턴_2번레버_오답02_1(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__1$', arg4=3, arg5=0)
        self.set_interact_object(triggerIds=[10000475], state=0) # Correct
        self.create_monster(spawnIds=[922], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[921]):
            return 번패턴_2번레버_마지막도전1(self.ctx)


class 번패턴_2번레버_마지막도전1(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000475], state=1) # Correct

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000475], stateValue=0):
            return 번패턴_정답1(self.ctx)


# 첫 번째 레버 정답 패턴에서 세 번째 레버 오답
class 번패턴_3번레버_오답01_1(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__0$', arg4=3, arg5=0)
        self.set_interact_object(triggerIds=[10000475], state=0) # Correct
        self.set_interact_object(triggerIds=[10000476], state=0) # Wrong
        self.create_monster(spawnIds=[921], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[921]):
            return 번패턴_3번레버_재도전1(self.ctx)


class 번패턴_3번레버_재도전1(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000475], state=1) # Correct
        self.set_interact_object(triggerIds=[10000476], state=1) # Wrong

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000475], stateValue=0):
            return 번패턴_정답1(self.ctx)
        if self.object_interacted(interactIds=[10000476], stateValue=0):
            return 번패턴_3번레버_오답02_1(self.ctx)


class 번패턴_3번레버_오답02_1(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__1$', arg4=3, arg5=0)
        self.set_interact_object(triggerIds=[10000475], state=0) # Correct
        self.create_monster(spawnIds=[922], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[921]):
            return 번패턴_3번레버_마지막도전1(self.ctx)


class 번패턴_3번레버_마지막도전1(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000475], state=1) # Correct

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000475], stateValue=0):
            return 번패턴_정답1(self.ctx)


# 두 번째 레버 정답 패턴
class 번패턴2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SetLever', value=1):
            return 번패턴_모든레버켜기2(self.ctx)


class 번패턴_모든레버켜기2(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000475], state=1) # Wrong
        self.set_interact_object(triggerIds=[10000476], state=1) # Correct
        self.set_interact_object(triggerIds=[10000477], state=1) # Wrong

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000475], stateValue=0):
            return 번패턴_1번레버_오답01_2(self.ctx)
        if self.object_interacted(interactIds=[10000476], stateValue=0):
            return 번패턴_정답2(self.ctx)
        if self.object_interacted(interactIds=[10000477], stateValue=0):
            return 번패턴_3번레버_오답01_2(self.ctx)


# 두 번째 레버 정답 맞춤
class 번패턴_정답2(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000475], state=0) # Wrong
        self.set_interact_object(triggerIds=[10000477], state=0) # Wrong
        self.set_user_value(triggerId=1, key='TrapOpen', value=1)
        self.set_user_value(triggerId=3, key='TrapOpen', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 종료(self.ctx)


# 두 번째 레버 정답 패턴에서 두 번째 레버 오답
class 번패턴_1번레버_오답01_2(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__0$', arg4=3, arg5=0)
        self.set_interact_object(triggerIds=[10000476], state=0) # Correct
        self.set_interact_object(triggerIds=[10000477], state=0) # Wrong
        self.create_monster(spawnIds=[921], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[921]):
            return 번패턴_1번레버_재도전2(self.ctx)


class 번패턴_1번레버_재도전2(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000476], state=1) # Correct
        self.set_interact_object(triggerIds=[10000477], state=1) # Wrong

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000476], stateValue=0):
            return 번패턴_정답2(self.ctx)
        if self.object_interacted(interactIds=[10000477], stateValue=0):
            return 번패턴_1번레버_오답02_2(self.ctx)


class 번패턴_1번레버_오답02_2(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__1$', arg4=3, arg5=0)
        self.set_interact_object(triggerIds=[10000476], state=0) # Correct
        self.create_monster(spawnIds=[922], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[921]):
            return 번패턴_1번레버_마지막도전2(self.ctx)


class 번패턴_1번레버_마지막도전2(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000476], state=1) # Correct

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000476], stateValue=0):
            return 번패턴_정답2(self.ctx)


# 두 번째 레버 정답 패턴에서 세 번째 레버 오답
class 번패턴_3번레버_오답01_2(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__0$', arg4=3, arg5=0)
        self.set_interact_object(triggerIds=[10000476], state=0) # Correct
        self.set_interact_object(triggerIds=[10000477], state=0) # Wrong
        self.create_monster(spawnIds=[921], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[921]):
            return 번패턴_3번레버_재도전2(self.ctx)


class 번패턴_3번레버_재도전2(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000476], state=1) # Correct
        self.set_interact_object(triggerIds=[10000477], state=1) # Wrong

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000476], stateValue=0):
            return 번패턴_정답2(self.ctx)
        if self.object_interacted(interactIds=[10000477], stateValue=0):
            return 번패턴_3번레버_오답02_2(self.ctx)


class 번패턴_3번레버_오답02_2(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__1$', arg4=3, arg5=0)
        self.set_interact_object(triggerIds=[10000476], state=0) # Correct
        self.create_monster(spawnIds=[922], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[921]):
            return 번패턴_3번레버_마지막도전2(self.ctx)


class 번패턴_3번레버_마지막도전2(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000476], state=1) # Correct

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000476], stateValue=0):
            return 번패턴_정답2(self.ctx)


# 세 번째 레버 정답 패턴
class 번패턴3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SetLever', value=1):
            return 번패턴_모든레버켜기3(self.ctx)


class 번패턴_모든레버켜기3(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000475], state=1) # Wrong
        self.set_interact_object(triggerIds=[10000476], state=1) # Wrong
        self.set_interact_object(triggerIds=[10000477], state=1) # Correct

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000475], stateValue=0):
            return 번패턴_1번레버_오답01_3(self.ctx)
        if self.object_interacted(interactIds=[10000476], stateValue=0):
            return 번패턴_2번레버_오답01_3(self.ctx)
        if self.object_interacted(interactIds=[10000477], stateValue=0):
            return 번패턴_정답3(self.ctx)


# 세 번째 레버 정답 맞춤
class 번패턴_정답3(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000475], state=0) # Wrong
        self.set_interact_object(triggerIds=[10000476], state=0) # Wrong
        self.set_user_value(triggerId=1, key='TrapOpen', value=1)
        self.set_user_value(triggerId=3, key='TrapOpen', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 종료(self.ctx)


# 세 번째 레버 정답 패턴에서 두 번째 레버 오답
class 번패턴_1번레버_오답01_3(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__0$', arg4=3, arg5=0)
        self.set_interact_object(triggerIds=[10000476], state=0) # Wrong
        self.set_interact_object(triggerIds=[10000477], state=0) # Correct
        self.create_monster(spawnIds=[921], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[921]):
            return 번패턴_1번레버_재도전3(self.ctx)


class 번패턴_1번레버_재도전3(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000476], state=1) # Wrong
        self.set_interact_object(triggerIds=[10000477], state=1) # Correct

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000476], stateValue=0):
            return 번패턴_1번레버_오답02_3(self.ctx)
        if self.object_interacted(interactIds=[10000477], stateValue=0):
            return 번패턴_정답3(self.ctx)


class 번패턴_1번레버_오답02_3(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__1$', arg4=3, arg5=0)
        self.set_interact_object(triggerIds=[10000477], state=0) # Correct
        self.create_monster(spawnIds=[922], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[921]):
            return 번패턴_1번레버_마지막도전3(self.ctx)


class 번패턴_1번레버_마지막도전3(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000477], state=1) # Correct

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000477], stateValue=0):
            return 번패턴_정답3(self.ctx)


# 세 번째 레버 정답 패턴에서 세 번째 레버 오답
class 번패턴_2번레버_오답01_3(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__0$', arg4=3, arg5=0)
        self.set_interact_object(triggerIds=[10000475], state=0) # Wrong
        self.set_interact_object(triggerIds=[10000477], state=0) # Correct
        self.create_monster(spawnIds=[921], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[921]):
            return 번패턴_2번레버_재도전3(self.ctx)


class 번패턴_2번레버_재도전3(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000475], state=1) # Wrong
        self.set_interact_object(triggerIds=[10000477], state=1) # Correct

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000475], stateValue=0):
            return 번패턴_2번레버_오답02_3(self.ctx)
        if self.object_interacted(interactIds=[10000477], stateValue=0):
            return 번패턴_정답3(self.ctx)


class 번패턴_2번레버_오답02_3(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52000027_QD__RANDOMLEVER02__1$', arg4=3, arg5=0)
        self.set_interact_object(triggerIds=[10000477], state=0) # Correct
        self.create_monster(spawnIds=[922], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[921]):
            return 번패턴_2번레버_마지막도전3(self.ctx)


class 번패턴_2번레버_마지막도전3(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000477], state=1) # Correct

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000477], stateValue=0):
            return 번패턴_정답3(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
