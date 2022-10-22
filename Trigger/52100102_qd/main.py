""" trigger/52100102_qd/main.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1000]):
            return 퀘스트체크()


class 퀘스트체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[1000], questIds=[50100890], questStates=[3]):
            return NPC소환()
        if quest_user_detected(boxIds=[1000], questIds=[50100890], questStates=[2]):
            return 연출끝()
        if quest_user_detected(boxIds=[1000], questIds=[50100890], questStates=[1]):
            return 연출끝()


class NPC소환(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=False) # 유저 투명 처리
        set_effect(triggerIds=[600], visible=False)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[604], visible=False)
        create_monster(spawnIds=[100], arg2=False)
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)
        create_monster(spawnIds=[103], arg2=False)
        create_monster(spawnIds=[104], arg2=False)
        create_monster(spawnIds=[105], arg2=False)
        create_monster(spawnIds=[200], arg2=False)
        create_monster(spawnIds=[201], arg2=False)
        create_monster(spawnIds=[202], arg2=False)
        create_monster(spawnIds=[203], arg2=False)
        create_monster(spawnIds=[204], arg2=False)
        create_monster(spawnIds=[205], arg2=False)
        create_monster(spawnIds=[206], arg2=False)
        set_cinematic_ui(type=1)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1000]):
            return narration01()


class narration01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=9, script='$52100102_QD__MAIN__0$')
        set_scene_skip(state=연출끝, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return narration02()


class narration02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[1,2], returnView=False)
        show_caption(type='VerticalCaption', title='$52100102_QD__MAIN__1$', desc='$52100102_QD__MAIN__2$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 암전1()


class 암전1(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 카메라무브1()


class 카메라무브1(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3,4], returnView=False)
        move_npc(spawnId=202, patrolName='PatrolData_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 위협1()


class 위협1(state.State):
    def on_enter(self):
        select_camera(triggerId=8, enable=True)
        add_cinematic_talk(npcId=11004429, msg='$52100102_QD__MAIN__3$', duration=3000, align='left')
        add_cinematic_talk(npcId=11004429, msg='$52100102_QD__MAIN__4$', duration=4000, align='left')
        set_npc_emotion_loop(spawnId=202, sequenceName='Bore_A', duration=1333)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 위협2()


class 위협2(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=301, sequenceName='Bore_B', duration=3667)
        add_cinematic_talk(npcId=11004426, msg='$52100102_QD__MAIN__5$', duration=4000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카등장()


class 투르카등장(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6,7,9], returnView=False)
        set_effect(triggerIds=[600], visible=True)
        create_monster(spawnIds=[300], arg2=False)
        add_cinematic_talk(npcId=11004430, msg='$52100102_QD__MAIN__6$', duration=3000, align='left')
        move_npc(spawnId=300, patrolName='PatrolData_Turka_1')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카대사소개()


class 투르카대사소개(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        show_caption(type='VerticalCaption', title='$52100102_QD__MAIN__7$', desc='$52100102_QD__MAIN__8$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카대사1()


class 투르카대사1(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=300, sequenceName='Bore_A', duration=5400)
        add_cinematic_talk(npcId=11004430, msg='$52100102_QD__MAIN__9$', duration=5000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 검은군단물러서기_1()


class 검은군단물러서기_1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=False)
        select_camera(triggerId=10, enable=True)
        set_npc_rotation(spawnId=202, rotation=180)
        add_cinematic_talk(npcId=11004429, msg='$52100102_QD__MAIN__10$', duration=2000, align='left')
        set_npc_rotation(spawnId=200, rotation=225)
        set_npc_rotation(spawnId=201, rotation=180)
        set_npc_rotation(spawnId=205, rotation=225)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 검은군단돌아보기_1()


class 검은군단돌아보기_1(state.State):
    def on_enter(self):
        set_npc_rotation(spawnId=203, rotation=180)
        set_npc_rotation(spawnId=204, rotation=135)
        set_npc_rotation(spawnId=206, rotation=135)
        add_cinematic_talk(npcId=11004430, msg='$52100102_QD__MAIN__11$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 검은군단물러서기_2()


class 검은군단물러서기_2(state.State):
    def on_enter(self):
        move_npc(spawnId=300, patrolName='PatrolData_Turka_2')
        move_npc(spawnId=201, patrolName='PatrolData_back_201')
        move_npc(spawnId=202, patrolName='PatrolData_back_202')
        move_npc(spawnId=205, patrolName='PatrolData_back_205')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 검은군단물러서기_3()


class 검은군단물러서기_3(state.State):
    def on_enter(self):
        move_npc(spawnId=200, patrolName='PatrolData_back_200')
        move_npc(spawnId=204, patrolName='PatrolData_Back_204')
        move_npc(spawnId=206, patrolName='PatrolData_back_206')
        move_npc(spawnId=203, patrolName='PatrolData_back_203')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 검은군단소멸시키기()


class 검은군단소멸시키기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[200])
        destroy_monster(spawnIds=[201])
        destroy_monster(spawnIds=[202])
        destroy_monster(spawnIds=[203])
        destroy_monster(spawnIds=[204])
        destroy_monster(spawnIds=[205])
        destroy_monster(spawnIds=[206])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 카메라전환_1()


class 카메라전환_1(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[300])
        create_monster(spawnIds=[301], arg2=False)
        select_camera(triggerId=11, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 투르카이동_1()


class 투르카이동_1(state.State):
    def on_enter(self):
        move_npc(spawnId=301, patrolName='PatrolData_Turka_2')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 게오르크장교대사()


class 게오르크장교대사(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004426, msg='$52100102_QD__MAIN__12$', duration=5000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 투르카공격1To1()


class 투르카공격1To1(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004430, msg='$52100102_QD__MAIN__13$', duration=3000, align='left')
        set_npc_emotion_loop(spawnId=301, sequenceName='Bore_B', duration=3667)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카공격1To2()


class 투르카공격1To2(state.State):
    def on_enter(self):
        move_npc(spawnId=301, patrolName='PatrolData_Turka_Attack')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 투르카공격1To3()


class 투르카공격1To3(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=301, sequenceName='Attack_01_B', duration=600)
        set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=600):
            return 투르카공격1To4()


class 투르카공격1To4(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[11,12], returnView=False)
        set_npc_emotion_loop(spawnId=301, sequenceName='Attack_02_B', duration=1400)
        set_effect(triggerIds=[602], visible=True)
        set_effect(triggerIds=[603], visible=True)
        set_npc_emotion_loop(spawnId=101, sequenceName='Dead_A', duration=1333)
        set_npc_emotion_loop(spawnId=103, sequenceName='Dead_A', duration=1333)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 투르카공격카메라()


class 투르카공격카메라(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[103])
        add_cinematic_talk(npcId=11004425, msg='$52100102_QD__MAIN__14$', duration=1000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 투르카질문_1()


class 투르카질문_1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[107])
        create_monster(spawnIds=[108])
        select_camera(triggerId=13, enable=True)
        add_cinematic_talk(npcId=11004426, msg='$52100102_QD__MAIN__15$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 투르카질문_2To1()


class 투르카질문_2To1(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=301, sequenceName='Bore_B', duration=3667)
        add_cinematic_talk(npcId=11004430, msg='$52100102_QD__MAIN__16$', duration=5000, align='left')
        add_cinematic_talk(npcId=11004426, msg='$52100102_QD__MAIN__17$', duration=3000, align='left')
        add_cinematic_talk(npcId=11004430, msg='$52100102_QD__MAIN__18$', duration=5000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 투르카공격2To1()


class 투르카공격2To1(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=301, sequenceName='Attack_01_B', duration=600)
        set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=600):
            return 투르카공격2To2()


class 투르카공격2To2(state.State):
    def on_enter(self):
        set_onetime_effect(id=100, enable=True, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')
        select_camera(triggerId=14, enable=True)
        set_time_scale(enable=True, startScale=0.3, endScale=1, duration=30, interpolator=1)
        set_npc_emotion_loop(spawnId=301, sequenceName='Attack_02_B', duration=1400)
        set_npc_emotion_loop(spawnId=102, sequenceName='Dead_A', duration=1333)
        add_cinematic_talk(npcId=11004426, msg='$52100102_QD__MAIN__19$', duration=1500, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 상황정리()


class 상황정리(state.State):
    def on_enter(self):
        set_time_scale(enable=False, startScale=0.3, endScale=1, duration=50, interpolator=1)
        destroy_monster(spawnIds=[102])
        destroy_monster(spawnIds=[103])
        destroy_monster(spawnIds=[107])
        destroy_monster(spawnIds=[108])
        create_monster(spawnIds=[109])
        create_monster(spawnIds=[110])
        create_monster(spawnIds=[111])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 엔딩카메라1()


class 엔딩카메라1(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[301])
        create_monster(spawnIds=[302])
        set_onetime_effect(id=100, enable=False, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')
        select_camera_path(pathIds=[15,16], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 투르카엔딩대사_1()


class 투르카엔딩대사_1(state.State):
    def on_enter(self):
        select_camera(triggerId=17, enable=True)
        move_npc(spawnId=302, patrolName='PatrolData_Turka_End_Move')
        set_effect(triggerIds=[604], visible=True)
        add_cinematic_talk(npcId=11004430, msg='$52100102_QD__MAIN__20$', duration=5000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 엔딩암전()


class 엔딩암전(state.State):
    def on_enter(self):
        set_onetime_effect(id=101, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출끝()


class 연출끝(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1], arg2=False)
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        visible_my_pc(isVisible=True)
        set_onetime_effect(id=101, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user(mapId=2020029, portalId=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None # Missing State: 


