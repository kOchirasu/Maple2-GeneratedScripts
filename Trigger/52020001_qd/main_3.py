""" trigger/52020001_qd/main_3.xml """
from common import *
import state


class 차감지2(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[3]):
            return 잠시기다림_1()


class 잠시기다림_1(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 타이머시작()


class 타이머시작(state.State):
    def on_enter(self):
        set_timer(timerId='102', seconds=180, clearAtZero=True, display=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 몬스터출현_5()


class 몬스터출현_5(state.State):
    def on_enter(self):
        create_monster(spawnIds=[6100003], arg2=False)
        create_monster(spawnIds=[6000018], arg2=False)
        create_monster(spawnIds=[6000019], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 몬스터체력50()
        if time_expired(timerId='102'):
            return 실패()


class 몬스터체력50(state.State):
    def on_tick(self) -> state.State:
        if any_one():
            return 생성_2()
        if time_expired(timerId='102'):
            return 실패()


class 생성_2(state.State):
    def on_enter(self):
        add_buff(boxIds=[6000018], skillId=49286001, level=1, arg4=True)
        add_buff(boxIds=[6000019], skillId=49286001, level=1, arg4=True)
        reset_timer(timerId='102')
        set_interact_object(triggerIds=[10002003], state=1)
        set_event_ui(type=1, arg2='아크레온이 거대해지며 모든공격을 튕겨내기 시작했습니다.', arg3='4000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 작동_2()

    def on_exit(self):
        set_user_value(triggerId=921, key='respawn', value=1)


class 작동_2(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002003], arg2=0):
            return 연출시작_2()

    def on_exit(self):
        set_user_value(triggerId=921, key='respawn_end', value=2)


class 연출시작_2(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[6100003])
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=1)
        visible_my_pc(isVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2000007], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 폭발_2()


class 폭발_2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10002], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=900):
            return 맵폭발연출_1()


class 맵폭발연출_1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10041], visible=True)
        set_skill(triggerIds=[6005], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400):
            return 카메라연출()


class 카메라연출(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2000008], returnView=False)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=0)
        destroy_monster(spawnIds=[6000018])
        destroy_monster(spawnIds=[6000019])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return pc소환_2()


class pc소환_2(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=True)
        move_user(mapId=52020001, portalId=13)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 맵폭발연출_2()


class 맵폭발연출_2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10042], visible=True)
        set_skill(triggerIds=[6006], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400):
            return 카메라리셋()


class 카메라리셋(state.State):
    def on_enter(self):
        set_portal(portalId=17, visible=True, enabled=True, minimapVisible=False)
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


class 끝(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return None


