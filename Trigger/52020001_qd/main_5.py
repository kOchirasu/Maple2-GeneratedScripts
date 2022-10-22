""" trigger/52020001_qd/main_5.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[4]):
            return 기다림()


class 기다림(state.State):
    def on_enter(self):
        shadow_expedition(type='OpenBossGauge', maxGaugePoint=300, title='출력 에너지')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 체력조건_1()


class 체력조건_1(state.State):
    def on_tick(self) -> state.State:
        if shadow_expedition_reach_point(point=150):
            return 알림_1()


class 알림_1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='에너지가 50%충전 되었습니다.', arg3='4000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 체력조건_2()

    def on_exit(self):
        create_monster(spawnIds=[6000041], arg2=False)
        create_monster(spawnIds=[6000042], arg2=False)
        add_buff(boxIds=[6000041], skillId=49286001, level=1, arg4=True)
        add_buff(boxIds=[6000042], skillId=49286001, level=1, arg4=True)


class 체력조건_2(state.State):
    def on_tick(self) -> state.State:
        if shadow_expedition_reach_point(point=300):
            return 알림_5()

    def on_exit(self):
        set_achievement(type='trigger', achieve='EscapeToKritias')


class 알림_5(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='에너지가 100%충전 되었습니다.', arg3='4000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 알림_6()


class 알림_6(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='곧 최대 출력으로 돌진 합니다.', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 마지막_연출()


class 마지막_연출(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        select_camera_path(pathIds=[2000009], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 캐릭터숨기기()


class 캐릭터숨기기(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=False)
        create_monster(spawnIds=[7002], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마지막_연출_2()


class 마지막_연출_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return AI연출()


class AI연출(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=1)
        select_camera_path(pathIds=[2000013], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return AI연출_2()


class AI연출_2(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=0, script='준비완료! 크리티아스로 돌진!', arg4=3, arg5=0)
        set_ai_extra_data(key='wing', value=1, boxId=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 끝()


class 끝(state.State):
    def on_enter(self):
        set_ai_extra_data(key='wing', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 끝_2()


class 끝_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 맵이동()


class 맵이동(state.State):
    def on_enter(self):
        move_user(mapId=2020001, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None


