""" trigger/52010011_qd/act01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True)
        set_effect(triggerIds=[5000], visible=False) # 이펙트

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 유저감지()


class 유저감지(state.State):
    def on_enter(self):
        set_timer(timerId='30', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            return 퀘스트시작()


class 퀘스트시작(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[10002811], questStates=[2]):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 진행()


class 진행(state.State):
    def on_enter(self):
        move_user(mapId=52010011, portalId=2, boxId=0)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대사_01_테모로()


class 대사_01_테모로(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__0$', arg4=5)
        set_skip(state=대사_01_테모로skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대사_01_테모로skip()


class 대사_01_테모로skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 대사_02_테모로()


class 대사_02_테모로(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__1$', arg4=5)
        set_skip(state=대사_02_테모로skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대사_02_테모로skip()


class 대사_02_테모로skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 대사_03_PC()


class 대사_03_PC(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52010011_QD__ACT01__2$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 대사_04_테모로()


class 대사_04_테모로(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__3$', arg4=5)
        set_skip(state=대사_04_테모로skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대사_04_테모로skip()


class 대사_04_테모로skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 대사_05_테모로()


class 대사_05_테모로(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__4$', arg4=5)
        set_skip(state=대사_05_테모로skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대사_05_테모로skip()


class 대사_05_테모로skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 대사_06_PC()


class 대사_06_PC(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52010011_QD__ACT01__5$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 대사_07_테모로()


class 대사_07_테모로(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__6$', arg4=5)
        set_skip(state=대사_07_테모로skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대사_07_테모로skip()


class 대사_07_테모로skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 대사_08_테모로()


class 대사_08_테모로(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__7$', arg4=5)
        set_skip(state=대사_08_테모로skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대사_08_테모로skip()


class 대사_08_테모로skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 대사_09_PC()


class 대사_09_PC(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52010011_QD__ACT01__8$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 대사_10_테모로()


class 대사_10_테모로(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__9$', arg4=5)
        set_skip(state=대사_10_테모로skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대사_10_테모로skip()


class 대사_10_테모로skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 대사_11_테모로()


class 대사_11_테모로(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__10$', arg4=5)
        set_skip(state=대사_11_테모로skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대사_11_테모로skip()


class 대사_11_테모로skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 대사_12_PC()


class 대사_12_PC(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52010011_QD__ACT01__11$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대사_13_테모로()


class 대사_13_테모로(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__12$', arg4=5)
        set_skip(state=대사_13_테모로skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대사_13_테모로skip()


class 대사_13_테모로skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 영상준비()


class 영상준비(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_timer(timerId='21', seconds=2)
        select_camera_path(pathIds=[601,602], returnView=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='21'):
            return 영상재생()


class 영상재생(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='common\KarKarIntro.usm', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 대사_14_PC()
        if wait_tick(waitTick=18000):
            return 대사_14_PC()


class 대사_14_PC(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=1, spawnId=0, script='$52010011_QD__ACT01__13$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대사_15_테모로()


class 대사_15_테모로(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__14$', arg4=5)
        set_skip(state=대사_15_테모로skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대사_15_테모로skip()


class 대사_15_테모로skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 대사_16_테모로()


class 대사_16_테모로(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001314, script='$52010011_QD__ACT01__15$', arg4=5)
        set_skip(state=대사_16_테모로skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대사_16_테모로skip()


class 대사_16_테모로skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        create_monster(spawnIds=[1001], arg2=True)
        set_skip(state=대사_17_덴덴)

    def on_tick(self) -> state.State:
        if true():
            return 대사_17_덴덴()


class 대사_17_덴덴(state.State):
    def on_enter(self):
        move_npc(spawnId=1001, patrolName='MS2PatrolData_2001')
        set_conversation(type=2, spawnId=11001313, script='$52010011_QD__ACT01__16$', arg4=5)
        set_skip(state=대사_17_덴덴skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대사_17_덴덴skip()


class 대사_17_덴덴skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 대사_18_PC()


class 대사_18_PC(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52010011_QD__ACT01__17$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대사_19_덴덴()


class 대사_19_덴덴(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001313, script='$52010011_QD__ACT01__18$', arg4=4)
        set_skip(state=대사_19_덴덴skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 대사_19_덴덴skip()


class 대사_19_덴덴skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 대사_20_PC()


class 대사_20_PC(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52010011_QD__ACT01__19$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 대사_21_덴덴()


class 대사_21_덴덴(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001313, script='$52010011_QD__ACT01__20$', arg4=3)
        set_skip(state=대사_21_덴덴skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대사_21_덴덴skip()


class 대사_21_덴덴skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


