""" trigger/52000142_qd/52000142_main.xml """
import common


class 준비(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.create_monster(spawnIds=[106], animationEffect=False)
        self.set_effect(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016,5017,5018,5019,5020,5021,5022,5023,5024,5025], visible=False)
        self.set_effect(triggerIds=[5026,5027,5028,5029,5030,5031,5032,5033,5034,5035,5036,5037,5038,5039], visible=False)
        self.set_effect(triggerIds=[5040,5041,5042,5043], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002721], questStates=[3]):
            return 단계별이동_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002721], questStates=[2]):
            return 단계별이동_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002720], questStates=[3]):
            return 단계별이동_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002720], questStates=[2]):
            return 단계별이동_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002720], questStates=[1]):
            return 퀘스트1진행_01(self.ctx)
        if self.user_detected(boxIds=[701]):
            return 영상준비_01(self.ctx)


class 영상준비_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.add_buff(boxIds=[701], skillId=70000124, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 영상재생_01(self.ctx)


class 영상재생_01(common.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='common\JobIntro_Knight.usm', movieId=1)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 시작_01(self.ctx)
        if self.wait_tick(waitTick=53000):
            return 시작_01(self.ctx)


class 시작_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 시작_02(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=2)


class 시작_02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 구보훈련_01(self.ctx)


class 구보훈련_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 구보훈련_01_1(self.ctx)


class 구보훈련_01_1(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003,8005], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 구보훈련_02(self.ctx)


class 구보훈련_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_2001')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 구보훈련_03(self.ctx)


class 구보훈련_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8007], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52000142_QD__52000142_MAIN__0$', duration=3500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 구보훈련_04_1(self.ctx)


class 구보훈련_04_1(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 구보훈련_04(self.ctx)


class 구보훈련_04(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25201421, textId=25201421)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002720], questStates=[1]):
            return 퀘스트1진행_01(self.ctx)


class 단계별이동_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_buff(boxIds=[701], skillId=70000124, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 단계별이동_02(self.ctx)


class 단계별이동_02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000142, portalId=99)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[702], questIds=[40002721], questStates=[3]):
            return 퀘2완료(self.ctx)
        if self.quest_user_detected(boxIds=[702], questIds=[40002721], questStates=[2]):
            return 퀘2완료가능(self.ctx)
        if self.quest_user_detected(boxIds=[702], questIds=[40002720], questStates=[3]):
            return 퀘1완료(self.ctx)
        if self.quest_user_detected(boxIds=[702], questIds=[40002720], questStates=[2]):
            return 퀘1완료가능(self.ctx)


class 퀘2완료(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[102])
        self.destroy_monster(spawnIds=[103])
        self.destroy_monster(spawnIds=[104])
        self.destroy_monster(spawnIds=[106])
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.create_monster(spawnIds=[109], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=109, sequenceName='Emotion_lie_facedown_Idle_A', duration=600000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트2완료_01(self.ctx)


class 퀘2완료가능(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[102])
        self.destroy_monster(spawnIds=[103])
        self.destroy_monster(spawnIds=[104])
        self.destroy_monster(spawnIds=[106])
        self.destroy_monster(spawnIds=[107])
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.create_monster(spawnIds=[109], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=109, sequenceName='Emotion_lie_facedown_Idle_A', duration=600000)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 수호사제찾기_01(self.ctx)


class 퀘1완료(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[106])
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=107, sequenceName='Down_Idle_B', duration=600000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트1완료_02(self.ctx)


class 퀘1완료가능(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[106])
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트1완료가능_01(self.ctx)


class 퀘스트1진행_01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[106])
        self.hide_guide_summary(entityId=25201421)
        self.show_guide_summary(entityId=25201422, textId=25201422)
        self.set_effect(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016,5017,5018,5019,5020,5021,5022,5023,5024,5025], visible=True)
        self.add_buff(boxIds=[701], skillId=70000124, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[702], questIds=[40002720], questStates=[2]):
            return 퀘스트1완료가능_01(self.ctx)


class 퀘스트1완료가능_01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016,5017,5018,5019,5020,5021,5022,5023,5024,5025], visible=False)
        self.hide_guide_summary(entityId=25201422)
        self.show_guide_summary(entityId=25201423, textId=25201423)
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=107, sequenceName='Down_Idle_B', duration=600000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[702], questIds=[40002720], questStates=[3]):
            return 퀘스트1완료_01(self.ctx)


class 퀘스트1완료_01(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=25201423)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트1완료_02(self.ctx)


class 퀘스트1완료_02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000142, portalId=99)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[108], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트1완료_03(self.ctx)


class 퀘스트1완료_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 로베와대화1_01(self.ctx)


class 로베와대화1_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=벌칙_01, action='nextState')
        self.add_cinematic_talk(npcId=0, msg='$52000142_QD__52000142_MAIN__1$', duration=3500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 로베와대화1_02(self.ctx)


class 로베와대화1_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003401, msg='$52000142_QD__52000142_MAIN__2$', duration=3000, illustId='Robe_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 로베와대화1_03(self.ctx)


class 로베와대화1_03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000142_QD__52000142_MAIN__3$', duration=3500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 로베와대화1_04(self.ctx)


class 로베와대화1_04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003401, msg='$52000142_QD__52000142_MAIN__4$', duration=4000, illustId='Robe_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 로베와대화1_05(self.ctx)


class 로베와대화1_05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000142_QD__52000142_MAIN__5$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 로베와대화1_06(self.ctx)


class 로베와대화1_06(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003401, msg='$52000142_QD__52000142_MAIN__6$', duration=3500, illustId='Robe_normal', align='right')
        self.add_cinematic_talk(npcId=11003401, msg='$52000142_QD__52000142_MAIN__7$', duration=2500, illustId='Robe_normal', align='right')
        self.add_cinematic_talk(npcId=11003401, msg='$52000142_QD__52000142_MAIN__8$', duration=4000, illustId='Robe_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=11000):
            return 로베와대화1_07(self.ctx)


class 로베와대화1_07(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000142_QD__52000142_MAIN__9$', duration=3500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 로베와대화1_08(self.ctx)


class 로베와대화1_08(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003401, msg='$52000142_QD__52000142_MAIN__10$', duration=3500, illustId='Robe_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 동료의비웃음_01(self.ctx)


class 동료의비웃음_01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52000142_QD__52000142_MAIN__11$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 동료의비웃음_02(self.ctx)


class 동료의비웃음_02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=103, script='$52000142_QD__52000142_MAIN__12$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 동료의비웃음_03(self.ctx)


class 동료의비웃음_03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=104, script='$52000142_QD__52000142_MAIN__13$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 해명에도불구_01(self.ctx)


class 해명에도불구_01(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000142_QD__52000142_MAIN__14$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 해명에도불구_02(self.ctx)


class 해명에도불구_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003401, msg='$52000142_QD__52000142_MAIN__15$', duration=3000, illustId='Robe_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 해명에도불구_03(self.ctx)


class 해명에도불구_03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000142_QD__52000142_MAIN__16$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 벌칙_01(self.ctx)


class 벌칙_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_onetime_effect(id=999, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 벌칙_02(self.ctx)


class 벌칙_02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000142_QD__52000142_MAIN__17$')
        self.destroy_monster(spawnIds=[102])
        self.destroy_monster(spawnIds=[103])
        self.destroy_monster(spawnIds=[104])
        self.destroy_monster(spawnIds=[107])
        self.create_monster(spawnIds=[109], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=109, sequenceName='Emotion_lie_facedown_Idle_A', duration=600000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 벌칙_03(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=2)


class 벌칙_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=999, enable=False, path='BG/Common/ScreenMask/Eff_fadein_0sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 벌칙_04(self.ctx)


class 벌칙_04(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=수호사제찾기_01, action='nextState')
        self.add_cinematic_talk(npcId=0, msg='$52000142_QD__52000142_MAIN__18$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 벌칙_04_1(self.ctx)


class 벌칙_04_1(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 벌칙_05(self.ctx)


class 벌칙_05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000142_QD__52000142_MAIN__19$', duration=3500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 벌칙_06(self.ctx)


class 벌칙_06(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003399, msg='$52000142_QD__52000142_MAIN__20$', duration=3500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 벌칙_06_1(self.ctx)


class 벌칙_06_1(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 벌칙_07(self.ctx)


class 벌칙_07(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003401, msg='$52000142_QD__52000142_MAIN__21$', duration=3500, illustId='Robe_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 벌칙_08(self.ctx)


class 벌칙_08(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000142_QD__52000142_MAIN__22$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 벌칙_09(self.ctx)


class 벌칙_09(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003401, msg='$52000142_QD__52000142_MAIN__23$', duration=4000, illustId='Robe_normal', align='right')
        self.add_cinematic_talk(npcId=11003401, msg='$52000142_QD__52000142_MAIN__24$', duration=2500, illustId='Robe_normal', align='right')
        self.add_cinematic_talk(npcId=11003401, msg='$52000142_QD__52000142_MAIN__25$', duration=3000, illustId='Robe_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 벌칙_10(self.ctx)


class 벌칙_10(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000142_QD__52000142_MAIN__26$', duration=3500, align='right')
        self.add_cinematic_talk(npcId=0, msg='$52000142_QD__52000142_MAIN__27$', duration=3500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7500):
            return 수호사제찾기_01(self.ctx)


class 수호사제찾기_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entityId=25201424, textId=25201424)
        self.set_effect(triggerIds=[5026,5027,5028,5029,5030,5031,5032,5033,5034,5035,5036,5037,5038,5039], visible=True)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[703]):
            return 수호사제찾기_02(self.ctx)


class 수호사제찾기_02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5026,5027,5028,5029,5030,5031,5032,5033,5034,5035,5036,5037,5038,5039], visible=False)
        self.hide_guide_summary(entityId=25201424)
        self.show_guide_summary(entityId=25201425, textId=25201425)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[703], questIds=[40002721], questStates=[2]):
            return 퀘스트2완료가능_01(self.ctx)


class 퀘스트2완료가능_01(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=25201425)
        self.show_guide_summary(entityId=25201426, textId=25201426)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[703], questIds=[40002721], questStates=[3]):
            return 퀘스트2완료_01(self.ctx)


class 퀘스트2완료_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트2완료_02(self.ctx)


class 퀘스트2완료_02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[105])
        self.create_monster(spawnIds=[110], animationEffect=False)
        self.move_user(mapId=52000142, portalId=99)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트2완료_03(self.ctx)


class 퀘스트2완료_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 란스구하기_01(self.ctx)


class 란스구하기_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=란스구하기스킵_01, action='nextState')
        self.add_cinematic_talk(npcId=0, msg='$52000142_QD__52000142_MAIN__28$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 란스구하기_02(self.ctx)


class 란스구하기_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003403, msg='$52000142_QD__52000142_MAIN__29$', duration=3500, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 란스구하기_03(self.ctx)


class 란스구하기_03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003401, msg='$52000142_QD__52000142_MAIN__30$', duration=2500, illustId='Robe_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 란스구하기_04(self.ctx)


class 란스구하기_04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=8000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 란스구하기_05(self.ctx)


class 란스구하기_05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000142_QD__52000142_MAIN__31$', duration=3000, align='right')
        self.add_cinematic_talk(npcId=0, msg='$52000142_QD__52000142_MAIN__32$', duration=3500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7500):
            return 란스구하기_06(self.ctx)


class 란스구하기_06(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003399, msg='$52000142_QD__52000142_MAIN__33$', duration=1000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 란스구하기_06_1(self.ctx)


class 란스구하기_06_1(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2006')
        self.destroy_monster(spawnIds=[109])
        self.create_monster(spawnIds=[111], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=111, sequenceName='Down_Idle_B', duration=600000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 란스구하기_07(self.ctx)


class 란스구하기_07(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 란스구하기_08(self.ctx)


class 란스구하기_08(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.move_user_path(patrolName='MS2PatrolData_2002')
        self.set_conversation(type=1, spawnId=0, script='$52000142_QD__52000142_MAIN__34$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 란스구하기_09(self.ctx)


class 란스구하기_09(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=108, script='$52000142_QD__52000142_MAIN__35$', arg4=3, arg5=0)
        # <action name="AddCinematicTalk" npcID="11003401" msg="$52000142_QD__52000142_MAIN__35$" duration="2500" illustID="Robe_normal" align="right" />

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 란스구하기_10(self.ctx)


class 란스구하기_10(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000142_QD__52000142_MAIN__36$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 란스구하기_10_1(self.ctx)


class 란스구하기_10_1(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8006], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 란스구하기_11(self.ctx)


class 란스구하기_11(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=110, sequenceName='Bore_B')
        self.add_cinematic_talk(npcId=11003403, msg='$52000142_QD__52000142_MAIN__37$', duration=5720, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5720):
            return 란스구하기_11_1(self.ctx)


class 란스구하기_11_1(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 란스구하기_12(self.ctx)


class 란스구하기_12(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003401, msg='$52000142_QD__52000142_MAIN__38$', duration=3000, illustId='Robe_normal', align='right')
        self.add_cinematic_talk(npcId=11003401, msg='$52000142_QD__52000142_MAIN__39$', duration=2500, illustId='Robe_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 란스구하기_13(self.ctx)


class 란스구하기_13(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2004')
        self.add_cinematic_talk(npcId=0, msg='$52000142_QD__52000142_MAIN__40$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 란스구하기_14(self.ctx)


class 란스구하기_14(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003401, msg='$52000142_QD__52000142_MAIN__41$', duration=5903, illustId='Robe_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8698):
            return 란스구하기_15(self.ctx)


class 란스구하기_15(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_2005')
        self.add_cinematic_talk(npcId=11003403, msg='$52000142_QD__52000142_MAIN__42$', duration=5955, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5955):
            return 란스구하기_16(self.ctx)


class 란스구하기_16(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003401, msg='$52000142_QD__52000142_MAIN__43$', duration=3500, illustId='Robe_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 란스구하기_17(self.ctx)


class 란스구하기_17(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003403, msg='$52000142_QD__52000142_MAIN__44$', duration=3500, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 란스구하기_18(self.ctx)


class 란스구하기_18(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000142_QD__52000142_MAIN__45$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 란스구하기_19(self.ctx)


class 란스구하기_19(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003401, msg='$52000142_QD__52000142_MAIN__46$', duration=3000, illustId='Robe_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 란스구하기_20(self.ctx)


class 란스구하기_20(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003403, msg='$52000142_QD__52000142_MAIN__47$', duration=3000, align='left')
        self.add_cinematic_talk(npcId=11003403, msg='$52000142_QD__52000142_MAIN__48$', duration=2500, align='left')
        self.add_cinematic_talk(npcId=11003403, msg='$52000142_QD__52000142_MAIN__49$', duration=3500, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 란스구하기_21(self.ctx)


class 란스구하기_21(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003401, msg='$52000142_QD__52000142_MAIN__50$', duration=3000, illustId='Robe_normal', align='right')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 퇴장_01(self.ctx)


class 란스구하기스킵_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawnIds=[109])
        self.create_monster(spawnIds=[111], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=111, sequenceName='Down_Idle_B', duration=600000)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 란스구하기스킵_02(self.ctx)


class 란스구하기스킵_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퇴장_01(self.ctx)


class 퇴장_01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=108, patrolName='MS2PatrolData_2003')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 퇴장_02(self.ctx)


class 퇴장_02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[108])
        self.show_guide_summary(entityId=25201427, textId=25201427)
        self.set_effect(triggerIds=[5040,5041,5042,5043], visible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[704]):
            return 강제이동(self.ctx)


class 강제이동(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=25201427)
        self.remove_buff(boxId=704, skillId=70000124)
        self.set_effect(triggerIds=[5040,5041,5042,5043], visible=False)
        self.move_user(mapId=52000143, portalId=1)


initial_state = 준비
