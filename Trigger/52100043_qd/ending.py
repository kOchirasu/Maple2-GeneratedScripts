""" trigger/52100043_qd/ending.xml """
import common


class Ending_Ready(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[720]):
            return Ending_Camera_1(self.ctx)


class Ending_Camera_1(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=500, enable=False)
        self.select_camera_path(pathIds=[500,501], returnView=False)
        self.set_effect(triggerIds=[5000], visible=False)
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_effect(triggerIds=[5005], visible=False)
        self.set_mesh(triggerIds=[4993], visible=False)
        self.set_mesh(triggerIds=[4994], visible=False)
        self.set_mesh(triggerIds=[4995], visible=False)
        self.set_mesh(triggerIds=[4996], visible=False)
        self.set_mesh(triggerIds=[4997], visible=False)
        self.set_mesh(triggerIds=[4998], visible=False)
        self.set_mesh(triggerIds=[4999], visible=False)
        self.visible_my_pc(isVisible=False) # 유저 투명 처리
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.create_monster(spawnIds=[600,601,602], animationEffect=False)
        self.set_mesh(triggerIds=[4993], visible=True)
        self.set_mesh(triggerIds=[4994], visible=True)
        self.set_mesh(triggerIds=[4995], visible=True)
        self.set_mesh(triggerIds=[4996], visible=True)
        self.set_mesh(triggerIds=[4997], visible=True)
        self.set_mesh(triggerIds=[4998], visible=True)
        self.set_mesh(triggerIds=[4999], visible=True)
        self.visible_my_pc(isVisible=True)
        self.move_npc(spawnId=600, patrolName='MS2PatrolData0')
        self.move_npc(spawnId=601, patrolName='MS2PatrolData1')
        self.move_npc(spawnId=602, patrolName='MS2PatrolData2')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Ending_Talk_1(self.ctx)


class Ending_Talk_1(common.Trigger):
    def on_enter(self):
        self.set_skip(state=narration01)
        self.select_camera(triggerId=1000, enable=True)
        self.set_npc_emotion_sequence(spawnId=602, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11001566, illustId='11001566', msg='$52100043_QD__ENDING__0$', duration=3000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Ending_Talk_2(self.ctx)


class Ending_Talk_2(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=1001, enable=True)
        self.set_npc_emotion_sequence(spawnId=601, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11001567, illustId='11001567', msg='$52100043_QD__ENDING__1$', duration=3000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Ending_Talk_3(self.ctx)


class Ending_Talk_3(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=1002, enable=True)
        self.set_npc_emotion_sequence(spawnId=600, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11001568, illustId='11001568', msg='$52100043_QD__ENDING__2$', duration=5000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Shake_Camera(self.ctx)


class Shake_Camera(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True)
        self.select_camera_path(pathIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4006,4007,4008,4006,4007,4005,4006,4007,4008,4006,4007,4008,4006,4007,4008,4006,4007,4008,4008,4006,4007,4008,4006,4007,4008,4006,4007,4008], returnView=True)
        self.add_cinematic_talk(npcId=11001567, illustId='11001567', msg='$52100043_QD__ENDING__3$', duration=2000, align='left')
        self.destroy_monster(spawnIds=[601,602], arg2=False)
        self.create_monster(spawnIds=[701,702], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Ending_Talk_4(self.ctx)


class Ending_Talk_4(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[701,702], arg2=False)
        self.destroy_monster(spawnIds=[601,602])
        self.set_effect(triggerIds=[5000], visible=True)
        self.set_effect(triggerIds=[5003], visible=True)
        self.set_effect(triggerIds=[5004], visible=True)
        self.set_effect(triggerIds=[5005], visible=True)
        self.add_cinematic_talk(npcId=11001566, illustId='11001566', msg='$52100043_QD__ENDING__4$', duration=2000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Ending_Talk_5(self.ctx)


class Ending_Talk_5(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[7000,7001], returnView=False)
        self.set_effect(triggerIds=[5001], visible=True)
        self.add_cinematic_talk(npcId=11001568, illustId='11001568', msg='$52100043_QD__ENDING__5$', duration=2000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return del6000(self.ctx)


class del6000(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_blackfast.xml')
        self.destroy_monster(spawnIds=[600])
        self.create_monster(spawnIds=[700], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return Ending_Talk_6(self.ctx)


class Ending_Talk_6(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_blackfast.xml')
        self.select_camera(triggerId=6000, enable=True)
        self.move_npc(spawnId=700, patrolName='MS2PatrolData4')
        self.add_cinematic_talk(npcId=11001568, illustId='11001568', msg='$52100043_QD__ENDING__6$', duration=3000, align='left')
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.set_time_scale(enable=True, startScale=0.8, endScale=0.03, duration=3, interpolator=1)
        self.set_effect(triggerIds=[5002], visible=True)
        self.set_effect(triggerIds=[5006], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Ending_Talk_7(self.ctx)


class Ending_Talk_7(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True)
        self.select_camera_path(pathIds=[3000,3001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return narration01(self.ctx)


class narration01(common.Trigger):
    def on_enter(self):
        self.set_skip()
        self.destroy_monster(spawnIds=[-1])
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.set_cinematic_ui(type=9, script='$52100043_QD__ENDING__7$')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return narration02(self.ctx)


class narration02(common.Trigger):
    def on_enter(self):
        self.set_skip(state=Map_Warf)
        self.set_cinematic_ui(type=9, script='$52100043_QD__ENDING__8$')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return narration03(self.ctx)


class narration03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52100043_QD__ENDING__9$')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return narration04(self.ctx)


class narration04(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52100043_QD__ENDING__10$')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return narration05(self.ctx)


class narration05(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52100043_QD__ENDING__11$')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return narration06(self.ctx)


class narration06(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52100043_QD__ENDING__12$')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Map_Warf(self.ctx)


class Map_Warf(common.Trigger):
    def on_enter(self):
        self.set_skip()
        self.destroy_monster(spawnIds=[-1])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.move_user(mapId=52010068, portalId=1)


initial_state = Ending_Ready
