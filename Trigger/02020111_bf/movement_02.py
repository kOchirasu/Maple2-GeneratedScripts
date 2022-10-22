""" trigger/02020111_bf/movement_02.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1001]):
            return 환경변화_2()


# **********************환경 변화 페이즈_2*********************************************************************************************
class 환경변화_2(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Movement', value=0):
            return 시작()
        if user_value(key='dark', value=3):
            return 페이드아웃_2()


class 페이드아웃_2(state.State):
    def on_enter(self):
        set_portal(portalId=5, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=6, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=7, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=8, visible=False, enabled=False, minimapVisible=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 조명변경_2()


class 조명변경_2(state.State):
    def on_enter(self):
        add_buff(boxIds=[101], skillId=62100014, level=1, arg4=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_ambient_light(primary=[52,48,38])
        set_directional_light(diffuseColor=[0,0,0], specularColor=[206,174,84])
        add_buff(boxIds=[1001], skillId=75000001, level=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return 페이드인_2()
        if user_value(key='Movement', value=0):
            return 시작()


class 페이드인_2(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 유저이동_2()


class 유저이동_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 조명리셋_2()


class 조명리셋_2(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02020111_BF__MOVEMENT_01__2$', arg4=3, arg5=0)
        move_npc_to_pos(spawnId=101, pos=[-28,4030,2551], rot=[0,0,45])
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_ambient_light(primary=[183,189,201])
        set_directional_light(diffuseColor=[192,210,211], specularColor=[170,170,170])
        add_buff(boxIds=[1001], skillId=75000002, level=1)
        add_buff(boxIds=[1002], skillId=75000002, level=1)
        add_buff(boxIds=[1003], skillId=75000002, level=1)
        add_buff(boxIds=[1004], skillId=75000002, level=1)
        add_buff(boxIds=[1005], skillId=75000002, level=1)
        set_effect(triggerIds=[200001,200002,200003,200004,200005], visible=True)
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=6, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=8, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if user_value(key='Movement', value=0):
            return 시작()
        if user_value(key='dark', value=4):
            return 중앙지역이동_2()


class 중앙지역이동_2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200001,200002,200003,200004,200005], visible=False)
        move_npc_to_pos(spawnId=101, pos=[-13,288,1951], rot=[0,0,45]) # 페이즈 꼬임을 방지하기 위한 npc이동장치
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        # <action name="SetOnetimeEffect" id="1" enable="1" path="BG/Common/ScreenMask/Eff_fadein_1sec.xml"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 중앙지역이동_2_페이드인()


class 중앙지역이동_2_페이드인(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 포탈설정_2()


class 포탈설정_2(state.State):
    def on_enter(self):
        set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=6, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=8, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if user_value(key='Movement', value=0):
            return 시작()


