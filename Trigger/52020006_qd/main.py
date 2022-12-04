""" trigger/52020006_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102,103,104])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001797], questStates=[3]):
            return 빈방(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001797], questStates=[2]):
            return 빈방(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001797], questStates=[1]):
            return 제이든_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[3]):
            return 제이든_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[2]):
            return 제이든_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[1]):
            return 세리하와함께전투_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[3]):
            return 세리하_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[2]):
            return 세리하_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[1]):
            return 세리하와아르망_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001794], questStates=[3]):
            return 세리하_대기(self.ctx)


class 세리하_대기(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102,105])
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[1]):
            return 세리하와함께전투_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[1]):
            return 세리하와아르망_대기(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 조건확인_대기01(self.ctx)


class 제이든_대기(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102,105])
        self.create_monster(spawnIds=[105], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[1]):
            return 세리하와함께전투_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[1]):
            return 세리하와아르망_대기(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 조건확인_대기01(self.ctx)


class 빈방(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102,105])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[1]):
            return 세리하와함께전투_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[1]):
            return 세리하와아르망_대기(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 조건확인_대기01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[1]):
            return 세리하와함께전투_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[1]):
            return 세리하와아르망_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[3]):
            return 조건확인_대기02(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[2]):
            return 조건확인_대기02(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[1]):
            return 조건확인_대기02(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[1]):
            return 조건확인_대기02(self.ctx)


class 조건확인_대기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[1]):
            return 세리하와함께전투_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[1]):
            return 세리하와아르망_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[3]):
            return 조건확인_대기01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[2]):
            return 조건확인_대기01(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[1]):
            return 조건확인_대기01(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[1]):
            return 조건확인_대기01(self.ctx)


class 세리하와아르망_대기(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102,105])
        self.create_monster(spawnIds=[101,102], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001795], questStates=[1]):
            return 퀘스트조건체크(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 세리하와아르망_준비(self.ctx)


class 세리하와아르망_준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.visible_my_pc(isVisible=False) # PC안보이게

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 세리하와아르망_연출시작(self.ctx)


class 세리하와아르망_연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=세리하와아르망_스킵완료, action='exit') # setsceneskip 1 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 세리하와아르망_연출01(self.ctx)


class 세리하와아르망_연출01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.add_cinematic_talk(npcId=11003548, illustId='Seriha_normal', msg='연출 보강 예정', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 세리하와아르망_연출02(self.ctx)


class 세리하와아르망_연출02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.add_cinematic_talk(npcId=11003658, illustId='Armand_normal', msg='조금만 기다려 주세요', duration=3000)
        self.visible_my_pc(isVisible=True) # PC보이게

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 세리하와아르망_연출03(self.ctx)


class 세리하와아르망_연출03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.add_cinematic_talk(npcId=11003548, illustId='Seriha_normal', msg='죄송합니다', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 세리하와아르망_마무리(self.ctx)


class 세리하와아르망_마무리(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[102])
        self.set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 세리하와아르망_연출종료(self.ctx)


class 세리하와아르망_스킵완료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102,105])
        self.create_monster(spawnIds=[101])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 세리하와아르망_연출종료(self.ctx)


class 세리하와아르망_연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=2)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(triggerId=9000, type='trigger', achieve='Armandsidentity')
        self.visible_my_pc(isVisible=True) # PC보이게
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 조건확인_대기01(self.ctx)


class 세리하와함께전투_대기(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102,105])
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001796], questStates=[1]):
            return 퀘스트조건체크(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 세리하와함께전투_준비(self.ctx)


class 세리하와함께전투_준비(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[150,151,152,153], animationEffect=True)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 세리하와함께전투_연출시작(self.ctx)


class 세리하와함께전투_연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=세리하와함께전투_전투직전스킵, action='exit') # setsceneskip 2 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 세리하와함께전투_연출01(self.ctx)


class 세리하와함께전투_연출01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.add_cinematic_talk(npcId=11003548, illustId='Seriha_normal', msg='그럼 누가 먼저 저것들을 쓸어버리나 내기하자고.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 세리하와함께전투_연출02(self.ctx)


class 세리하와함께전투_연출02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='임시연출이라 몬스터가 허약할 거야.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 세리하와함께전투_연출03(self.ctx)


class 세리하와함께전투_연출03(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[111], animationEffect=False)
        self.select_camera_path(pathIds=[8010], returnView=False)
        self.add_cinematic_talk(npcId=29000335, illustId='Seriha_normal', msg='간다!', duration=3000)
        self.set_scene_skip() # setsceneskip 2 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전투대기01(self.ctx)


class 세리하와함께전투_전투직전스킵(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102,105])
        self.create_monster(spawnIds=[101])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투대기01(self.ctx)


class 전투대기01(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=2)
        # <action name="AddCinematicTalk" npcID="29000251" illustID="11000015" msg="$52000121_QD__MAIN__17$" duration="2000" align="left" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투준비01(self.ctx)


class 전투준비01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[150,151,152,153]):
            return 전투끝(self.ctx)


class 전투끝(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8040], returnView=False)
        # <action name="업적이벤트를발생시킨다" arg1="9000" arg2="trigger" arg3="FightingSeriha"/>
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 암전02(self.ctx)


class 암전02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return npc교체01(self.ctx)


class npc교체01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[111])
        self.create_monster(spawnIds=[110], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투후제이든등장_연출준비(self.ctx)


class 전투후제이든등장_연출준비(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[111])
        self.create_monster(spawnIds=[110], animationEffect=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[8020], returnView=False)
        self.set_scene_skip(state=전투후제이든등장_스킵완료, action='exit') # setsceneskip 3 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전투후제이든등장_01_세리하소멸(self.ctx)


class 전투후제이든등장_01_세리하소멸(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003548, illustId='Seriha_normal', msg='내가 이긴 듯. 그럼 이만!', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전투후제이든등장_02_PC독백(self.ctx)


class 전투후제이든등장_02_PC독백(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[110])
        self.add_cinematic_talk(npcId=0, illustId='Seriha_normal', msg='이제 저 너머로 갈 차례인가...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전투후제이든등장_03_제이든등장(self.ctx)


class 전투후제이든등장_03_제이든등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.add_cinematic_talk(npcId=11003677, illustId='Jaiden_normal', msg='무사했구나, $MyPCName$.', duration=3000)
        self.set_scene_skip() # setsceneskip 3 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 세리하와함께전투_제이든등장_연출종료(self.ctx)


class 전투후제이든등장_스킵완료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102,105,110,111,150,151,152,153])
        self.create_monster(spawnIds=[105])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return None # Missing State: 세리하와함께전투_연출종료


class 세리하와함께전투_제이든등장_연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=2)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(triggerId=9000, type='trigger', achieve='FightingSeriha')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=2)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
