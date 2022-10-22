""" trigger/02000298_bf/number.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[608], visible=False)
        set_effect(triggerIds=[610], visible=False)
        set_effect(triggerIds=[611], visible=False)
        set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_mesh(triggerIds=[3224,3225,3226], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[198]):
            return 암호체크()


class 암호체크(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20002982, textId=20002982)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=197, spawnIds=[1279]):
            return 입력대기중_1279()
        if npc_detected(boxId=197, spawnIds=[1238]):
            return 입력대기중_1238()
        if npc_detected(boxId=197, spawnIds=[1358]):
            return 입력대기중_1358()
        if npc_detected(boxId=197, spawnIds=[1489]):
            return 입력대기중_1489()
        if npc_detected(boxId=197, spawnIds=[1567]):
            return 입력대기중_1567()
        if npc_detected(boxId=197, spawnIds=[1679]):
            return 입력대기중_1679()
        if npc_detected(boxId=197, spawnIds=[2389]):
            return 입력대기중_2389()
        if npc_detected(boxId=197, spawnIds=[2347]):
            return 입력대기중_2347()
        if npc_detected(boxId=197, spawnIds=[2478]):
            return 입력대기중_2478()
        if npc_detected(boxId=197, spawnIds=[2456]):
            return 입력대기중_2456()
        if npc_detected(boxId=197, spawnIds=[2569]):
            return 입력대기중_2569()
        if npc_detected(boxId=197, spawnIds=[2678]):
            return 입력대기중_2678()
        if npc_detected(boxId=197, spawnIds=[3458]):
            return 입력대기중_3458()
        if npc_detected(boxId=197, spawnIds=[3589]):
            return 입력대기중_3589()
        if npc_detected(boxId=197, spawnIds=[3679]):
            return 입력대기중_3679()
        if npc_detected(boxId=197, spawnIds=[3789]):
            return 입력대기중_3789()
        if npc_detected(boxId=197, spawnIds=[4567]):
            return 입력대기중_4567()
        if npc_detected(boxId=197, spawnIds=[4578]):
            return 입력대기중_4578()
        if npc_detected(boxId=197, spawnIds=[4689]):
            return 입력대기중_4689()
        if npc_detected(boxId=197, spawnIds=[4789]):
            return 입력대기중_4789()


class 입력대기중_1279(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000001,12000002,12000007,12000009], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000003], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000004], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000005], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000006], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000008], arg2=0):
            return 오답()


class 입력대기중_1238(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000001,12000002,12000003,12000008], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000004], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000005], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000006], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000007], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000009], arg2=0):
            return 오답()


class 입력대기중_1358(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000001,12000003,12000005,12000008], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000002], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000004], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000006], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000007], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000009], arg2=0):
            return 오답()


class 입력대기중_1489(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000001,12000004,12000008,12000009], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000002], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000003], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000005], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000006], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000007], arg2=0):
            return 오답()


class 입력대기중_1567(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000001,12000005,12000006,12000007], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000002], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000003], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000004], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000008], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000009], arg2=0):
            return 오답()


class 입력대기중_1679(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000001,12000006,12000007,12000009], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000002], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000003], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000004], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000005], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000008], arg2=0):
            return 오답()


class 입력대기중_2389(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000002,12000003,12000008,12000009], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000001], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000004], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000005], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000006], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000007], arg2=0):
            return 오답()


class 입력대기중_2347(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000002,12000003,12000004,12000007], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000001], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000005], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000006], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000008], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000009], arg2=0):
            return 오답()


class 입력대기중_2478(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000002,12000004,12000007,12000008], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000001], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000003], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000005], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000006], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000009], arg2=0):
            return 오답()


class 입력대기중_2456(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000002,12000004,12000005,12000006], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000001], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000003], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000007], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000008], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000009], arg2=0):
            return 오답()


class 입력대기중_2569(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000002,12000005,12000006,12000009], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000001], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000003], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000004], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000007], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000008], arg2=0):
            return 오답()


class 입력대기중_2678(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000002,12000006,12000007,12000008], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000001], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000003], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000004], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000005], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000009], arg2=0):
            return 오답()


class 입력대기중_3458(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000003,12000004,12000005,12000008], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000001], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000002], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000006], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000007], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000009], arg2=0):
            return 오답()


class 입력대기중_3589(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000003,12000005,12000008,12000009], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000001], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000002], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000004], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000006], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000007], arg2=0):
            return 오답()


class 입력대기중_3679(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000003,12000006,12000007,12000009], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000001], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000002], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000004], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000005], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000008], arg2=0):
            return 오답()


class 입력대기중_3789(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000003,12000007,12000008,12000009], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000001], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000002], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000004], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000005], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000006], arg2=0):
            return 오답()


class 입력대기중_4567(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000004,12000005,12000006,12000007], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000001], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000002], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000003], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000008], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000009], arg2=0):
            return 오답()


class 입력대기중_4578(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000004,12000005,12000007,12000008], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000001], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000002], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000003], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000006], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000009], arg2=0):
            return 오답()


class 입력대기중_4689(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000004,12000006,12000008,12000009], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000001], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000002], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000003], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000005], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000007], arg2=0):
            return 오답()


class 입력대기중_4789(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000004,12000007,12000008,12000009], arg2=0):
            return 정답()
        if object_interacted(interactIds=[12000001], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000002], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000003], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000005], arg2=0):
            return 오답()
        if object_interacted(interactIds=[12000006], arg2=0):
            return 오답()


class 정답(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002982)
        set_timer(timerId='3', seconds=3)
        show_guide_summary(entityId=20002983, textId=20002983)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            hide_guide_summary(entityId=20002983)
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_effect(triggerIds=[608], visible=True)
        set_mesh(triggerIds=[3221,3222,3223], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3224,3225,3226], visible=True, arg3=1000, arg4=1000, arg5=5)
        show_guide_summary(entityId=20002984, textId=20002984)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            hide_guide_summary(entityId=20002984)
            return 종료()


class 오답(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002982)
        set_effect(triggerIds=[610], visible=True)
        set_timer(timerId='3', seconds=3)
        show_guide_summary(entityId=20002985, textId=20002985)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_interact_object(triggerIds=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            hide_guide_summary(entityId=20002985)
            return 방어모드()


class 방어모드(state.State):
    def on_enter(self):
        set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_On')
        set_effect(triggerIds=[611], visible=True)
        show_guide_summary(entityId=20002986, textId=20002986)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        create_monster(spawnIds=[1098,1099], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1098,1099]):
            hide_guide_summary(entityId=20002986)
            set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_effect(triggerIds=[611], visible=False)
            return 암호체크()


class 종료(state.State):
    pass


