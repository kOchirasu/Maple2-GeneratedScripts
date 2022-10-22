""" trigger/02000498_bf/main_2.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[610], visible=False)
        set_effect(triggerIds=[620], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[6110], visible=False)
        set_effect(triggerIds=[6111], visible=False)
        set_effect(triggerIds=[6112], visible=False)
        set_effect(triggerIds=[6113], visible=False)
        set_effect(triggerIds=[6201], visible=False)
        set_skill(triggerIds=[703], isEnable=False)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 시작대기()


class 시작대기(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='6,10,6')
        dark_stream(type='StartRound', round=6, uiDuration=3000, damagePenalty=10)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드6()


class 라운드6(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000350_BF__MAIN_2__0$', arg3='4000', arg4='0')
        dark_stream(type='SpawnMonster', spawnIds=[106001,106002,106003,106004,106005], score=18000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[106001,106002,106003,106004,106005]):
            dark_stream(type='ClearRound', round=6)
            set_achievement(triggerId=102, type='trigger', achieve='6roundpass')
            return 라운드대기7()


class 라운드대기7(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='7,10,6')
        dark_stream(type='StartRound', round=7, uiDuration=3000, damagePenalty=10)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드7()


class 라운드7(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[107001,107002,107003,107004,107005], score=22000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[107001,107002,107003,107004,107005]):
            dark_stream(type='ClearRound', round=7)
            set_achievement(triggerId=102, type='trigger', achieve='7roundpass')
            return 라운드대기8()


class 라운드대기8(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='8,10,6')
        set_timer(timerId='3', seconds=3)
        dark_stream(type='StartRound', round=8, uiDuration=3000, damagePenalty=10)
        set_event_ui(type=1, arg2='$02000350_BF__MAIN_2__1$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드8()


class 라운드8(state.State):
    def on_enter(self):
        set_timer(timerId='30', seconds=30, clearAtZero=True, display=True, arg5=80)
        create_monster(spawnIds=[108099], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            destroy_monster(spawnIds=[108099])
            reset_timer(timerId='30')
            dark_stream(type='ClearRound', round=8)
            set_achievement(triggerId=102, type='trigger', achieve='8roundpass')
            return 라운드대기9()


class 라운드대기9(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='9,10,6')
        set_timer(timerId='3', seconds=3)
        dark_stream(type='StartRound', round=9, uiDuration=3000, damagePenalty=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드9()


class 라운드9(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[109001,109002,109003,109004], score=65000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[109001,109002,109003,109004]):
            dark_stream(type='ClearRound', round=9)
            set_achievement(triggerId=102, type='trigger', achieve='9roundpass')
            return 라운드대기10()


class 라운드대기10(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='10,10,6')
        set_effect(triggerIds=[6201], visible=True)
        dark_stream(type='StartRound', round=10, uiDuration=3000, damagePenalty=10)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드10()


class 라운드10(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[110001], score=270000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[110001]):
            dark_stream(type='ClearRound', round=10)
            set_achievement(triggerId=102, type='trigger', achieve='10roundpass')
            return 바닥부심()


class 바닥부심(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[600], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            set_effect(triggerIds=[620], visible=True)
            set_skill(triggerIds=[703], isEnable=True)
            set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235], visible=False, arg3=0, arg4=0, arg5=0)
            set_event_ui(type=0, arg2='0,0')
            return 종료()


class 종료(state.State):
    pass


