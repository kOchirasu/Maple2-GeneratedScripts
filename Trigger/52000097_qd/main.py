""" trigger/52000097_qd/main.xml """
import common


class main(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000097, portalId=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.create_monster(spawnIds=[101,102,201], animationEffect=False) # 배우 등장

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return ready(self.ctx)


class ready(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return start(self.ctx)


class start(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[8001,8002], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_01(self.ctx)


class scene_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_02(self.ctx)


class scene_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003,8004], returnView=False)
        self.set_conversation(type=2, spawnId=11003084, script='$52000097_QD__MAIN__0$', arg4=5)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_03(self.ctx)


class scene_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8006], returnView=False)
        self.set_conversation(type=2, spawnId=11003085, script='$52000097_QD__MAIN__1$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_04(self.ctx)


class scene_04(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003086, script='$52000097_QD__MAIN__2$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_05(self.ctx)


class scene_05(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003086, script='$52000097_QD__MAIN__3$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_06(self.ctx)


class scene_06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8007], returnView=False)
        self.set_pc_emotion_sequence(sequenceNames=['Talk_A'])
        self.set_conversation(type=1, spawnId=0, script='$52000097_QD__MAIN__4$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=0, script='$52000097_QD__MAIN__5$', arg4=3, arg5=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_07(self.ctx)


class scene_07(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8008], returnView=False)
        self.set_conversation(type=2, spawnId=11003086, script='$52000097_QD__MAIN__6$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_08(self.ctx)


class scene_08(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003086, script='$52000097_QD__MAIN__7$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_09(self.ctx)


class scene_09(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000097_QD__MAIN__8$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_10(self.ctx)


class scene_10(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003086, script='$52000097_QD__MAIN__9$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return scene_11(self.ctx)


class scene_11(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Attack_01_E')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_12_ready(self.ctx)


class scene_12_ready(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8009], returnView=False)
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Failure_Idle_A'])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_12(self.ctx)


class scene_12(common.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='ProphecyofFall.swf', movieId=1)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return scene_13(self.ctx)

    def on_exit(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')


class scene_13(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2002')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2001')
        self.set_conversation(type=1, spawnId=102, script='$52000097_QD__MAIN__10$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=101, script='$52000097_QD__MAIN__11$', arg4=2, arg5=0)
        self.select_camera_path(pathIds=[8008], returnView=False)
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Failure_Idle_A'])
        self.set_conversation(type=2, spawnId=11003086, script='$52000097_QD__MAIN__12$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_14(self.ctx)


class scene_14(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8010], returnView=False)
        self.set_conversation(type=1, spawnId=0, script='$52000097_QD__MAIN__13$', arg4=3, arg5=1)
        self.move_user_path(patrolName='MS2PatrolData_2003')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2004')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_15(self.ctx)


class scene_15(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Talk_A'])
        self.set_conversation(type=1, spawnId=0, script='$52000097_QD__MAIN__14$', arg4=4, arg5=0)
        self.set_conversation(type=1, spawnId=0, script='$52000097_QD__MAIN__15$', arg4=4, arg5=4)
        self.set_conversation(type=1, spawnId=0, script='$52000097_QD__MAIN__16$', arg4=4, arg5=8)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=12000):
            return scene_16(self.ctx)


class scene_16(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003086, script='$52000097_QD__MAIN__17$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_17(self.ctx)


class scene_17(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003086, script='$52000097_QD__MAIN__18$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_18(self.ctx)


class scene_18(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003086, script='$52000097_QD__MAIN__19$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_19(self.ctx)


class scene_19(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2005')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_20(self.ctx)


class scene_20(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8011], returnView=False)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2006')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2007')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_21(self.ctx)


class scene_21(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[201])
        self.set_conversation(type=2, spawnId=11003085, script='$52000097_QD__MAIN__20$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_22(self.ctx)


class scene_22(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003084, script='$52000097_QD__MAIN__21$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_23(self.ctx)


class scene_23(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2008')
        self.move_user_path(patrolName='MS2PatrolData_2009')
        self.set_conversation(type=2, spawnId=11003084, script='$52000097_QD__MAIN__22$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_24(self.ctx)


class scene_24(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003085, script='$52000097_QD__MAIN__23$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_25(self.ctx)


class scene_25(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000097_QD__MAIN__24$', arg4=4, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_26(self.ctx)


class scene_26(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        # <action name="업적이벤트를발생시킨다" arg1="701" arg2="trigger" arg3="meetalbanos"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return end(self.ctx)


class end(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000068, portalId=1)


initial_state = main
