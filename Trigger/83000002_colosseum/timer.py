""" trigger/83000002_colosseum/timer.xml """
import trigger_api


# <라운드 시작하면서 5분 시간 제한 타이머>
class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Timer', value=1):
            return 스테이지1(self.ctx)
        if self.user_value(key='Timer', value=2):
            return 스테이지2(self.ctx)
        if self.user_value(key='Timer', value=3):
            return 스테이지3(self.ctx)
        if self.user_value(key='Timer', value=4):
            return 스테이지4(self.ctx)
        if self.user_value(key='Timer', value=5):
            return 스테이지5(self.ctx)
        if self.user_value(key='Timer', value=6):
            return 스테이지6(self.ctx)
        if self.user_value(key='Timer', value=7):
            return 스테이지7(self.ctx)
        if self.user_value(key='Timer', value=8):
            return 스테이지8(self.ctx)
        if self.user_value(key='Timer', value=9):
            return 스테이지9(self.ctx)
        if self.user_value(key='Timer', value=10):
            return 스테이지10(self.ctx)


class 스테이지1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='LimitTimer', seconds=180, startDelay=1)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="101" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 타이머체크1(self.ctx)


class 타이머체크1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='LimitTimer'):
            self.set_user_value(triggerId=900001, key='Fail', value=1)
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[101]):
            self.set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 스테이지2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='LimitTimer2', seconds=180, startDelay=1)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="102" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 타이머체크2(self.ctx)


class 타이머체크2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='LimitTimer'):
            self.set_user_value(triggerId=900001, key='Fail', value=1)
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[102]):
            self.set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 스테이지3(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='LimitTimer3', seconds=180, startDelay=1)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="103" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 타이머체크3(self.ctx)


class 타이머체크3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='LimitTimer'):
            self.set_user_value(triggerId=900001, key='Fail', value=1)
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[103]):
            self.set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 스테이지4(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='LimitTimer4', seconds=180, startDelay=1)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="104" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 타이머체크4(self.ctx)


class 타이머체크4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='LimitTimer'):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[104]):
            self.set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 스테이지5(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='LimitTimer5', seconds=180, startDelay=1)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="105" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 타이머체크5(self.ctx)


class 타이머체크5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='LimitTimer'):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[105]):
            self.set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 스테이지6(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='LimitTimer6', seconds=180, startDelay=1)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="106" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 타이머체크6(self.ctx)


class 타이머체크6(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='LimitTimer'):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[106]):
            self.set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 스테이지7(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='LimitTimer7', seconds=180, startDelay=1)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="107" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 타이머체크7(self.ctx)


class 타이머체크7(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='LimitTimer'):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[107]):
            self.set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 스테이지8(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='LimitTimer8', seconds=300, startDelay=1)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="108" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 타이머체크8(self.ctx)


class 타이머체크8(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='LimitTimer'):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[108]):
            self.set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 스테이지9(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='LimitTimer9', seconds=300, startDelay=1)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="109" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 타이머체크9(self.ctx)


class 타이머체크9(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='LimitTimer'):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[109]):
            self.set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 스테이지10(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='LimitTimer10', seconds=300, startDelay=1)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="110" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 타이머체크10(self.ctx)


class 타이머체크10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='LimitTimer'):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[110]):
            self.set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='LimitTimer')
        self.reset_timer(timerId='LimitTimer2')
        self.reset_timer(timerId='LimitTimer3')
        self.reset_timer(timerId='LimitTimer4')
        self.reset_timer(timerId='LimitTimer5')
        self.reset_timer(timerId='LimitTimer6')
        self.reset_timer(timerId='LimitTimer7')
        self.reset_timer(timerId='LimitTimer8')
        self.reset_timer(timerId='LimitTimer9')
        self.reset_timer(timerId='LimitTimer10')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


initial_state = 대기
