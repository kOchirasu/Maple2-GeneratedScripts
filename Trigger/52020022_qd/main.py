""" trigger/52020022_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,103,104,111,115])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 퀘스트조건체크()


class 퀘스트조건체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001791], questStates=[3]):
            return 빈방()
        if quest_user_detected(boxIds=[9000], questIds=[50001791], questStates=[2]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001791], questStates=[1]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001790], questStates=[3]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001790], questStates=[2]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001790], questStates=[1]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001784], questStates=[3]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001784], questStates=[2]):
            return 세리하_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001784], questStates=[1]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001783], questStates=[3]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001783], questStates=[2]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001783], questStates=[1]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001782], questStates=[3]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001782], questStates=[2]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001782], questStates=[1]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001781], questStates=[3]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001781], questStates=[2]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001781], questStates=[1]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[3]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[2]):
            return 아르망_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[1]):
            return 레지스탕스_대기()


class 기본(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 기본_대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001791], questStates=[3]):
            return 빈방()
        if quest_user_detected(boxIds=[9000], questIds=[50001784], questStates=[2]):
            return 세리하_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[2]):
            return 아르망_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[1]):
            return 레지스탕스_대기()
        if wait_tick(waitTick=1000):
            return 종료()


class 레지스탕스_대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102,103,104], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if not quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[1]):
            return 퀘스트조건체크()
        if wait_tick(waitTick=1000):
            return 레지스탕스_준비()


class 레지스탕스_준비(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000,8001], returnView=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 레지스탕스_연출시작()


class 레지스탕스_연출시작(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=레지스탕스_스킵완료, arg2='exit') # setsceneskip 1 set
        move_user_path(patrolName='MS2PatrolData_PC_Walkin')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 레지스탕스_체키01()


class 레지스탕스_체키01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        add_cinematic_talk(npcId=11003661, illustId='Checky_normal', msg='여기 뭐가 있긴 있는 거야?', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 레지스탕스_헨리테01()


class 레지스탕스_헨리테01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        add_cinematic_talk(npcId=11003662, illustId='henritte_normal', msg='여기 뭔가 있다는 소문도 사실은 거짓 정보 아니야?', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 레지스탕스_지그문트01()


class 레지스탕스_지그문트01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        add_cinematic_talk(npcId=11003663, illustId='sigmund_normal', msg='아니야. 연출이 있는 건 사실이지만 보강 예정이라고.\n1월 마감 이전에 업데이트한대.', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 레지스탕스_이동()


class 레지스탕스_이동(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8006], returnView=False)
        move_npc(spawnId=102, patrolName='MS2PatrolData_Goingout_Checky')
        move_npc(spawnId=103, patrolName='MS2PatrolData_Goingout_Henritte')
        move_npc(spawnId=104, patrolName='MS2PatrolData_Goingout_Sigmund')
        add_cinematic_talk(npcId=11003663, illustId='sigmund_normal', msg='그럼, 조금만 기다려 주시길...', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 레지스탕스_마무리()


class 레지스탕스_마무리(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102,103,104])
        # <action name="몬스터를생성한다" arg1="101"/>
        set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 레지스탕스_연출종료()


class 레지스탕스_스킵완료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,103,104])
        create_monster(spawnIds=[101])
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 레지스탕스_연출종료()


class 레지스탕스_연출종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 조건확인_대기01()


class 조건확인_대기01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[2]):
            return 아르망_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[1]):
            return 조건확인_대기02()
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[3]):
            return 조건확인_대기02()
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[2]):
            return 조건확인_대기02()
        if not quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[2]):
            return 조건확인_대기02()


class 조건확인_대기02(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[2]):
            return 아르망_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[1]):
            return 조건확인_대기01()
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[3]):
            return 조건확인_대기01()
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[2]):
            return 조건확인_대기01()
        if not quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[2]):
            return 조건확인_대기01()


class 아르망_대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[101], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if not quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[2]):
            return 퀘스트조건체크()
        if wait_tick(waitTick=1000):
            return 아르망_준비()


class 아르망_준비(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8010], returnView=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 아르망_연출시작()


class 아르망_연출시작(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=아르망_스킵완료, arg2='exit') # setsceneskip 2 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아르망_연출01()


class 아르망_연출01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8010,8011], returnView=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_Armand_comingout')
        move_user_path(patrolName='MS2PatrolData_PC_Surprised')
        add_cinematic_talk(npcId=11003672, illustId='Armand_normal', msg='연출 추가 예정입니다.', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 아르망_마무리()


class 아르망_마무리(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,111])
        create_monster(spawnIds=[111])
        set_scene_skip() # setsceneskip 2 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출종료()


class 아르망_스킵완료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,111])
        create_monster(spawnIds=[111])
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 세리하_대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111,115], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if not quest_user_detected(boxIds=[9000], questIds=[50001784], questStates=[2]):
            return 퀘스트조건체크()
        if wait_tick(waitTick=1000):
            return 세리하_준비()


class 세리하_준비(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8014], returnView=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        visible_my_pc(isVisible=False) # PC안보이게

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 세리하_연출시작()


class 세리하_연출시작(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=세리하_스킵완료, arg2='exit') # setsceneskip 3 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 세리하_연출01()


class 세리하_연출01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8021], returnView=False)
        add_cinematic_talk(npcId=11003660, illustId='Seriha_normal', msg='1월 중 연출 보강 예정', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 세리하_연출02()


class 세리하_연출02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8014], returnView=False)
        add_cinematic_talk(npcId=11003672, illustId='Armand_normal', msg='대사 위주 보강 예정', duration=4000)
        visible_my_pc(isVisible=True) # PC보이게

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 세리하_마무리()


class 세리하_마무리(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[115])
        set_scene_skip() # setsceneskip 3 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출종료()


class 세리하_스킵완료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[115])
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 빈방(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,103,104,111,115], arg2=False)

    def on_tick(self) -> state.State:
        if not quest_user_detected(boxIds=[9000], questIds=[50001791], questStates=[3]):
            return 퀘스트조건체크()
        if wait_tick(waitTick=1000):
            return 종료()


class 연출종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 종료(state.State):
    pass


