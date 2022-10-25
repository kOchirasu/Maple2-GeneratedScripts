""" trigger/66000004_gd/pvp.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='60', seconds=30, startDelay=0, interval=1)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=104, boxId=20):
            return PvP(self.ctx)
        if self.time_expired(timerId='60'):
            return 대기(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='60')


class 대기(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=104, boxId=2):
            return PvP(self.ctx)
        if not self.count_users(boxId=104, boxId=2):
            return 비김(self.ctx)


class PvP(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1, startDelay=0)
        # action name="업적이벤트를발생시킨다" arg1="106" arg2="trigger" arg3="dailyquest_start"/
        self.set_pvp_zone(boxId=104, arg2=3, duration=600, additionalEffectId=90001002, arg5=3, boxIds=[1,2,101,102,103])

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 문열림(self.ctx)


class 문열림(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[105]):
            return PvP종료(self.ctx)


class PvP종료(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.pvp_zone_ended(boxId=104):
            return 게임종료(self.ctx)


class 게임종료(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10'):
            return 종료(self.ctx)


class 비김(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            self.set_event_ui(type=5, arg2='$65000002_BD__PVP__5$', arg3='3000', arg4='0')
            return 완료(self.ctx)


class 완료(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            self.move_user(mapId=0, portalId=0)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 시작
