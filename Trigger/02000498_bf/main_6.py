""" trigger/02000498_bf/main_6.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3601], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[6601], visible=False)
        set_effect(triggerIds=[6602], visible=False)
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[106]):
            return 시작대기()


class 시작대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6601], visible=True)
        dark_stream(type='StartRound', round=26, uiDuration=3000, damagePenalty=200)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            set_event_ui(type=0, arg2='26,30,26')
            return 라운드26()


class 라운드26(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000350_BF__MAIN_6__0$', arg3='4000', arg4='0')
        dark_stream(type='SpawnMonster', spawnIds=[126001], score=2200000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[126001]):
            dark_stream(type='ClearRound', round=26)
            set_achievement(triggerId=106, type='trigger', achieve='26roundpass')
            return 라운드대기27()


class 라운드대기27(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6601], visible=True)
        dark_stream(type='StartRound', round=27, uiDuration=3000, damagePenalty=200)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            set_event_ui(type=0, arg2='27,30,26')
            return 라운드27()


class 라운드27(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[127001], score=2500000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[127001]):
            dark_stream(type='ClearRound', round=27)
            set_achievement(triggerId=106, type='trigger', achieve='27roundpass')
            return 라운드대기28()


class 라운드대기28(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6601], visible=True)
        dark_stream(type='StartRound', round=28, uiDuration=3000, damagePenalty=200)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            set_event_ui(type=0, arg2='28,30,26')
            return 라운드28()


class 라운드28(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[128001], score=3000000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[128001]):
            dark_stream(type='ClearRound', round=28)
            set_achievement(triggerId=106, type='trigger', achieve='28roundpass')
            return 라운드대기29()


class 라운드대기29(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6601], visible=True)
        dark_stream(type='StartRound', round=29, uiDuration=3000, damagePenalty=200)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            set_event_ui(type=0, arg2='29,30,26')
            return 라운드29()


class 라운드29(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[129001], score=5000000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[129001]):
            dark_stream(type='ClearRound', round=29)
            set_achievement(triggerId=106, type='trigger', achieve='29roundpass')
            return 라운드대기30()


class 라운드대기30(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6602], visible=True)
        dark_stream(type='StartRound', round=30, uiDuration=3000, damagePenalty=200)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            set_event_ui(type=0, arg2='30,30,26')
            return 라운드30()


class 라운드30(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3601], visible=True, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[130001], arg2=True)
        dark_stream(type='SpawnMonster', spawnIds=[130002], score=8000000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[130002]):
            set_mesh(triggerIds=[3601], visible=False, arg3=0, arg4=0, arg5=0)
            destroy_monster(spawnIds=[130001])
            dark_stream(type='ClearRound', round=30)
            set_achievement(triggerId=106, type='trigger', achieve='30roundpass')
            return 성공()


class 성공(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='0,0')
        set_event_ui(type=7, arg2='$02000350_BF__MAIN_6__1$', arg3='3000', arg4='0')
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 포털생성()


class 포털생성(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000350_BF__MAIN_6__2$', arg3='2500', arg4='0')
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True)


