""" trigger/02000301_bf/trap_07.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=214, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=215, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[610], visible=False)
        self.create_monster(spawnIds=[1005], animationEffect=False)
        self.create_monster(spawnIds=[1103], animationEffect=False)
        self.set_mesh(triggerIds=[3071,3072,3073,3074,3075,3076], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[4701,4702,4703,4704,4705,4706,4707,4708,4709,4710,4711,4712,4713], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3077,3078], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[107]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10701]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10702]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10703]):
            return 경보(self.ctx)
        if self.monster_dead(boxIds=[1103]):
            return 경보(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return 해제(self.ctx)


class 경보(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=214, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=215, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_effect(triggerIds=[601], visible=True)
        self.set_effect(triggerIds=[610], visible=True)
        self.create_monster(spawnIds=[1006], animationEffect=False)
        self.move_npc(spawnId=1006, patrolName='MS2PatrolData_1006')
        self.create_monster(spawnIds=[2008], animationEffect=False)
        self.show_guide_summary(entityId=20003002, textId=20003002)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_conversation(type=1, spawnId=1005, script='$02000301_BF__TRAP_07__1$', arg4=2)
        self.set_mesh(triggerIds=[4701,4702,4703,4704,4705,4706,4707,4708,4709,4710,4711,4712,4713], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3077,3078], visible=False, arg3=0, delay=0, scale=5)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2008]):
            self.hide_guide_summary(entityId=20003002)
            self.set_effect(triggerIds=[610], visible=False)
            self.set_actor(triggerId=214, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=215, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 해제(self.ctx)


class 해제(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2008]):
            self.set_mesh(triggerIds=[3071,3072,3073,3074,3075,3076], visible=False, arg3=0, delay=0, scale=5)
            self.set_mesh(triggerIds=[4701,4702,4703,4704,4705,4706,4707,4708,4709,4710,4711,4712,4713], visible=False, arg3=0, delay=0, scale=5)
            return 해제(self.ctx)


initial_state = 시작
