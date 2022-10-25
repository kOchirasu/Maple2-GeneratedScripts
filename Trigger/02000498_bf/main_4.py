""" trigger/02000498_bf/main_4.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521,3522,3523,3524,3525,3526,3527,3528], visible=True, arg3=0, delay=0, scale=0)
        self.set_skill(triggerIds=[705], enable=False)
        self.set_effect(triggerIds=[6401], visible=False)
        self.set_effect(triggerIds=[640], visible=False)
        self.set_effect(triggerIds=[630], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[104]):
            return 시작대기(self.ctx)


class 시작대기(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='16,20,16')
        self.dark_stream(type='StartRound', round=16, uiDuration=3000, damagePenalty=50)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 라운드16(self.ctx)


class 라운드16(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN_4__0$', arg3='4000', arg4='0')
        self.dark_stream(type='SpawnMonster', spawnIds=[116001], score=73000)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[116001]):
            self.dark_stream(type='ClearRound', round=16)
            self.set_achievement(triggerId=104, type='trigger', achieve='16roundpass')
            return 라운드대기17(self.ctx)


class 라운드대기17(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='17,20,16')
        self.dark_stream(type='StartRound', round=17, uiDuration=3000, damagePenalty=50)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 라운드17(self.ctx)


class 라운드17(common.Trigger):
    def on_enter(self):
        self.dark_stream(type='SpawnMonster', spawnIds=[117001], score=56250)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[117001]):
            self.dark_stream(type='ClearRound', round=17)
            self.set_achievement(triggerId=104, type='trigger', achieve='17roundpass')
            return 라운드대기18(self.ctx)


class 라운드대기18(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='18,20,16')
        self.set_timer(timerId='3', seconds=3)
        self.dark_stream(type='StartRound', round=18, uiDuration=3000, damagePenalty=50)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 라운드18(self.ctx)


class 라운드18(common.Trigger):
    def on_enter(self):
        self.dark_stream(type='SpawnMonster', spawnIds=[118001], score=90000)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[118001]):
            self.dark_stream(type='ClearRound', round=18)
            self.set_achievement(triggerId=104, type='trigger', achieve='18roundpass')
            return 라운드대기19(self.ctx)


class 라운드대기19(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='19,20,16')
        self.set_timer(timerId='3', seconds=3)
        self.dark_stream(type='StartRound', round=19, uiDuration=3000, damagePenalty=50)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 라운드19(self.ctx)


class 라운드19(common.Trigger):
    def on_enter(self):
        self.dark_stream(type='SpawnMonster', spawnIds=[119001,119002], score=80000)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[119001,119002]):
            self.dark_stream(type='ClearRound', round=19)
            self.set_achievement(triggerId=104, type='trigger', achieve='19roundpass')
            return 라운드대기20(self.ctx)


class 라운드대기20(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='20,20,16')
        self.set_effect(triggerIds=[6401], visible=True)
        self.set_timer(timerId='3', seconds=3)
        self.dark_stream(type='StartRound', round=20, uiDuration=3000, damagePenalty=50)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 라운드20(self.ctx)


class 라운드20(common.Trigger):
    def on_enter(self):
        self.dark_stream(type='SpawnMonster', spawnIds=[120001], score=600000)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[120001]):
            self.dark_stream(type='ClearRound', round=20)
            self.set_achievement(triggerId=104, type='trigger', achieve='20roundpass')
            return 바닥부심(self.ctx)


class 바닥부심(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[600], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            self.set_effect(triggerIds=[640], visible=True)
            self.set_skill(triggerIds=[705], enable=True)
            self.set_mesh(triggerIds=[3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521,3522,3523,3524,3525,3526,3527,3528], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
