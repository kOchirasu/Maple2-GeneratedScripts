""" trigger/52020025_qd/52020025_main.xml """
import trigger_api


class 감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[1001], visible=True)
        self.set_agent(triggerIds=[9001], visible=True)
        self.set_agent(triggerIds=[9002], visible=True)
        self.set_agent(triggerIds=[9003], visible=True)
        self.set_agent(triggerIds=[9004], visible=True)
        self.set_agent(triggerIds=[9005], visible=True)
        self.set_agent(triggerIds=[9006], visible=True)
        self.set_agent(triggerIds=[9007], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[901]):
            return 카메라_시작(self.ctx)


class 카메라_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=0, script='으아아악!!!', arg4=2)
        self.set_scene_skip(state=카메라_종료, action='exit')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_mesh(triggerIds=[1001], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카메라_PC(self.ctx)


class 카메라_PC(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=501, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카메라_보스등장(self.ctx)


class 카메라_보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Bossmove')
        self.set_npc_rotation(spawnId=0, rotation=180)
        self.set_conversation(type=1, spawnId=0, script='응??', arg4=2)
        self.select_camera(triggerId=502, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라_PC도망준비(self.ctx)


class 카메라_PC도망준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_rotation(spawnId=0, rotation=180)
        self.set_conversation(type=1, spawnId=0, script='튀자!!', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카메라_종료(self.ctx)


class 카메라_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101])
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_agent(triggerIds=[9001], visible=False)
        self.set_agent(triggerIds=[9002], visible=False)
        self.set_agent(triggerIds=[9003], visible=False)
        self.set_agent(triggerIds=[9004], visible=False)
        self.set_agent(triggerIds=[9005], visible=False)
        self.set_agent(triggerIds=[9006], visible=False)
        self.set_agent(triggerIds=[9007], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 달리기시작(self.ctx)


class 달리기시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.set_local_camera(cameraId=511, enable=True)
        self.move_user_path(patrolName='MS2PatrolData_PCrun')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_Bossrun')
        self.set_event_ui(type=1, arg2='무서운 몬스터로부터 도망치세요', arg3='4000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[902]):
            return 탈출성공(self.ctx)


class 탈출성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[102])
        self.set_onetime_effect(id=1, enable=True, path='BG\\Common\\ScreenMask\\Eff_CameraMasking_white.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=2020008, portalId=6001)


initial_state = 감지
