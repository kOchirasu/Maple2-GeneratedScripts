""" trigger/02010087_bf/boss.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7301], visible=False)
        set_effect(triggerIds=[7302], visible=False)
        set_effect(triggerIds=[7303], visible=False)
        set_effect(triggerIds=[7304], visible=False)
        set_effect(triggerIds=[7305], visible=False)
        set_effect(triggerIds=[7306], visible=False)
        set_effect(triggerIds=[7307], visible=False)
        set_effect(triggerIds=[7308], visible=False)
        set_effect(triggerIds=[7309], visible=False)
        set_effect(triggerIds=[7310], visible=True)
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 폭발예고()

    def on_exit(self):
        add_buff(boxIds=[706], skillId=50000453, level=1) # 이속 버프를 걸어준다


class 폭발예고(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=8002, enable=True)
        set_mesh(triggerIds=[6001,6002,6003,6004], visible=False, arg4=0, arg5=10) # 벽 해제
        set_effect(triggerIds=[7308], visible=True) # 지진 이펙트
        set_timer(timerId='2', seconds=2, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 폭발()


class 폭발(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7306], visible=True) # 폭발 이펙트
        set_skill(triggerIds=[8306], isEnable=True) # 벽 날리는 스킬
        set_skill(triggerIds=[8307], isEnable=True) # 벽 날리는 스킬
        set_timer(timerId='2', seconds=2, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 폭발후()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


class 폭발후(state.State):
    def on_enter(self):
        select_camera(triggerId=8002, enable=False)
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=111, textId=20003371) # [b:기관실] 내부로 이동하세요.

    def on_tick(self) -> state.State:
        if count_users(boxId=705, boxId=1):
            return 폭발후_02()

    def on_exit(self):
        hide_guide_summary(entityId=111)


class 폭발후_02(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=112, textId=20003372) # 스위치를 작동시키세요
        set_interact_object(triggerIds=[10000891], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000891], arg2=0):
            return 클리어()

    def on_exit(self):
        hide_guide_summary(entityId=112)


class 클리어(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201])
        create_monster(spawnIds=[202])
        set_effect(triggerIds=[7301], visible=False)
        set_effect(triggerIds=[7302], visible=False)
        set_effect(triggerIds=[7303], visible=False)
        set_effect(triggerIds=[7304], visible=False)
        set_effect(triggerIds=[7305], visible=False)
        set_effect(triggerIds=[7306], visible=False)
        set_effect(triggerIds=[7307], visible=False)
        set_effect(triggerIds=[7308], visible=False)
        set_effect(triggerIds=[7309], visible=False)
        set_effect(triggerIds=[7310], visible=False)
        set_effect(triggerIds=[7311], visible=False)
        play_system_sound_in_box(sound='System_Dark_Ending_Chord_01')
        set_actor(triggerId=5001, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=5002, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=5003, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=5004, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=5005, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=5006, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=5007, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=5008, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_timer(timerId='3', seconds=3, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 웨이홍_대사01()

    def on_exit(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)


class 웨이홍_대사01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[199]) # 웨이홍
        select_camera(triggerId=8001, enable=True)
        set_conversation(type=2, spawnId=11003125, script='$02010087_BF__BOSS__0$', arg4=3) # 웨이홍 대사
        set_skip(state=웨이홍_대사02)
        set_timer(timerId='3', seconds=3, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 웨이홍_대사02()

    def on_exit(self):
        remove_cinematic_talk()


class 웨이홍_대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003125, script='$02010087_BF__BOSS__1$', arg4=3) # 웨이홍 대사
        set_skip(state=종료)
        set_timer(timerId='3', seconds=3, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 종료()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


class 웨이홍_대사03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003125, script='$02010087_BF__BOSS__2$', arg4=3) # 웨이홍 대사
        set_skip(state=종료)
        set_timer(timerId='4', seconds=4, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 종료()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


class 종료(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            dungeon_clear()
            return 종료_02()


class 종료_02(state.State):
    def on_enter(self):
        select_camera(triggerId=8001, enable=False)
        set_conversation(type=1, spawnId=199, script='$02000337_BF__BOSS__3$', arg4=3, arg5=2) # 웨이홍 말풍선 대사
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=True) # 보상으로 연결되는 포탈 제어 (켬)


