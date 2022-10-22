""" trigger/02020111_bf/movement_01.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1001]):
            return 환경변화()


# **********************환경 변화 페이즈_1*******************************************************************************************
class 환경변화(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Movement', value=0):
            return 시작()
        if user_value(key='dark', value=1):
            return 페이드아웃()


class 페이드아웃(state.State):
    def on_enter(self):
        set_portal(portalId=5, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=6, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=7, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=8, visible=False, enabled=False, minimapVisible=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 조명변경()


class 조명변경(state.State):
    def on_enter(self):
        add_buff(boxIds=[101], skillId=62100014, level=1, arg4=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_event_ui(type=1, arg2='$02020111_BF__MOVEMENT_01__0$', arg3='3000')
        set_ambient_light(primary=[52,48,38])
        set_directional_light(diffuseColor=[0,0,0], specularColor=[206,174,84])
        add_buff(boxIds=[1001], skillId=75000001, level=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return 페이드인()
        if user_value(key='Movement', value=0):
            return 시작()


class 페이드인(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 유저이동()


class 유저이동(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020111_BF__MOVEMENT_01__2$', arg3='4000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 조명리셋()


class 조명리셋(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02020111_BF__MOVEMENT_01__1$', arg4=3, arg5=0)
        move_npc_to_pos(spawnId=101, pos=[-3743,294,1651], rot=[0,0,45])
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_ambient_light(primary=[183,189,201])
        set_directional_light(diffuseColor=[192,210,211], specularColor=[170,170,170])
        add_buff(boxIds=[1001], skillId=75000002, level=1)
        add_buff(boxIds=[1002], skillId=75000002, level=1)
        add_buff(boxIds=[1003], skillId=75000002, level=1)
        add_buff(boxIds=[1004], skillId=75000002, level=1)
        add_buff(boxIds=[1005], skillId=75000002, level=1)
        set_effect(triggerIds=[200031,200032,200033,200034,200035], visible=True)
        set_portal(portalId=9, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=5, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=6, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=8, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if user_value(key='Movement', value=0):
            return 시작()
        if user_value(key='dark', value=2):
            return 중앙지역이동_1()


class 중앙지역이동_1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200031,200032,200033,200034,200035], visible=False)
        move_npc_to_pos(spawnId=101, pos=[-13,288,1951], rot=[0,0,45]) # 페이즈 꼬임을 방지하기 위한 npc이동장치
        set_portal(portalId=9, visible=False, enabled=False, minimapVisible=False)
        # <action name="SetOnetimeEffect" id="1" enable="1" path="BG/Common/ScreenMask/Eff_fadein_1sec.xml"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 중앙지역이동_1_페이드인()


class 중앙지역이동_1_페이드인(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 포탈설정_1()


class 포탈설정_1(state.State):
    def on_enter(self):
        set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=6, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=8, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if user_value(key='Movement', value=0):
            return 시작()


