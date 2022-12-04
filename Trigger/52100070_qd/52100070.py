""" trigger/52100070_qd/52100070.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=400, enable=True)
        self.set_effect(triggerIds=[5000], visible=False)
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_effect(triggerIds=[5005], visible=False)
        self.set_effect(triggerIds=[5006], visible=False)
        self.set_effect(triggerIds=[5007], visible=False)
        self.visible_my_pc(isVisible=False) # 유저 투명 처리
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1000]):
            return narration01(self.ctx)


class narration01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=9, script='$52100070_QD__52100070__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 암전1(self.ctx)


class 암전1(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return Camera_Move_01(self.ctx)


class Camera_Move_01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[400,401], returnView=False)
        self.show_caption(type='VerticalCaption', title='$52100070_QD__52100070__1$', desc='$52100070_QD__52100070__2$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip(state=연출끝)
        self.create_monster(spawnIds=[101,102,103], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 전경카메라1(self.ctx)


class 전경카메라1(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=600, enable=True)
        self.select_camera_path(pathIds=[600,601], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 퐈이야(self.ctx)


class 퐈이야(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_effect(triggerIds=[5002], visible=True)
        self.set_effect(triggerIds=[5004], visible=True)
        self.set_effect(triggerIds=[5007], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 이슈라카메라1(self.ctx)


class 이슈라카메라1(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[402,403], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 이슈라카메라2(self.ctx)


class 이슈라카메라2(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=500, enable=True)
        self.select_camera_path(pathIds=[500,501], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 이슈라카메라3(self.ctx)


class 이슈라카메라3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=404, enable=False)
        self.select_camera_path(pathIds=[404,405], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 이슈라카메라4(self.ctx)


class 이슈라카메라4(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=406, enable=False)
        self.select_camera_path(pathIds=[406,407], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 렌듀비앙이동1(self.ctx)


class 렌듀비앙이동1(trigger_api.Trigger):
    def on_enter(self):
        self.set_time_scale(enable=True, startScale=0.5, endScale=0.5, duration=50, interpolator=1)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_11003867')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 유페리아이동1(self.ctx)


class 유페리아이동1(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_11003868')
        self.set_effect(triggerIds=[5000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 이슈라이동1(self.ctx)


class 이슈라이동1(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5005], visible=True)
        self.set_effect(triggerIds=[5006], visible=True)
        self.set_time_scale(enable=True, startScale=0.3, endScale=0.3, duration=50, interpolator=1)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_11003866')
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출끝(self.ctx)


class 연출끝(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=False)
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_effect(triggerIds=[5005], visible=False)
        self.set_effect(triggerIds=[5006], visible=False)
        self.set_effect(triggerIds=[5007], visible=False)
        self.set_time_scale(enable=False, startScale=0.5, endScale=0.5, duration=50, interpolator=1)
        self.destroy_monster(spawnIds=[101,102,103], arg2=False)
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.visible_my_pc(isVisible=True)
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52010068, portalId=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Ready(self.ctx)


initial_state = Ready
