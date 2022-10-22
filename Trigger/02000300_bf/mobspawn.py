""" trigger/02000300_bf/mobspawn.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[1099]):
            return 랜덤생성조건()
        if monster_dead(boxIds=[1099]):
            return 소멸()


class 랜덤생성조건(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=25):
            return 초40()
        if random_condition(rate=25):
            return 초35()
        if random_condition(rate=25):
            return 초30()
        if random_condition(rate=25):
            return 초45()


class 초40(state.State):
    def on_enter(self):
        set_timer(timerId='45', seconds=45)

    def on_tick(self) -> state.State:
        if time_expired(timerId='45'):
            return 생성()
        if monster_dead(boxIds=[1099]):
            return 소멸()


class 초35(state.State):
    def on_enter(self):
        set_timer(timerId='50', seconds=50)

    def on_tick(self) -> state.State:
        if time_expired(timerId='50'):
            return 생성()
        if monster_dead(boxIds=[1099]):
            return 소멸()


class 초30(state.State):
    def on_enter(self):
        set_timer(timerId='55', seconds=55)

    def on_tick(self) -> state.State:
        if time_expired(timerId='55'):
            return 생성()
        if monster_dead(boxIds=[1099]):
            return 소멸()


class 초45(state.State):
    def on_enter(self):
        set_timer(timerId='60', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='60'):
            return 생성()
        if monster_dead(boxIds=[1099]):
            return 소멸()


class 생성(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1099, script='$02000300_BF__MOBSPAWN__0$', arg4=2)
        set_conversation(type=1, spawnId=1001, script='$02000300_BF__MOBSPAWN__1$', arg4=3)
        create_monster(spawnIds=[1097,1098], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1097,1098]):
            return 랜덤생성조건()
        if monster_dead(boxIds=[1099]):
            return 소멸()


class 소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1098])
        destroy_monster(spawnIds=[1097])


