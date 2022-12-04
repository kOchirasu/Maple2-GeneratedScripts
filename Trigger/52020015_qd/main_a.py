""" trigger/52020015_qd/main_a.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_effect(triggerIds=[5005], visible=False)
        self.set_effect(triggerIds=[5006], visible=False)
        self.set_effect(triggerIds=[5007], visible=False)
        self.set_effect(triggerIds=[5008], visible=False)
        self.set_effect(triggerIds=[5100], visible=False) # 커튼 이펙트
        self.set_effect(triggerIds=[5101], visible=False) # 입구 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60200095], questStates=[1]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.create_monster(spawnIds=[102], animationEffect=True)
        self.create_monster(spawnIds=[103], animationEffect=True)
        self.create_monster(spawnIds=[104], animationEffect=True)
        self.create_monster(spawnIds=[105], animationEffect=True)
        self.create_monster(spawnIds=[106], animationEffect=True)
        self.create_monster(spawnIds=[107], animationEffect=True)
        self.create_monster(spawnIds=[108], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[60200095], questStates=[1]):
            return Scene_Ready(self.ctx)


class Scene_Ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Scene_01(self.ctx)


class Scene_01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Scene_02(self.ctx)


class Scene_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5100], visible=True) # 입구 이펙트
        self.set_effect(triggerIds=[5101], visible=True) # 입구 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Scene_03(self.ctx)


class Scene_03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4101,4102], returnView=False)
        self.set_scene_skip(state=MobSpawn_A, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Scene_04(self.ctx)


class Scene_04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4105], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Scene_05(self.ctx)


class Scene_05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4104,4103], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return Scene_06(self.ctx)


class Scene_06(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4201], returnView=False)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Down_Idle_A', duration=10000)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Down_Idle_A', duration=10000)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Down_Idle_A', duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Scene_07(self.ctx)


class Scene_07(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4202], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Scene_08(self.ctx)


class Scene_08(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4204], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Scene_09(self.ctx)


class Scene_09(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4202], returnView=False)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return MobSpawn_A(self.ctx)


class MobSpawn_A(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=101, addSpawnId=201)
        self.change_monster(removeSpawnId=102, addSpawnId=202)
        self.change_monster(removeSpawnId=103, addSpawnId=203)
        self.set_effect(triggerIds=[5006], visible=True)
        self.set_effect(triggerIds=[5007], visible=True)
        self.set_effect(triggerIds=[5008], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Play(self.ctx)


class Play(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2003]):
            return MobSpawn_B(self.ctx)


class MobSpawn_B(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=104, addSpawnId=204)
        self.change_monster(removeSpawnId=105, addSpawnId=205)
        self.change_monster(removeSpawnId=106, addSpawnId=206)
        self.change_monster(removeSpawnId=107, addSpawnId=207)
        self.change_monster(removeSpawnId=108, addSpawnId=208)
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_effect(triggerIds=[5002], visible=True)
        self.set_effect(triggerIds=[5003], visible=True)
        self.set_effect(triggerIds=[5004], visible=True)
        self.set_effect(triggerIds=[5005], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201,202,203,204,205,206,207,208]):
            return Scene_10(self.ctx)


class Scene_10(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.set_scene_skip(state=End, action='Exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Scene_11(self.ctx)


class Scene_11(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5100], visible=False) # 입구 이펙트
        self.set_effect(triggerIds=[5101], visible=False) # 입구 이펙트
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)


initial_state = Idle
