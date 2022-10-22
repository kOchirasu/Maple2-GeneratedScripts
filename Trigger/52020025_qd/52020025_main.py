""" trigger/52020025_qd/52020025_main.xml """
from common import *
import state


class 감지(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1001], visible=True)
        set_agent(triggerIds=[9001], visible=True)
        set_agent(triggerIds=[9002], visible=True)
        set_agent(triggerIds=[9003], visible=True)
        set_agent(triggerIds=[9004], visible=True)
        set_agent(triggerIds=[9005], visible=True)
        set_agent(triggerIds=[9006], visible=True)
        set_agent(triggerIds=[9007], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 카메라_시작()


class 카메라_시작(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='으아아악!!!', arg4=2)
        set_scene_skip(state=카메라_종료, arg2='exit')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_mesh(triggerIds=[1001], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카메라_PC()


class 카메라_PC(state.State):
    def on_enter(self):
        select_camera(triggerId=501, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카메라_보스등장()


class 카메라_보스등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_Bossmove')
        set_npc_rotation(spawnId=0, rotation=180)
        set_conversation(type=1, spawnId=0, script='응??', arg4=2)
        select_camera(triggerId=502, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라_PC도망준비()


class 카메라_PC도망준비(state.State):
    def on_enter(self):
        set_npc_rotation(spawnId=0, rotation=180)
        set_conversation(type=1, spawnId=0, script='튀자!!', arg4=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카메라_종료()


class 카메라_종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        reset_camera()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_agent(triggerIds=[9001], visible=False)
        set_agent(triggerIds=[9002], visible=False)
        set_agent(triggerIds=[9003], visible=False)
        set_agent(triggerIds=[9004], visible=False)
        set_agent(triggerIds=[9005], visible=False)
        set_agent(triggerIds=[9006], visible=False)
        set_agent(triggerIds=[9007], visible=False)

    def on_tick(self) -> state.State:
        if true():
            return 달리기시작()


class 달리기시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=False)
        set_local_camera(cameraId=511, enable=True)
        move_user_path(patrolName='MS2PatrolData_PCrun')
        move_npc(spawnId=102, patrolName='MS2PatrolData_Bossrun')
        set_event_ui(type=1, arg2='무서운 몬스터로부터 도망치세요', arg3='4000', arg4='0')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[902]):
            return 탈출성공()


class 탈출성공(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])
        set_onetime_effect(id=1, enable=True, path='BG\Common\ScreenMask\Eff_CameraMasking_white.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        move_user(mapId=2020008, portalId=6001)


