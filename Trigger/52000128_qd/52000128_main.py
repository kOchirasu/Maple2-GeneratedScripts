""" trigger/52000128_qd/52000128_main.xml """
import common


class 준비(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0) # 유저 이동 하게
        self.set_cinematic_ui(type=2) # UI 복구
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.set_skill(triggerIds=[7001], enable=False)
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_effect(triggerIds=[5005], visible=False)
        self.set_effect(triggerIds=[5006], visible=False)
        self.set_effect(triggerIds=[5007], visible=False)
        self.set_effect(triggerIds=[5008], visible=False)
        self.set_effect(triggerIds=[5009], visible=False)
        self.set_mesh(triggerIds=[4001], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return 영상준비_01(self.ctx)


class 영상준비_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 영상재생_01(self.ctx)


class 영상재생_01(common.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='common\JobIntro_Thief.usm', movieId=1)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 시작_01(self.ctx)
        if self.wait_tick(waitTick=33000):
            return 시작_01(self.ctx)


class 시작_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 금고폭파_01(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=2)


class 금고폭파_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1) # 유저 이동 못 하게
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 금고폭파_02(self.ctx)


class 금고폭파_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 금고폭파_03(self.ctx)


class 금고폭파_03(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7001], enable=True)
        self.set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 폭파확인_01(self.ctx)


class 폭파확인_01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 빅스소개_01(self.ctx)


class 빅스소개_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001,8002], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 빅스소개_02(self.ctx)


class 빅스소개_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003272, msg='$52000128_QD__52000128_MAIN__0$', duration=2000, align='left')
        self.set_scene_skip(state=제시소개_01, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 빅스소개_03(self.ctx)


class 빅스소개_03(common.Trigger):
    def on_enter(self):
        self.show_caption(type='VerticalCaption', title='$52000128_QD__52000128_MAIN__1$', desc='$52000128_QD__52000128_MAIN__2$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 제시소개_01(self.ctx)


class 제시소개_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.select_camera_path(pathIds=[8002,8003], returnView=False)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2003')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 제시소개_02(self.ctx)


class 제시소개_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003273, msg='$52000128_QD__52000128_MAIN__3$', duration=2000, align='left')
        self.set_scene_skip(state=카일소개_01, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 제시소개_03(self.ctx)


class 제시소개_03(common.Trigger):
    def on_enter(self):
        self.show_caption(type='VerticalCaption', title='$52000128_QD__52000128_MAIN__4$', desc='$52000128_QD__52000128_MAIN__5$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 카일소개_01(self.ctx)


class 카일소개_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.select_camera_path(pathIds=[8003,8004], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카일소개_02(self.ctx)


class 카일소개_02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_2004')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카일소개_03(self.ctx)


class 카일소개_03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003280, msg='$52000128_QD__52000128_MAIN__6$', duration=2351, align='left')
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Bore_B')
        self.set_scene_skip(state=퀘스트시작_01, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카일소개_04(self.ctx)


class 카일소개_04(common.Trigger):
    def on_enter(self):
        self.show_caption(type='VerticalCaption', title='$52000128_QD__52000128_MAIN__7$', desc='$52000128_QD__52000128_MAIN__8$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 퀘스트시작_01(self.ctx)


class 퀘스트시작_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=2)
        self.show_guide_summary(entityId=25201281, textId=25201281)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002690], questStates=[1]):
            return 퀘스트진행_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002690], questStates=[2]):
            return 퀘스트완료가능_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002690], questStates=[3]):
            return 암전_01(self.ctx)


class 퀘스트진행_01(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=25201281)
        self.show_guide_summary(entityId=25201282, textId=25201282)
        self.set_effect(triggerIds=[5003,5004,5005,5006,5007,5008,5009], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[702]):
            return 퀘스트진행_02(self.ctx)


class 퀘스트진행_02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5003,5004,5005,5006,5007,5008,5009], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002690], questStates=[2]):
            return 퀘스트완료가능_01(self.ctx)


class 퀘스트완료가능_01(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=25201281)
        self.hide_guide_summary(entityId=25201282)
        self.show_guide_summary(entityId=25201283, textId=25201283)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002690], questStates=[3]):
            return 암전_01(self.ctx)


class 암전_01(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=25201281)
        self.hide_guide_summary(entityId=25201282)
        self.hide_guide_summary(entityId=25201283)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 암전_02(self.ctx)


class 암전_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8005], returnView=False)
        self.destroy_monster(spawnIds=[103])
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.move_user_path(patrolName='MS2PatrolData_2005')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2006')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2007')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 밝은화면_01(self.ctx)


class 밝은화면_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 잡담_01(self.ctx)


class 잡담_01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000128_QD__52000128_MAIN__9$', arg4=2, arg5=0)
        self.set_scene_skip(state=교도관등장_06, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 잡담_02(self.ctx)


class 잡담_02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[107,109,111,113,115], animationEffect=False)
        self.set_conversation(type=1, spawnId=104, script='$52000128_QD__52000128_MAIN__10$', arg4=2, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 교도관등장_01(self.ctx)


class 교도관등장_01(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2010')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2008')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2009')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 교도관등장_02(self.ctx)


class 교도관등장_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8006], returnView=False)
        self.set_conversation(type=1, spawnId=111, script='$52000128_QD__52000128_MAIN__21$', arg4=2, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 교도관등장_03(self.ctx)


class 교도관등장_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8005], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 교도관등장_04(self.ctx)


class 교도관등장_04(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2012')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 교도관등장_05(self.ctx)


class 교도관등장_05(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000128_QD__52000128_MAIN__11$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3300):
            return 교도관등장_06(self.ctx)


class 교도관등장_06(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.move_user_path(patrolName='MS2PatrolData_2013')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 교도관등장_07(self.ctx)


class 교도관등장_07(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2014')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2014')
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_2014')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 교도관등장_08(self.ctx)


class 교도관등장_08(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 교도관전투_01(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[101,102,104])


class 교도관전투_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entityId=25201284, textId=25201284)
        self.destroy_monster(spawnIds=[107,109,111,113,115])
        self.create_monster(spawnIds=[108,110,112,114,116], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[108,110,112,114,116]):
            return 교도관전투끝_01(self.ctx)


class 교도관전투끝_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.hide_guide_summary(entityId=25201284)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 교도관전투끝_02(self.ctx)


class 교도관전투끝_02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000128, portalId=99)
        self.create_monster(spawnIds=[117,118,119,120,121])
        self.create_monster(spawnIds=[105], animationEffect=True)
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_2011')
        self.select_camera_path(pathIds=[8009], returnView=False)
        self.set_npc_emotion_loop(spawnId=117, sequenceName='Dead_Idle_A', duration=3600000)
        self.set_npc_emotion_loop(spawnId=118, sequenceName='Dead_Idle_B', duration=3600000)
        self.set_npc_emotion_loop(spawnId=119, sequenceName='Dead_Idle_B', duration=3600000)
        self.set_npc_emotion_loop(spawnId=120, sequenceName='Dead_Idle_B', duration=3600000)
        self.set_npc_emotion_loop(spawnId=121, sequenceName='Dead_Idle_A', duration=3600000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 교도관전투끝_03(self.ctx)


class 교도관전투끝_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투끝_04(self.ctx)


class 전투끝_04(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=벨마등장_06, action='nextState')
        self.add_cinematic_talk(npcId=0, msg='$52000128_QD__52000128_MAIN__12$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3300):
            return 전투끝_05(self.ctx)


class 전투끝_05(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Suprise_A'])
        self.add_cinematic_talk(npcId=0, msg='$52000128_QD__52000128_MAIN__13$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3300):
            return 벨마등장_01(self.ctx)


class 벨마등장_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8006], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 벨마등장_02(self.ctx)


class 벨마등장_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003274, msg='$52000128_QD__52000128_MAIN__14$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3300):
            return 벨마등장_03(self.ctx)


class 벨마등장_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8007], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52000128_QD__52000128_MAIN__15$', duration=4000, align='right')
        self.set_pc_emotion_sequence(sequenceNames=['Talk_A'])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 벨마등장_04(self.ctx)


class 벨마등장_04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8008], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 벨마등장_05(self.ctx)


class 벨마등장_05(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=105, sequenceName='Attack_01_B')
        self.add_cinematic_talk(npcId=11003274, msg='$52000128_QD__52000128_MAIN__16$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 벨마등장_06(self.ctx)


class 벨마등장_06(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 벨마전투_01(self.ctx)


class 벨마전투_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entityId=25201285, textId=25201285)
        self.destroy_monster(spawnIds=[105])
        self.create_monster(spawnIds=[106], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='battleStop', value=1):
            return 벨마전투끝_01(self.ctx)


class 벨마전투끝_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.hide_guide_summary(entityId=25201285)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 벨마전투끝_02(self.ctx)


class 벨마전투끝_02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000128, portalId=99)
        self.destroy_monster(spawnIds=[106])
        self.create_monster(spawnIds=[105], animationEffect=True)
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_2011')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 벨마전투끝_03(self.ctx)


class 벨마전투끝_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전투후대화_01(self.ctx)


class 전투후대화_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=마무리, action='exit')
        self.select_camera_path(pathIds=[8010], returnView=False)
        self.face_emotion(spawnId=0)
        self.set_pc_emotion_sequence(sequenceNames=['Talk_A'])
        self.add_cinematic_talk(npcId=0, msg='$52000128_QD__52000128_MAIN__17$', duration=3000, align='right')
        self.add_cinematic_talk(npcId=0, msg='$52000128_QD__52000128_MAIN__18$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6500):
            return 전투후대화_02(self.ctx)


class 전투후대화_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8006], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 불길_01(self.ctx)


class 불길_01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5002], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 탈출_01(self.ctx)


class 탈출_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8011], returnView=False)
        self.set_conversation(type=1, spawnId=0, script='$52000128_QD__52000128_MAIN__19$', arg4=2, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 탈출_02(self.ctx)


class 탈출_02(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2014')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 탈출_03(self.ctx)


class 탈출_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8008], returnView=False)
        self.set_npc_emotion_sequence(spawnId=105, sequenceName='Attack_01_B')
        self.add_cinematic_talk(npcId=11003274, msg='$52000128_QD__52000128_MAIN__20$', duration=2000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마무리(self.ctx)


class 마무리(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 강제이동(self.ctx)


class 강제이동(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000129, portalId=1)


initial_state = 준비
