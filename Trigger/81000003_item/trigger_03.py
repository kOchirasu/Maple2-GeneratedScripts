""" trigger/81000003_item/trigger_03.xml """
from common import *
import state


class 입장(state.State):
    def on_enter(self):
        set_timer(timerId='59', seconds=180, clearAtZero=True, display=True, arg5=-90, desc='wait.xml 시작 타이머 설정 UI') # 3분 후 시작

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[402]):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=999, visible=True, enabled=True, minimapVisible=True)
        set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=180000):
            return 어나운스0()
        """
        <condition name="여러명의유저를감지했으면" arg1="402" arg2="20">
                    <transition state="어나운스0" />
                </condition>
        """


class 어나운스0(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='ME_Trigger_03_00')
        set_event_ui(type=1, arg2='$61000006_ME__TRIGGER_03__0$', arg3='4000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
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
        set_timer(timerId='160', seconds=160, clearAtZero=False, display=True, desc='trigger_03.xml 시작 타이머 설정')
        set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509], visible=False)
        set_interact_object(triggerIds=[10000224], state=1)
        set_interact_object(triggerIds=[10000214], state=1)
        # <action name="업적이벤트를발생시킨다" arg1="402" arg2="trigger" arg3="dailyquest_start"/>
        start_mini_game(isShowResultUI=False, boxId=499, round=1, gameName='UserMassive_Crazyrunner')
        start_mini_game_round(boxId=499, round=1)
        move_user_to_box(boxId=400, portalId=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='160'):
            return 경기종료()


class 경기종료(state.State):
    def on_enter(self):
        set_event_ui(type=3, arg2='$61000006_ME__TRIGGER_03__2$', arg3='5000', arg4='401')
        set_event_ui(type=4, arg2='$61000006_ME__TRIGGER_03__3$', arg3='5000', arg4='!401')
        add_buff(boxIds=[401], skillId=70000132, level=1) # action name="이벤트UI를설정한다" arg1="5" arg2="$61000004_ME__TRIGGER_01__2$" arg3="3000" arg4="0" /

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            end_mini_game_round(winnerBoxId=401, expRate=0.13333334, isGainLoserBonus=True, gameName='UserMassive_Crazyrunner')
            end_mini_game(winnerBoxId=401, gameName='UserMassive_Crazyrunner')
            return 강제이동()


class 강제이동(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            move_user(mapId=0, portalId=0)
            return 종료()


class 종료(state.State):
    pass


