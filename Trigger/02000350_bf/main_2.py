""" trigger/02000350_bf/main_2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[610], visible=False)
        self.set_effect(triggerIds=[620], visible=False)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_effect(triggerIds=[6110], visible=False)
        self.set_effect(triggerIds=[6111], visible=False)
        self.set_effect(triggerIds=[6112], visible=False)
        self.set_effect(triggerIds=[6113], visible=False)
        self.set_effect(triggerIds=[6201], visible=False)
        self.set_skill(triggerIds=[703], enable=False)
        self.set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[102]):
            return 시작대기(self.ctx)


class 시작대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='6,10,6')
        self.dark_stream(type='StartRound', round=6, uiDuration=3000, damagePenalty=10)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 라운드6(self.ctx)


class 라운드6(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN_2__0$', arg3='4000', arg4='0')
        self.dark_stream(type='SpawnMonster', spawnIds=[106001,106002,106003,106004,106005], score=18000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[106001,106002,106003,106004,106005]):
            self.dark_stream(type='ClearRound', round=6)
            self.set_achievement(triggerId=102, type='trigger', achieve='6roundpass')
            return 라운드대기7(self.ctx)


class 라운드대기7(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='7,10,6')
        self.dark_stream(type='StartRound', round=7, uiDuration=3000, damagePenalty=10)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 라운드7(self.ctx)


class 라운드7(trigger_api.Trigger):
    def on_enter(self):
        self.dark_stream(type='SpawnMonster', spawnIds=[107001,107002,107003,107004,107005], score=22000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[107001,107002,107003,107004,107005]):
            self.dark_stream(type='ClearRound', round=7)
            self.set_achievement(triggerId=102, type='trigger', achieve='7roundpass')
            return 라운드대기8(self.ctx)


class 라운드대기8(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='8,10,6')
        self.set_timer(timerId='3', seconds=3)
        self.dark_stream(type='StartRound', round=8, uiDuration=3000, damagePenalty=10)
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN_2__1$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 라운드8(self.ctx)


class 라운드8(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='30', seconds=30, startDelay=1, interval=1, vOffset=80)
        self.create_monster(spawnIds=[108099], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='30'):
            self.destroy_monster(spawnIds=[108099])
            self.reset_timer(timerId='30')
            self.dark_stream(type='ClearRound', round=8)
            self.set_achievement(triggerId=102, type='trigger', achieve='8roundpass')
            return 라운드대기9(self.ctx)


class 라운드대기9(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='9,10,6')
        self.set_timer(timerId='3', seconds=3)
        self.dark_stream(type='StartRound', round=9, uiDuration=3000, damagePenalty=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 라운드9(self.ctx)


class 라운드9(trigger_api.Trigger):
    def on_enter(self):
        self.dark_stream(type='SpawnMonster', spawnIds=[109001,109002,109003,109004], score=65000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[109001,109002,109003,109004]):
            self.dark_stream(type='ClearRound', round=9)
            self.set_achievement(triggerId=102, type='trigger', achieve='9roundpass')
            return 라운드대기10(self.ctx)


class 라운드대기10(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='10,10,6')
        self.set_effect(triggerIds=[6201], visible=True)
        self.dark_stream(type='StartRound', round=10, uiDuration=3000, damagePenalty=10)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 라운드10(self.ctx)


class 라운드10(trigger_api.Trigger):
    def on_enter(self):
        self.dark_stream(type='SpawnMonster', spawnIds=[110001], score=270000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[110001]):
            self.dark_stream(type='ClearRound', round=10)
            self.set_achievement(triggerId=102, type='trigger', achieve='10roundpass')
            return 바닥부심(self.ctx)


class 바닥부심(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[600], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.set_effect(triggerIds=[620], visible=True)
            self.set_skill(triggerIds=[703], enable=True)
            self.set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235], visible=False, arg3=0, delay=0, scale=0)
            self.set_event_ui(type=0, arg2='0,0')
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
