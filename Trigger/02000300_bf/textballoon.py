""" trigger/02000300_bf/textballoon.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[1099]):
            return 랜덤대화()
        if monster_dead(boxIds=[1099]):
            return 종료대화()


class 랜덤대화(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=25):
            return 초20()
        if random_condition(rate=25):
            return 초25()
        if random_condition(rate=25):
            return 초30()
        if random_condition(rate=25):
            return 초35()
        if monster_dead(boxIds=[1099]):
            return 종료대화()


class 초20(state.State):
    def on_enter(self):
        set_timer(timerId='20', seconds=20)

    def on_tick(self) -> state.State:
        if time_expired(timerId='20'):
            return 대화()
        if monster_dead(boxIds=[1099]):
            return 종료대화()


class 초25(state.State):
    def on_enter(self):
        set_timer(timerId='25', seconds=25)

    def on_tick(self) -> state.State:
        if time_expired(timerId='25'):
            return 대화()
        if monster_dead(boxIds=[1099]):
            return 종료대화()


class 초30(state.State):
    def on_enter(self):
        set_timer(timerId='30', seconds=30)

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            return 대화()
        if monster_dead(boxIds=[1099]):
            return 종료대화()


class 초35(state.State):
    def on_enter(self):
        set_timer(timerId='35', seconds=35)

    def on_tick(self) -> state.State:
        if time_expired(timerId='35'):
            return 대화()
        if monster_dead(boxIds=[1099]):
            return 종료대화()


class 대화(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=25):
            return 대사1()
        if random_condition(rate=25):
            return 대사2()
        if random_condition(rate=25):
            return 대사3()
        if random_condition(rate=25):
            return 대사4()


class 대사1(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_conversation(type=1, spawnId=1002, script='$02000300_BF__TEXTBALLOON__0$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 대기()


class 대사2(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_conversation(type=1, spawnId=1003, script='$02000300_BF__TEXTBALLOON__1$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 대기()


class 대사3(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_conversation(type=1, spawnId=1003, script='$02000300_BF__TEXTBALLOON__2$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 대기()


class 대사4(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_conversation(type=1, spawnId=1004, script='$02000300_BF__TEXTBALLOON__3$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 대기()


class 종료대화(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            set_conversation(type=1, spawnId=1001, script='$02000300_BF__TEXTBALLOON__4$', arg4=3, arg5=0)
            set_conversation(type=1, spawnId=1003, script='$02000300_BF__TEXTBALLOON__5$', arg4=2, arg5=2)
            set_conversation(type=1, spawnId=1002, script='$02000300_BF__TEXTBALLOON__6$', arg4=2, arg5=4)
            return 종료()


class 종료(state.State):
    pass


