""" trigger/52020035_qd/main30000317.xml """
from common import *
import state


#  퀘스트 수락 후 연출 시작 
class idle2(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[702], questIds=[30000317], questStates=[1]):
            return 연출시작2()
        if quest_user_detected(boxIds=[702], questIds=[30000317], questStates=[2]):
            return Skip_1()


#  라딘과 대화 시작 
class 연출시작2(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출시작3()


class 연출시작3(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52020035, portalId=6001)
        create_monster(spawnIds=[110], arg2=False, arg3=0) # 연출라딘
        select_camera_path(pathIds=[4007], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 라딘과대화시작()


class 라딘과대화시작(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=Skip_1, arg2='exit')
        add_cinematic_talk(npcId=11003753, msg='자네도 알겠지만 수호군이 크리티아스에 쉽게 오지는 못할걸세.', duration=3000)
        add_cinematic_talk(npcId=11003753, msg='지원군을 소집하는데도 시간이 걸리겠지만\n우리가 포털 수리 및 방어 시스템을 무력화시키지 않는다면\n결국 또 다른 많은 희생을 치루게 되겠지.', duration=4500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7500):
            return 라딘과대화시작_02()


class 라딘과대화시작_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4027], returnView=False)
        add_cinematic_talk(npcId=0, msg='그렇다면 저희가 나서서 수호군이 안전하게 올 수 있도록 조치를 취해야겠군요.', duration=3500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 라딘과대화시작_03()


class 라딘과대화시작_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4028], returnView=False)
        add_cinematic_talk(npcId=11003753, msg='그렇지. 게다가 자네가 얘기해준 티어스 코어라는 물건에 대해서도 빨리 정보를 찾아\n왜 어둠의 세력이 그것을 노리고 있는지도 알아내야 하고 말이야.', duration=4500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 라딘과대화시작_04()


class 라딘과대화시작_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4027], returnView=False)
        add_cinematic_talk(npcId=0, msg='해야할 일이 많네요… 이럴 때 수호군의 동료들이 있었다면…', duration=3500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 라딘과대화시작_05()


class 라딘과대화시작_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4028], returnView=False)
        add_cinematic_talk(npcId=11003753, msg='그래서 우리를 도와줄만한 사람들에게 연락을 취해두었네.\n곧 도착할 시간인데…', duration=4000)
        move_user(mapId=52020035, portalId=6002)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 흑성회다같이입장1()


#  들어오는 흑성회 
class 흑성회다같이입장1(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4007], returnView=False)
        set_npc_rotation(spawnId=110, rotation=-45)
        add_cinematic_talk(npcId=11003753, msg='아. 마침 저기 들어오는군.', duration=3000)
        add_cinematic_talk(npcId=0, msg='<font size=\'40\'>!!! 저 녀석들은?</font>', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 카메라이동()


class 카메라이동(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[111], arg2=False, arg3=0) # 연출웨이홍
        create_monster(spawnIds=[115], arg2=False, arg3=0) # 연출브리드민
        create_monster(spawnIds=[112], arg2=False, arg3=0) # 연출바사라첸
        create_monster(spawnIds=[113], arg2=False, arg3=0) # 연출하렌
        create_monster(spawnIds=[114], arg2=False, arg3=0) # 연출카일

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 간부얼굴준비()


#  각 간부들의 얼굴을 비추자 1 
class 간부얼굴준비(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4010,4011], returnView=False)
        move_npc(spawnId=111, patrolName='MS2PatrolData_3007')
        move_npc(spawnId=112, patrolName='MS2PatrolData_3006')
        move_npc(spawnId=113, patrolName='MS2PatrolData_3003')
        move_npc(spawnId=114, patrolName='MS2PatrolData_3004')
        move_npc(spawnId=115, patrolName='MS2PatrolData_3005')
        set_onetime_effect(id=9, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=0, msg='<font size=\'40\'>흑성회?!</font>', duration=6000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 하렌()


#  각 간부들의 얼굴을 비추자 2 
class 하렌(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4012], returnView=False)
        set_npc_emotion_sequence(spawnId=113, sequenceName='Bore_A')
        show_caption(type='VerticalCaption', title='하렌', desc='흑성회 제 3 간부', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카일()


class 카일(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4024], returnView=False)
        set_npc_emotion_sequence(spawnId=114, sequenceName='Bore_B')
        show_caption(type='VerticalCaption', title='카일', desc='흑성회 제 4 간부', align='centerRight', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 브리드민()


class 브리드민(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        set_npc_emotion_sequence(spawnId=115, sequenceName='Bore_B')
        show_caption(type='VerticalCaption', title='브리드 민', desc='흑성회 제 5 간부', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 바사라첸()


class 바사라첸(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4025], returnView=False)
        set_npc_emotion_sequence(spawnId=112, sequenceName='Bore_A')
        show_caption(type='VerticalCaption', title='바사라첸', desc='흑성회 제 2 간부', align='centerRight', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 웨이홍()


class 웨이홍(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4026], returnView=False)
        set_npc_emotion_sequence(spawnId=111, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003754, msg='여어~ $MyPCName$, 용케도 살아있었군.\n정말 그 끈질긴 생명력은 칭찬하지 않을 수 없군 그래.', duration=4000)
        show_caption(type='VerticalCaption', title='웨이홍', desc='흑성회 보스', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 흑성회와의동맹에대하여()


#  흑성회와 힘을 합치자고 말하는 라딘 
class 흑성회와의동맹에대하여(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4029], returnView=False)
        face_emotion(spawnId=0, emotionName='defaultBattle')
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=4000)
        add_cinematic_talk(npcId=0, msg='흑성회 놈들! 이번에야말로…!', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 흑성회와의동맹에대하여1_2()


class 흑성회와의동맹에대하여1_2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4028], returnView=False)
        add_cinematic_talk(npcId=11003753, msg='진정하게. 저들이 바로 내가 도움을 요청했다는 자들일세.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 흑성회와의동맹에대하여1_3()


class 흑성회와의동맹에대하여1_3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4029], returnView=False)
        set_pc_emotion_sequence(sequenceNames=['Emotion_Suprise_A'])
        add_cinematic_talk(npcId=0, msg='<font size=\'40\'>!!! 뭐라고요?</font>', duration=2000)
        add_cinematic_talk(npcId=0, msg='저들에게 도움을 요청하다니, 도대체 무슨 생각이신거죠!', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5500):
            return 흑성회와의동맹에대하여2()


#  그래 그럽시다 
class 흑성회와의동맹에대하여2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4026], returnView=False)
        add_cinematic_talk(npcId=11003754, msg='제법 똑똑한 녀석인줄 알았는데 이제보니 영 머리가 안굴러 가는 녀석이군.\n세상물정 모르는 꼬맹이같으니라고.', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 흑성회와의동맹에대하여3()


class 흑성회와의동맹에대하여3(state.State):
    def on_enter(self):
        select_camera(triggerId=4028, enable=True)
        add_cinematic_talk(npcId=11003753, msg='$MyPCName$, 자네의 마음은 이해하네.\n자네 말대로 흑성회는 신뢰할 수없는, 적이나 다름없는 이들이지.', duration=4000)
        add_cinematic_talk(npcId=11003753, msg='그러나 지금은 냉정하게 판단할 때일세.\n지금 우리는 자원도 부족하고 아무런 지원도 받을 수 없는 상황이네.', duration=4000)
        add_cinematic_talk(npcId=11003753, msg='누군가의 힘을 빌려 수호군이 안전하게 크리티아스에 도착하고\n어둠의 세력으로부터 이곳을 지켜낼 수만 있다면…', duration=4000)
        add_cinematic_talk(npcId=11003753, msg='설령 그것이 흑성회라 할지라도 지금은 손을 잡아야 하지 않겠나?', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16000):
            return 흑성회와의동맹에대하여4()


class 흑성회와의동맹에대하여4(state.State):
    def on_enter(self):
        select_camera(triggerId=4029, enable=True)
        add_cinematic_talk(npcId=0, msg='……네, 알겠습니다.', duration=2000)
        add_cinematic_talk(npcId=0, msg='하지만 언제 우리를 배신할지 모르는 자들이에요.\n절대 경계를 늦춰서는 안될 겁니다.', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6500):
            return 흑성회와의동맹에대하여5()


class 흑성회와의동맹에대하여5(state.State):
    def on_enter(self):
        select_camera(triggerId=4028, enable=True)
        add_cinematic_talk(npcId=11003753, msg='이해해줘서 고맙군.\n그럼 웨이 홍, 약속한 정보는 가져왔나?', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 정보전달하기()


#  웨이 홍의 정보 전달 
class 정보전달하기(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4026], returnView=False)
        add_cinematic_talk(npcId=11003754, msg='뭐, 징징거리는 어린아이는 다 달랜 것 같으니…\n본격적으로 거래를 시작해보자구.', duration=4000)
        add_cinematic_talk(npcId=11003754, msg='선불을 하는 취미는 없지만 호의를 베풀어 먼저 알려주도록 하지.\n의심많은 녀석의 입도 다물게 할겸. 후후.', duration=4000)
        add_cinematic_talk(npcId=11003754, msg='일단 우리 쪽에서 입수한 정보에 따르면 크리티아스의 방어 시스템은\n티아만 에너지 포트라는 곳에서 제어되고 있다고 한다.', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return 정보전달하기_02()


class 정보전달하기_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4028], returnView=False)
        add_cinematic_talk(npcId=11003753, msg='티아만 에너지 포트라…\n내 기억이 맞다면 최신식 장비들을 연구, 생산해내는\n크리티아스의 첨단 개발지역이었던 것으로 기억하네.', duration=5000)
        add_cinematic_talk(npcId=11003753, msg='유학시절 방문해보고 싶었지만 크리티아스의 기술력이 집약된 장소라\n외부인에게는 접근 자체가 불가능한 지역이었지.', duration=4000)
        add_cinematic_talk(npcId=11003754, msg='왕족 나으리의 호사스런 유학 생활 이야기는 관심없고,\n그곳을 장악하지 못하면 수호군 녀석들의 크리티아스 소풍은 포기해야할거야.', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=14000):
            return 정보전달하기_03()


class 정보전달하기_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4029], returnView=False)
        add_cinematic_talk(npcId=0, msg='더 들을 필요도 없는 것 같군요.\n서둘러 티아만 에너지 포트로 가서 방어 시스템을 무력화시키죠.', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 정보전달하기_04()


class 정보전달하기_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4026], returnView=False)
        add_cinematic_talk(npcId=11003754, msg='어이어이, 애송이. 서두르지 말라고?\n아직 중요한 얘기가 하나 더 있으니깐 말이야.', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 정보전달하기_05()


class 정보전달하기_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4028], returnView=False)
        add_cinematic_talk(npcId=11003753, msg='티어스 코어에 대한건가?', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 정보전달하기_06()


class 정보전달하기_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4026], returnView=False)
        add_cinematic_talk(npcId=11003754, msg='크리티아스의 방어 시스템, 그리고 티어스 코어라는 물건에 대한 정보.\n그게 거래조건이었으니 당연히 알아봤지.', duration=4000)
        add_cinematic_talk(npcId=11003754, msg='그런데 그 티어스 코어라는 물건말이야…\n정확하게 어디에 쓰는 것인지는 몰라도 보통 물건은 아닌 것 같더군.', duration=4000)
        add_cinematic_talk(npcId=11003754, msg='헤카톤 왕이 직접 개발한 장치라는데 티마이온?\n아무튼 무슨 거대 장치의 동력원으로 사용되었다고 하더군.', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return 정보전달하기2()


#  아르망을 찾아가보렴 
class 정보전달하기2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4007], returnView=False)
        add_balloon_talk(msg='!!!', duration=2000, delayTick=1000)
        add_balloon_talk(spawnId=110, msg='!!!', duration=2000, delayTick=1000)
        set_pc_emotion_sequence(sequenceNames=['Emotion_Suprise_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 정보전달하기3()


class 정보전달하기3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003753, msg='$MyPCName$… 생각보다 상황이 좋지 않을지도 모르겠군…', duration=3000)
        add_cinematic_talk(npcId=0, msg='예… 녀석들이 티어스 코어를 노리는 것이 티마이온 때문이라면…', duration=3000)
        add_cinematic_talk(npcId=11003753, msg='혹시 티어스 코어에 대한 정보는 그게 다인가? 어디에 있다던지 하는건…', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 정보전달하기3_1()


class 정보전달하기3_1(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4026], returnView=False)
        add_cinematic_talk(npcId=11003754, msg='이봐 라딘 사장, 이것도 정말 어렵게 얻은 정보라고.\n이 정도면 충분히 거래조건을 지킨 것 같은데?', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 정보전달하기3_2()


class 정보전달하기3_2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4007], returnView=False)
        add_cinematic_talk(npcId=11003753, msg='알겠네. 잠시 $MyPCName$와 얘기 좀 할테니 기다려주게나.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 정보전달하기4()


class 정보전달하기4(state.State):
    def on_enter(self):
        set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_achievement(triggerId=702, type='trigger', achieve='MeetRadin')
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[111])
        destroy_monster(spawnIds=[112])
        destroy_monster(spawnIds=[113])
        destroy_monster(spawnIds=[114])
        destroy_monster(spawnIds=[115])
        create_monster(spawnIds=[117], arg2=False, arg3=0) # 연출웨이홍
        create_monster(spawnIds=[118], arg2=False, arg3=0) # 연출브리드민
        create_monster(spawnIds=[119], arg2=False, arg3=0) # 연출바사라첸
        create_monster(spawnIds=[120], arg2=False, arg3=0) # 연출하렌
        create_monster(spawnIds=[121], arg2=False, arg3=0) # 연출카일

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class Skip_1(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[111])
        destroy_monster(spawnIds=[112])
        destroy_monster(spawnIds=[113])
        destroy_monster(spawnIds=[114])
        destroy_monster(spawnIds=[115])
        create_monster(spawnIds=[117], arg2=False, arg3=0) # 연출웨이홍
        create_monster(spawnIds=[118], arg2=False, arg3=0) # 연출브리드민
        create_monster(spawnIds=[119], arg2=False, arg3=0) # 연출바사라첸
        create_monster(spawnIds=[120], arg2=False, arg3=0) # 연출하렌
        create_monster(spawnIds=[121], arg2=False, arg3=0) # 연출카일
        set_cinematic_ui(type=4)
        reset_camera(interpolationTime=0)
        set_achievement(triggerId=702, type='trigger', achieve='MeetRadin')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_onetime_effect(id=7, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[110])


