""" trigger/65000001_bd/enter.xml """
import trigger_api


class 시간표확인(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_timer(timerId='60', seconds=60, startDelay=0, interval=1)
        self.set_effect(triggerIds=[601], visible=False) # 공지 효과음

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=101, boxId=10):
            return 어나운스0(self.ctx)
        if self.time_expired(timerId='60'):
            return 대기(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='60')


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=101, boxId=2):
            return 어나운스0(self.ctx)
        if not self.count_users(boxId=101, boxId=2):
            return 비김(self.ctx)


class 어나운스0(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='6', seconds=6, startDelay=0)
        self.play_system_sound_in_box(sound='BD_Enter_00')
        self.set_event_ui(type=1, arg2='$65000001_BD__ENTER__0$', arg3='6000', arg4='101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 어나운스1(self.ctx)


class 어나운스1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3, startDelay=0)
        self.play_system_sound_in_box(sound='BD_Enter_01')
        self.set_event_ui(type=1, arg2='$65000001_BD__ENTER__1$', arg3='3000', arg4='101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return PvP(self.ctx)


class PvP(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.set_achievement(triggerId=105, type='trigger', achieve='dailyquest_start')
            self.give_guild_exp(boxId=0, type=2)
            self.set_pvp_zone(boxId=102, arg2=1, duration=120, additionalEffectId=90001002, arg5=1)
            return PvP종료(self.ctx)


class PvP종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.pvp_zone_ended(boxId=102):
            return 게임종료(self.ctx)


class 비김(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.set_event_ui(type=5, arg2='$65000001_BD__ENTER__2$', arg3='3000', arg4='0')
            return 완료(self.ctx)


class 게임종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='6', seconds=6)
        self.set_event_ui(type=0, arg2='0,0')
        self.set_event_ui(type=3, arg2='$65000001_BD__ENTER__3$', arg3='5000', arg4='102')
        self.add_buff(boxIds=[102], skillId=70000063, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 보상(self.ctx)


class 보상(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='15', seconds=15)
        self.play_system_sound_in_box(boxIds=[102], sound='BD_Enter_04')
        self.play_system_sound_in_box(boxIds=[103], sound='BD_Enter_05')
        self.set_event_ui(type=3, arg2='$65000001_BD__ENTER__4$', arg3='5000', arg4='102')
        self.set_event_ui(type=6, arg2='$65000001_BD__ENTER__5$', arg3='5000', arg4='!102')
        self.create_item(spawnIds=[9001,9002,9003])
        self.create_item(spawnIds=[9004], triggerId=104)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='15'):
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            self.move_user(mapId=0, portalId=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시간표확인
