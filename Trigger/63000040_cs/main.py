""" trigger/63000040_cs/main.xml """
import trigger_api


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101,103,104], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002652], questStates=[3]):
            return start_02(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002652], questStates=[2]):
            return start_02_ready(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002652], questStates=[1]):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=25200474, textId=25200474)
        self.set_effect(triggerIds=[7001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002652], questStates=[2]):
            return start_02_ready(self.ctx)


class start_02_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=25200474)
        self.set_effect(triggerIds=[7001], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002652], questStates=[3]):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_2001') # 연출용 틴차이 이동
        self.move_user_path(patrolName='MS2PatrolData_2002') # 유저를 이동시킨다
        self.select_camera_path(pathIds=[8001,8002], returnView=False)
        self.set_conversation(type=2, spawnId=11001708, script='$63000040_CS__MAIN__0$', arg4=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=3000)
        self.set_conversation(type=2, spawnId=11001708, script='$63000040_CS__MAIN__1$', arg4=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return start_04(self.ctx)


class start_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_2003') # 연출용 틴차이 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return start_05(self.ctx)


class start_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2003') # 연출용 틴차이 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return start_06(self.ctx)


class start_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_2003') # 유저를 이동시킨다

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.select_camera_path(pathIds=[8003], returnView=False)
            return start_07(self.ctx)


class start_07(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8003], returnView=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = ready
