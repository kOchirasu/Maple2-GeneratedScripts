""" trigger/52020031_qd/main30000332.xml """
from common import *
import state


#  제단 입장 
# 
# 예상치 못한 인물 하렌(11003747) - spawnpoint : 1 
# 한순간의 방심 하렌(11003749) - spawnpoint : 2
# 연출용 하렌(11003756) - spawnpoint : 101 
# 
class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[30000332], questStates=[1]):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출시작_02()


class 연출시작_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52020031, portalId=6002)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 제단보여주기()


class 제단보여주기(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005,4001], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        show_caption(type='VerticalCaption', title='천공의 제단', desc='천공의 심장의 보관소', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=4000, scale=2)
        set_scene_skip(state=끝, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 다음스타트()


class 다음스타트(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        move_user_path(patrolName='MS2PatrolData_3001')
        add_cinematic_talk(npcId=0, msg='이곳이 천공의 심장이 보관되어 있다는 곳이구나.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3200):
            return 제단확인()


class 제단확인(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[4005,4009], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 제단관찰()


class 제단관찰(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=0, msg='누군가 이미 들어온 흔적이 있어 보였는데... 기분 탓인가...', duration=4000)
        add_cinematic_talk(npcId=0, msg='저 벽에 있는 장치에 천공의 심장이 보관 되어있는 거겠지?', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 제단관찰_02()


class 제단관찰_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4011], returnView=False)
        add_cinematic_talk(npcId=0, msg='...어라? 천공의 심장으로 보이는 물건이 없는 것 같은데... ', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 제단관찰_02_1()


class 제단관찰_02_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 제단관찰_03()


class 제단관찰_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        move_user_path(patrolName='MS2PatrolData_3004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 제단관찰_04()


class 제단관찰_04(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=0, msg='가까이 가봐도 되려나..?', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 부시럭()


class 부시럭(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 부시럭_02()


class 부시럭_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003756, msg='어머? 이게 누구야?', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 하렌발견01()


class 하렌발견01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4006,4007], returnView=False)
        add_cinematic_talk(npcId=11003756, msg='설마 했는데... 너였구나?', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 하렌발견01_2()


class 하렌발견01_2(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_3003')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 하렌발견01_3()


class 하렌발견01_3(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11003756, msg='많이 늦었네?', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 하렌발견02()


class 하렌발견02(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0.1)
        add_cinematic_talk(npcId=0, msg='아니, 너는?', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 하렌발견03()


class 하렌발견03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4010], returnView=False)
        show_caption(type='VerticalCaption', title='하렌', desc='흑성회의 제 3 간부', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=4000, scale=2)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003756, msg='...이렇게 만나다니 우연이네.', duration=3000)
        add_cinematic_talk(npcId=11003756, msg='혼자 이것저것 하기 힘들지? 후후.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 유저이동()


class 유저이동(state.State):
    def on_enter(self):
        move_user(mapId=52020031, portalId=6001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 하렌등장2()


class 하렌등장2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        face_emotion(spawnId=0, emotionName='Music_Cello_Play_03_A')
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=3000)
        add_cinematic_talk(npcId=0, msg='어떻게 여기에... 네가?', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 끝()


class 끝(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_achievement(triggerId=2001, type='trigger', achieve='MeetHaren')
        create_monster(spawnIds=[102], arg2=False) # 퀘스트 하렌
        destroy_monster(spawnIds=[101])
        reset_camera(interpolationTime=0.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 끝02()


class 끝02(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        destroy_monster(spawnIds=[101])
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


