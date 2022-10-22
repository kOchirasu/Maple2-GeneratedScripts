""" trigger/52020027_qd/52020027_main.xml """
from common import *
import state


class 감지(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990002, key='Boss', value=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 연출감지()


class 연출감지(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[902]):
            return 카메라_시작()


class 카메라_시작(state.State):
    def on_enter(self):
        set_scene_skip(state=카메라_종료, arg2='exit')
        move_user(mapId=52020027, portalId=2)
        create_monster(spawnIds=[101], arg2=False)
        set_npc_emotion_loop(spawnId=101, sequenceName='Sit_Down_A', duration=5000)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=501, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카메라_세리하대사1()


class 카메라_세리하대사1(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=22000114, script='대체 어딨는거지?', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카메라_세리하대사2()


class 카메라_세리하대사2(state.State):
    def on_enter(self):
        select_camera(triggerId=502, enable=True)
        set_npc_rotation(spawnId=101, rotation=180)
        set_conversation(type=2, spawnId=22000114, script='여기까지 쫓아왔어?', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라_세리하대사3()


class 카메라_세리하대사3(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=22000114, script='이제 결판을 내자!!', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라_종료()


class 카메라_종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        reset_camera(interpolationTime=0.1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 보스전시작()


class 보스전시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111], arg2=True)
        set_user_value(triggerId=99990002, key='Boss', value=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[111]):
            return 보스전종료()


class 보스전종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        set_achievement(triggerId=904, achieve='KritiasScrimmage')
        set_event_ui(type=1, arg2='연출들어갈 예정입니다', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        move_user(mapId=2020006, portalId=6001)


