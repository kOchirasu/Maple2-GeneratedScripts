""" trigger/02000498_bf/main_5.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416,3417,3418,3419,3420,3421,3422,3423,3424], visible=True, arg3=0, arg4=0, arg5=0)
        set_skill(triggerIds=[706], isEnable=False)
        set_effect(triggerIds=[640], visible=False)
        set_effect(triggerIds=[650], visible=False)
        set_effect(triggerIds=[6501], visible=False)
        set_effect(triggerIds=[6502], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[105]):
            return 시작대기()


class 시작대기(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='21,25,21')
        set_timer(timerId='3', seconds=3)
        dark_stream(type='StartRound', round=21, uiDuration=3000, damagePenalty=100)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드21()


class 라운드21(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000350_BF__MAIN_5__0$', arg3='4000', arg4='0')
        dark_stream(type='SpawnMonster', spawnIds=[121001], score=110000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[121001]):
            dark_stream(type='ClearRound', round=21)
            set_achievement(triggerId=105, type='trigger', achieve='21roundpass')
            return 라운드대기22()


class 라운드대기22(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='22,25,21')
        dark_stream(type='StartRound', round=22, uiDuration=3000, damagePenalty=100)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드22()


class 라운드22(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[122001,122002,122003], score=70000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[122001,122002,122003]):
            dark_stream(type='ClearRound', round=22)
            set_achievement(triggerId=105, type='trigger', achieve='22roundpass')
            return 라운드대기23()


class 라운드대기23(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_event_ui(type=0, arg2='23,25,21')
        dark_stream(type='StartRound', round=23, uiDuration=3000, damagePenalty=100)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드23()


class 라운드23(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[123001], score=80000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[123001]):
            dark_stream(type='ClearRound', round=23)
            set_achievement(triggerId=105, type='trigger', achieve='23roundpass')
            return 라운드대기24()


class 라운드대기24(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='24,25,21')
        dark_stream(type='StartRound', round=24, uiDuration=3000, damagePenalty=100)
        set_event_ui(type=1, arg2='$02000350_BF__MAIN_5__1$', arg3='2000', arg4='0')
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드24()


class 라운드24(state.State):
    def on_enter(self):
        set_timer(timerId='30', seconds=30, clearAtZero=True, display=True, arg5=80)
        create_monster(spawnIds=[124099], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            destroy_monster(spawnIds=[124099])
            reset_timer(timerId='30')
            dark_stream(type='ClearRound', round=24)
            set_achievement(triggerId=105, type='trigger', achieve='24roundpass')
            return 라운드대기25()


class 라운드대기25(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='25,25,21')
        set_effect(triggerIds=[6501], visible=True)
        set_effect(triggerIds=[6502], visible=True)
        dark_stream(type='StartRound', round=25, uiDuration=3000, damagePenalty=100)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드25()


class 라운드25(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[125001,125002], score=750000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[125001,125002]):
            dark_stream(type='ClearRound', round=25)
            set_achievement(triggerId=105, type='trigger', achieve='25roundpass')
            return 바닥부심()


class 바닥부심(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[600], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            set_effect(triggerIds=[650], visible=True)
            set_skill(triggerIds=[706], isEnable=True)
            set_mesh(triggerIds=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416,3417,3418,3419,3420,3421,3422,3423,3424], visible=False, arg3=0, arg4=0, arg5=0)
            return 종료()


class 종료(state.State):
    pass


