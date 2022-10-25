""" trigger/02000065_bf/main.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001630], questStates=[3]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001630], questStates=[2]):
            return 앤있음(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001630], questStates=[1]):
            return 앤있음(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001625], questStates=[3]):
            return 앤있음(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001625], questStates=[2]):
            return 연출2준비(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001625], questStates=[1]):
            return 앤있음(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001624], questStates=[3]):
            return 앤있음(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001624], questStates=[2]):
            return 앤있음(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001624], questStates=[1]):
            return 앤있음(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001623], questStates=[3]):
            return 앤있음(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001623], questStates=[2]):
            return 앤있음(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001623], questStates=[1]):
            return 연출1준비(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001622], questStates=[3]):
            return 기본상태(self.ctx)


class 기본상태(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,111])

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 퀘스트조건체크(self.ctx)


class 앤있음(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[111], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001625], questStates=[2]):
            return 연출2준비(self.ctx)
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 연출1준비(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 연출1앤등장준비(self.ctx)


class 연출1앤등장준비(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 앤등장(self.ctx)


class 앤등장(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_ann01')
        self.add_cinematic_talk(npcId=11003432, illustId='Ann_normal', msg='$02000065_BF__MAIN__0$', duration=3000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 앤등장2(self.ctx)


class 앤등장2(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.add_balloon_talk(spawnId=101, msg='$02000065_BF__MAIN__1$', duration=3000, delayTick=0)
        # <action name="NPC를이동시킨다" arg1="101" arg2="MS2PatrolData_ann02" />

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출종료(self.ctx)


class 연출2준비(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[111], animationEffect=False)
        self.visible_my_pc(isVisible=False) # 유저 투명 처리
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 연출2준비1(self.ctx)


class 연출2준비1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 앤대사01(self.ctx)


class 앤대사01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8010,8011], returnView=False)
        self.add_cinematic_talk(npcId=11003432, msg='$02000065_BF__MAIN__2$', duration=3000)
        self.set_npc_emotion_loop(spawnId=111, sequenceName='Talk_A', duration=3000)
        self.set_scene_skip(state=칼과앤_스킵완료, action='nextState') # setsceneskip set
        self.set_skip(state=앤대사01_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 칼대사01(self.ctx)


class 앤대사01_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 칼대사01(self.ctx)


class 칼대사01(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11000074, msg='$02000065_BF__MAIN__3$', duration=3000)
        self.set_skip(state=칼대사01_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 앤대사02(self.ctx)


class 칼대사01_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 앤대사02(self.ctx)


class 앤대사02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003432, msg='$02000065_BF__MAIN__4$', duration=4000)
        self.set_npc_emotion_loop(spawnId=111, sequenceName='Talk_A', duration=3000)
        self.set_skip(state=앤대사02_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6400):
            return 칼대사02(self.ctx)


class 앤대사02_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 칼대사02(self.ctx)


class 칼대사02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11000074, msg='$02000065_BF__MAIN__5$', duration=3000)
        self.set_skip(state=칼대사02_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8071):
            return 앤대사03(self.ctx)


class 칼대사02_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 앤대사03(self.ctx)


class 앤대사03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003432, msg='$02000065_BF__MAIN__6$', duration=3000)
        self.set_npc_emotion_loop(spawnId=111, sequenceName='Talk_A', duration=2000)
        self.set_skip(state=앤대사03_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6713):
            return 칼대사03(self.ctx)


class 앤대사03_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 칼대사03(self.ctx)


class 칼대사03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11000074, msg='$02000065_BF__MAIN__7$', duration=4000)
        self.set_skip(state=칼대사03_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9769):
            return 앤대사04(self.ctx)


class 칼대사03_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 앤대사04(self.ctx)


class 앤대사04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003432, msg='$02000065_BF__MAIN__8$', duration=3000)
        self.set_npc_emotion_loop(spawnId=111, sequenceName='Talk_A', duration=2000)
        self.set_skip(state=앤대사04_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 칼대사04(self.ctx)


class 앤대사04_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 칼대사04(self.ctx)


class 칼대사04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11000074, msg='$02000065_BF__MAIN__9$', duration=3000)
        self.set_skip(state=칼대사04_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7471):
            return 앤대사05(self.ctx)


class 칼대사04_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 앤대사05(self.ctx)


class 앤대사05(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.set_conversation(type=2, spawnId=11003432, script='$02000065_BF__MAIN__10$', arg4=3, arg5=0)
        self.set_npc_emotion_loop(spawnId=111, sequenceName='Talk_A', duration=2000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3160):
            return 카메라아웃(self.ctx)


class 카메라아웃(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8000,8001], returnView=False)
        self.visible_my_pc(isVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출종료(self.ctx)


class 칼과앤_스킵완료(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.visible_my_pc(isVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 연출종료(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=3)
        self.set_achievement(triggerId=9000, type='trigger', achieve='meetingAnn')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
