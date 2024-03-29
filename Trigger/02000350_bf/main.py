""" trigger/02000350_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[600], visible=False)
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[610], visible=False)
        self.set_effect(triggerIds=[6010], visible=False)
        self.set_effect(triggerIds=[6011], visible=False)
        self.set_effect(triggerIds=[6012], visible=False)
        self.set_effect(triggerIds=[6013], visible=False)
        self.set_effect(triggerIds=[6015], visible=False)
        self.set_effect(triggerIds=[6110], visible=False)
        self.set_effect(triggerIds=[6111], visible=False)
        self.set_effect(triggerIds=[6112], visible=False)
        self.set_effect(triggerIds=[6113], visible=False)
        self.set_effect(triggerIds=[6101], visible=False)
        self.set_skill(triggerIds=[701], enable=False)
        self.set_skill(triggerIds=[702], enable=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[100]):
            return 시작대기(self.ctx)


class 시작대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6010], visible=True)
        self.set_effect(triggerIds=[6011], visible=True)
        self.set_effect(triggerIds=[6012], visible=True)
        self.set_effect(triggerIds=[6013], visible=True)
        self.set_effect(triggerIds=[6015], visible=True)
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN__0$', arg3='3000', arg4='0')
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 안내02(self.ctx)


class 안내02(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN__1$', arg3='3000', arg4='0')
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 안내03(self.ctx)


class 안내03(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN__2$', arg3='4000', arg4='0')
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 진동대기(self.ctx)


class 진동대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[600], visible=True)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 유저감지(self.ctx)


class 유저감지(trigger_api.Trigger):
    def on_enter(self):
        self.dark_stream(type='StartGame', round=30)
        self.set_effect(triggerIds=[601], visible=True)
        self.set_skill(triggerIds=[701], enable=True)
        self.set_effect(triggerIds=[6010], visible=False)
        self.set_effect(triggerIds=[6011], visible=False)
        self.set_effect(triggerIds=[6012], visible=False)
        self.set_effect(triggerIds=[6013], visible=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 라운드대기1(self.ctx)


class 라운드대기1(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6110], visible=True)
        self.set_effect(triggerIds=[6111], visible=True)
        self.set_effect(triggerIds=[6112], visible=True)
        self.set_effect(triggerIds=[6113], visible=True)
        self.set_timer(timerId='3', seconds=3)
        self.dark_stream(type='StartRound', round=1, uiDuration=3000, damagePenalty=5)
        self.set_event_ui(type=0, arg2='1,5,1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 라운드1(self.ctx)


class 라운드1(trigger_api.Trigger):
    def on_enter(self):
        self.dark_stream(type='SpawnMonster', spawnIds=[101001], score=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101001]):
            self.dark_stream(type='ClearRound', round=1)
            self.set_achievement(triggerId=101, type='trigger', achieve='1roundpass')
            return 라운드대기2(self.ctx)


class 라운드대기2(trigger_api.Trigger):
    def on_enter(self):
        self.dark_stream(type='StartRound', round=2, uiDuration=3000, damagePenalty=5)
        self.set_timer(timerId='3', seconds=3)
        self.set_event_ui(type=0, arg2='2,5,1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 라운드2(self.ctx)


class 라운드2(trigger_api.Trigger):
    def on_enter(self):
        self.dark_stream(type='SpawnMonster', spawnIds=[102001], score=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[102001]):
            self.dark_stream(type='ClearRound', round=2)
            self.set_achievement(triggerId=101, type='trigger', achieve='2roundpass')
            return 라운드대기3(self.ctx)


class 라운드대기3(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='3,5,1')
        self.dark_stream(type='StartRound', round=3, uiDuration=3000, damagePenalty=5)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 라운드3(self.ctx)


class 라운드3(trigger_api.Trigger):
    def on_enter(self):
        self.dark_stream(type='SpawnMonster', spawnIds=[103001], score=16000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[103001]):
            self.dark_stream(type='ClearRound', round=3)
            self.set_achievement(triggerId=101, type='trigger', achieve='3roundpass')
            return 라운드대기4(self.ctx)


class 라운드대기4(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='4,5,1')
        self.set_timer(timerId='3', seconds=3)
        self.dark_stream(type='StartRound', round=4, uiDuration=3000, damagePenalty=5)
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN__3$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.set_event_ui(type=0, arg2='4,5,1')
            return 라운드4(self.ctx)


class 라운드4(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='30', seconds=30, startDelay=1, interval=1, vOffset=80)
        self.create_monster(spawnIds=[104099], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='30'):
            self.destroy_monster(spawnIds=[104099])
            self.reset_timer(timerId='30')
            self.dark_stream(type='ClearRound', round=4)
            self.set_achievement(triggerId=101, type='trigger', achieve='4roundpass')
            return 라운드대기5(self.ctx)


class 라운드대기5(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='5,5,1')
        self.set_effect(triggerIds=[6101], visible=True)
        self.dark_stream(type='StartRound', round=5, uiDuration=3000, damagePenalty=5)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 라운드5(self.ctx)


class 라운드5(trigger_api.Trigger):
    def on_enter(self):
        self.dark_stream(type='SpawnMonster', spawnIds=[105001], score=135000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[105001]):
            self.dark_stream(type='ClearRound', round=5)
            self.set_achievement(triggerId=101, type='trigger', achieve='5roundpass')
            return 바닥부심(self.ctx)


class 바닥부심(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[600], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.set_effect(triggerIds=[610], visible=True)
            self.set_effect(triggerIds=[6110], visible=False)
            self.set_effect(triggerIds=[6111], visible=False)
            self.set_effect(triggerIds=[6112], visible=False)
            self.set_effect(triggerIds=[6113], visible=False)
            self.set_skill(triggerIds=[702], enable=True)
            self.set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146], visible=False, arg3=0, delay=0, scale=0)
            self.set_event_ui(type=0, arg2='0,0')
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
