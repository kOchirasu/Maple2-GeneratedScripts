""" trigger/52020029_qd/main30000330.xml """
from common import *
import state


#  진리의 문 입장 
class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[30000330], questStates=[2]):
            return 암전()


class 암전(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출시작1()


class 연출시작1(state.State):
    def on_enter(self):
        move_user(mapId=52020029, portalId=6002)
        destroy_monster(spawnIds=[105])
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[103], arg2=False)
        destroy_monster(spawnIds=[104])
        create_monster(spawnIds=[104], arg2=False)
        set_npc_emotion_loop(spawnId=104, sequenceName='Quest_Programming', duration=15000000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출시작2()


class 연출시작2(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4005], returnView=False)
        set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=9000)
        face_emotion(spawnId=0, emotionName='defaultBattle')
        add_cinematic_talk(npcId=11003755, msg='어떤가요? 사용할 수 있겠어요?', duration=3000)
        add_cinematic_talk(npcId=11003717, msg='절 너무 물로보면 곤란합니다.', duration=3000)
        add_cinematic_talk(npcId=11003755, msg='그럼 순서대로 검색해볼까요?', duration=3000)
        set_scene_skip(state=이동, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 정보검색첫번째()


class 정보검색첫번째(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11003755, msg='티어스 코어에 대해서 검색해 주세요.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 정보검색첫번째2()


class 정보검색첫번째2(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[4006], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003717, msg='데이터 서칭 완료입니다.', duration=3000)
        add_cinematic_talk(npcId=11003717, msg='고대 문자라 읽기 어려운데... 내용은 이렇습니다.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 정보검색첫번째2_1()


class 정보검색첫번째2_1(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4013,4010], returnView=False)
        add_cinematic_talk(npcId=11003717, msg='티어스 코어는 티마이온의 에너지 원으로, 강력한 마력의 힘이 담겨 있다.', duration=3000)
        add_cinematic_talk(npcId=11003717, msg='티어스 코어는 몇 가지의 재료로 조합할 수 있으며, 이 재료는 크리티아스의 사방에 흩어져 있다.', duration=3000)
        add_cinematic_talk(npcId=11003717, msg='주 재료가 되는 파멸의 날개는 크리티아스 왕가에 내려져 오는 가보로, 하나는 헤카톤 국왕이, 하나는 왕비가 가지고 있다.', duration=3000)
        add_cinematic_talk(npcId=11003717, msg='왕비가 가지고 있던 파멸의 날개는 딸 이오네에게 넘겨졌다.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return 정보검색첫번째3()


class 정보검색첫번째3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003717, msg='파멸의 날개 이외의 재료는 천공의 심장, 신의 눈, 영혼의 구슬, 지혜의 고리이다. ', duration=3000)
        add_cinematic_talk(npcId=11003717, msg='천공의 심장은 마력의 숲의 천공의 탑에 보관되어 있으며, 실제적인 티어스 코어의 베이스가 되는 물질이다.', duration=3000)
        add_cinematic_talk(npcId=11003717, msg='신의 눈은 티아만 시간의...', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 정보검색첫번째3_1()


class 정보검색첫번째3_1(state.State):
    def on_enter(self):
        face_emotion(spawnId=104, emotionName='dance_S')
        select_camera_path(pathIds=[4011], returnView=False)
        add_cinematic_talk(npcId=11003717, msg='엇!?', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 정보검색첫번째4()


class 정보검색첫번째4(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        set_npc_emotion_sequence(spawnId=104, sequenceName='Emotion_Troubled_A')
        add_cinematic_talk(npcId=11003717, msg='으음...', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 정보검색첫번째4_2()


class 정보검색첫번째4_2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        move_npc(spawnId=103, patrolName='MS2PatrolData_3005')
        add_cinematic_talk(npcId=11003755, msg='무슨일이지요?', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 정보검색첫번째4_3()


class 정보검색첫번째4_3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        add_cinematic_talk(npcId=11003717, msg='갑자기... 티어스 코어에 대한 정보를 볼수가 없게 되었습니다.', duration=3000)
        add_cinematic_talk(npcId=11003717, msg='누군가가... 데이터 접근을 막고 있습니다.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 정보검색첫번째4_4()


class 정보검색첫번째4_4(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=3000)
        add_cinematic_talk(npcId=11003755, msg='흐음. 누가 접근을 막고 있는건지는 알 수 있을까나?', duration=3000)
        add_cinematic_talk(npcId=11003717, msg='노력은 해보겠지만, 시간이 필요합니다.', duration=3000)
        add_cinematic_talk(npcId=11003717, msg='그 외의 정보라면 먼저 검색해 볼 수 있을 것 같습니다.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 정보검색첫번째5()


class 정보검색첫번째5(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        set_pc_emotion_loop(sequenceName='Talk_A', duration=20000)
        add_cinematic_talk(npcId=0, msg='그렇다면, 제가 먼저 천공의 심장을 찾으러 가겠어요.', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 정보검색첫번째5_1()


class 정보검색첫번째5_1(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=9000)
        add_cinematic_talk(npcId=11003755, msg='...아무래도 그게 좋겠군요.', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 정보검색첫번째5_2()


class 정보검색첫번째5_2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        add_cinematic_talk(npcId=0, msg='당신은 같이 안 가나요?', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 정보검색첫번째5_3()


class 정보검색첫번째5_3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=3000)
        add_cinematic_talk(npcId=11003755, msg='예. 저는 더 찾고 싶은 정보가 있습니다.\n나중에 뵙죠.', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 정보검색첫번째6()


class 정보검색첫번째6(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        add_cinematic_talk(npcId=0, msg='알겠어요. 더 알게 되는 것이 있으면 알려주세요.', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 정보검색첫번째7_1()


class 정보검색첫번째7_1(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_3004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 정보검색첫번째7()


class 정보검색첫번째7(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4007], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 정보검색첫번째8()


class 정보검색첫번째8(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=False)
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[4004], returnView=False)
        set_npc_emotion_sequence(spawnId=104, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003755, msg='방해꾼이 사라졌군요.', duration=3000)
        add_cinematic_talk(npcId=11003717, msg='헤헤. 그럼 이제 뭘 찾으면 될까요?', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 정보검색첫번째8_1()


class 정보검색첫번째8_1(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=104, sequenceName='Emotion_Troubled_A')
        add_cinematic_talk(npcId=11003717, msg='희귀한 보석? 헤카톤 왕의 비밀?', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 정보검색첫번째9()


class 정보검색첫번째9(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        set_npc_emotion_sequence(spawnId=103, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003755, msg='훗. 찾고 있는 것은 따로 있지.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 정보검색첫번째9_1()


class 정보검색첫번째9_1(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=103, sequenceName='Bore_B')
        face_emotion(spawnId=103, emotionName='Idle_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 정보검색첫번째10()


class 정보검색첫번째10(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4012], returnView=False)
        face_emotion(spawnId=103, emotionName='Trigger_Bore_03')
        add_cinematic_talk(npcId=11003755, msg='비밀 병기 프로젝트 아포칼립스...!', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 이동()


class 이동(state.State):
    def on_enter(self):
        set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 이동_1()


class 이동_1(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[103])
        destroy_monster(spawnIds=[104])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 이동_2()


class 이동_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        visible_my_pc(isVisible=True)
        move_user(mapId=2020016, portalId=3)


