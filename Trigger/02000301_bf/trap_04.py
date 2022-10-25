""" trigger/02000301_bf/trap_04.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=209, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[610], visible=False)
        self.create_monster(spawnIds=[1003], animationEffect=False)
        self.create_monster(spawnIds=[1102], animationEffect=False)
        self.set_mesh(triggerIds=[3041,3042,3043,3044,3045,3046], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[4401,4402,4403,4404,4405,4406,4407,4408,4409,4410,4411,4412,4413,4414], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3047,3048], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[104]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10401]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10402]):
            return 경보(self.ctx)
        if self.monster_dead(boxIds=[1102]):
            return 경보(self.ctx)
        if self.monster_dead(boxIds=[1003]):
            return 해제(self.ctx)


class 경보(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=209, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_effect(triggerIds=[601], visible=True)
        self.set_effect(triggerIds=[610], visible=True)
        self.create_monster(spawnIds=[1004], animationEffect=False)
        self.move_npc(spawnId=1004, patrolName='MS2PatrolData_1004')
        self.create_monster(spawnIds=[2005], animationEffect=False)
        self.show_guide_summary(entityId=20003002, textId=20003002)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_conversation(type=1, spawnId=1003, script='$02000301_BF__TRAP_04__1$', arg4=2)
        self.set_mesh(triggerIds=[4401,4402,4403,4404,4405,4406,4407,4408,4409,4410,4411,4412,4413,4414], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3047,3048], visible=False, arg3=0, delay=0, scale=5)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2005]):
            self.hide_guide_summary(entityId=20003002)
            self.set_effect(triggerIds=[610], visible=False)
            self.set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=209, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 해제(self.ctx)


class 해제(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2005]):
            self.set_mesh(triggerIds=[3041,3042,3043,3044,3045,3046], visible=False, arg3=0, delay=0, scale=5)
            self.set_mesh(triggerIds=[4401,4402,4403,4404,4405,4406,4407,4408,4409,4410,4411,4412,4413,4414], visible=False, arg3=0, delay=0, scale=5)
            return 해제(self.ctx)


initial_state = 시작
