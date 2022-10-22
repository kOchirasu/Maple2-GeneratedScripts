""" trigger/52020001_qd/main_4.xml """
from common import *
import state


class 차감지2(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002010], state=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[4]):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 카메리이동()


class 카메리이동(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2000010], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 탈것등장()


class 탈것등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[7001], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 폭발_1()


class 폭발_1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10052], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 폭발_2()


class 폭발_2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10053], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 폭발_3()


class 폭발_3(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10054], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 맵폭발연출()


class 맵폭발연출(state.State):
    def on_enter(self):
        set_effect(triggerIds=[10051], visible=True)
        set_skill(triggerIds=[6007], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4400):
            return 연출끝()


class 연출끝(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2000010], returnView=True)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 오브젝트반응()

    def on_exit(self):
        create_monster(spawnIds=[6100004], arg2=False)


class 오브젝트반응(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='좋아! 이 녀석을 타고 돌격해야겠어!!', arg4=3, arg5=0)
        set_interact_object(triggerIds=[10002010], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 오브젝트반응_2()


class 오브젝트반응_2(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002010], arg2=0):
            return 오브젝트반응_3()


class 오브젝트반응_3(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002010], state=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 카메라연출()

    def on_exit(self):
        destroy_monster(spawnIds=[7001], arg2=False)


class 카메라연출(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 알림()


class 알림(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='출력이 부족해 크리티아스로 진입할 수 없습니다.', arg3='4000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 알림_2()


class 알림_2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='적들을 처치하면 에너지를 충전할 수 있습니다.\n제한시간 내에 100%충전해, 크리티아스로 진입하세요!', arg3='4000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 타이머시작()


class 타이머시작(state.State):
    def on_enter(self):
        set_timer(timerId='110', seconds=360, clearAtZero=True, display=True, arg5=80)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 몬스터생성()


class 몬스터생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[6000030], arg2=False)
        create_monster(spawnIds=[6000031], arg2=False)
        create_monster(spawnIds=[6000032], arg2=False)
        create_monster(spawnIds=[6000033], arg2=False)
        create_monster(spawnIds=[6000034], arg2=False)
        set_user_value(triggerId=909, key='respawn', value=1)
        set_user_value(triggerId=910, key='respawn', value=1)
        set_user_value(triggerId=911, key='respawn', value=1)
        set_user_value(triggerId=912, key='respawn', value=1)
        set_user_value(triggerId=913, key='respawn', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='110'):
            return 실패()


class 실패(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2000009], returnView=True)
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


