""" trigger/52100070_qd/52100070.xml """
from common import *
import state


class Ready(state.State):
    def on_enter(self):
        select_camera(triggerId=400, enable=True)
        set_effect(triggerIds=[5000], visible=False)
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)
        set_effect(triggerIds=[5005], visible=False)
        set_effect(triggerIds=[5006], visible=False)
        set_effect(triggerIds=[5007], visible=False)
        visible_my_pc(isVisible=False) # 유저 투명 처리
        set_cinematic_ui(type=1)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1000]):
            return narration01()


class narration01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=9, script='$52100070_QD__52100070__0$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 암전1()


class 암전1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return Camera_Move_01()


class Camera_Move_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[400,401], returnView=False)
        show_caption(type='VerticalCaption', title='$52100070_QD__52100070__1$', desc='$52100070_QD__52100070__2$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 몬스터생성()


class 몬스터생성(state.State):
    def on_enter(self):
        set_skip(state=연출끝)
        create_monster(spawnIds=[101,102,103], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 전경카메라1()


class 전경카메라1(state.State):
    def on_enter(self):
        select_camera(triggerId=600, enable=True)
        select_camera_path(pathIds=[600,601], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 퐈이야()


class 퐈이야(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True)
        set_effect(triggerIds=[5002], visible=True)
        set_effect(triggerIds=[5004], visible=True)
        set_effect(triggerIds=[5007], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 이슈라카메라1()


class 이슈라카메라1(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[402,403], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 이슈라카메라2()


class 이슈라카메라2(state.State):
    def on_enter(self):
        select_camera(triggerId=500, enable=True)
        select_camera_path(pathIds=[500,501], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 이슈라카메라3()


class 이슈라카메라3(state.State):
    def on_enter(self):
        select_camera(triggerId=404, enable=False)
        select_camera_path(pathIds=[404,405], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 이슈라카메라4()


class 이슈라카메라4(state.State):
    def on_enter(self):
        select_camera(triggerId=406, enable=False)
        select_camera_path(pathIds=[406,407], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 렌듀비앙이동1()


class 렌듀비앙이동1(state.State):
    def on_enter(self):
        set_time_scale(enable=True, startScale=0.5, endScale=0.5, duration=50, interpolator=1)
        move_npc(spawnId=102, patrolName='MS2PatrolData_11003867')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 유페리아이동1()


class 유페리아이동1(state.State):
    def on_enter(self):
        move_npc(spawnId=103, patrolName='MS2PatrolData_11003868')
        set_effect(triggerIds=[5000], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 이슈라이동1()


class 이슈라이동1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5005], visible=True)
        set_effect(triggerIds=[5006], visible=True)
        set_time_scale(enable=True, startScale=0.3, endScale=0.3, duration=50, interpolator=1)
        move_npc(spawnId=101, patrolName='MS2PatrolData_11003866')
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출끝()


class 연출끝(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False)
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)
        set_effect(triggerIds=[5005], visible=False)
        set_effect(triggerIds=[5006], visible=False)
        set_effect(triggerIds=[5007], visible=False)
        set_time_scale(enable=False, startScale=0.5, endScale=0.5, duration=50, interpolator=1)
        destroy_monster(spawnIds=[101,102,103], arg2=False)
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        visible_my_pc(isVisible=True)
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user(mapId=52010068, portalId=6001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Ready()


