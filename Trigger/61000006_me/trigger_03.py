""" trigger/61000006_me/trigger_03.xml """
from common import *
import state


class 입장(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[402]):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=999, visible=True, enabled=True, minimapVisible=True)
        set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=60000):
            return 어나운스0()
        if count_users(boxId=402, boxId=20):
            return 어나운스0()


class 어나운스0(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='ME_Trigger_03_00')
        set_event_ui(type=1, arg2='$61000006_ME__TRIGGER_03__0$', arg3='7000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 어나운스1()


class 어나운스1(state.State):
    def on_enter(self):
        show_count_ui(text='$61000006_ME__TRIGGER_03__1$', stage=0, count=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_user_value(triggerId=999111, key='gameStart', value=1)
        set_timer(timerId='160', seconds=160, clearAtZero=False, display=True)
        set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509], visible=False)
        set_interact_object(triggerIds=[10000224], state=1)
        set_interact_object(triggerIds=[10000214], state=1)
        set_achievement(triggerId=402, type='trigger', achieve='dailyquest_start') # 길드 경험치 지급 / boxID="타겟박스id", 0이면 맵전체, type="GuildGainExp의 id" 2가 매시브이벤트
        give_guild_exp(boxId=0, type=2)
        start_mini_game(boxId=499, round=1, gameName='crazyrunner')
        start_mini_game_round(boxId=499, round=1)
        move_user_to_box(boxId=400, portalId=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='160'):
            return 경기종료()


class 경기종료(state.State):
    def on_enter(self):
        set_achievement(triggerId=401, type='trigger', achieve='crazyrunner_win') # action name="MiniGameCameraDirection" boxId="401" cameraId="301" /
        set_event_ui(type=3, arg2='$61000006_ME__TRIGGER_03__2$', arg3='5000', arg4='401')
        set_event_ui(type=6, arg2='$61000006_ME__TRIGGER_03__3$', arg3='5000', arg4='!401')
        add_buff(boxIds=[401], skillId=70000019, level=1) # action name="이벤트UI를설정한다" arg1="5" arg2="$61000004_ME__TRIGGER_01__2$" arg3="3000" arg4="0" /

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            end_mini_game_round(winnerBoxId=401, expRate=0.25, isGainLoserBonus=True)
            mini_game_give_reward(winnerBoxId=401, contentType='miniGame')
            end_mini_game(winnerBoxId=401, gameName='crazyrunner')
            return 강제이동()


class 강제이동(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            move_user(mapId=0, portalId=0)
            return 종료()


class 종료(state.State):
    pass


