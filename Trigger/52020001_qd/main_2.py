""" trigger/52020001_qd/main_2.xml """
from common import *
import state


class 차감지2(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2]):
            return 잠시기다림_1()


class 잠시기다림_1(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 타이머시작()

    def on_exit(self):
        set_event_ui(type=1, arg2='폭격이 더욱 거세집니다. 서둘러 이동하세요!', arg3='4000')


class 타이머시작(state.State):
    def on_enter(self):
        set_timer(timerId='101', seconds=180, clearAtZero=True, display=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 몬스터출현_3()


class 몬스터출현_3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[6100002], arg2=False)
        create_monster(spawnIds=[6000011], arg2=False)
        create_monster(spawnIds=[6000012], arg2=False)
        create_monster(spawnIds=[6000013], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 몬스터사망_3()
        if time_expired(timerId='101'):
            return 실패()


class 몬스터사망_3(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 몬스터출현_4()
        if time_expired(timerId='101'):
            return 실패()


class 몬스터출현_4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[6000014], arg2=False)
        create_monster(spawnIds=[6000015], arg2=False)
        create_monster(spawnIds=[6000016], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 몬스터사망_4()
        if time_expired(timerId='101'):
            return 실패()


class 몬스터사망_4(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 생성_2()
        if time_expired(timerId='101'):
            return 실패()


class 생성_2(state.State):
    def on_enter(self):
        reset_timer(timerId='101')
        set_interact_object(triggerIds=[10002002], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 작동_2()


class 작동_2(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002002], arg2=0):
            return 연출시작_2()


class 연출시작_2(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[6100002])
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=1)
        visible_my_pc(isVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2000005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 폭발_2()


class 폭발_2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10001], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 맵폭발연출_1()


class 맵폭발연출_1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10031], visible=True)
        set_skill(triggerIds=[6004], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400):
            return 카메라연출()


class 카메라연출(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2000006], returnView=False)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return pc소환_2()


class pc소환_2(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=True)
        move_user(mapId=52020001, portalId=12)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return 카메라리셋()


class 카메라리셋(state.State):
    def on_enter(self):
        set_portal(portalId=16, visible=True, enabled=True, minimapVisible=False)
        reset_camera(interpolationTime=0.8)

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


