""" trigger/52000145_qd/52000145_main.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.create_monster(spawnIds=[101], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002711], questStates=[3]):
            return 퀘스트2완료_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002711], questStates=[2]):
            return 퀘스트2진행_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002711], questStates=[1]):
            return 퀘스트2시작_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002710], questStates=[3]):
            return 퀘스트1완료가능_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002710], questStates=[2]):
            return 퀘스트1진행_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002710], questStates=[1]):
            return 퀘스트1수락_02(self.ctx)
        if self.user_detected(boxIds=[701]):
            return 영상준비_01(self.ctx)


class 영상준비_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 영상재생_01(self.ctx)


class 영상재생_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='common\JobIntro_Ranger.usm', movieId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 독백_01(self.ctx)
        if self.wait_tick(waitTick=45000):
            return 독백_01(self.ctx)


class 독백_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000145_QD__52000145_MAIN__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 시작_01(self.ctx)


class 시작_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        # <action name="연출UI를설정한다" arg1="0"/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 시작_02(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=2)


class 시작_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52000145, portalId=99)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 하스터숙면_01(self.ctx)


class 하스터숙면_01(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000145_QD__52000145_MAIN__1$', duration=3000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 하스터숙면_02(self.ctx)


class 하스터숙면_02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000145_QD__52000145_MAIN__2$', duration=3000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 하스터숙면_03(self.ctx)


class 하스터숙면_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 하스터숙면_04(self.ctx)


class 하스터숙면_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=퀘스트1수락_01, action='nextState')
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52000145_QD__52000145_MAIN__3$', duration=3000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 하스터숙면_05(self.ctx)


class 하스터숙면_05(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__4$', duration=3000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 하스터숙면_06(self.ctx)


class 하스터숙면_06(trigger_api.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=0, emotionName='Think_A')
        self.add_cinematic_talk(npcId=0, msg='$52000145_QD__52000145_MAIN__5$', duration=3000, align='right')
        # <action name="AddCinematicTalk" npcID="0" msg="$52000145_QD__52000145_MAIN__6$" duration="3000" align="right" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 퀘스트1수락_01(self.ctx)


class 퀘스트1수락_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 퀘스트1수락_02(self.ctx)


class 퀘스트1수락_02(trigger_api.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entityId=25201456, textId=25201456)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701,702], questIds=[40002710], questStates=[1]):
            return 퀘스트1진행_00(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=25201456)


class 퀘스트1진행_00(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트1진행_01(self.ctx)


class 퀘스트1진행_01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25201451, textId=25201451)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701,702], questIds=[40002710], questStates=[2]):
            return 퀘스트1완료가능_00(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=25201451)


class 퀘스트1완료가능_00(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트1완료가능_01(self.ctx)


class 퀘스트1완료가능_01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25201452, textId=25201452)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701,702], questIds=[40002710], questStates=[3]):
            return 퀘스트1완료_01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=25201452)


class 퀘스트1완료_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트2시작_01(self.ctx)


class 퀘스트2시작_01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25201453, textId=25201453)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701,702], questIds=[40002711], questStates=[1]):
            return 퀘스트2진행_00(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=25201453)


class 퀘스트2진행_00(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트2진행_01(self.ctx)


class 퀘스트2진행_01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25201454, textId=25201454)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701,703], questIds=[40002711], questStates=[2]):
            return 퀘스트2완료가능_00(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=25201454)


class 퀘스트2완료가능_00(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트2완료가능_01(self.ctx)


class 퀘스트2완료가능_01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25201455, textId=25201455)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701,702], questIds=[40002711], questStates=[3]):
            return 퀘스트2완료_01(self.ctx)


class 퀘스트2완료_01(trigger_api.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=25201455)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트2완료_02(self.ctx)


class 퀘스트2완료_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.move_user(mapId=52000145, portalId=99)
        self.create_monster(spawnIds=[103], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 오스칼등장_01(self.ctx)


class 오스칼등장_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Troubled_A'])
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 오스칼등장_02(self.ctx)


class 오스칼등장_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Suprise_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 오스칼등장_03(self.ctx)


class 오스칼등장_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=마무리, action='exit')
        self.face_emotion(spawnId=0, emotionName='Think_A')
        self.add_cinematic_talk(npcId=0, msg='$52000145_QD__52000145_MAIN__7$', duration=3000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 오스칼등장_04(self.ctx)


class 오스칼등장_04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__8$', duration=3000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 오스칼등장_05(self.ctx)


class 오스칼등장_05(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000145_QD__52000145_MAIN__9$', duration=3000, align='right')
        self.add_cinematic_talk(npcId=0, msg='$52000145_QD__52000145_MAIN__10$', duration=2500, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 오스칼등장_06(self.ctx)


class 오스칼등장_06(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__11$', duration=4000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5485):
            return 오스칼등장_07(self.ctx)


class 오스칼등장_07(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 오스칼등장_08(self.ctx)


class 오스칼등장_08(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__12$', duration=3000, align='left')
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Sit_Down_A', duration=70000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 오스칼등장_08_1(self.ctx)


class 오스칼등장_08_1(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__13$', duration=2500, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 오스칼등장_09(self.ctx)


class 오스칼등장_09(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 오스칼등장_10(self.ctx)


class 오스칼등장_10(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__14$', duration=4000, illustId='Hastur_normal', align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 오스칼등장_11(self.ctx)


class 오스칼등장_11(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__15$', duration=3000, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 오스칼등장_12(self.ctx)


class 오스칼등장_12(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__16$', duration=3500, illustId='Hastur_normal', align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 오스칼등장_13(self.ctx)


class 오스칼등장_13(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__17$', duration=2500, illustId='Oskhal_normal', align='left')
        self.add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__18$', duration=3500, illustId='Oskhal_normal', align='left')
        self.add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__19$', duration=3000, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9500):
            return 오스칼등장_14(self.ctx)


class 오스칼등장_14(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__20$', duration=3000, illustId='Hastur_normal', align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 오스칼등장_15(self.ctx)


class 오스칼등장_15(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__21$', duration=3500, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5172):
            return 오스칼등장_16(self.ctx)


class 오스칼등장_16(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__22$', duration=3000, illustId='Hastur_normal', align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 오스칼등장_17(self.ctx)


class 오스칼등장_17(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__23$', duration=2500, illustId='Oskhal_normal', align='left')
        self.add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__24$', duration=3500, illustId='Oskhal_normal', align='left')
        self.add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__25$', duration=2500, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9742):
            return 오스칼등장_18(self.ctx)


class 오스칼등장_18(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__26$', duration=3000, illustId='Hastur_normal', align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 오스칼등장_19(self.ctx)


class 오스칼등장_19(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__27$', duration=3000, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3631):
            return 오스칼등장_20(self.ctx)


class 오스칼등장_20(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__28$', duration=3500, illustId='Hastur_normal', align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 오스칼등장_21(self.ctx)


class 오스칼등장_21(trigger_api.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=0)
        self.add_cinematic_talk(npcId=0, msg='$52000145_QD__52000145_MAIN__29$', duration=2500, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 마무리(self.ctx)


class 마무리(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000146, portalId=1)


initial_state = 준비
