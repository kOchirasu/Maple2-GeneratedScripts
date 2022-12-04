""" trigger/99999950/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 시작대기(self.ctx)


class 시작대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            self.set_event_ui(type=1, arg2='$99999950__MAIN__0$', arg3='2000', arg4='0')
            return 라운드1(self.ctx)


class 라운드1(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101001], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101001]):
            return 라운드02_1(self.ctx)


class 라운드02_1(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101001], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101001]):
            return 라운드대기2(self.ctx)


class 라운드대기2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            self.set_event_ui(type=1, arg2='$99999950__MAIN__1$', arg3='2000', arg4='0')
            return 라운드2(self.ctx)


class 라운드2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101002], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101002]):
            return 라운드02_2(self.ctx)


class 라운드02_2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101002], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101002]):
            return 라운드대기3(self.ctx)


class 라운드대기3(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            self.set_event_ui(type=1, arg2='$99999950__MAIN__2$', arg3='2000', arg4='0')
            return 라운드3(self.ctx)


class 라운드3(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101003], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101003]):
            return 라운드02_3(self.ctx)


class 라운드02_3(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101003], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101003]):
            return 라운드대기4(self.ctx)


class 라운드대기4(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            self.set_event_ui(type=1, arg2='$99999950__MAIN__3$', arg3='2000', arg4='0')
            return 라운드4(self.ctx)


class 라운드4(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101004], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101004]):
            return 라운드02_4(self.ctx)


class 라운드02_4(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101004], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101004]):
            return 라운드03_4(self.ctx)


class 라운드03_4(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101004], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101004]):
            return 라운드대기5(self.ctx)


class 라운드대기5(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            self.set_event_ui(type=1, arg2='$99999950__MAIN__4$', arg3='2000', arg4='0')
            return 라운드5(self.ctx)


class 라운드5(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101005], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101005]):
            return None # Missing State: 라운드대기6


initial_state = 대기
