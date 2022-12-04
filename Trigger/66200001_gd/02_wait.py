""" trigger/66200001_gd/02_wait.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=90, startDelay=1, interval=0) # 테스트 수정 가능 지점

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return Notice_90sec_Left(self.ctx)


class Notice_90sec_Left(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=26620112, textId=26620112, duration=5000) # 길드 미니 게임 대전을 [b:1분 30초] 후 시작합니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Notice_till75sec_01(self.ctx)
        if self.time_expired(timerId='1'):
            return Quit(self.ctx)


class Notice_till75sec_01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26620106, textId=26620106, duration=5000) # 다른 친구들이 올 때까지 조금만 기다려주세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Notice_till75sec_02(self.ctx)
        if self.time_expired(timerId='1'):
            return Quit(self.ctx)


class Notice_till75sec_02(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26620107, textId=26620107, duration=5000) # 한 팀의 입장 인원이 [b:10명보다 적으면 기권 처리] 됩니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Notice_75sec_Left(self.ctx)
        if self.time_expired(timerId='1'):
            return Quit(self.ctx)


class Notice_75sec_Left(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=26620113, textId=26620113, duration=5000) # 길드 미니 게임 대전을 [b:1분 15초] 후 시작합니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Notice_till60sec_01(self.ctx)
        if self.time_expired(timerId='1'):
            return Quit(self.ctx)


class Notice_till60sec_01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26620106, textId=26620106, duration=5000) # 다른 친구들이 올 때까지 조금만 기다려주세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Notice_till60sec_02(self.ctx)
        if self.time_expired(timerId='1'):
            return Quit(self.ctx)


class Notice_till60sec_02(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26620107, textId=26620107, duration=5000) # 한 팀의 입장 인원이 [b:10명보다 적으면 기권 처리] 됩니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Notice_60sec_Left(self.ctx)
        if self.time_expired(timerId='1'):
            return Quit(self.ctx)


class Notice_60sec_Left(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=26620108, textId=26620108, duration=5000) # 길드 미니 게임 대전을 [b:1분] 후 시작합니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Notice_till45sec_01(self.ctx)
        if self.time_expired(timerId='1'):
            return Quit(self.ctx)


class Notice_till45sec_01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26620106, textId=26620106, duration=5000) # 다른 친구들이 올 때까지 조금만 기다려주세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Notice_till45sec_02(self.ctx)
        if self.time_expired(timerId='1'):
            return Quit(self.ctx)


class Notice_till45sec_02(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26620107, textId=26620107, duration=5000) # 한 팀의 입장 인원이 [b:10명보다 적으면 기권 처리] 됩니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Notice_45sec_Left(self.ctx)
        if self.time_expired(timerId='1'):
            return Quit(self.ctx)


class Notice_45sec_Left(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=26620109, textId=26620109, duration=5000) # 길드 미니 게임 대전을 [b:45초] 후 시작합니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Notice_till30sec_01(self.ctx)
        if self.time_expired(timerId='1'):
            return Quit(self.ctx)


class Notice_till30sec_01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26620106, textId=26620106, duration=5000) # 다른 친구들이 올 때까지 조금만 기다려주세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Notice_till30sec_02(self.ctx)
        if self.time_expired(timerId='1'):
            return Quit(self.ctx)


class Notice_till30sec_02(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26620107, textId=26620107, duration=5000) # 한 팀의 입장 인원이 [b:10명보다 적으면 기권 처리] 됩니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Notice_30sec_Left(self.ctx)
        if self.time_expired(timerId='1'):
            return Quit(self.ctx)


class Notice_30sec_Left(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=26620110, textId=26620110, duration=5000) # 길드 미니 게임 대전을 [b:30초] 후 시작합니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Notice_till15sec_01(self.ctx)
        if self.time_expired(timerId='1'):
            return Quit(self.ctx)


class Notice_till15sec_01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26620106, textId=26620106, duration=5000) # 다른 친구들이 올 때까지 조금만 기다려주세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Notice_till15sec_02(self.ctx)
        if self.time_expired(timerId='1'):
            return Quit(self.ctx)


class Notice_till15sec_02(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26620107, textId=26620107, duration=5000) # 한 팀의 입장 인원이 [b:10명보다 적으면 기권 처리] 됩니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Notice_15sec_Left(self.ctx)
        if self.time_expired(timerId='1'):
            return Quit(self.ctx)


class Notice_15sec_Left(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=26620111, textId=26620111, duration=5000) # 길드 미니 게임 대전을 잠시 후에 시작합니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Notice_till0sec_01(self.ctx)
        if self.time_expired(timerId='1'):
            return Quit(self.ctx)


class Notice_till0sec_01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26620106, textId=26620106, duration=5000) # 다른 친구들이 올 때까지 조금만 기다려주세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Notice_till0sec_02(self.ctx)
        if self.time_expired(timerId='1'):
            return Quit(self.ctx)


class Notice_till0sec_02(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26620107, textId=26620107, duration=5000) # 한 팀의 입장 인원이 [b:10명보다 적으면 기권 처리] 됩니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Quit(self.ctx)
        if self.time_expired(timerId='1'):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='BattleField_Event')


initial_state = Wait
