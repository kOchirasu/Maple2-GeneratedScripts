""" trigger/66000004_gd/pvp.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='60', seconds=30, startDelay=0, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=104, minUsers='20'):
            return PvP(self.ctx)
        if self.time_expired(timerId='60'):
            return 대기(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timerId='60')


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timerId='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=104, minUsers='2'):
            return PvP(self.ctx)
        if not self.count_users(boxId=104, minUsers='2'):
            return 비김(self.ctx)


class PvP(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1, startDelay=0)
        # self.set_achievement(triggerId=106, type='trigger', achieve='dailyquest_start')
        self.set_pvp_zone(boxId=104, arg2=3, duration=600, additionalEffectId=90001002, arg5=3, boxIds=[1,2,101,102,103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[105]):
            return PvP종료(self.ctx)


class PvP종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.pvp_zone_ended(boxId=104):
            return 게임종료(self.ctx)


class 게임종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 종료(self.ctx)


class 비김(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='3', seconds=3, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.set_event_ui(type=5, arg2='$65000002_BD__PVP__5$', arg3='3000', arg4='0')
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            self.move_user(mapId=0, portalId=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
