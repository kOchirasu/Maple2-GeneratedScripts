""" trigger/52000043_qd/50001452.xml """
import trigger_api


class 선행퀘스트체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10001017], state=2)
        self.set_interact_object(triggerIds=[10001018], state=2)
        self.set_interact_object(triggerIds=[10001019], state=2)
        self.set_interact_object(triggerIds=[10001020], state=2)
        self.set_interact_object(triggerIds=[10001021], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[50001451], questStates=[3]):
            self.destroy_monster(spawnIds=[1001,2001])
            return 시작조건(self.ctx)


class 시작조건(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1001,2001], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[50001452], questStates=[1]):
            return 연출시작(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50001452], questStates=[2]):
            self.destroy_monster(spawnIds=[1003,2003])
            return NPC만배치(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50001452], questStates=[3]):
            self.destroy_monster(spawnIds=[1003,2003])
            return NPC만배치(self.ctx)


class NPC만배치(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1001,2001])
        self.create_monster(spawnIds=[1003,2003], animationEffect=False)
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[50001454], questStates=[2]):
            self.destroy_monster(spawnIds=[1003,2003])
            return 종료(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50001454], questStates=[3]):
            self.destroy_monster(spawnIds=[1003,2003])
            return 종료(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1001,2001])
        self.create_monster(spawnIds=[1002,2002], animationEffect=False)
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=True, arg3=0, delay=0, scale=0)
        self.select_camera(triggerId=304, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return NPC이동01(self.ctx)


class NPC이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002A')
        self.move_npc(spawnId=2002, patrolName='MS2PatrolData_2002A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=101, spawnIds=[2002]):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=304, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002B')
        self.move_npc(spawnId=2002, patrolName='MS2PatrolData_2002B')
        self.set_interact_object(triggerIds=[10001017], state=1)
        self.set_interact_object(triggerIds=[10001018], state=1)
        self.set_interact_object(triggerIds=[10001019], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001019], stateValue=0):
            return 부서짐연출(self.ctx)


class 부서짐연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10001017], state=2)
        self.set_interact_object(triggerIds=[10001018], state=2)
        self.set_interact_object(triggerIds=[10001020], state=1)
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=False, arg3=0, delay=200, scale=2)
        self.select_camera(triggerId=306, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=향로반응대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 향로반응대기(self.ctx)

    def on_exit(self) -> None:
        self.select_camera(triggerId=306, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 향로반응대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[50001452], questStates=[2]):
            return NPC이동02(self.ctx)


class NPC이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002C')
        self.move_npc(spawnId=2002, patrolName='MS2PatrolData_2002C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[1002]):
            return NPC교체01(self.ctx)


class NPC교체01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1002])
        self.create_monster(spawnIds=[1003], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=103, spawnIds=[2002]):
            return NPC교체02(self.ctx)


class NPC교체02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[2002])
        self.create_monster(spawnIds=[2003], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 선행퀘스트체크
