""" trigger/52020015_qd/main_a.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)
        set_effect(triggerIds=[5005], visible=False)
        set_effect(triggerIds=[5006], visible=False)
        set_effect(triggerIds=[5007], visible=False)
        set_effect(triggerIds=[5008], visible=False)
        set_effect(triggerIds=[5100], visible=False) # 커튼 이펙트
        set_effect(triggerIds=[5101], visible=False) # 입구 사운드

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200095], questStates=[1]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True)
        create_monster(spawnIds=[102], arg2=True)
        create_monster(spawnIds=[103], arg2=True)
        create_monster(spawnIds=[104], arg2=True)
        create_monster(spawnIds=[105], arg2=True)
        create_monster(spawnIds=[106], arg2=True)
        create_monster(spawnIds=[107], arg2=True)
        create_monster(spawnIds=[108], arg2=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[60200095], questStates=[1]):
            return Scene_Ready()


class Scene_Ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Scene_01()


class Scene_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Scene_02()


class Scene_02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5100], visible=True) # 입구 이펙트
        set_effect(triggerIds=[5101], visible=True) # 입구 이펙트

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Scene_03()


class Scene_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4101,4102], returnView=False)
        set_scene_skip(state=MobSpawn_A, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Scene_04()


class Scene_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4105], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Scene_05()


class Scene_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4104,4103], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return Scene_06()


class Scene_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4201], returnView=False)
        set_npc_emotion_loop(spawnId=101, sequenceName='Down_Idle_A', duration=10000)
        set_npc_emotion_loop(spawnId=102, sequenceName='Down_Idle_A', duration=10000)
        set_npc_emotion_loop(spawnId=103, sequenceName='Down_Idle_A', duration=10000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Scene_07()


class Scene_07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4202], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Scene_08()


class Scene_08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4204], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Scene_09()


class Scene_09(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4202], returnView=False)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return MobSpawn_A()


class MobSpawn_A(state.State):
    def on_enter(self):
        change_monster(removeSpawnId=101, addSpawnId=201)
        change_monster(removeSpawnId=102, addSpawnId=202)
        change_monster(removeSpawnId=103, addSpawnId=203)
        set_effect(triggerIds=[5006], visible=True)
        set_effect(triggerIds=[5007], visible=True)
        set_effect(triggerIds=[5008], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Play()


class Play(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2003]):
            return MobSpawn_B()


class MobSpawn_B(state.State):
    def on_enter(self):
        change_monster(removeSpawnId=104, addSpawnId=204)
        change_monster(removeSpawnId=105, addSpawnId=205)
        change_monster(removeSpawnId=106, addSpawnId=206)
        change_monster(removeSpawnId=107, addSpawnId=207)
        change_monster(removeSpawnId=108, addSpawnId=208)
        set_effect(triggerIds=[5001], visible=True)
        set_effect(triggerIds=[5002], visible=True)
        set_effect(triggerIds=[5003], visible=True)
        set_effect(triggerIds=[5004], visible=True)
        set_effect(triggerIds=[5005], visible=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,203,204,205,206,207,208]):
            return Scene_10()


class Scene_10(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001], returnView=False)
        set_scene_skip(state=End, arg2='Exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Scene_11()


class Scene_11(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5100], visible=False) # 입구 이펙트
        set_effect(triggerIds=[5101], visible=False) # 입구 이펙트
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return End()


class End(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)


