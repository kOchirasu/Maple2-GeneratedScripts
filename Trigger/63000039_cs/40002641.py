""" trigger/63000039_cs/40002641.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=201, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_off')
        self.set_mesh(triggerIds=[3000,3001,3002], visible=True)
        self.set_mesh(triggerIds=[3003,3004,3005], visible=False)
        self.set_interact_object(triggerIds=[10001025], state=0)
        self.create_monster(spawnIds=[1001,1002,1003,1004,1005], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[40002641], questStates=[1]):
            return NPC말풍선(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[40002641], questStates=[2]):
            return 유저이동(self.ctx)


class NPC말풍선(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_conversation(type=1, spawnId=1002, script='$63000039_CS__40002641__0$', arg4=4, arg5=0)
            self.set_conversation(type=1, spawnId=1005, script='$63000039_CS__40002641__1$', arg4=4, arg5=2)
            return 오브젝트반응대기(self.ctx)


class 오브젝트반응대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001025], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001025], stateValue=0):
            self.set_mesh(triggerIds=[3000,3001,3002], visible=False)
            self.set_mesh(triggerIds=[3003,3004,3005], visible=True)
            return NPC를이동(self.ctx)


class NPC를이동(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_1001')
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002')
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_1003')
        self.move_npc(spawnId=1004, patrolName='MS2PatrolData_1004')
        self.move_npc(spawnId=1005, patrolName='MS2PatrolData_1005')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return PC이동(self.ctx)


class PC이동(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=201, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_on')
        self.move_user_path(patrolName='MS2PatrolData_PC')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4500):
            return PC말풍선(self.ctx)


class PC말풍선(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=302, enable=True)
        self.set_conversation(type=1, spawnId=0, script='$63000039_CS__40002641__2$', arg4=4, arg5=0)
        self.set_achievement(triggerId=199, type='trigger', achieve='SaveBackstreetPeople')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 유저이동조건(self.ctx)


class 유저이동조건(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[40002641], questStates=[2]):
            return 유저이동(self.ctx)


class 유저이동(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=302, enable=False)
        self.move_user(mapId=2000275, portalId=30)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
