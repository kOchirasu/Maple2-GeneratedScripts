""" trigger/02000301_bf/trap_05.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=210, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=211, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_interact_object(triggerIds=[10000513], state=1)
        self.set_effect(triggerIds=[606], visible=False)
        self.set_effect(triggerIds=[604], visible=False)
        self.set_effect(triggerIds=[610], visible=False)
        self.set_mesh(triggerIds=[3051,3052,3053,3054,3055,3056], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[4501,4502,4503,4504,4505,4506,4507,4508,4509,4510,4511,4512,4513,4514,4515,4516,4517,4518,4519], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[105]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10501]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10502]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10503]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10504]):
            return 경보(self.ctx)
        if self.user_detected(boxIds=[10505]):
            return 경보(self.ctx)
        if self.object_interacted(interactIds=[10000513], stateValue=0):
            return 해제(self.ctx)


class 경보(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=210, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=211, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_interact_object(triggerIds=[10000513], state=0)
        self.create_monster(spawnIds=[2006], animationEffect=False)
        self.set_effect(triggerIds=[606], visible=True)
        self.set_effect(triggerIds=[604], visible=True)
        self.set_effect(triggerIds=[610], visible=True)
        self.show_guide_summary(entityId=20003001, textId=20003001)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_mesh(triggerIds=[3051,3052,3053,3054,3055,3056], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[4501,4502,4503,4504,4505,4506,4507,4508,4509,4510,4511,4512,4513,4514,4515,4516,4517,4518,4519], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2006]):
            self.hide_guide_summary(entityId=20003001)
            self.set_effect(triggerIds=[610], visible=False)
            self.set_actor(triggerId=210, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=211, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 해제(self.ctx)


class 해제(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2006])
        self.set_mesh(triggerIds=[3051,3052,3053,3054,3055,3056], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[4501,4502,4503,4504,4505,4506,4507,4508,4509,4510,4511,4512,4513,4514,4515,4516,4517,4518,4519], visible=False, arg3=0, delay=0, scale=5)


initial_state = 시작
