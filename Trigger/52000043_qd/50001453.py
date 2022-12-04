""" trigger/52000043_qd/50001453.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1003,2003])
        self.set_agent(triggerIds=[9000], visible=False)
        self.set_agent(triggerIds=[9001], visible=False)
        self.set_agent(triggerIds=[9002], visible=False)
        self.set_agent(triggerIds=[9003], visible=False)
        self.set_agent(triggerIds=[9004], visible=False)
        self.set_agent(triggerIds=[9005], visible=False)
        self.set_agent(triggerIds=[9006], visible=False)
        self.set_agent(triggerIds=[9007], visible=False)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_effect(triggerIds=[604], visible=False)
        self.set_effect(triggerIds=[605], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[50001453], questStates=[1]):
            self.destroy_monster(spawnIds=[1003,2003])
            return 시작조건(self.ctx)


class 시작조건(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1003,2003], animationEffect=False)
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=False, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001020], state=2)
        self.set_interact_object(triggerIds=[10001021], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001021], stateValue=0):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9000], visible=True)
        self.set_agent(triggerIds=[9001], visible=True)
        self.set_agent(triggerIds=[9002], visible=True)
        self.set_agent(triggerIds=[9003], visible=True)
        self.set_agent(triggerIds=[9004], visible=True)
        self.set_agent(triggerIds=[9005], visible=True)
        self.set_agent(triggerIds=[9006], visible=True)
        self.set_agent(triggerIds=[9007], visible=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[2100,2101], animationEffect=False)
        self.select_camera(triggerId=303, enable=True)
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_1004A')
        self.move_npc(spawnId=2003, patrolName='MS2PatrolData_2004A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return NPC대사01(self.ctx)


class NPC대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[603], visible=True)
        self.set_conversation(type=2, spawnId=29000121, script='$52000043_QD__50001453__0$', arg4=3)
        self.set_skip(state=NPC대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 준타대사01(self.ctx)


class NPC대사01스킵(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[603], visible=False)
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 준타대사01(self.ctx)


class 준타대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[604], visible=True)
        self.set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001453__1$', arg4=3)
        self.set_skip(state=준타대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 준타대사02(self.ctx)


class 준타대사01스킵(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[604], visible=False)
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 준타대사02(self.ctx)


class 준타대사02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001453__2$', arg4=2)
        self.set_skip(state=준타대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 틴차이대사01(self.ctx)


class 준타대사02스킵(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 틴차이대사01(self.ctx)


class 틴차이대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[605], visible=True)
        self.set_conversation(type=2, spawnId=11001708, script='$52000043_QD__50001453__3$', arg4=4)
        self.set_skip(state=틴차이대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출종료(self.ctx)


class 틴차이대사01스킵(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[605], visible=False)
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1003,2003])
        self.create_monster(spawnIds=[1004,2004], animationEffect=False)
        self.set_agent(triggerIds=[9000], visible=False)
        self.set_agent(triggerIds=[9001], visible=False)
        self.set_agent(triggerIds=[9002], visible=False)
        self.set_agent(triggerIds=[9003], visible=False)
        self.set_agent(triggerIds=[9004], visible=False)
        self.set_agent(triggerIds=[9005], visible=False)
        self.set_agent(triggerIds=[9006], visible=False)
        self.set_agent(triggerIds=[9007], visible=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=303, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2100,2101]):
            return 연출02시작(self.ctx)


class 연출02시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_interact_object(triggerIds=[10001021], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1004, patrolName='MS2PatrolData_1002C')
        self.move_npc(spawnId=2004, patrolName='MS2PatrolData_2002C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[1004]):
            return NPC교체01(self.ctx)


class NPC교체01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1004])
        self.create_monster(spawnIds=[1003], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=103, spawnIds=[2004]):
            return NPC교체02(self.ctx)


class NPC교체02(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2004])
        self.create_monster(spawnIds=[2003], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 연출종료2(self.ctx)


class 연출종료2(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
