""" trigger/52100102_qd/main.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1000]):
            return 퀘스트체크(self.ctx)


class 퀘스트체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[1000], questIds=[50100890], questStates=[3]):
            return NPC소환(self.ctx)
        if self.quest_user_detected(boxIds=[1000], questIds=[50100890], questStates=[2]):
            return 연출끝(self.ctx)
        if self.quest_user_detected(boxIds=[1000], questIds=[50100890], questStates=[1]):
            return 연출끝(self.ctx)


class NPC소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(isVisible=False) # 유저 투명 처리
        self.set_effect(triggerIds=[600], visible=False)
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_effect(triggerIds=[604], visible=False)
        self.create_monster(spawnIds=[100], animationEffect=False)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.create_monster(spawnIds=[200], animationEffect=False)
        self.create_monster(spawnIds=[201], animationEffect=False)
        self.create_monster(spawnIds=[202], animationEffect=False)
        self.create_monster(spawnIds=[203], animationEffect=False)
        self.create_monster(spawnIds=[204], animationEffect=False)
        self.create_monster(spawnIds=[205], animationEffect=False)
        self.create_monster(spawnIds=[206], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1000]):
            return narration01(self.ctx)


class narration01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=9, script='$52100102_QD__MAIN__0$')
        self.set_scene_skip(state=연출끝, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return narration02(self.ctx)


class narration02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[1,2], returnView=False)
        self.show_caption(type='VerticalCaption', title='$52100102_QD__MAIN__1$', desc='$52100102_QD__MAIN__2$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 암전1(self.ctx)


class 암전1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 카메라무브1(self.ctx)


class 카메라무브1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[3,4], returnView=False)
        self.move_npc(spawnId=202, patrolName='PatrolData_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 위협1(self.ctx)


class 위협1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=8, enable=True)
        self.add_cinematic_talk(npcId=11004429, msg='$52100102_QD__MAIN__3$', duration=3000, align='left')
        self.add_cinematic_talk(npcId=11004429, msg='$52100102_QD__MAIN__4$', duration=4000, align='left')
        self.set_npc_emotion_loop(spawnId=202, sequenceName='Bore_A', duration=1333)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 위협2(self.ctx)


class 위협2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=301, sequenceName='Bore_B', duration=3667)
        self.add_cinematic_talk(npcId=11004426, msg='$52100102_QD__MAIN__5$', duration=4000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카등장(self.ctx)


class 투르카등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[6,7,9], returnView=False)
        self.set_effect(triggerIds=[600], visible=True)
        self.create_monster(spawnIds=[300], animationEffect=False)
        self.add_cinematic_talk(npcId=11004430, msg='$52100102_QD__MAIN__6$', duration=3000, align='left')
        self.move_npc(spawnId=300, patrolName='PatrolData_Turka_1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카대사소개(self.ctx)


class 투르카대사소개(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.show_caption(type='VerticalCaption', title='$52100102_QD__MAIN__7$', desc='$52100102_QD__MAIN__8$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카대사1(self.ctx)


class 투르카대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=300, sequenceName='Bore_A', duration=5400)
        self.add_cinematic_talk(npcId=11004430, msg='$52100102_QD__MAIN__9$', duration=5000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 검은군단물러서기_1(self.ctx)


class 검은군단물러서기_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[600], visible=False)
        self.select_camera(triggerId=10, enable=True)
        self.set_npc_rotation(spawnId=202, rotation=180)
        self.add_cinematic_talk(npcId=11004429, msg='$52100102_QD__MAIN__10$', duration=2000, align='left')
        self.set_npc_rotation(spawnId=200, rotation=225)
        self.set_npc_rotation(spawnId=201, rotation=180)
        self.set_npc_rotation(spawnId=205, rotation=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 검은군단돌아보기_1(self.ctx)


class 검은군단돌아보기_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_rotation(spawnId=203, rotation=180)
        self.set_npc_rotation(spawnId=204, rotation=135)
        self.set_npc_rotation(spawnId=206, rotation=135)
        self.add_cinematic_talk(npcId=11004430, msg='$52100102_QD__MAIN__11$', duration=3000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 검은군단물러서기_2(self.ctx)


class 검은군단물러서기_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=300, patrolName='PatrolData_Turka_2')
        self.move_npc(spawnId=201, patrolName='PatrolData_back_201')
        self.move_npc(spawnId=202, patrolName='PatrolData_back_202')
        self.move_npc(spawnId=205, patrolName='PatrolData_back_205')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 검은군단물러서기_3(self.ctx)


class 검은군단물러서기_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=200, patrolName='PatrolData_back_200')
        self.move_npc(spawnId=204, patrolName='PatrolData_Back_204')
        self.move_npc(spawnId=206, patrolName='PatrolData_back_206')
        self.move_npc(spawnId=203, patrolName='PatrolData_back_203')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 검은군단소멸시키기(self.ctx)


class 검은군단소멸시키기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[200])
        self.destroy_monster(spawnIds=[201])
        self.destroy_monster(spawnIds=[202])
        self.destroy_monster(spawnIds=[203])
        self.destroy_monster(spawnIds=[204])
        self.destroy_monster(spawnIds=[205])
        self.destroy_monster(spawnIds=[206])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 카메라전환_1(self.ctx)


class 카메라전환_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[300])
        self.create_monster(spawnIds=[301], animationEffect=False)
        self.select_camera(triggerId=11, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 투르카이동_1(self.ctx)


class 투르카이동_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=301, patrolName='PatrolData_Turka_2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 게오르크장교대사(self.ctx)


class 게오르크장교대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004426, msg='$52100102_QD__MAIN__12$', duration=5000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 투르카공격1To1(self.ctx)


class 투르카공격1To1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004430, msg='$52100102_QD__MAIN__13$', duration=3000, align='left')
        self.set_npc_emotion_loop(spawnId=301, sequenceName='Bore_B', duration=3667)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카공격1To2(self.ctx)


class 투르카공격1To2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=301, patrolName='PatrolData_Turka_Attack')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 투르카공격1To3(self.ctx)


class 투르카공격1To3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=301, sequenceName='Attack_01_B', duration=600)
        self.set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=600):
            return 투르카공격1To4(self.ctx)


class 투르카공격1To4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[11,12], returnView=False)
        self.set_npc_emotion_loop(spawnId=301, sequenceName='Attack_02_B', duration=1400)
        self.set_effect(triggerIds=[602], visible=True)
        self.set_effect(triggerIds=[603], visible=True)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Dead_A', duration=1333)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Dead_A', duration=1333)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 투르카공격카메라(self.ctx)


class 투르카공격카메라(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[103])
        self.add_cinematic_talk(npcId=11004425, msg='$52100102_QD__MAIN__14$', duration=1000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 투르카질문_1(self.ctx)


class 투르카질문_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[107])
        self.create_monster(spawnIds=[108])
        self.select_camera(triggerId=13, enable=True)
        self.add_cinematic_talk(npcId=11004426, msg='$52100102_QD__MAIN__15$', duration=3000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 투르카질문_2To1(self.ctx)


class 투르카질문_2To1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=301, sequenceName='Bore_B', duration=3667)
        self.add_cinematic_talk(npcId=11004430, msg='$52100102_QD__MAIN__16$', duration=5000, align='left')
        self.add_cinematic_talk(npcId=11004426, msg='$52100102_QD__MAIN__17$', duration=3000, align='left')
        self.add_cinematic_talk(npcId=11004430, msg='$52100102_QD__MAIN__18$', duration=5000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 투르카공격2To1(self.ctx)


class 투르카공격2To1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=301, sequenceName='Attack_01_B', duration=600)
        self.set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=600):
            return 투르카공격2To2(self.ctx)


class 투르카공격2To2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=100, enable=True, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')
        self.select_camera(triggerId=14, enable=True)
        self.set_time_scale(enable=True, startScale=0.3, endScale=1, duration=30, interpolator=1)
        self.set_npc_emotion_loop(spawnId=301, sequenceName='Attack_02_B', duration=1400)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Dead_A', duration=1333)
        self.add_cinematic_talk(npcId=11004426, msg='$52100102_QD__MAIN__19$', duration=1500, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 상황정리(self.ctx)


class 상황정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale(enable=False, startScale=0.3, endScale=1, duration=50, interpolator=1)
        self.destroy_monster(spawnIds=[102])
        self.destroy_monster(spawnIds=[103])
        self.destroy_monster(spawnIds=[107])
        self.destroy_monster(spawnIds=[108])
        self.create_monster(spawnIds=[109])
        self.create_monster(spawnIds=[110])
        self.create_monster(spawnIds=[111])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 엔딩카메라1(self.ctx)


class 엔딩카메라1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[301])
        self.create_monster(spawnIds=[302])
        self.set_onetime_effect(id=100, enable=False, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')
        self.select_camera_path(pathIds=[15,16], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 투르카엔딩대사_1(self.ctx)


class 투르카엔딩대사_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=17, enable=True)
        self.move_npc(spawnId=302, patrolName='PatrolData_Turka_End_Move')
        self.set_effect(triggerIds=[604], visible=True)
        self.add_cinematic_talk(npcId=11004430, msg='$52100102_QD__MAIN__20$', duration=5000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 엔딩암전(self.ctx)


class 엔딩암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출끝(self.ctx)


class 연출끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[-1], arg2=False)
        # Missing State: State
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.visible_my_pc(isVisible=True)
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=2020029, portalId=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return None # Missing State: State


initial_state = Ready
