""" trigger/02000046_ad/01_mob.xml """
from common import *
import state


class 반응대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000084], state=1)
        set_interact_object(triggerIds=[10000085], state=1)
        set_interact_object(triggerIds=[10000086], state=1)
        set_interact_object(triggerIds=[10000087], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000084,10000085,10000086,10000087], arg2=0):
            return 몬스터리젠()


class 몬스터리젠(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101])
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 카단대사()


class 카단대사(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02000046_AD__01_MOB__0$', arg4=2)
        set_conversation(type=1, spawnId=101, script='$02000046_AD__01_MOB__1$', arg4=2)
        set_conversation(type=1, spawnId=101, script='$02000046_AD__01_MOB__2$', arg4=2)
        set_timer(timerId='1', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            destroy_monster(spawnIds=[101])
            return 휴지()

    def on_exit(self):
        create_monster(spawnIds=[102], arg2=True)


class 휴지(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 몬스터와전투()


class 몬스터와전투(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102]):
            return 소멸대기()
        if not monster_in_combat(boxIds=[102]):
            return 카단소멸()


class 카단소멸(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[102]):
            reset_timer(timerId='1')
            return None
        if monster_dead(boxIds=[102]):
            return 소멸대기()
        if time_expired(timerId='1'):
            return 소멸대기()


class 소멸대기(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 트리거초기화()
        if monster_in_combat(boxIds=[102]):
            return 카단소멸()


class 트리거초기화(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[102]):
            return 카단소멸()
        if not monster_in_combat(boxIds=[102]):
            destroy_monster(spawnIds=[102])
            return 반응대기()


