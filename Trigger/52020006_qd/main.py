""" trigger/52020006_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,103,104])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 퀘스트조건체크()


class 퀘스트조건체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001797], questStates=[3]):
            return 빈방()
        if quest_user_detected(boxIds=[9000], questIds=[50001797], questStates=[2]):
            return 빈방()
        if quest_user_detected(boxIds=[9000], questIds=[50001797], questStates=[1]):
            return 제이든_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[3]):
            return 제이든_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[2]):
            return 제이든_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[1]):
            return 세리하와함께전투_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[3]):
            return 세리하_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[2]):
            return 세리하_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[1]):
            return 세리하와아르망_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001794], questStates=[3]):
            return 세리하_대기()


class 세리하_대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,105])
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[1]):
            return 세리하와함께전투_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[1]):
            return 세리하와아르망_대기()
        if wait_tick(waitTick=1000):
            return 조건확인_대기01()


class 제이든_대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,105])
        create_monster(spawnIds=[105], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[1]):
            return 세리하와함께전투_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[1]):
            return 세리하와아르망_대기()
        if wait_tick(waitTick=1000):
            return 조건확인_대기01()


class 빈방(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,105])

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[1]):
            return 세리하와함께전투_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[1]):
            return 세리하와아르망_대기()
        if wait_tick(waitTick=1000):
            return 종료()


class 조건확인_대기01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[1]):
            return 세리하와함께전투_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[1]):
            return 세리하와아르망_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[3]):
            return 조건확인_대기02()
        if quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[2]):
            return 조건확인_대기02()
        if not quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[1]):
            return 조건확인_대기02()
        if not quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[1]):
            return 조건확인_대기02()


class 조건확인_대기02(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[1]):
            return 세리하와함께전투_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[1]):
            return 세리하와아르망_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[3]):
            return 조건확인_대기01()
        if quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[2]):
            return 조건확인_대기01()
        if not quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[1]):
            return 조건확인_대기01()
        if not quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[1]):
            return 조건확인_대기01()


class 세리하와아르망_대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,105])
        create_monster(spawnIds=[101,102], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if not quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[1]):
            return 퀘스트조건체크()
        if wait_tick(waitTick=1000):
            return 세리하와아르망_준비()


class 세리하와아르망_준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        visible_my_pc(isVisible=False) # PC안보이게

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 세리하와아르망_연출시작()


class 세리하와아르망_연출시작(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=세리하와아르망_스킵완료, arg2='exit') # setsceneskip 1 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 세리하와아르망_연출01()


class 세리하와아르망_연출01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        add_cinematic_talk(npcId=11003548, illustId='Seriha_normal', msg='연출 보강 예정', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세리하와아르망_연출02()


class 세리하와아르망_연출02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        add_cinematic_talk(npcId=11003658, illustId='Armand_normal', msg='조금만 기다려 주세요', duration=3000)
        visible_my_pc(isVisible=True) # PC보이게

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세리하와아르망_연출03()


class 세리하와아르망_연출03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        add_cinematic_talk(npcId=11003548, illustId='Seriha_normal', msg='죄송합니다', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세리하와아르망_마무리()


class 세리하와아르망_마무리(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])
        set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 세리하와아르망_연출종료()


class 세리하와아르망_스킵완료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,105])
        create_monster(spawnIds=[101])
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 세리하와아르망_연출종료()


class 세리하와아르망_연출종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_achievement(triggerId=9000, type='trigger', achieve='Armandsidentity')
        visible_my_pc(isVisible=True) # PC보이게
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 조건확인_대기01()


class 세리하와함께전투_대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,105])
        create_monster(spawnIds=[101], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if not quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[1]):
            return 퀘스트조건체크()
        if wait_tick(waitTick=1000):
            return 세리하와함께전투_준비()


class 세리하와함께전투_준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[150,151,152,153], arg2=True)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 세리하와함께전투_연출시작()


class 세리하와함께전투_연출시작(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=세리하와함께전투_전투직전스킵, arg2='exit') # setsceneskip 2 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 세리하와함께전투_연출01()


class 세리하와함께전투_연출01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        add_cinematic_talk(npcId=11003548, illustId='Seriha_normal', msg='그럼 누가 먼저 저것들을 쓸어버리나 내기하자고.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세리하와함께전투_연출02()


class 세리하와함께전투_연출02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        add_cinematic_talk(npcId=0, msg='임시연출이라 몬스터가 허약할 거야.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세리하와함께전투_연출03()


class 세리하와함께전투_연출03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[111], arg2=False)
        select_camera_path(pathIds=[8010], returnView=False)
        add_cinematic_talk(npcId=29000335, illustId='Seriha_normal', msg='간다!', duration=3000)
        set_scene_skip() # setsceneskip 2 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전투대기01()


class 세리하와함께전투_전투직전스킵(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,105])
        create_monster(spawnIds=[101])
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투대기01()


class 전투대기01(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        # <action name="AddCinematicTalk" npcID="29000251" illustID="11000015" msg="$52000121_QD__MAIN__17$" duration="2000" align="left" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투준비01()


class 전투준비01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[150,151,152,153]):
            return 전투끝()


class 전투끝(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8040], returnView=False)
        # <action name="업적이벤트를발생시킨다" arg1="9000" arg2="trigger" arg3="FightingSeriha"/>
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 암전02()


class 암전02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return npc교체01()


class npc교체01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[111])
        create_monster(spawnIds=[110], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투후제이든등장_연출준비()


class 전투후제이든등장_연출준비(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[111])
        create_monster(spawnIds=[110], arg2=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[8020], returnView=False)
        set_scene_skip(state=전투후제이든등장_스킵완료, arg2='exit') # setsceneskip 3 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전투후제이든등장_01_세리하소멸()


class 전투후제이든등장_01_세리하소멸(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003548, illustId='Seriha_normal', msg='내가 이긴 듯. 그럼 이만!', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전투후제이든등장_02_PC독백()


class 전투후제이든등장_02_PC독백(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[110])
        add_cinematic_talk(npcId=0, illustId='Seriha_normal', msg='이제 저 너머로 갈 차례인가...', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전투후제이든등장_03_제이든등장()


class 전투후제이든등장_03_제이든등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[105], arg2=False)
        add_cinematic_talk(npcId=11003677, illustId='Jaiden_normal', msg='무사했구나, $MyPCName$.', duration=3000)
        set_scene_skip() # setsceneskip 3 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세리하와함께전투_제이든등장_연출종료()


class 전투후제이든등장_스킵완료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,105,110,111,150,151,152,153])
        create_monster(spawnIds=[105])
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None # Missing State: 세리하와함께전투_연출종료


class 세리하와함께전투_제이든등장_연출종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_achievement(triggerId=9000, type='trigger', achieve='FightingSeriha')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출종료()


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


