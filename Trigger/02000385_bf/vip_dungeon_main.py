""" trigger/02000385_bf/vip_dungeon_main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[601,602,603], visible=False)
        move_user(mapId=2000385, portalId=1)
        set_interact_object(triggerIds=[10001083], state=1)
        set_interact_object(triggerIds=[10001084], state=1)
        set_interact_object(triggerIds=[10001085], state=1)
        select_camera(triggerId=299, enable=True) # action name="카메라리셋" interpolationTime="0.0"/
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 이벤트시작()


class 이벤트시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            select_camera(triggerId=300, enable=True)
            set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
            return 캐릭터선택대기()


class 캐릭터선택대기(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        show_guide_summary(entityId=20003851, textId=20003851)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001083], arg2=0):
            return 천둥선택()
        if object_interacted(interactIds=[10001084], arg2=0):
            return 알론선택()
        if object_interacted(interactIds=[10001085], arg2=0):
            return 오스칼선택()

    def on_exit(self):
        hide_guide_summary(entityId=20003851)
        move_user(mapId=2000385, portalId=2)


class 천둥선택(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        add_buff(boxIds=[199], skillId=99910090, level=1, arg4=False, arg5=False)
        select_camera(triggerId=311, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 게임준비()


class 알론선택(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=True)
        add_buff(boxIds=[199], skillId=99910100, level=1, arg4=False, arg5=False)
        select_camera(triggerId=312, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 게임준비()


class 오스칼선택(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=True)
        add_buff(boxIds=[199], skillId=99910110, level=1, arg4=False, arg5=False)
        select_camera(triggerId=313, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 게임준비()


class 게임준비(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_UI_Start_01')
        create_widget(type='ScoreBoard')
        widget_action(type='ScoreBoard', func='OpenBoard', widgetArg='1') # 스코어 창 열기  arg3는 위치 (1:중앙:다크스트림, 2:우상단:아케이드)
        select_camera(triggerId=301, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 게임시작()


class 게임시작(state.State):
    def on_enter(self):
        widget_action(type='ScoreBoard', func='SetScore', widgetArg='0', desc='점수 강제 설정') # action name="WidgetAction" arg1="ScoreBoard" arg2="AddScore" arg3="10" desc="점수 강제 추가"/
        show_count_ui(text='$02000385_BF__VIP_DUNGEON_MAIN__0$', stage=1, count=3)
        set_event_ui(type=0, arg2='1,5')
        select_camera(triggerId=302, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드시작1()


class 라운드시작1(state.State):
    def on_enter(self):
        set_user_value(triggerId=9991001, key='round1start', value=1)
        set_timer(timerId='30', seconds=30, clearAtZero=False, display=True, arg5=80)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 라운드종료1()


class 라운드종료1(state.State):
    def on_enter(self):
        show_count_ui(text='$02000385_BF__VIP_DUNGEON_MAIN__1$', stage=2, count=3)
        set_event_ui(type=0, arg2='2,5')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드시작2()


class 라운드시작2(state.State):
    def on_enter(self):
        set_user_value(triggerId=9991001, key='round2start', value=1)
        set_timer(timerId='30', seconds=30, clearAtZero=False, display=True, arg5=80)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 라운드종료2()


class 라운드종료2(state.State):
    def on_enter(self):
        show_count_ui(text='$02000385_BF__VIP_DUNGEON_MAIN__2$', stage=3, count=3)
        set_event_ui(type=0, arg2='3,5')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드시작3()


class 라운드시작3(state.State):
    def on_enter(self):
        set_user_value(triggerId=9991001, key='round3start', value=1)
        set_timer(timerId='30', seconds=30, clearAtZero=False, display=True, arg5=80)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 라운드종료3()


class 라운드종료3(state.State):
    def on_enter(self):
        show_count_ui(text='$02000385_BF__VIP_DUNGEON_MAIN__3$', stage=4, count=3)
        set_event_ui(type=0, arg2='4,5')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드시작4()


class 라운드시작4(state.State):
    def on_enter(self):
        set_user_value(triggerId=9991001, key='round4start', value=1)
        set_timer(timerId='30', seconds=30, clearAtZero=False, display=True, arg5=80)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 라운드종료4()


class 라운드종료4(state.State):
    def on_enter(self):
        show_count_ui(text='$02000385_BF__VIP_DUNGEON_MAIN__4$', stage=5, count=3)
        set_event_ui(type=0, arg2='5,5')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드시작5()


class 라운드시작5(state.State):
    def on_enter(self):
        set_user_value(triggerId=9991001, key='round5start', value=1)
        set_timer(timerId='30', seconds=30, clearAtZero=False, display=True, arg5=80)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 게임종료()


class 게임종료(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        set_event_ui(type=0, arg2='0,0')
        move_user(mapId=2000385, portalId=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 정산()


class 정산(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[0])
        widget_action(type='ScoreBoard', func='CloseBoard')
        remove_buff(boxId=199, skillId=99910090)
        remove_buff(boxId=199, skillId=99910100)
        remove_buff(boxId=199, skillId=99910110)

    def on_tick(self) -> state.State:
        if widget_condition(type='ScoreBoard', name='Compare', condition='>=,1500', desc='비교 연산 (연산자,대상값)'):
            debug_string(value='1500점 이상')
            return 보상()
        if widget_condition(type='ScoreBoard', name='Compare', condition='>=,1000', desc='비교 연산 (연산자,대상값)'):
            debug_string(value='1000점 이상')
            return 보상()
        if wait_tick(waitTick=1000):
            return 보상()


class 보상(state.State):
    def on_enter(self):
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True)
        dungeon_clear()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


