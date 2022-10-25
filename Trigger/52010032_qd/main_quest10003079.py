""" trigger/52010032_qd/main_quest10003079.xml """
import common


# 나메드가 페리온이야기하고 에바고르는 삐져서 나감
class 무르파고스에들어오면(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003079], questStates=[1]):
            self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[202])
        self.destroy_monster(spawnIds=[301])
        self.destroy_monster(spawnIds=[302])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return Ready01(self.ctx)


class Ready01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.face_emotion(spawnId=401, emotionName='Trigger_angry')
        self.create_monster(spawnIds=[401], animationEffect=True) # 나메드
        self.create_monster(spawnIds=[301], animationEffect=True) # 시끄러운 주먹
        self.create_monster(spawnIds=[302], animationEffect=True) # 에바고르
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_3003')
        self.move_npc(spawnId=302, patrolName='MS2PatrolData_3004')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 대화시작(self.ctx)


class 대화시작(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Talk_A')
        self.move_user(mapId=52010032, portalId=6002)
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__0$', duration=3000)
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__1$', duration=4000)
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__2$', duration=4000)
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__3$', duration=2000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=13000):
            return 대화시작01(self.ctx)


class 대화시작01(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__4$', duration=4000)
        self.add_cinematic_talk(npcId=0, msg='$52010032_QD__MAIN_QUEST10003079__5$', duration=3500)
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__6$', duration=3500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=11000):
            return 대화시작02(self.ctx)


class 대화시작02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4008], returnView=False)
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Focus_A'])
        self.add_cinematic_talk(npcId=0, msg='$52010032_QD__MAIN_QUEST10003079__7$', duration=3500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 대화시작03(self.ctx)


class 대화시작03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Bore_A')
        self.face_emotion(spawnId=203, emotionName='Trigger_Sad')
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__8$', duration=2000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 에바고르삐짐(self.ctx)


class 에바고르삐짐(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4005], returnView=False)
        self.add_cinematic_talk(npcId=11003391, msg='$52010032_QD__MAIN_QUEST10003079__9$', duration=4000)
        self.add_cinematic_talk(npcId=11003391, msg='$52010032_QD__MAIN_QUEST10003079__10$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 에바고르삐짐01(self.ctx)


class 에바고르삐짐01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Bore_B')
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__11$', duration=3000)
        self.add_cinematic_talk(npcId=11003391, msg='$52010032_QD__MAIN_QUEST10003079__12$', duration=2000)
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__13$', duration=5000)
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__14$', duration=3500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=14000):
            return 에바고르삐짐02(self.ctx)


class 에바고르삐짐02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4005], returnView=False)
        self.set_npc_emotion_sequence(spawnId=302, sequenceName='Attack_01_A')
        self.add_cinematic_talk(npcId=11003391, msg='$52010032_QD__MAIN_QUEST10003079__15$', duration=4000)
        self.add_cinematic_talk(npcId=11003391, msg='$52010032_QD__MAIN_QUEST10003079__16$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 에바고르퇴장(self.ctx)


class 에바고르퇴장(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4006], returnView=False)
        self.add_cinematic_talk(npcId=11003388, msg='$52010032_QD__MAIN_QUEST10003079__17$', duration=3000)
        self.move_npc(spawnId=302, patrolName='MS2PatrolData_3006')
        self.set_achievement(triggerId=2001, type='trigger', achieve='Namid')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 에바고르퇴장후(self.ctx)


class 에바고르퇴장후(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Bore_B')
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__18$', duration=3500)
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__19$', duration=3500)
        self.add_cinematic_talk(npcId=11003388, msg='$52010032_QD__MAIN_QUEST10003079__20$', duration=2000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return 에바고르퇴장후_1(self.ctx)


class 에바고르퇴장후_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 나메드에게퀘스트마무리(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawnIds=[302])
        self.destroy_monster(spawnIds=[401])
        self.reset_camera(interpolationTime=0.5)
        self.set_achievement(triggerId=2001, type='trigger', achieve='Namid')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 나메드에게퀘스트마무리(self.ctx)


class 나메드에게퀘스트마무리(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.destroy_monster(spawnIds=[302])
        self.destroy_monster(spawnIds=[401])
        self.create_monster(spawnIds=[202], animationEffect=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return None # Missing State: 


initial_state = 무르파고스에들어오면
