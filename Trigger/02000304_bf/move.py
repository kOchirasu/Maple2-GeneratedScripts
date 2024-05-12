""" trigger/02000304_bf/move.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 몬스터체크(self.ctx)


class 몬스터체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[2001]):
            return 카운트랜덤(self.ctx)


class 카운트랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=25):
            return 이동대기01(self.ctx)
        if self.random_condition(rate=25):
            return 이동대기02(self.ctx)
        if self.random_condition(rate=25):
            return 이동대기03(self.ctx)
        if self.random_condition(rate=25):
            return 이동대기04(self.ctx)


class 이동대기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='90', seconds=90)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timerId='90'):
            return 이동(self.ctx)


class 이동대기02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='100', seconds=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timerId='100'):
            return 이동(self.ctx)


class 이동대기03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='110', seconds=110)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timerId='110'):
            return 이동(self.ctx)


class 이동대기04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='120', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timerId='120'):
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[601], visible=True)
        self.set_conversation(type=1, spawnId=2001, script='$02000304_BF__MOVE__0$', arg4=2)
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timerId='2'):
            self.set_conversation(type=1, spawnId=2001, script='$02000304_BF__MOVE__1$', arg4=1)
            self.move_random_user(mapId=2000304, portalId=11, triggerId=101, count=1)
            return 이동2(self.ctx)


class 이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timerId='1'):
            self.set_conversation(type=1, spawnId=2001, script='$02000304_BF__MOVE__2$', arg4=1)
            self.move_random_user(mapId=2000304, portalId=12, triggerId=101, count=1)
            return 이동3(self.ctx)


class 이동3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timerId='1'):
            self.set_conversation(type=1, spawnId=2001, script='$02000304_BF__MOVE__3$', arg4=1)
            self.move_random_user(mapId=2000304, portalId=13, triggerId=101, count=1)
            return 이동4(self.ctx)


class 이동4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 종료(self.ctx)
        if self.time_expired(timerId='1'):
            self.set_conversation(type=1, spawnId=2001, script='$02000304_BF__MOVE__4$', arg4=1)
            self.move_random_user(mapId=2000304, portalId=14, triggerId=101, count=1)
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1800000', seconds=1800000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1800000'):
            return None # Missing State: 종료2


initial_state = 대기
