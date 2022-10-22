""" trigger/02000498_bf/main_3.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344], visible=True, arg3=0, arg4=0, arg5=0)
        set_skill(triggerIds=[704], isEnable=False)
        set_effect(triggerIds=[630], visible=False)
        set_effect(triggerIds=[620], visible=False)
        set_effect(triggerIds=[6301], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 시작대기()


class 시작대기(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_event_ui(type=1, arg2='$02000350_BF__MAIN_3__0$', arg3='2000', arg4='0')
        dark_stream(type='StartRound', round=11, uiDuration=3000, damagePenalty=30)
        set_event_ui(type=0, arg2='11,15,11')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드11()


class 라운드11(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000350_BF__MAIN_3__1$', arg3='4000', arg4='0')
        dark_stream(type='SpawnMonster', spawnIds=[111001], score=295000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[111001]):
            dark_stream(type='ClearRound', round=11)
            set_achievement(triggerId=103, type='trigger', achieve='11roundpass')
            return 라운드대기12()


class 라운드대기12(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='12,15,11')
        dark_stream(type='StartRound', round=12, uiDuration=3000, damagePenalty=30)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드12()


class 라운드12(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[112001], score=78750)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[112001]):
            dark_stream(type='ClearRound', round=12)
            set_achievement(triggerId=103, type='trigger', achieve='12roundpass')
            return 라운드대기13()


class 라운드대기13(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='13,15,11')
        set_timer(timerId='3', seconds=3)
        dark_stream(type='StartRound', round=13, uiDuration=3000, damagePenalty=30)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드13()


class 라운드13(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[113001], score=43750)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[113001]):
            dark_stream(type='ClearRound', round=13)
            set_achievement(triggerId=103, type='trigger', achieve='13roundpass')
            return 라운드대기14()


class 라운드대기14(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='14,15,11')
        dark_stream(type='StartRound', round=14, uiDuration=3000, damagePenalty=30)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드14()


class 라운드14(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[114001], score=48750)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[114001]):
            dark_stream(type='ClearRound', round=14)
            set_achievement(triggerId=103, type='trigger', achieve='14roundpass')
            return 라운드대기15()


class 라운드대기15(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='15,15,11')
        set_effect(triggerIds=[6301], visible=True)
        dark_stream(type='StartRound', round=15, uiDuration=3000, damagePenalty=30)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드15()


class 라운드15(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[115001], score=415000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[115001]):
            dark_stream(type='ClearRound', round=15)
            set_achievement(triggerId=103, type='trigger', achieve='15roundpass')
            return 바닥부심()


class 바닥부심(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[600], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            set_effect(triggerIds=[630], visible=True)
            set_skill(triggerIds=[704], isEnable=True)
            set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344], visible=False, arg3=0, arg4=0, arg5=0)
            return 종료()


class 종료(state.State):
    pass


