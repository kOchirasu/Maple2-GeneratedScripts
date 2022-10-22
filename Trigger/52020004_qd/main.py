""" trigger/52020004_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 퀘스트조건체크()


class 퀘스트조건체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[3]):
            return 빈방()
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[2]):
            return 트럭으로가세요_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[1]):
            return 세리하첫등장연출_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001762], questStates=[3]):
            return 제이든만_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001762], questStates=[2]):
            return 제이든만_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001762], questStates=[1]):
            return 제이든만_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001761], questStates=[3]):
            return 제이든만_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001761], questStates=[2]):
            return 제이든호출_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001761], questStates=[1]):
            return 제이든호출_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001760], questStates=[3]):
            return 라딘에게돌아가_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001760], questStates=[2]):
            return 라딘에게돌아가_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001760], questStates=[1]):
            return 공주님과기사연출_대기()


class 기본(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 라딘에게돌아가_대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001760], questStates=[3]):
            return 라딘에게돌아가()
        if quest_user_detected(boxIds=[9000], questIds=[50001760], questStates=[2]):
            return 라딘에게돌아가()
        if not quest_user_detected(boxIds=[9000], questIds=[50001760], questStates=[2]):
            return 퀘스트조건체크()


class 라딘에게돌아가(state.State):
    def on_enter(self):
        move_user(mapId=52020002, portalId=1)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 라딘에게돌아가()


class 제이든호출_대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001761], questStates=[2]):
            return 제이든호출_연출준비()
        if quest_user_detected(boxIds=[9000], questIds=[50001761], questStates=[1]):
            return 제이든호출_연출준비()
        if not quest_user_detected(boxIds=[9000], questIds=[50001761], questStates=[2]):
            return 퀘스트조건체크()


class 기본_대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[1]):
            return 세리하첫등장연출_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001762], questStates=[3]):
            return 조건확인_대기01()
        if quest_user_detected(boxIds=[9000], questIds=[50001762], questStates=[2]):
            return 조건확인_대기01()
        if quest_user_detected(boxIds=[9000], questIds=[50001762], questStates=[1]):
            return 조건확인_대기01()
        if quest_user_detected(boxIds=[9000], questIds=[50001761], questStates=[3]):
            return 조건확인_대기01()
        if not quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return 퀘스트조건체크()


class 조건확인_대기01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[1]):
            return 세리하첫등장연출_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001762], questStates=[3]):
            return 조건확인_대기02()
        if quest_user_detected(boxIds=[9000], questIds=[50001762], questStates=[2]):
            return 조건확인_대기02()
        if quest_user_detected(boxIds=[9000], questIds=[50001762], questStates=[1]):
            return 몬스터체크()
        if quest_user_detected(boxIds=[9000], questIds=[50001761], questStates=[3]):
            return 조건확인_대기02()
        if not quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[1]):
            return 조건확인_대기02()


class 조건확인_대기02(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[1]):
            return 세리하첫등장연출_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001762], questStates=[3]):
            return 조건확인_대기01()
        if quest_user_detected(boxIds=[9000], questIds=[50001762], questStates=[2]):
            return 조건확인_대기01()
        if quest_user_detected(boxIds=[9000], questIds=[50001762], questStates=[1]):
            return 몬스터체크()
        if quest_user_detected(boxIds=[9000], questIds=[50001761], questStates=[3]):
            return 조건확인_대기01()
        if not quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[1]):
            return 조건확인_대기01()


class 트럭으로가세요_대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[3]):
            return 트럭으로가세요()
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[2]):
            return 트럭으로가세요()
        if not quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[3]):
            return 퀘스트조건체크()


class 트럭으로가세요(state.State):
    def on_enter(self):
        move_user(mapId=52020005, portalId=1)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 트럭으로가세요()


class 빈방(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,105,106,107,108,109,110,111,121,122,131,132,133])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 공주님과기사연출_대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52020004, portalId=1) # 유저 첫 위치 잡기
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=공주님과기사연출_스킵완료, arg2='exit') # setsceneskip 1 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 공주님과기사연출_시작()


class 공주님과기사연출_시작(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        visible_my_pc(isVisible=False) # PC안보이게

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 공주와기사00()


class 공주와기사00(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11003675, illustId='Krantz_normal', msg='이곳은… 꽤나 오랜만에 오는 것 같군요. ', duration=3000)
        move_npc(spawnId=102, patrolName='krantz_walkin')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 공주와기사01()


class 공주와기사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        add_cinematic_talk(npcId=11003674, illustId='Eone_normal', msg='그렇구나. …다시 올 일이 없을 줄 알았지만. ', duration=3000)
        move_npc(spawnId=102, patrolName='MS2PatrolData_Krantz_walking')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 공주와기사02()


class 공주와기사02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        add_cinematic_talk(npcId=11003675, illustId='Krantz_normal', msg='제게 내리실 명령이 무엇입니까?', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 공주와기사03()


class 공주와기사03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        move_npc(spawnId=102, patrolName='MS2PatrolData_Krantz_promise')
        add_cinematic_talk(npcId=11003674, illustId='Eone_normal', msg='기다려 달라.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 공주와기사04()


class 공주와기사04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        add_cinematic_talk(npcId=11003675, illustId='Krantz_normal', msg='헐….', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 마무리()


class 마무리(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        add_cinematic_talk(npcId=11003674, illustId='Eone_normal', msg='연출을 보강할 예정이니 기다려 달라.\n이 연출엔 대사가 추가될 것이다.', duration=3000)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 공주님과기사연출_종료()


class 공주님과기사연출_스킵완료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 공주님과기사연출_종료()


class 공주님과기사연출_종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_achievement(triggerId=9000, type='trigger', achieve='PrincessMeetsHerKnight')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 라딘에게돌아가()


class 제이든만_대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,110,111,112,121,122,131,132,133])
        create_monster(spawnIds=[110])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 조건확인_대기01()


class 제이든호출_연출준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[110])
        create_monster(spawnIds=[105,106,107,108,109])
        destroy_monster(spawnIds=[101,102,111,112,121,122,131,132,133])
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 제이든호출_연출시작()


class 제이든호출_연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_scene_skip(state=제이든호출_스킵완료, arg2='nextState') # setsceneskip 2 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PC진입_놀람()


class PC진입_놀람(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8007,8008,8009], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=0, msg='이건 대체… 무슨 상황이지?', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 제이든짜증01()


class 제이든짜증01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8010], returnView=False)
        add_cinematic_talk(npcId=11003541, illustId='Jaiden_normal', msg='…몰라서 물어?', duration=3000)
        # <action name="SetNpcEmotionLoop" arg1="110" arg2="Talk_A" arg3="3000"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 제이든짜증02()


class 제이든짜증02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8011], returnView=False)
        add_cinematic_talk(npcId=11003541, illustId='Jaiden_normal', msg='부주의한 누구 덕에 난리가 난 상황이다.', duration=3000)
        set_npc_emotion_loop(spawnId=110, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 제이든짜증03()


class 제이든짜증03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8012], returnView=False)
        add_cinematic_talk(npcId=11003541, illustId='Jaiden_normal', msg='빨리 이쪽으로 넘어와! 어서!', duration=2000)
        set_npc_emotion_loop(spawnId=110, sequenceName='Talk_A', duration=3000)
        set_scene_skip() # setsceneskip 2 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 제이든호출_연출종료()


class 제이든호출_스킵완료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 제이든호출_연출종료()


class 제이든호출_연출종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 조건확인_대기01()


class 몬스터체크(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[105,106,107,108,109]):
            return 몬스터추가스폰01()
        if monster_dead(boxIds=[105]):
            return 몬스터추가스폰105()
        if monster_dead(boxIds=[106]):
            return 몬스터추가스폰106()
        if monster_dead(boxIds=[107]):
            return 몬스터추가스폰107()
        if monster_dead(boxIds=[108]):
            return 몬스터추가스폰108()
        if monster_dead(boxIds=[109]):
            return 몬스터추가스폰109()
        if wait_tick(waitTick=1000):
            return 조건확인_대기01()


class 몬스터추가스폰01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[105,106,107,108,109], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[105,106,107,108,109]):
            return 조건확인_대기01()
        if wait_tick(waitTick=1000):
            return 조건확인_대기01()


class 몬스터추가스폰105(state.State):
    def on_enter(self):
        create_monster(spawnIds=[105], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[105]):
            return 몬스터추가스폰106()
        if wait_tick(waitTick=1000):
            return 조건확인_대기01()


class 몬스터추가스폰106(state.State):
    def on_enter(self):
        create_monster(spawnIds=[106], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[106]):
            return 몬스터추가스폰107()
        if wait_tick(waitTick=1000):
            return 조건확인_대기01()


class 몬스터추가스폰107(state.State):
    def on_enter(self):
        create_monster(spawnIds=[107], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[107]):
            return 몬스터추가스폰108()
        if wait_tick(waitTick=1000):
            return 조건확인_대기01()


class 몬스터추가스폰108(state.State):
    def on_enter(self):
        create_monster(spawnIds=[108], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[108]):
            return 몬스터추가스폰109()
        if wait_tick(waitTick=1000):
            return 조건확인_대기01()


class 몬스터추가스폰109(state.State):
    def on_enter(self):
        create_monster(spawnIds=[109], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[109]):
            return 조건확인_대기01()
        if wait_tick(waitTick=1000):
            return 조건확인_대기01()


class 세리하첫등장연출_대기(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[111])
        destroy_monster(spawnIds=[101,102,105,106,107,108,109,110,112,121,122,131,132,133])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 세리하첫등장연출_준비()


class 세리하첫등장연출_준비(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52020004, portalId=10) # 유저 첫 위치 잡기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 세리하첫등장연출_시작()


class 세리하첫등장연출_시작(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8015], returnView=False)
        set_scene_skip(state=세리하첫등장연출_스킵완료, arg2='nextState') # setsceneskip 3 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 탐색실패01()


class 탐색실패01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8015], returnView=False)
        add_balloon_talk(spawnId=0, msg='흐음….', duration=2000, delayTick=0)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 탐색실패02()


class 탐색실패02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003541, illustId='Jaiden_normal', msg='단서가 될 만한 게 없는 건지, 있는데도 모르겠는 건지.\n답답하네, 좀.', duration=3000)
        move_user_path(patrolName='PC_walkinCenter')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 흑성회등장01()


class 흑성회등장01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[121,122])
        add_cinematic_talk(npcId=11003659, illustId='WeiHong_normal', msg='그럼, 답답한 사람들끼리 이야기를 좀 해보면 어떨까?', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 흑성회등장02()


class 흑성회등장02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8020], returnView=False)
        move_npc(spawnId=121, patrolName='Weihong_walkin01')
        add_cinematic_talk(npcId=11003659, illustId='WeiHong_normal', msg='알고 있는 것을 나누면, 목표에 보다 빨리 다가갈 수 있을 테니.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 흑성회등장03()


class 흑성회등장03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8021], returnView=False)
        move_npc(spawnId=122, patrolName='Seriha_walkin01')
        add_cinematic_talk(npcId=11003659, illustId='WeiHong_normal', msg='크리티아스의 왕족.\n너희가 찾고 있는 건 바로 그들의 행적 아닌가.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 흑성회등장04()


class 흑성회등장04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003659, illustId='WeiHong_normal', msg='아마 이곳에 들어온 모두가 그들을 찾고 있을 거야.\n흑성회도 마찬가지다.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 흑성회등장05()


class 흑성회등장05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8022], returnView=False)
        add_cinematic_talk(npcId=11003659, illustId='WeiHong_normal', msg='과연 누가 가장 먼저 목적을 이루게 될까… 궁금하지 않나?\n물론, 나는 정답을 알 것 같지만.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC독백01()


class PC독백01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[131,132,133])
        select_camera_path(pathIds=[8015], returnView=False)
        add_cinematic_talk(npcId=0, msg='(흑성회라니… 일이 생각보다 복잡하게 돌아가는 것 같다.)', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 레지스탕스등장01()


class 레지스탕스등장01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8030], returnView=False)
        add_cinematic_talk(npcId=11003663, msg='생각하고 계시는 그 답이 정답이 맞을까요, 영감님?', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 레지스탕스등장02()


class 레지스탕스등장02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003661, msg='틀렸을 것 같은데?', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 레지스탕스등장03()


class 레지스탕스등장03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003662, msg='우리도 여기까지 힘들게 왔는데, 빈 손으로 갈 수는 없잖아요.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 레지스탕스등장04()


class 레지스탕스등장04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003662, msg='우리 등장이 좀 밋밋했죠?\n멋있게 등장하도록 연출 보강 예정이니 참고해 주세요.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세리하등장01()


class 세리하등장01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8022], returnView=False)
        add_cinematic_talk(npcId=11003659, illustId='WeiHong_normal', msg='불청객이 많아서 그런가, 좀 시끄럽군.\n나는 시끄러운 건 영 체질에 안 맞는단 말이야.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세리하등장02()


class 세리하등장02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003659, illustId='WeiHong_normal', msg='$npc:11003660$, 정리해라.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세리하등장03()


class 세리하등장03(state.State):
    def on_enter(self):
        move_npc(spawnId=122, patrolName='Seriha_walkinto')
        show_caption(type='NameCaption', title='$npc:11003660$', desc='흑성회 특수부대장, $npc:11003659$의 측근', align='centerLeft', offsetRateX=0.5, offsetRateY=0.15, duration=5000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세리하등장04()


class 세리하등장04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8023], returnView=False)
        add_cinematic_talk(npcId=11003660, illustId='Seriha_normal', msg='네, 보스.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 제이든경고01()


class 제이든경고01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8015], returnView=False)
        move_npc(spawnId=111, patrolName='Jaiden_whispertoPC')
        add_cinematic_talk(npcId=11003541, illustId='Jaiden_normal', msg='도망가자.', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 제이든경고02()


class 제이든경고02(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=0, msg='갑자기 그게 무슨 소리…', duration=2000, delayTick=0)
        add_cinematic_talk(npcId=11003541, illustId='Jaiden_normal', msg='$npcName:11003660$$pp:가,이$ 나선 이상, 이제 여긴 불지옥이 될거야.\n시간 없어. 빨리.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC제이든과도망()


class PC제이든과도망(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        add_balloon_talk(spawnId=111, msg='저쪽으로. 서둘러…!', duration=2000, delayTick=0)
        move_npc(spawnId=111, patrolName='Jaiden_run')
        move_user_path(patrolName='PC_run')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세리하공격준비()


class 세리하공격준비(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8023], returnView=False)
        add_cinematic_talk(npcId=11003660, illustId='Seriha_normal', msg='입만 산 것들. 깨끗하게 정리해 주마.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 자막구간_준비()


#  설명문 출력 
class 자막구간_준비(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 자막구간_01()


class 자막구간_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='제이든과 함께 그곳을 빠져나오던 순간\n들려왔던 어마어마한 소리.')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 자막구간_02()


class 자막구간_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='왕족의 비상상황을 대비해 견고하게 지어졌을 지하실 내부는\n순식간에 굉음을 내며 무너져 내렸다.')
        # Missing State: ShowCaption03Skip
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 자막구간_03()


class 자막구간_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='나는 달려야 했다.\n오직 살아남는 것만을 생각하면서.')
        set_scene_skip() # setsceneskip 3 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 세리하첫등장연출_종료()


class 세리하첫등장연출_스킵완료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 세리하첫등장연출_종료()


class 세리하첫등장연출_종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        set_achievement(triggerId=9000, type='trigger', achieve='BlackStarVSResistance')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 최종맵이동()


class 최종맵이동(state.State):
    def on_enter(self):
        move_user(mapId=52020005, portalId=10) # 버려진 트럭으로 자동 이동
        visible_my_pc(isVisible=False) # PC안보이게
        visible_my_pc(isVisible=True) # PC보이게
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 최종맵이동()


class 종료(state.State):
    pass


