""" trigger/02000047_bf/02_mob.xml """
from common import *
import state


class 반응대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000078], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000078], arg2=0):
            return 몬스터리젠()


class 몬스터리젠(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102])
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 우레우스대사()


class 우레우스대사(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000047_BF__02_MOB__0$', arg4=3)
        set_conversation(type=1, spawnId=102, script='$02000047_BF__02_MOB__1$', arg4=3)
        set_timer(timerId='1', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 몬스터와전투()
        """
        <onExit>
            <action name="몬스터를생성한다" arg1="102"/>
        </onExit>
        """


class 몬스터와전투(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102]):
            return 트리거초기화()
        if not monster_in_combat(boxIds=[102]):
            return 우레우스소멸()


class 우레우스소멸(state.State):
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
            return 우레우스소멸()


class 트리거초기화(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[102]):
            return 우레우스소멸()
        if not monster_in_combat(boxIds=[102]):
            destroy_monster(spawnIds=[102])
            return 반응대기()


