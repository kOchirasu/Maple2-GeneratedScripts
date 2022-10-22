""" trigger/02000304_bf/move.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 몬스터체크()


class 몬스터체크(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[2001]):
            return 카운트랜덤()


class 카운트랜덤(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=25):
            return 이동대기01()
        if random_condition(rate=25):
            return 이동대기02()
        if random_condition(rate=25):
            return 이동대기03()
        if random_condition(rate=25):
            return 이동대기04()


class 이동대기01(state.State):
    def on_enter(self):
        set_timer(timerId='90', seconds=90)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='90'):
            return 이동()


class 이동대기02(state.State):
    def on_enter(self):
        set_timer(timerId='100', seconds=100)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='100'):
            return 이동()


class 이동대기03(state.State):
    def on_enter(self):
        set_timer(timerId='110', seconds=110)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='110'):
            return 이동()


class 이동대기04(state.State):
    def on_enter(self):
        set_timer(timerId='120', seconds=120)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='120'):
            return 이동()


class 이동(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_conversation(type=1, spawnId=2001, script='$02000304_BF__MOVE__0$', arg4=2)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='2'):
            set_conversation(type=1, spawnId=2001, script='$02000304_BF__MOVE__1$', arg4=1)
            move_random_user(mapId=2000304, portalId=11, triggerId=101, count=1)
            return 이동2()


class 이동2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='1'):
            set_conversation(type=1, spawnId=2001, script='$02000304_BF__MOVE__2$', arg4=1)
            move_random_user(mapId=2000304, portalId=12, triggerId=101, count=1)
            return 이동3()


class 이동3(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='1'):
            set_conversation(type=1, spawnId=2001, script='$02000304_BF__MOVE__3$', arg4=1)
            move_random_user(mapId=2000304, portalId=13, triggerId=101, count=1)
            return 이동4()


class 이동4(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='1'):
            set_conversation(type=1, spawnId=2001, script='$02000304_BF__MOVE__4$', arg4=1)
            move_random_user(mapId=2000304, portalId=14, triggerId=101, count=1)
            return 대기()


class 종료(state.State):
    def on_enter(self):
        set_timer(timerId='1800000', seconds=1800000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1800000'):
            return None # Missing State: 종료2


