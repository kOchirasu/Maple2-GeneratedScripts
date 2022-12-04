""" trigger/52020022_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102,103,104,111,115])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001791], questStates=[3]):
            return 빈방(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001791], questStates=[2]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001791], questStates=[1]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001790], questStates=[3]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001790], questStates=[2]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001790], questStates=[1]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001784], questStates=[3]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001784], questStates=[2]):
            return 세리하_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001784], questStates=[1]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001783], questStates=[3]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001783], questStates=[2]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001783], questStates=[1]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001782], questStates=[3]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001782], questStates=[2]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001782], questStates=[1]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001781], questStates=[3]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001781], questStates=[2]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001781], questStates=[1]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[3]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[2]):
            return 아르망_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[1]):
            return 레지스탕스_대기(self.ctx)


class 기본(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 기본_대기(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[111], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001791], questStates=[3]):
            return 빈방(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001784], questStates=[2]):
            return 세리하_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[2]):
            return 아르망_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[1]):
            return 레지스탕스_대기(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 레지스탕스_대기(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[102,103,104], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[1]):
            return 퀘스트조건체크(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 레지스탕스_준비(self.ctx)


class 레지스탕스_준비(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8000,8001], returnView=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 레지스탕스_연출시작(self.ctx)


class 레지스탕스_연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=레지스탕스_스킵완료, action='exit') # setsceneskip 1 set
        self.move_user_path(patrolName='MS2PatrolData_PC_Walkin')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 레지스탕스_체키01(self.ctx)


class 레지스탕스_체키01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.add_cinematic_talk(npcId=11003661, illustId='Checky_normal', msg='여기 뭐가 있긴 있는 거야?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 레지스탕스_헨리테01(self.ctx)


class 레지스탕스_헨리테01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.add_cinematic_talk(npcId=11003662, illustId='henritte_normal', msg='여기 뭔가 있다는 소문도 사실은 거짓 정보 아니야?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 레지스탕스_지그문트01(self.ctx)


class 레지스탕스_지그문트01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)
        self.add_cinematic_talk(npcId=11003663, illustId='sigmund_normal', msg='아니야. 연출이 있는 건 사실이지만 보강 예정이라고.\n1월 마감 이전에 업데이트한대.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 레지스탕스_이동(self.ctx)


class 레지스탕스_이동(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8006], returnView=False)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_Goingout_Checky')
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_Goingout_Henritte')
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_Goingout_Sigmund')
        self.add_cinematic_talk(npcId=11003663, illustId='sigmund_normal', msg='그럼, 조금만 기다려 주시길...', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 레지스탕스_마무리(self.ctx)


class 레지스탕스_마무리(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[102,103,104])
        # <action name="몬스터를생성한다" arg1="101"/>
        self.set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 레지스탕스_연출종료(self.ctx)


class 레지스탕스_스킵완료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102,103,104])
        self.create_monster(spawnIds=[101])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 레지스탕스_연출종료(self.ctx)


class 레지스탕스_연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=2)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 조건확인_대기01(self.ctx)


class 조건확인_대기01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[2]):
            return 아르망_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[1]):
            return 조건확인_대기02(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[3]):
            return 조건확인_대기02(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[2]):
            return 조건확인_대기02(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[2]):
            return 조건확인_대기02(self.ctx)


class 조건확인_대기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[2]):
            return 아르망_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[1]):
            return 조건확인_대기01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[3]):
            return 조건확인_대기01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[2]):
            return 조건확인_대기01(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[2]):
            return 조건확인_대기01(self.ctx)


class 아르망_대기(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101], arg2=False)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001780], questStates=[2]):
            return 퀘스트조건체크(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 아르망_준비(self.ctx)


class 아르망_준비(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8010], returnView=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 아르망_연출시작(self.ctx)


class 아르망_연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=아르망_스킵완료, action='exit') # setsceneskip 2 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 아르망_연출01(self.ctx)


class 아르망_연출01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8010,8011], returnView=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Armand_comingout')
        self.move_user_path(patrolName='MS2PatrolData_PC_Surprised')
        self.add_cinematic_talk(npcId=11003672, illustId='Armand_normal', msg='연출 추가 예정입니다.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 아르망_마무리(self.ctx)


class 아르망_마무리(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,111])
        self.create_monster(spawnIds=[111])
        self.set_scene_skip() # setsceneskip 2 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출종료(self.ctx)


class 아르망_스킵완료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,111])
        self.create_monster(spawnIds=[111])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 세리하_대기(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[111,115], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001784], questStates=[2]):
            return 퀘스트조건체크(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 세리하_준비(self.ctx)


class 세리하_준비(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8014], returnView=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.visible_my_pc(isVisible=False) # PC안보이게

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 세리하_연출시작(self.ctx)


class 세리하_연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=세리하_스킵완료, action='exit') # setsceneskip 3 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 세리하_연출01(self.ctx)


class 세리하_연출01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8021], returnView=False)
        self.add_cinematic_talk(npcId=11003660, illustId='Seriha_normal', msg='1월 중 연출 보강 예정', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 세리하_연출02(self.ctx)


class 세리하_연출02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8014], returnView=False)
        self.add_cinematic_talk(npcId=11003672, illustId='Armand_normal', msg='대사 위주 보강 예정', duration=4000)
        self.visible_my_pc(isVisible=True) # PC보이게

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 세리하_마무리(self.ctx)


class 세리하_마무리(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[115])
        self.set_scene_skip() # setsceneskip 3 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출종료(self.ctx)


class 세리하_스킵완료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[115])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 빈방(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102,103,104,111,115], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001791], questStates=[3]):
            return 퀘스트조건체크(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


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
