""" trigger/65000002_bd/pvp.xml """
import trigger_api


class 시간표확인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_timer(timerId='60', seconds=60, startDelay=0, interval=1)
        self.set_effect(triggerIds=[601], visible=False) # 공지 효과음
        self.set_effect(triggerIds=[602], visible=False) # 종료 효과음

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=102, minUsers='10'):
            return 어나운스0(self.ctx)
        if self.time_expired(timerId='60'):
            return 대기(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timerId='60')


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=102, minUsers='2'):
            return 어나운스0(self.ctx)
        if not self.count_users(boxId=102, minUsers='2'):
            return 비김(self.ctx)


class 어나운스0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='6', seconds=6, startDelay=0)
        self.play_system_sound_in_box(sound='BD_PVP_00')
        self.set_event_ui(type=1, arg2='$65000002_BD__PVP__0$', arg3='6000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 어나운스1(self.ctx)


class 어나운스1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='6', seconds=6, startDelay=0)
        self.play_system_sound_in_box(sound='BD_PVP_01')
        self.set_event_ui(type=1, arg2='$65000002_BD__PVP__1$', arg3='6000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 어나운스2(self.ctx)


class 어나운스2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='6', seconds=6, startDelay=0)
        self.play_system_sound_in_box(sound='BD_PVP_02')
        self.set_event_ui(type=1, arg2='$65000002_BD__PVP__2$', arg3='6000', arg4='101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 어나운스3(self.ctx)


class 어나운스3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='3', seconds=3, startDelay=0)
        self.play_system_sound_in_box(sound='BD_PVP_03')
        self.set_event_ui(type=1, arg2='$65000002_BD__PVP__3$', arg3='3000')
        self.set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return PvP(self.ctx)


class PvP(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 길드 경험치 지급 / boxID="타겟박스id", 0이면 맵전체, type="GuildGainExp의 id" 2가 매시브이벤트
        self.set_achievement(triggerId=101, type='trigger', achieve='dailyquest_start')
        self.give_guild_exp(boxId=0, type=2)
        self.add_buff(boxIds=[101], skillId=70000088, level=1, isPlayer=False, isSkillSet=False)
        self.add_buff(boxIds=[101], skillId=70000089, level=1, isPlayer=False, isSkillSet=False)
        self.set_timer(timerId='1', seconds=1, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            self.set_pvp_zone(boxId=101, arg2=5, duration=300, additionalEffectId=90001002, arg5=2)
            return PvP종료(self.ctx)


class PvP종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.pvp_zone_ended(boxId=101):
            return 경기종료(self.ctx)


class 경기종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='4', seconds=4, startDelay=0)
        self.play_system_sound_in_box(sound='BD_PVP_04')
        self.set_event_ui(type=1, arg2='$65000002_BD__PVP__4$', arg3='3000', arg4='101')
        self.set_effect(triggerIds=[602], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 완료(self.ctx)


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


initial_state = 시간표확인
