""" trigger/02000498_bf/main_4.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521,3522,3523,3524,3525,3526,3527,3528], visible=True, arg3=0, arg4=0, arg5=0)
        set_skill(triggerIds=[705], isEnable=False)
        set_effect(triggerIds=[6401], visible=False)
        set_effect(triggerIds=[640], visible=False)
        set_effect(triggerIds=[630], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return 시작대기()


class 시작대기(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='16,20,16')
        dark_stream(type='StartRound', round=16, uiDuration=3000, damagePenalty=50)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드16()


class 라운드16(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000350_BF__MAIN_4__0$', arg3='4000', arg4='0')
        dark_stream(type='SpawnMonster', spawnIds=[116001], score=73000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[116001]):
            dark_stream(type='ClearRound', round=16)
            set_achievement(triggerId=104, type='trigger', achieve='16roundpass')
            return 라운드대기17()


class 라운드대기17(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='17,20,16')
        dark_stream(type='StartRound', round=17, uiDuration=3000, damagePenalty=50)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드17()


class 라운드17(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[117001], score=56250)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[117001]):
            dark_stream(type='ClearRound', round=17)
            set_achievement(triggerId=104, type='trigger', achieve='17roundpass')
            return 라운드대기18()


class 라운드대기18(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='18,20,16')
        set_timer(timerId='3', seconds=3)
        dark_stream(type='StartRound', round=18, uiDuration=3000, damagePenalty=50)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드18()


class 라운드18(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[118001], score=90000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[118001]):
            dark_stream(type='ClearRound', round=18)
            set_achievement(triggerId=104, type='trigger', achieve='18roundpass')
            return 라운드대기19()


class 라운드대기19(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='19,20,16')
        set_timer(timerId='3', seconds=3)
        dark_stream(type='StartRound', round=19, uiDuration=3000, damagePenalty=50)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드19()


class 라운드19(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[119001,119002], score=80000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[119001,119002]):
            dark_stream(type='ClearRound', round=19)
            set_achievement(triggerId=104, type='trigger', achieve='19roundpass')
            return 라운드대기20()


class 라운드대기20(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='20,20,16')
        set_effect(triggerIds=[6401], visible=True)
        set_timer(timerId='3', seconds=3)
        dark_stream(type='StartRound', round=20, uiDuration=3000, damagePenalty=50)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드20()


class 라운드20(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[120001], score=600000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[120001]):
            dark_stream(type='ClearRound', round=20)
            set_achievement(triggerId=104, type='trigger', achieve='20roundpass')
            return 바닥부심()


class 바닥부심(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[600], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            set_effect(triggerIds=[640], visible=True)
            set_skill(triggerIds=[705], isEnable=True)
            set_mesh(triggerIds=[3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521,3522,3523,3524,3525,3526,3527,3528], visible=False, arg3=0, arg4=0, arg5=0)
            return 종료()


class 종료(state.State):
    pass


