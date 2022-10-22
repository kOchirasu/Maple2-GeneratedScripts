""" trigger/52000097_qd/main.xml """
from common import *
import state


class main(state.State):
    def on_enter(self):
        move_user(mapId=52000097, portalId=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[101,102,201], arg2=False) # 배우 등장

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return start()


class start(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[8001,8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scene_01()


class scene_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003,8004], returnView=False)
        set_conversation(type=2, spawnId=11003084, script='$52000097_QD__MAIN__0$', arg4=5)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8006], returnView=False)
        set_conversation(type=2, spawnId=11003085, script='$52000097_QD__MAIN__1$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003086, script='$52000097_QD__MAIN__2$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_05()


class scene_05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003086, script='$52000097_QD__MAIN__3$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_06()


class scene_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8007], returnView=False)
        set_pc_emotion_sequence(sequenceNames=['Talk_A'])
        set_conversation(type=1, spawnId=0, script='$52000097_QD__MAIN__4$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=0, script='$52000097_QD__MAIN__5$', arg4=3, arg5=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scene_07()


class scene_07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8008], returnView=False)
        set_conversation(type=2, spawnId=11003086, script='$52000097_QD__MAIN__6$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scene_08()


class scene_08(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003086, script='$52000097_QD__MAIN__7$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scene_09()


class scene_09(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000097_QD__MAIN__8$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_10()


class scene_10(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003086, script='$52000097_QD__MAIN__9$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return scene_11()


class scene_11(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Attack_01_E')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_12_ready()


class scene_12_ready(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8009], returnView=False)
        set_pc_emotion_sequence(sequenceNames=['Emotion_Failure_Idle_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_12()


class scene_12(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='ProphecyofFall.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return scene_13()

    def on_exit(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')


class scene_13(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2002')
        move_npc(spawnId=102, patrolName='MS2PatrolData_2001')
        set_conversation(type=1, spawnId=102, script='$52000097_QD__MAIN__10$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=101, script='$52000097_QD__MAIN__11$', arg4=2, arg5=0)
        select_camera_path(pathIds=[8008], returnView=False)
        set_pc_emotion_sequence(sequenceNames=['Emotion_Failure_Idle_A'])
        set_conversation(type=2, spawnId=11003086, script='$52000097_QD__MAIN__12$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scene_14()


class scene_14(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8010], returnView=False)
        set_conversation(type=1, spawnId=0, script='$52000097_QD__MAIN__13$', arg4=3, arg5=1)
        move_user_path(patrolName='MS2PatrolData_2003')
        move_npc(spawnId=201, patrolName='MS2PatrolData_2004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_15()


class scene_15(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Talk_A'])
        set_conversation(type=1, spawnId=0, script='$52000097_QD__MAIN__14$', arg4=4, arg5=0)
        set_conversation(type=1, spawnId=0, script='$52000097_QD__MAIN__15$', arg4=4, arg5=4)
        set_conversation(type=1, spawnId=0, script='$52000097_QD__MAIN__16$', arg4=4, arg5=8)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return scene_16()


class scene_16(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003086, script='$52000097_QD__MAIN__17$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_17()


class scene_17(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003086, script='$52000097_QD__MAIN__18$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_18()


class scene_18(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003086, script='$52000097_QD__MAIN__19$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_19()


class scene_19(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_2005')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_20()


class scene_20(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8011], returnView=False)
        move_npc(spawnId=102, patrolName='MS2PatrolData_2006')
        move_npc(spawnId=101, patrolName='MS2PatrolData_2007')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_21()


class scene_21(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201])
        set_conversation(type=2, spawnId=11003085, script='$52000097_QD__MAIN__20$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scene_22()


class scene_22(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003084, script='$52000097_QD__MAIN__21$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scene_23()


class scene_23(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2008')
        move_user_path(patrolName='MS2PatrolData_2009')
        set_conversation(type=2, spawnId=11003084, script='$52000097_QD__MAIN__22$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scene_24()


class scene_24(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003085, script='$52000097_QD__MAIN__23$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scene_25()


class scene_25(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000097_QD__MAIN__24$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scene_26()


class scene_26(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        # <action name="업적이벤트를발생시킨다" arg1="701" arg2="trigger" arg3="meetalbanos"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return end()


class end(state.State):
    def on_enter(self):
        move_user(mapId=2000068, portalId=1)


