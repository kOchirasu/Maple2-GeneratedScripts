""" trigger/52000040_qd/main.xml """
import trigger_api


class ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[1]):
            self.hide_guide_summary(entityId=20020020)
            return ready_02(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[2]):
            return start_22(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[50001445], questStates=[3]):
            return end_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[50001445], questStates=[2]):
            return sb_ready_b_13(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[50001445], questStates=[1]):
            return sb_ready_b_12(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[50001444], questStates=[3]):
            return sb_ready_b_12(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[50001444], questStates=[2]):
            self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
            self.hide_guide_summary(entityId=20020020)
            return sb_ready_b_02(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[50001443], questStates=[3]):
            self.add_buff(boxIds=[701], skillId=70000096, level=1)
            self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
            self.hide_guide_summary(entityId=20020020)
            return sb_ready_04(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[50001442], questStates=[3]):
            return sb_ready_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[50001442], questStates=[2]):
            return sb_ready_01(self.ctx)


class sb_ready_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[145], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[50001443], questStates=[2]):
            self.add_buff(boxIds=[701], skillId=70000096, level=1)
            self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
            self.hide_guide_summary(entityId=20020020)
            return sb_ready_02(self.ctx)


class sb_ready_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='Cut_BeyondLink_CCTV.swf', movieId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return sb_ready_03(self.ctx)


class sb_ready_03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[144], animationEffect=True)
        self.create_monster(spawnIds=[145], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[50001443], questStates=[3]):
            return sb_ready_04(self.ctx)


class sb_ready_04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=True)
        self.show_guide_summary(entityId=40010, textId=40010) # 모든 몬스터를  처치하세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201]):
            self.add_buff(boxIds=[701], skillId=70000094, level=1)
            self.hide_guide_summary(entityId=40010)
            return sb_ready_05(self.ctx)


class sb_ready_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return sb_ready_06(self.ctx)


class sb_ready_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Push_A', duration=5000)
        self.add_buff(boxIds=[701], skillId=70000095, level=1) # 현기증 2단계 버프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return sb_ready_07(self.ctx)


class sb_ready_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.add_buff(boxIds=[701], skillId=70000096, level=1)
            return sb_ready_08(self.ctx)


class sb_ready_08(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000017, portalId=1)


# 이도 공간에서 돌아온 소울 바인더
class sb_ready_b_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000040, portalId=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return sb_ready_b_03(self.ctx)


class sb_ready_b_03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[221,222,223], animationEffect=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[7001,7002,7003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=11000):
            return sb_ready_b_04(self.ctx)


class sb_ready_b_04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[7100], returnView=False)
        self.move_npc(spawnId=221, patrolName='MS2PatrolData_2101')
        self.move_npc(spawnId=222, patrolName='MS2PatrolData_2102')
        self.move_npc(spawnId=223, patrolName='MS2PatrolData_2103')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return sb_ready_b_06(self.ctx)


class sb_ready_b_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001726, script='$52000040_QD__MAIN__26$', arg4=4)
        self.set_skip(state=sb_ready_b_07_skip)
        self.set_npc_emotion_loop(spawnId=221, sequenceName='Talk_A', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return sb_ready_b_07_skip(self.ctx)


class sb_ready_b_07_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return sb_ready_b_07(self.ctx)


class sb_ready_b_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001728, script='$52000040_QD__MAIN__27$', arg4=4)
        self.set_skip(state=sb_ready_b_08_skip)
        self.set_npc_emotion_loop(spawnId=222, sequenceName='Talk_A', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return sb_ready_b_08_skip(self.ctx)


class sb_ready_b_08_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return sb_ready_b_08(self.ctx)


class sb_ready_b_08(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001726, script='$52000040_QD__MAIN__28$', arg4=4)
        self.set_skip(state=sb_ready_b_09_skip)
        self.set_npc_emotion_loop(spawnId=221, sequenceName='Talk_A', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return sb_ready_b_09_skip(self.ctx)


class sb_ready_b_09_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return sb_ready_b_09(self.ctx)


class sb_ready_b_09(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001724, script='$52000040_QD__MAIN__29$', arg4=4)
        self.set_skip(state=sb_ready_b_10_skip)
        self.set_npc_emotion_loop(spawnId=223, sequenceName='Talk_A', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return sb_ready_b_10_skip(self.ctx)


class sb_ready_b_10_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return sb_ready_b_10(self.ctx)


class sb_ready_b_10(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[145], animationEffect=True)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.select_camera_path(pathIds=[7010], returnView=True)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return sb_ready_b_11(self.ctx)


class sb_ready_b_11(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class sb_ready_b_12(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[145], animationEffect=True)
        self.create_monster(spawnIds=[221,222,223], animationEffect=True)
        self.move_npc(spawnId=221, patrolName='MS2PatrolData_2101')
        self.move_npc(spawnId=222, patrolName='MS2PatrolData_2102')
        self.move_npc(spawnId=223, patrolName='MS2PatrolData_2103')


class sb_ready_b_13(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[145], animationEffect=True)


class sb_end(trigger_api.Trigger):
    pass


class ready_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2001')
        self.create_monster(spawnIds=[101,102], animationEffect=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[7001,7002,7003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ready_03(self.ctx)


class ready_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001545, script='$52000040_QD__MAIN__0$', arg4=5)
        self.set_skip(state=ready_04_skip)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Idle_A', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ready_04(self.ctx)


class ready_04_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ready_04(self.ctx)


class ready_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001545, script='$52000040_QD__MAIN__1$', arg4=5)
        self.set_skip(state=ready_05_skip)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Idle_A', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ready_05(self.ctx)


class ready_05_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ready_05(self.ctx)


class ready_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001545, script='$52000040_QD__MAIN__2$', arg4=5)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Idle_A', duration=5000)
        self.set_skip(state=ready_06_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ready_06(self.ctx)


class ready_06_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ready_06(self.ctx)


class ready_06(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[7004], returnView=False)
        self.set_conversation(type=2, spawnId=11001546, script='$52000040_QD__MAIN__3$', arg4=5)
        self.set_skip(state=ready_07_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ready_07(self.ctx)


class ready_07_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ready_07(self.ctx)


class ready_07(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[7004], returnView=False)
        self.set_conversation(type=2, spawnId=11001545, script='$52000040_QD__MAIN__4$', arg4=5)
        self.set_skip(state=ready_08_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ready_08(self.ctx)


class ready_08_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ready_08(self.ctx)


class ready_08(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[7004], returnView=False)
        self.set_conversation(type=2, spawnId=11001546, script='$52000040_QD__MAIN__5$', arg4=5)
        self.set_skip(state=ready_09_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ready_09(self.ctx)


class ready_09_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ready_09(self.ctx)


class ready_09(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[7004], returnView=False)
        self.set_conversation(type=2, spawnId=11001545, script='$52000040_QD__MAIN__6$', arg4=5)
        self.set_skip(state=ready_10_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ready_10(self.ctx)


class ready_10_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ready_10(self.ctx)


class ready_10(trigger_api.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='Cut_BeyondLink_CCTV.swf', movieId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return start_01(self.ctx)


class start_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__7$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_01_ready(self.ctx)


class start_01_ready(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2004')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2003')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[7005], returnView=False)
        self.create_monster(spawnIds=[103], animationEffect=True)
        self.set_conversation(type=2, spawnId=11001545, script='$52000040_QD__MAIN__8$', arg4=5)
        self.set_skip(state=start_02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_03(self.ctx)


class start_02_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001546, script='$52000040_QD__MAIN__9$', arg4=5)
        self.set_skip(state=start_03_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_04(self.ctx)


class start_03_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return start_04(self.ctx)


class start_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001545, script='$52000040_QD__MAIN__10$', arg4=4)
        self.set_skip(state=start_04_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_05(self.ctx)


class start_04_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return start_05(self.ctx)


class start_05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[7006,7007], returnView=False)
        self.set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__11$', arg4=5)
        self.set_skip(state=start_05_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_06(self.ctx)


class start_05_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return start_06(self.ctx)


class start_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__12$', arg4=4)
        self.set_skip(state=start_06_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_07(self.ctx)


class start_06_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return start_07(self.ctx)


class start_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001546, script='$52000040_QD__MAIN__13$', arg4=5)
        self.set_skip(state=start_07_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_08(self.ctx)


class start_07_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return start_08(self.ctx)


class start_08(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[7008], returnView=False)
        self.set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__14$', arg4=5)
        self.set_skip(state=start_08_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_09(self.ctx)


class start_08_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return start_09(self.ctx)


class start_09(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001545, script='$52000040_QD__MAIN__15$', arg4=3)
        self.set_skip(state=start_09_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_10(self.ctx)


class start_09_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return start_10(self.ctx)


class start_10(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001545, script='$52000040_QD__MAIN__16$', arg4=5)
        self.set_skip(state=start_10_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_11(self.ctx)


class start_10_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return start_11(self.ctx)


class start_11(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__17$', arg4=4)
        self.set_skip(state=start_11_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_12(self.ctx)


class start_11_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return start_12(self.ctx)


class start_12(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001546, script='$52000040_QD__MAIN__18$', arg4=3)
        self.set_skip(state=start_12_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_13(self.ctx)


class start_12_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return start_13(self.ctx)


class start_13(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__19$', arg4=5)
        self.set_skip(state=start_13_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_14(self.ctx)


class start_13_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return start_14(self.ctx)


class start_14(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__20$', arg4=5)
        self.set_skip(state=start_14_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_15(self.ctx)


class start_14_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return start_15(self.ctx)


class start_15(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__21$', arg4=5)
        self.set_skip(state=start_15_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_16(self.ctx)


class start_15_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return start_16(self.ctx)


class start_16(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__22$', arg4=5)
        self.set_skip(state=start_16_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_17(self.ctx)


class start_16_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return start_17(self.ctx)


class start_17(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001546, script='$52000040_QD__MAIN__23$', arg4=3)
        # Missing State: start_17_skip
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_18(self.ctx)


class start_18(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_2005')
        self.select_camera_path(pathIds=[7009], returnView=False)
        self.set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__24$', arg4=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_19(self.ctx)


class start_19(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001548, script='$52000040_QD__MAIN__25$', arg4=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            self.destroy_monster(spawnIds=[103,102,101])
            return start_20(self.ctx)


class start_20(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[7010], returnView=True)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_cinematic_ui(type=0)
            self.create_monster(spawnIds=[104,111,112], animationEffect=True)
            self.set_cinematic_ui(type=2)
            return start_21(self.ctx)


class start_21(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20020020, textId=20020020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[2]):
            self.hide_guide_summary(entityId=20020020)
            return end_01(self.ctx)


class start_22(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[104,111,112], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[2]):
            self.hide_guide_summary(entityId=20020020)
            return end_01(self.ctx)


class end_01(trigger_api.Trigger):
    pass


initial_state = ready
