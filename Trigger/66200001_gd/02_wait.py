""" trigger/66200001_gd/02_wait.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=90, clearAtZero=True, display=False) # 테스트 수정 가능 지점

    def on_tick(self) -> state.State:
        if check_user():
            return Notice_90sec_Left()


class Notice_90sec_Left(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=26620112, textId=26620112, duration=5000) # 길드 미니 게임 대전을 [b:1분 30초] 후 시작합니다.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Notice_till75sec_01()
        if time_expired(timerId='1'):
            return Quit()


class Notice_till75sec_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26620106, textId=26620106, duration=5000) # 다른 친구들이 올 때까지 조금만 기다려주세요.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Notice_till75sec_02()
        if time_expired(timerId='1'):
            return Quit()


class Notice_till75sec_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26620107, textId=26620107, duration=5000) # 한 팀의 입장 인원이 [b:10명보다 적으면 기권 처리] 됩니다.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Notice_75sec_Left()
        if time_expired(timerId='1'):
            return Quit()


class Notice_75sec_Left(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=26620113, textId=26620113, duration=5000) # 길드 미니 게임 대전을 [b:1분 15초] 후 시작합니다.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Notice_till60sec_01()
        if time_expired(timerId='1'):
            return Quit()


class Notice_till60sec_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26620106, textId=26620106, duration=5000) # 다른 친구들이 올 때까지 조금만 기다려주세요.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Notice_till60sec_02()
        if time_expired(timerId='1'):
            return Quit()


class Notice_till60sec_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26620107, textId=26620107, duration=5000) # 한 팀의 입장 인원이 [b:10명보다 적으면 기권 처리] 됩니다.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Notice_60sec_Left()
        if time_expired(timerId='1'):
            return Quit()


class Notice_60sec_Left(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=26620108, textId=26620108, duration=5000) # 길드 미니 게임 대전을 [b:1분] 후 시작합니다.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Notice_till45sec_01()
        if time_expired(timerId='1'):
            return Quit()


class Notice_till45sec_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26620106, textId=26620106, duration=5000) # 다른 친구들이 올 때까지 조금만 기다려주세요.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Notice_till45sec_02()
        if time_expired(timerId='1'):
            return Quit()


class Notice_till45sec_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26620107, textId=26620107, duration=5000) # 한 팀의 입장 인원이 [b:10명보다 적으면 기권 처리] 됩니다.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Notice_45sec_Left()
        if time_expired(timerId='1'):
            return Quit()


class Notice_45sec_Left(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=26620109, textId=26620109, duration=5000) # 길드 미니 게임 대전을 [b:45초] 후 시작합니다.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Notice_till30sec_01()
        if time_expired(timerId='1'):
            return Quit()


class Notice_till30sec_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26620106, textId=26620106, duration=5000) # 다른 친구들이 올 때까지 조금만 기다려주세요.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Notice_till30sec_02()
        if time_expired(timerId='1'):
            return Quit()


class Notice_till30sec_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26620107, textId=26620107, duration=5000) # 한 팀의 입장 인원이 [b:10명보다 적으면 기권 처리] 됩니다.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Notice_30sec_Left()
        if time_expired(timerId='1'):
            return Quit()


class Notice_30sec_Left(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=26620110, textId=26620110, duration=5000) # 길드 미니 게임 대전을 [b:30초] 후 시작합니다.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Notice_till15sec_01()
        if time_expired(timerId='1'):
            return Quit()


class Notice_till15sec_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26620106, textId=26620106, duration=5000) # 다른 친구들이 올 때까지 조금만 기다려주세요.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Notice_till15sec_02()
        if time_expired(timerId='1'):
            return Quit()


class Notice_till15sec_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26620107, textId=26620107, duration=5000) # 한 팀의 입장 인원이 [b:10명보다 적으면 기권 처리] 됩니다.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Notice_15sec_Left()
        if time_expired(timerId='1'):
            return Quit()


class Notice_15sec_Left(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=26620111, textId=26620111, duration=5000) # 길드 미니 게임 대전을 잠시 후에 시작합니다.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Notice_till0sec_01()
        if time_expired(timerId='1'):
            return Quit()


class Notice_till0sec_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26620106, textId=26620106, duration=5000) # 다른 친구들이 올 때까지 조금만 기다려주세요.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Notice_till0sec_02()
        if time_expired(timerId='1'):
            return Quit()


class Notice_till0sec_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26620107, textId=26620107, duration=5000) # 한 팀의 입장 인원이 [b:10명보다 적으면 기권 처리] 됩니다.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit()
        if time_expired(timerId='1'):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='BattleField_Event')


