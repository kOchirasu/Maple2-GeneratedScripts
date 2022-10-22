""" trigger/52020001_qd/main.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_skill(triggerIds=[40001], isEnable=False)
        set_skill(triggerIds=[6001], isEnable=False)
        set_interact_object(triggerIds=[10002001], state=2)
        set_interact_object(triggerIds=[10002002], state=2)
        set_interact_object(triggerIds=[10002003], state=2)
        create_monster(spawnIds=[6000020], arg2=False)
        set_effect(triggerIds=[10090], visible=False)
        set_effect(triggerIds=[10091], visible=False)
        set_effect(triggerIds=[10092], visible=False)
        set_mesh(triggerIds=[80000], visible=False, arg3=0, arg4=0, arg5=0)
        set_portal(portalId=14, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[5]):
            return 인트로()


class 인트로(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 인트로_카메라()


class 인트로_카메라(state.State):
    def on_enter(self):
        select_camera(triggerId=2000012, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 인트로_폭발_1()


class 인트로_폭발_1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10011], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 인트로_폭발_2()


class 인트로_폭발_2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10012], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 인트로_폭발_3()


class 인트로_폭발_3(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10013], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 인트로_폭발_4()


class 인트로_폭발_4(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10014], visible=True)
        set_skill(triggerIds=[6001], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return 인트로_종료()


class 인트로_종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=0)
        select_camera(triggerId=2000012, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 알림()


class 알림(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='시간이 얼마 없습니다.\n폭격을 일삼는 에고웨폰들을 처치하며 크리티아스로 침투하세요.', arg3='4000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 감지()


class 감지(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1]):
            return 타이머시작()


class 타이머시작(state.State):
    def on_enter(self):
        set_timer(timerId='100', seconds=180, clearAtZero=True, display=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 몬스터출현_1()


class 몬스터출현_1(state.State):
    def on_enter(self):
        set_skill(triggerIds=[40001], isEnable=True)
        create_monster(spawnIds=[6000001], arg2=False)
        create_monster(spawnIds=[6000002], arg2=False)
        create_monster(spawnIds=[6000003], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 몬스터사망_1()
        if time_expired(timerId='100'):
            return 실패()

    def on_exit(self):
        set_conversation(type=1, spawnId=0, script='서둘러야 해!', arg4=3, arg5=0)


class 몬스터사망_1(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 몬스터출현_2()
        if time_expired(timerId='100'):
            return 실패()


class 몬스터출현_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[6000004], arg2=False)
        create_monster(spawnIds=[6000005], arg2=False)
        create_monster(spawnIds=[6000006], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 몬스터사망_2()
        if time_expired(timerId='100'):
            return 실패()


class 몬스터사망_2(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 스위치생성연출()
        if time_expired(timerId='100'):
            return 실패()


class 스위치생성연출(state.State):
    def on_enter(self):
        reset_timer(timerId='100')
        destroy_monster(spawnIds=[6100001])
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 스위치생성연출_카메라()


class 스위치생성연출_카메라(state.State):
    def on_enter(self):
        select_camera(triggerId=2000003, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 생성_1()


class 생성_1(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002001], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 스위치생성연출_카메라_초기화()


class 스위치생성연출_카메라_초기화(state.State):
    def on_enter(self):
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=0)
        select_camera(triggerId=2000003, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 작동()

    def on_exit(self):
        create_monster(spawnIds=[6100001], arg2=False)
        set_conversation(type=1, spawnId=0, script='저 스위치를 한번 작동시켜 볼까?', arg4=3, arg5=0)


class 작동(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002001], arg2=0):
            return 연출시작_1()


class 연출시작_1(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[6100001])
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=1)
        visible_my_pc(isVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 발사_카메라연출_1()


class 발사_카메라연출_1(state.State):
    def on_enter(self):
        select_camera(triggerId=2000001, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 폭발배경연출_1()


class 폭발배경연출_1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10028], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 폭발배경연출_2()


class 폭발배경연출_2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10029], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 폭발_1()


class 폭발_1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10000], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 날라감_1()


class 날라감_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=0)
        select_camera_path(pathIds=[2000002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return pc소환()


class pc소환(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=True)
        move_user(mapId=52020001, portalId=11)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 폭발배경연출_3()


class 폭발배경연출_3(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10023], visible=True)
        set_skill(triggerIds=[6002], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400):
            return 폭발배경연출_4()


class 폭발배경연출_4(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10024], visible=True)
        set_skill(triggerIds=[6002], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 폭발배경연출_5()


class 폭발배경연출_5(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10025], visible=True)
        set_skill(triggerIds=[6002], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400):
            return 맵폭발연출_1()


class 맵폭발연출_1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10021], visible=True)
        set_skill(triggerIds=[6002], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 맵폭발연출_2()


class 폭발배경연출_6(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10026], visible=True)
        set_skill(triggerIds=[6002], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 폭발배경연출_7()


class 폭발배경연출_7(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10027], visible=True)
        set_skill(triggerIds=[6002], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 맵폭발연출_2()


class 맵폭발연출_2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10022], visible=True)
        set_skill(triggerIds=[6003], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 카메라리셋()


class 카메라리셋(state.State):
    def on_enter(self):
        set_portal(portalId=15, visible=True, enabled=True, minimapVisible=False)
        reset_camera(interpolationTime=0.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None


class 실패(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10090], visible=True)
        set_effect(triggerIds=[10091], visible=True)
        set_effect(triggerIds=[10092], visible=True)
        set_mesh(triggerIds=[80000], visible=True, arg3=0, arg4=0, arg5=0)
        destroy_monster(spawnIds=[-1])
        set_event_ui(type=1, arg2='미션에 실패하였습니다. 다시 재도전 해보세요.', arg3='4000')
        move_user(mapId=52020001, portalId=99)
        set_portal(portalId=14, visible=True, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return None


