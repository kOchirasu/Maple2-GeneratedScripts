""" trigger/02010087_bf/boss.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7301], visible=False)
        self.set_effect(triggerIds=[7302], visible=False)
        self.set_effect(triggerIds=[7303], visible=False)
        self.set_effect(triggerIds=[7304], visible=False)
        self.set_effect(triggerIds=[7305], visible=False)
        self.set_effect(triggerIds=[7306], visible=False)
        self.set_effect(triggerIds=[7307], visible=False)
        self.set_effect(triggerIds=[7308], visible=False)
        self.set_effect(triggerIds=[7309], visible=False)
        self.set_effect(triggerIds=[7310], visible=True)
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 폭발예고(self.ctx)

    def on_exit(self):
        self.add_buff(boxIds=[706], skillId=50000453, level=1) # 이속 버프를 걸어준다


class 폭발예고(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=8002, enable=True)
        self.set_mesh(triggerIds=[6001,6002,6003,6004], visible=False, delay=0, scale=10) # 벽 해제
        self.set_effect(triggerIds=[7308], visible=True) # 지진 이펙트
        self.set_timer(timerId='2', seconds=2, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 폭발(self.ctx)


class 폭발(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7306], visible=True) # 폭발 이펙트
        self.set_skill(triggerIds=[8306], enable=True) # 벽 날리는 스킬
        self.set_skill(triggerIds=[8307], enable=True) # 벽 날리는 스킬
        self.set_timer(timerId='2', seconds=2, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 폭발후(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 폭발후(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=8002, enable=False)
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=111, textId=20003371) # [b:기관실] 내부로 이동하세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=705, boxId=1):
            return 폭발후_02(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=111)


class 폭발후_02(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=112, textId=20003372) # 스위치를 작동시키세요
        self.set_interact_object(triggerIds=[10000891], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000891], stateValue=0):
            return 클리어(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=112)


class 클리어(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201])
        self.create_monster(spawnIds=[202])
        self.set_effect(triggerIds=[7301], visible=False)
        self.set_effect(triggerIds=[7302], visible=False)
        self.set_effect(triggerIds=[7303], visible=False)
        self.set_effect(triggerIds=[7304], visible=False)
        self.set_effect(triggerIds=[7305], visible=False)
        self.set_effect(triggerIds=[7306], visible=False)
        self.set_effect(triggerIds=[7307], visible=False)
        self.set_effect(triggerIds=[7308], visible=False)
        self.set_effect(triggerIds=[7309], visible=False)
        self.set_effect(triggerIds=[7310], visible=False)
        self.set_effect(triggerIds=[7311], visible=False)
        self.play_system_sound_in_box(sound='System_Dark_Ending_Chord_01')
        self.set_actor(triggerId=5001, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=5002, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=5003, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=5004, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=5005, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=5006, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=5007, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=5008, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_timer(timerId='3', seconds=3, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 웨이홍_대사01(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)


class 웨이홍_대사01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[199]) # 웨이홍
        self.select_camera(triggerId=8001, enable=True)
        self.set_conversation(type=2, spawnId=11003125, script='$02010087_BF__BOSS__0$', arg4=3) # 웨이홍 대사
        self.set_skip(state=웨이홍_대사02)
        self.set_timer(timerId='3', seconds=3, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 웨이홍_대사02(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class 웨이홍_대사02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003125, script='$02010087_BF__BOSS__1$', arg4=3) # 웨이홍 대사
        self.set_skip(state=종료)
        self.set_timer(timerId='3', seconds=3, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 종료(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 웨이홍_대사03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003125, script='$02010087_BF__BOSS__2$', arg4=3) # 웨이홍 대사
        self.set_skip(state=종료)
        self.set_timer(timerId='4', seconds=4, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 종료(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.dungeon_clear()
            return 종료_02(self.ctx)


class 종료_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=8001, enable=False)
        self.set_conversation(type=1, spawnId=199, script='$02000337_BF__BOSS__3$', arg4=3, arg5=2) # 웨이홍 말풍선 대사
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=True) # 보상으로 연결되는 포탈 제어 (켬)


initial_state = 시작
