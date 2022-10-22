""" trigger/02000498_bf/stage_01.xml """
from common import *
import state


class 시작연출_6(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            return 페이드아웃()


class 페이드아웃(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 페이드아웃_2()


class 페이드아웃_2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='곧 새로운 차원으로 당신을 안내 합니다.', arg3='3000')
        set_effect(triggerIds=[500], visible=True)
        set_effect(triggerIds=[501], visible=True)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 시작대기_1()


class 시작대기_1(state.State):
    def on_enter(self):
        move_user_to_pos(pos=[433,-6777,8701])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 페이드인()


class 페이드인(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        change_background(dds='BG_Lith_C.dds')
        set_ambient_light(primary=[199,207,214])
        set_directional_light(diffuseColor=[255,255,255], specularColor=[255,255,255])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 시작대기()


class 시작대기(state.State):
    def on_enter(self):
        add_buff(boxIds=[100010], skillId=70000103, level=1)
        # <action name="이펙트를설정한다" arg1="6010" arg2="1" />
        # <action name="이펙트를설정한다" arg1="6011" arg2="1" />
        # <action name="이펙트를설정한다" arg1="6012" arg2="1" />
        # <action name="이펙트를설정한다" arg1="6013" arg2="1" />
        # <action name="이펙트를설정한다" arg1="6015" arg2="1" />
        # <action name="타이머를설정한다" arg1="3" arg2="3"/>

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return None # Missing State: 안내02


class 종료(state.State):
    pass


