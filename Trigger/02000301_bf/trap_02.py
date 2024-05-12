""" trigger/02000301_bf/trap_02.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=205, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[605], visible=False)
        self.set_effect(triggerIds=[610], visible=False)
        self.create_monster(spawnIds=[1001], animationEffect=False)
        self.create_monster(spawnIds=[1101], animationEffect=False)
        self.set_mesh(triggerIds=[3021,3022,3023,3024,3025,3026], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[4201,4202,4203,4204,4205,4206,4207,4208,4209,4210,4211,4212], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3027,3028], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[102]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10201]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10202]):
            return 경보(self.ctx)
        if self.monster_dead(boxIds=[1101]):
            return 경보(self.ctx)
        if self.monster_dead(boxIds=[1001]):
            return 해제(self.ctx)


class 경보(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=205, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_effect(triggerIds=[601], visible=True)
        self.set_effect(triggerIds=[605], visible=True)
        self.set_effect(triggerIds=[610], visible=True)
        self.create_monster(spawnIds=[1002], animationEffect=False)
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002')
        self.create_monster(spawnIds=[2003], animationEffect=False)
        self.show_guide_summary(entityId=20003002, textId=20003002)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_conversation(type=1, spawnId=1001, script='$02000301_BF__TRAP_02__1$', arg4=2)
        self.set_mesh(triggerIds=[4201,4202,4203,4204,4205,4206,4207,4208,4209,4210,4211,4212], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3027,3028], visible=False, arg3=0, delay=0, scale=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2003]):
            self.hide_guide_summary(entityId=20003002)
            self.set_effect(triggerIds=[610], visible=False)
            self.set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=205, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 해제(self.ctx)


class 해제(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2003]):
            self.set_mesh(triggerIds=[3021,3022,3023,3024,3025,3026], visible=False, arg3=0, delay=0, scale=5)
            self.set_mesh(triggerIds=[4201,4202,4203,4204,4205,4206,4207,4208,4209,4210,4211,4212], visible=False, arg3=0, delay=0, scale=5)
            return 해제(self.ctx)


initial_state = 시작
