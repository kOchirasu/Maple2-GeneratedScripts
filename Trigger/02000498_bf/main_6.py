""" trigger/02000498_bf/main_6.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3601], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[6601], visible=False)
        self.set_effect(triggerIds=[6602], visible=False)
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[106]):
            return 시작대기(self.ctx)


class 시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6601], visible=True)
        self.dark_stream(type='StartRound', round=26, uiDuration=3000, damagePenalty=200)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.set_event_ui(type=0, arg2='26,30,26')
            return 라운드26(self.ctx)


class 라운드26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN_6__0$', arg3='4000', arg4='0')
        self.dark_stream(type='SpawnMonster', spawnIds=[126001], score=2200000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[126001]):
            self.dark_stream(type='ClearRound', round=26)
            self.set_achievement(triggerId=106, type='trigger', achieve='26roundpass')
            return 라운드대기27(self.ctx)


class 라운드대기27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6601], visible=True)
        self.dark_stream(type='StartRound', round=27, uiDuration=3000, damagePenalty=200)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.set_event_ui(type=0, arg2='27,30,26')
            return 라운드27(self.ctx)


class 라운드27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream(type='SpawnMonster', spawnIds=[127001], score=2500000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[127001]):
            self.dark_stream(type='ClearRound', round=27)
            self.set_achievement(triggerId=106, type='trigger', achieve='27roundpass')
            return 라운드대기28(self.ctx)


class 라운드대기28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6601], visible=True)
        self.dark_stream(type='StartRound', round=28, uiDuration=3000, damagePenalty=200)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.set_event_ui(type=0, arg2='28,30,26')
            return 라운드28(self.ctx)


class 라운드28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream(type='SpawnMonster', spawnIds=[128001], score=3000000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[128001]):
            self.dark_stream(type='ClearRound', round=28)
            self.set_achievement(triggerId=106, type='trigger', achieve='28roundpass')
            return 라운드대기29(self.ctx)


class 라운드대기29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6601], visible=True)
        self.dark_stream(type='StartRound', round=29, uiDuration=3000, damagePenalty=200)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.set_event_ui(type=0, arg2='29,30,26')
            return 라운드29(self.ctx)


class 라운드29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream(type='SpawnMonster', spawnIds=[129001], score=5000000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[129001]):
            self.dark_stream(type='ClearRound', round=29)
            self.set_achievement(triggerId=106, type='trigger', achieve='29roundpass')
            return 라운드대기30(self.ctx)


class 라운드대기30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6602], visible=True)
        self.dark_stream(type='StartRound', round=30, uiDuration=3000, damagePenalty=200)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.set_event_ui(type=0, arg2='30,30,26')
            return 라운드30(self.ctx)


class 라운드30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3601], visible=True, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[130001], animationEffect=True)
        self.dark_stream(type='SpawnMonster', spawnIds=[130002], score=8000000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[130002]):
            self.set_mesh(triggerIds=[3601], visible=False, arg3=0, delay=0, scale=0)
            self.destroy_monster(spawnIds=[130001])
            self.dark_stream(type='ClearRound', round=30)
            self.set_achievement(triggerId=106, type='trigger', achieve='30roundpass')
            return 성공(self.ctx)


class 성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='0,0')
        self.set_event_ui(type=7, arg2='$02000350_BF__MAIN_6__1$', arg3='3000', arg4='0')
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN_6__2$', arg3='2500', arg4='0')
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)


initial_state = 대기
