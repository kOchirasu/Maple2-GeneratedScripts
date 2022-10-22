""" trigger/52000040_qd/main.xml """
from common import *
import state


class ready(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[1]):
            hide_guide_summary(entityId=20020020)
            return ready_02()
        if quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[2]):
            return start_22()
        if quest_user_detected(boxIds=[701], questIds=[50001445], questStates=[3]):
            return end_01()
        if quest_user_detected(boxIds=[701], questIds=[50001445], questStates=[2]):
            return sb_ready_b_13()
        if quest_user_detected(boxIds=[701], questIds=[50001445], questStates=[1]):
            return sb_ready_b_12()
        if quest_user_detected(boxIds=[701], questIds=[50001444], questStates=[3]):
            return sb_ready_b_12()
        if quest_user_detected(boxIds=[701], questIds=[50001444], questStates=[2]):
            set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
            hide_guide_summary(entityId=20020020)
            return sb_ready_b_02()
        if quest_user_detected(boxIds=[701], questIds=[50001443], questStates=[3]):
            add_buff(boxIds=[701], skillId=70000096, level=1)
            set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
            hide_guide_summary(entityId=20020020)
            return sb_ready_04()
        if quest_user_detected(boxIds=[701], questIds=[50001442], questStates=[3]):
            return sb_ready_01()
        if quest_user_detected(boxIds=[701], questIds=[50001442], questStates=[2]):
            return sb_ready_01()


class sb_ready_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[145], arg2=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[50001443], questStates=[2]):
            add_buff(boxIds=[701], skillId=70000096, level=1)
            set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
            hide_guide_summary(entityId=20020020)
            return sb_ready_02()


class sb_ready_02(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='Cut_BeyondLink_CCTV.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return sb_ready_03()


class sb_ready_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[144], arg2=True)
        create_monster(spawnIds=[145], arg2=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[50001443], questStates=[3]):
            return sb_ready_04()


class sb_ready_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True)
        show_guide_summary(entityId=40010, textId=40010) # 모든 몬스터를  처치하세요

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201]):
            add_buff(boxIds=[701], skillId=70000094, level=1)
            hide_guide_summary(entityId=40010)
            return sb_ready_05()


class sb_ready_05(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return sb_ready_06()


class sb_ready_06(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Push_A', duration=5000)
        add_buff(boxIds=[701], skillId=70000095, level=1) # 현기증 2단계 버프

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return sb_ready_07()


class sb_ready_07(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            add_buff(boxIds=[701], skillId=70000096, level=1)
            return sb_ready_08()


class sb_ready_08(state.State):
    def on_enter(self):
        move_user(mapId=52000017, portalId=1)


#  이도 공간에서 돌아온 소울 바인더 
class sb_ready_b_02(state.State):
    def on_enter(self):
        move_user(mapId=52000040, portalId=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return sb_ready_b_03()


class sb_ready_b_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[221,222,223], arg2=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[7001,7002,7003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return sb_ready_b_04()


class sb_ready_b_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[7100], returnView=False)
        move_npc(spawnId=221, patrolName='MS2PatrolData_2101')
        move_npc(spawnId=222, patrolName='MS2PatrolData_2102')
        move_npc(spawnId=223, patrolName='MS2PatrolData_2103')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return sb_ready_b_06()


class sb_ready_b_06(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001726, script='$52000040_QD__MAIN__26$', arg4=4)
        set_skip(state=sb_ready_b_07_skip)
        set_npc_emotion_loop(spawnId=221, sequenceName='Talk_A', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return sb_ready_b_07_skip()


class sb_ready_b_07_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return sb_ready_b_07()


class sb_ready_b_07(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001728, script='$52000040_QD__MAIN__27$', arg4=4)
        set_skip(state=sb_ready_b_08_skip)
        set_npc_emotion_loop(spawnId=222, sequenceName='Talk_A', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return sb_ready_b_08_skip()


class sb_ready_b_08_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return sb_ready_b_08()


class sb_ready_b_08(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001726, script='$52000040_QD__MAIN__28$', arg4=4)
        set_skip(state=sb_ready_b_09_skip)
        set_npc_emotion_loop(spawnId=221, sequenceName='Talk_A', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return sb_ready_b_09_skip()


class sb_ready_b_09_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return sb_ready_b_09()


class sb_ready_b_09(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001724, script='$52000040_QD__MAIN__29$', arg4=4)
        set_skip(state=sb_ready_b_10_skip)
        set_npc_emotion_loop(spawnId=223, sequenceName='Talk_A', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return sb_ready_b_10_skip()


class sb_ready_b_10_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return sb_ready_b_10()


class sb_ready_b_10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[145], arg2=True)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        select_camera_path(pathIds=[7010], returnView=True)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return sb_ready_b_11()


class sb_ready_b_11(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class sb_ready_b_12(state.State):
    def on_enter(self):
        create_monster(spawnIds=[145], arg2=True)
        create_monster(spawnIds=[221,222,223], arg2=True)
        move_npc(spawnId=221, patrolName='MS2PatrolData_2101')
        move_npc(spawnId=222, patrolName='MS2PatrolData_2102')
        move_npc(spawnId=223, patrolName='MS2PatrolData_2103')


class sb_ready_b_13(state.State):
    def on_enter(self):
        create_monster(spawnIds=[145], arg2=True)


class sb_end(state.State):
    pass


class ready_02(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2001')
        create_monster(spawnIds=[101,102], arg2=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[7001,7002,7003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ready_03()


class ready_03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001545, script='$52000040_QD__MAIN__0$', arg4=5)
        set_skip(state=ready_04_skip)
        set_npc_emotion_loop(spawnId=102, sequenceName='Idle_A', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ready_04()


class ready_04_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return ready_04()


class ready_04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001545, script='$52000040_QD__MAIN__1$', arg4=5)
        set_skip(state=ready_05_skip)
        set_npc_emotion_loop(spawnId=102, sequenceName='Idle_A', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ready_05()


class ready_05_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return ready_05()


class ready_05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001545, script='$52000040_QD__MAIN__2$', arg4=5)
        set_npc_emotion_loop(spawnId=102, sequenceName='Idle_A', duration=5000)
        set_skip(state=ready_06_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ready_06()


class ready_06_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return ready_06()


class ready_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[7004], returnView=False)
        set_conversation(type=2, spawnId=11001546, script='$52000040_QD__MAIN__3$', arg4=5)
        set_skip(state=ready_07_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ready_07()


class ready_07_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return ready_07()


class ready_07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[7004], returnView=False)
        set_conversation(type=2, spawnId=11001545, script='$52000040_QD__MAIN__4$', arg4=5)
        set_skip(state=ready_08_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ready_08()


class ready_08_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return ready_08()


class ready_08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[7004], returnView=False)
        set_conversation(type=2, spawnId=11001546, script='$52000040_QD__MAIN__5$', arg4=5)
        set_skip(state=ready_09_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ready_09()


class ready_09_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return ready_09()


class ready_09(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[7004], returnView=False)
        set_conversation(type=2, spawnId=11001545, script='$52000040_QD__MAIN__6$', arg4=5)
        set_skip(state=ready_10_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ready_10()


class ready_10_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return ready_10()


class ready_10(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='Cut_BeyondLink_CCTV.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return start_01()


class start_01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__7$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_01_ready()


class start_01_ready(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2004')
        move_npc(spawnId=101, patrolName='MS2PatrolData_2003')
        move_npc(spawnId=102, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return start_02()


class start_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[7005], returnView=False)
        create_monster(spawnIds=[103], arg2=True)
        set_conversation(type=2, spawnId=11001545, script='$52000040_QD__MAIN__8$', arg4=5)
        set_skip(state=start_02_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_03()


class start_02_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return start_03()


class start_03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001546, script='$52000040_QD__MAIN__9$', arg4=5)
        set_skip(state=start_03_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_04()


class start_03_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return start_04()


class start_04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001545, script='$52000040_QD__MAIN__10$', arg4=4)
        set_skip(state=start_04_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_05()


class start_04_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return start_05()


class start_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[7006,7007], returnView=False)
        set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__11$', arg4=5)
        set_skip(state=start_05_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_06()


class start_05_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return start_06()


class start_06(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__12$', arg4=4)
        set_skip(state=start_06_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_07()


class start_06_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return start_07()


class start_07(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001546, script='$52000040_QD__MAIN__13$', arg4=5)
        set_skip(state=start_07_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_08()


class start_07_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return start_08()


class start_08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[7008], returnView=False)
        set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__14$', arg4=5)
        set_skip(state=start_08_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_09()


class start_08_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return start_09()


class start_09(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001545, script='$52000040_QD__MAIN__15$', arg4=3)
        set_skip(state=start_09_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_10()


class start_09_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return start_10()


class start_10(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001545, script='$52000040_QD__MAIN__16$', arg4=5)
        set_skip(state=start_10_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_11()


class start_10_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return start_11()


class start_11(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__17$', arg4=4)
        set_skip(state=start_11_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_12()


class start_11_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return start_12()


class start_12(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001546, script='$52000040_QD__MAIN__18$', arg4=3)
        set_skip(state=start_12_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_13()


class start_12_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return start_13()


class start_13(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__19$', arg4=5)
        set_skip(state=start_13_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_14()


class start_13_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return start_14()


class start_14(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__20$', arg4=5)
        set_skip(state=start_14_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_15()


class start_14_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return start_15()


class start_15(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__21$', arg4=5)
        set_skip(state=start_15_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_16()


class start_15_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return start_16()


class start_16(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__22$', arg4=5)
        set_skip(state=start_16_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_17()


class start_16_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return start_17()


class start_17(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001546, script='$52000040_QD__MAIN__23$', arg4=3)
        # Missing State: start_17_skip
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_18()


class start_18(state.State):
    def on_enter(self):
        move_npc(spawnId=103, patrolName='MS2PatrolData_2005')
        select_camera_path(pathIds=[7009], returnView=False)
        set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__24$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_19()


class start_19(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__25$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            destroy_monster(spawnIds=[103,102,101])
            return start_20()


class start_20(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[7010], returnView=True)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_cinematic_ui(type=0)
            create_monster(spawnIds=[104,111,112], arg2=True)
            set_cinematic_ui(type=2)
            return start_21()


class start_21(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20020020, textId=20020020)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[2]):
            hide_guide_summary(entityId=20020020)
            return end_01()


class start_22(state.State):
    def on_enter(self):
        create_monster(spawnIds=[104,111,112], arg2=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[2]):
            hide_guide_summary(entityId=20020020)
            return end_01()


class end_01(state.State):
    pass


