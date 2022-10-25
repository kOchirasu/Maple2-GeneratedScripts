""" trigger/52010011_qd/act01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.set_effect(triggerIds=[5000], visible=False) # 이펙트

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 유저감지(self.ctx)


class 유저감지(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='30', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='30'):
            return 퀘스트시작(self.ctx)


class 퀘스트시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[10002811], questStates=[2]):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 진행(self.ctx)


class 진행(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52010011, portalId=2, boxId=0)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대사_01_테모로(self.ctx)


class 대사_01_테모로(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__0$', arg4=5)
        self.set_skip(state=대사_01_테모로skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대사_01_테모로skip(self.ctx)


class 대사_01_테모로skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대사_02_테모로(self.ctx)


class 대사_02_테모로(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__1$', arg4=5)
        self.set_skip(state=대사_02_테모로skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대사_02_테모로skip(self.ctx)


class 대사_02_테모로skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대사_03_PC(self.ctx)


class 대사_03_PC(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52010011_QD__ACT01__2$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 대사_04_테모로(self.ctx)


class 대사_04_테모로(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__3$', arg4=5)
        self.set_skip(state=대사_04_테모로skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대사_04_테모로skip(self.ctx)


class 대사_04_테모로skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대사_05_테모로(self.ctx)


class 대사_05_테모로(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__4$', arg4=5)
        self.set_skip(state=대사_05_테모로skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대사_05_테모로skip(self.ctx)


class 대사_05_테모로skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대사_06_PC(self.ctx)


class 대사_06_PC(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52010011_QD__ACT01__5$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 대사_07_테모로(self.ctx)


class 대사_07_테모로(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__6$', arg4=5)
        self.set_skip(state=대사_07_테모로skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대사_07_테모로skip(self.ctx)


class 대사_07_테모로skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대사_08_테모로(self.ctx)


class 대사_08_테모로(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__7$', arg4=5)
        self.set_skip(state=대사_08_테모로skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대사_08_테모로skip(self.ctx)


class 대사_08_테모로skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대사_09_PC(self.ctx)


class 대사_09_PC(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52010011_QD__ACT01__8$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 대사_10_테모로(self.ctx)


class 대사_10_테모로(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__9$', arg4=5)
        self.set_skip(state=대사_10_테모로skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대사_10_테모로skip(self.ctx)


class 대사_10_테모로skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대사_11_테모로(self.ctx)


class 대사_11_테모로(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__10$', arg4=5)
        self.set_skip(state=대사_11_테모로skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대사_11_테모로skip(self.ctx)


class 대사_11_테모로skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대사_12_PC(self.ctx)


class 대사_12_PC(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52010011_QD__ACT01__11$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대사_13_테모로(self.ctx)


class 대사_13_테모로(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__12$', arg4=5)
        self.set_skip(state=대사_13_테모로skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대사_13_테모로skip(self.ctx)


class 대사_13_테모로skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 영상준비(self.ctx)


class 영상준비(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_timer(timerId='21', seconds=2)
        self.select_camera_path(pathIds=[601,602], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='21'):
            return 영상재생(self.ctx)


class 영상재생(common.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='common\KarKarIntro.usm', movieId=1)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 대사_14_PC(self.ctx)
        if self.wait_tick(waitTick=18000):
            return 대사_14_PC(self.ctx)


class 대사_14_PC(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=1, spawnId=0, script='$52010011_QD__ACT01__13$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대사_15_테모로(self.ctx)


class 대사_15_테모로(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__14$', arg4=5)
        self.set_skip(state=대사_15_테모로skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대사_15_테모로skip(self.ctx)


class 대사_15_테모로skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대사_16_테모로(self.ctx)


class 대사_16_테모로(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__15$', arg4=5)
        self.set_skip(state=대사_16_테모로skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대사_16_테모로skip(self.ctx)


class 대사_16_테모로skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.create_monster(spawnIds=[1001], animationEffect=True)
        self.set_skip(state=대사_17_덴덴)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대사_17_덴덴(self.ctx)


class 대사_17_덴덴(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_2001')
        self.set_conversation(type=2, spawnId=11001313, script='$52010011_QD__ACT01__16$', arg4=5)
        self.set_skip(state=대사_17_덴덴skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대사_17_덴덴skip(self.ctx)


class 대사_17_덴덴skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대사_18_PC(self.ctx)


class 대사_18_PC(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52010011_QD__ACT01__17$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대사_19_덴덴(self.ctx)


class 대사_19_덴덴(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001313, script='$52010011_QD__ACT01__18$', arg4=4)
        self.set_skip(state=대사_19_덴덴skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 대사_19_덴덴skip(self.ctx)


class 대사_19_덴덴skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대사_20_PC(self.ctx)


class 대사_20_PC(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52010011_QD__ACT01__19$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 대사_21_덴덴(self.ctx)


class 대사_21_덴덴(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001313, script='$52010011_QD__ACT01__20$', arg4=3)
        self.set_skip(state=대사_21_덴덴skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대사_21_덴덴skip(self.ctx)


class 대사_21_덴덴skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 대기
