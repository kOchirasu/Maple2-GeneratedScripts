""" trigger/02000064_tw_triatown02/massive_door_1.xml """
import trigger_api


class 오픈대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[11,12,13], visible=True)
        self.set_actor(triggerId=1, visible=True, initialSequence='Eff_MassiveEvent_Bridge_Opened')
        self.set_actor(triggerId=2, visible=True, initialSequence='Eff_MassiveEvent_Bridge_Opened')
        self.set_actor(triggerId=3, visible=True, initialSequence='Eff_MassiveEvent_Door_Closed')


class 오픈중1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 오픈중2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timerId='1')


class 오픈중2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='2', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 클로즈대기중(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timerId='2')
        self.set_actor(triggerId=3, visible=True, initialSequence='Eff_MassiveEvent_Door_Opened')


class 클로즈대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='3', seconds=114)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 클로즈5초전(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timerId='3')


class 클로즈5초전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.notice(arg1=False, script='$02000064_TW_Triatown02__MASSIVE_DOOR_1__0$', arg3=True)
        self.set_timer(timerId='4', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 클로즈중1(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timerId='4')
        self.set_actor(triggerId=3, visible=True, initialSequence='Eff_MassiveEvent_Door_Closed')


class 클로즈중1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 클로즈중2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timerId='5')


class 클로즈중2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.notice(arg1=False, script='$02000064_TW_Triatown02__MASSIVE_DOOR_1__1$', arg3=True)
        self.set_timer(timerId='6', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 오픈대기중(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timerId='6')


initial_state = 오픈대기중
