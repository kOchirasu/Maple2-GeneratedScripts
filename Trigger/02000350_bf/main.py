""" trigger/02000350_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=False)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[610], visible=False)
        set_effect(triggerIds=[6010], visible=False)
        set_effect(triggerIds=[6011], visible=False)
        set_effect(triggerIds=[6012], visible=False)
        set_effect(triggerIds=[6013], visible=False)
        set_effect(triggerIds=[6015], visible=False)
        set_effect(triggerIds=[6110], visible=False)
        set_effect(triggerIds=[6111], visible=False)
        set_effect(triggerIds=[6112], visible=False)
        set_effect(triggerIds=[6113], visible=False)
        set_effect(triggerIds=[6101], visible=False)
        set_skill(triggerIds=[701], isEnable=False)
        set_skill(triggerIds=[702], isEnable=False)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            return 시작대기()


class 시작대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6010], visible=True)
        set_effect(triggerIds=[6011], visible=True)
        set_effect(triggerIds=[6012], visible=True)
        set_effect(triggerIds=[6013], visible=True)
        set_effect(triggerIds=[6015], visible=True)
        set_event_ui(type=1, arg2='$02000350_BF__MAIN__0$', arg3='3000', arg4='0')
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 안내02()


class 안내02(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000350_BF__MAIN__1$', arg3='3000', arg4='0')
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 안내03()


class 안내03(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000350_BF__MAIN__2$', arg3='4000', arg4='0')
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 진동대기()


class 진동대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=True)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 유저감지()


class 유저감지(state.State):
    def on_enter(self):
        dark_stream(type='StartGame', round=30)
        set_effect(triggerIds=[601], visible=True)
        set_skill(triggerIds=[701], isEnable=True)
        set_effect(triggerIds=[6010], visible=False)
        set_effect(triggerIds=[6011], visible=False)
        set_effect(triggerIds=[6012], visible=False)
        set_effect(triggerIds=[6013], visible=False)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 라운드대기1()


class 라운드대기1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6110], visible=True)
        set_effect(triggerIds=[6111], visible=True)
        set_effect(triggerIds=[6112], visible=True)
        set_effect(triggerIds=[6113], visible=True)
        set_timer(timerId='3', seconds=3)
        dark_stream(type='StartRound', round=1, uiDuration=3000, damagePenalty=5)
        set_event_ui(type=0, arg2='1,5,1')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드1()


class 라운드1(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[101001], score=6000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101001]):
            dark_stream(type='ClearRound', round=1)
            set_achievement(triggerId=101, type='trigger', achieve='1roundpass')
            return 라운드대기2()


class 라운드대기2(state.State):
    def on_enter(self):
        dark_stream(type='StartRound', round=2, uiDuration=3000, damagePenalty=5)
        set_timer(timerId='3', seconds=3)
        set_event_ui(type=0, arg2='2,5,1')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드2()


class 라운드2(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[102001], score=6000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102001]):
            dark_stream(type='ClearRound', round=2)
            set_achievement(triggerId=101, type='trigger', achieve='2roundpass')
            return 라운드대기3()


class 라운드대기3(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='3,5,1')
        dark_stream(type='StartRound', round=3, uiDuration=3000, damagePenalty=5)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드3()


class 라운드3(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[103001], score=16000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[103001]):
            dark_stream(type='ClearRound', round=3)
            set_achievement(triggerId=101, type='trigger', achieve='3roundpass')
            return 라운드대기4()


class 라운드대기4(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='4,5,1')
        set_timer(timerId='3', seconds=3)
        dark_stream(type='StartRound', round=4, uiDuration=3000, damagePenalty=5)
        set_event_ui(type=1, arg2='$02000350_BF__MAIN__3$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            set_event_ui(type=0, arg2='4,5,1')
            return 라운드4()


class 라운드4(state.State):
    def on_enter(self):
        set_timer(timerId='30', seconds=30, clearAtZero=True, display=True, arg5=80)
        create_monster(spawnIds=[104099], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            destroy_monster(spawnIds=[104099])
            reset_timer(timerId='30')
            dark_stream(type='ClearRound', round=4)
            set_achievement(triggerId=101, type='trigger', achieve='4roundpass')
            return 라운드대기5()


class 라운드대기5(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='5,5,1')
        set_effect(triggerIds=[6101], visible=True)
        dark_stream(type='StartRound', round=5, uiDuration=3000, damagePenalty=5)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 라운드5()


class 라운드5(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[105001], score=135000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[105001]):
            dark_stream(type='ClearRound', round=5)
            set_achievement(triggerId=101, type='trigger', achieve='5roundpass')
            return 바닥부심()


class 바닥부심(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[600], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            set_effect(triggerIds=[610], visible=True)
            set_effect(triggerIds=[6110], visible=False)
            set_effect(triggerIds=[6111], visible=False)
            set_effect(triggerIds=[6112], visible=False)
            set_effect(triggerIds=[6113], visible=False)
            set_skill(triggerIds=[702], isEnable=True)
            set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146], visible=False, arg3=0, arg4=0, arg5=0)
            set_event_ui(type=0, arg2='0,0')
            return 종료()


class 종료(state.State):
    pass


