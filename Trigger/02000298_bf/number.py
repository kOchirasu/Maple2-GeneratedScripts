""" trigger/02000298_bf/number.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[608], visible=False)
        self.set_effect(triggerIds=[610], visible=False)
        self.set_effect(triggerIds=[611], visible=False)
        self.set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_mesh(triggerIds=[3224,3225,3226], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[198]):
            return 암호체크(self.ctx)


class 암호체크(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20002982, textId=20002982)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=197, spawnIds=[1279]):
            return 입력대기중_1279(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[1238]):
            return 입력대기중_1238(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[1358]):
            return 입력대기중_1358(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[1489]):
            return 입력대기중_1489(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[1567]):
            return 입력대기중_1567(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[1679]):
            return 입력대기중_1679(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[2389]):
            return 입력대기중_2389(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[2347]):
            return 입력대기중_2347(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[2478]):
            return 입력대기중_2478(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[2456]):
            return 입력대기중_2456(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[2569]):
            return 입력대기중_2569(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[2678]):
            return 입력대기중_2678(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[3458]):
            return 입력대기중_3458(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[3589]):
            return 입력대기중_3589(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[3679]):
            return 입력대기중_3679(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[3789]):
            return 입력대기중_3789(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[4567]):
            return 입력대기중_4567(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[4578]):
            return 입력대기중_4578(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[4689]):
            return 입력대기중_4689(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[4789]):
            return 입력대기중_4789(self.ctx)


class 입력대기중_1279(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000001,12000002,12000007,12000009], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000003], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000004], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000005], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000006], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000008], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_1238(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000001,12000002,12000003,12000008], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000004], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000005], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000006], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000007], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000009], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_1358(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000001,12000003,12000005,12000008], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000002], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000004], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000006], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000007], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000009], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_1489(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000001,12000004,12000008,12000009], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000002], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000003], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000005], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000006], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000007], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_1567(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000001,12000005,12000006,12000007], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000002], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000003], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000004], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000008], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000009], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_1679(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000001,12000006,12000007,12000009], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000002], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000003], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000004], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000005], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000008], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_2389(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000002,12000003,12000008,12000009], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000001], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000004], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000005], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000006], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000007], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_2347(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000002,12000003,12000004,12000007], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000001], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000005], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000006], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000008], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000009], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_2478(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000002,12000004,12000007,12000008], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000001], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000003], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000005], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000006], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000009], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_2456(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000002,12000004,12000005,12000006], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000001], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000003], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000007], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000008], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000009], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_2569(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000002,12000005,12000006,12000009], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000001], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000003], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000004], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000007], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000008], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_2678(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000002,12000006,12000007,12000008], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000001], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000003], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000004], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000005], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000009], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_3458(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000003,12000004,12000005,12000008], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000001], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000002], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000006], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000007], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000009], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_3589(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000003,12000005,12000008,12000009], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000001], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000002], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000004], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000006], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000007], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_3679(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000003,12000006,12000007,12000009], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000001], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000002], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000004], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000005], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000008], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_3789(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000003,12000007,12000008,12000009], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000001], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000002], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000004], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000005], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000006], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_4567(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000004,12000005,12000006,12000007], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000001], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000002], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000003], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000008], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000009], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_4578(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000004,12000005,12000007,12000008], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000001], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000002], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000003], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000006], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000009], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_4689(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000004,12000006,12000008,12000009], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000001], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000002], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000003], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000005], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000007], stateValue=0):
            return 오답(self.ctx)


class 입력대기중_4789(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000004,12000007,12000008,12000009], stateValue=0):
            return 정답(self.ctx)
        if self.object_interacted(interactIds=[12000001], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000002], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000003], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000005], stateValue=0):
            return 오답(self.ctx)
        if self.object_interacted(interactIds=[12000006], stateValue=0):
            return 오답(self.ctx)


class 정답(trigger_api.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20002982)
        self.set_timer(timerId='3', seconds=3)
        self.show_guide_summary(entityId=20002983, textId=20002983)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.hide_guide_summary(entityId=20002983)
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_effect(triggerIds=[608], visible=True)
        self.set_mesh(triggerIds=[3221,3222,3223], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3224,3225,3226], visible=True, arg3=1000, delay=1000, scale=5)
        self.show_guide_summary(entityId=20002984, textId=20002984)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            self.hide_guide_summary(entityId=20002984)
            return 종료(self.ctx)


class 오답(trigger_api.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20002982)
        self.set_effect(triggerIds=[610], visible=True)
        self.set_timer(timerId='3', seconds=3)
        self.show_guide_summary(entityId=20002985, textId=20002985)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.hide_guide_summary(entityId=20002985)
            return 방어모드(self.ctx)


class 방어모드(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_effect(triggerIds=[611], visible=True)
        self.show_guide_summary(entityId=20002986, textId=20002986)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.create_monster(spawnIds=[1098,1099], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1098,1099]):
            self.hide_guide_summary(entityId=20002986)
            self.set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_effect(triggerIds=[611], visible=False)
            return 암호체크(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
