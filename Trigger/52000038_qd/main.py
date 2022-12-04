""" trigger/52000038_qd/main.xml """
import trigger_api


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20020010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002632], questStates=[3]):
            self.set_actor(triggerId=3001, visible=False, initialSequence='Dead_A')
            self.set_actor(triggerId=3002, visible=False, initialSequence='Dead_A')
            self.set_actor(triggerId=3003, visible=False, initialSequence='Dead_A')
            self.set_actor(triggerId=3004, visible=False, initialSequence='Dead_A')
            self.set_actor(triggerId=3005, visible=False, initialSequence='Dead_A')
            return scene_c_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002632], questStates=[2]):
            self.set_actor(triggerId=3001, visible=False, initialSequence='Dead_A')
            self.set_actor(triggerId=3002, visible=False, initialSequence='Dead_A')
            self.set_actor(triggerId=3003, visible=False, initialSequence='Dead_A')
            self.set_actor(triggerId=3004, visible=False, initialSequence='Dead_A')
            self.set_actor(triggerId=3005, visible=False, initialSequence='Dead_A')
            self.create_monster(spawnIds=[131,132], animationEffect=True)
            return scene_c_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002631], questStates=[3]):
            self.set_actor(triggerId=3001, visible=False, initialSequence='Dead_A')
            self.set_actor(triggerId=3002, visible=False, initialSequence='Dead_A')
            self.set_actor(triggerId=3003, visible=False, initialSequence='Dead_A')
            self.set_actor(triggerId=3004, visible=False, initialSequence='Dead_A')
            self.set_actor(triggerId=3005, visible=False, initialSequence='Dead_A')
            self.create_monster(spawnIds=[131,132], animationEffect=True)
            return scene_c_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002631], questStates=[2]):
            self.set_actor(triggerId=3001, visible=False, initialSequence='Dead_A')
            self.set_actor(triggerId=3002, visible=False, initialSequence='Dead_A')
            self.set_actor(triggerId=3003, visible=False, initialSequence='Dead_A')
            self.set_actor(triggerId=3004, visible=False, initialSequence='Dead_A')
            self.set_actor(triggerId=3005, visible=False, initialSequence='Dead_A')
            self.create_monster(spawnIds=[131,132], animationEffect=True)
            return scene_c_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002631], questStates=[1]):
            self.create_monster(spawnIds=[121,122], animationEffect=True)
            return scene_b_02(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002630], questStates=[3]):
            return scene_b_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002630], questStates=[2]):
            return scene_b_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002630], questStates=[1]):
            return ready_02(self.ctx)


class ready_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,102], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[702], questIds=[40002630], questStates=[1]):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2001')
        self.set_conversation(type=1, spawnId=101, script='$52000038_QD__MAIN__0$', arg4=2, arg5=0)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2002')
        self.set_conversation(type=1, spawnId=102, script='$52000038_QD__MAIN__1$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2003')
        self.set_conversation(type=1, spawnId=101, script='$52000038_QD__MAIN__2$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return start_04(self.ctx)


class start_04(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2004')
        self.set_conversation(type=1, spawnId=102, script='$52000038_QD__MAIN__3$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_05(self.ctx)


class start_05(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return start_05_b(self.ctx)


class start_05_b(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3001, visible=False, initialSequence='Dead_A')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2005')
        self.set_conversation(type=1, spawnId=101, script='$52000038_QD__MAIN__4$', arg4=2, arg5=0)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2006')
        self.set_conversation(type=1, spawnId=102, script='$52000038_QD__MAIN__5$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return start_06(self.ctx)


class start_06(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[202], animationEffect=True)
        self.create_monster(spawnIds=[203], animationEffect=True)
        self.create_monster(spawnIds=[204], animationEffect=True)
        self.create_monster(spawnIds=[205], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return start_07(self.ctx)


class start_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3002, visible=False, initialSequence='Dead_A')
        self.set_actor(triggerId=3003, visible=False, initialSequence='Dead_A')
        self.set_actor(triggerId=3004, visible=False, initialSequence='Dead_A')
        self.set_actor(triggerId=3005, visible=False, initialSequence='Dead_A')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2007')
        self.set_conversation(type=1, spawnId=101, script='$52000038_QD__MAIN__6$', arg4=2, arg5=2)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2008')
        self.set_conversation(type=1, spawnId=102, script='$52000038_QD__MAIN__7$', arg4=2, arg5=4)
        self.show_guide_summary(entityId=40010, textId=40010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201,202,203,204,205]):
            self.destroy_monster(spawnIds=[101,102])
            self.hide_guide_summary(entityId=40010)
            return scene_b_01(self.ctx)


class scene_b_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=701, type='trigger', achieve='beyondroid1')
        self.create_monster(spawnIds=[111,112], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002631], questStates=[1]):
            self.destroy_monster(spawnIds=[111,112])
            self.create_monster(spawnIds=[121,122], animationEffect=True)
            return scene_b_02(self.ctx)


class scene_b_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=121, patrolName='MS2PatrolData_2009')
        self.set_conversation(type=1, spawnId=121, script='$52000038_QD__MAIN__8$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return scene_b_03(self.ctx)


class scene_b_03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=122, patrolName='MS2PatrolData_2010')
        self.set_conversation(type=1, spawnId=122, script='$52000038_QD__MAIN__9$', arg4=2, arg5=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return scene_b_04(self.ctx)


class scene_b_04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[103], animationEffect=True)
        self.show_guide_summary(entityId=20020010, textId=20020010)
        self.set_conversation(type=1, spawnId=121, script='$52000038_QD__MAIN__10$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002631], questStates=[2]):
            self.destroy_monster(spawnIds=[121,122])
            self.create_monster(spawnIds=[131,132], animationEffect=True)
            self.hide_guide_summary(entityId=20020010)
            return scene_c_01(self.ctx)


class scene_c_01(trigger_api.Trigger):
    pass


initial_state = ready
