""" trigger/02020111_bf/lapenta_attack_guide.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200001,200002,200003,200004,200005,200011,200012,200013,200014,200015,200021,200022,200023,200024,200025,200031,200032,200033,200034,200035], visible=False)
        set_ambient_light(primary=[183,189,201])
        set_directional_light(diffuseColor=[192,210,211], specularColor=[170,170,170])

    def on_tick(self) -> state.State:
        if user_value(key='Lapenta_Attack_Guide', value=1):
            return 어둠효과_페이드아웃()


class 어둠효과_페이드아웃(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_buff(boxIds=[1001], skillId=75000001, level=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_ambient_light(primary=[52,48,38])
            set_directional_light(diffuseColor=[0,0,0], specularColor=[206,174,84])
            return 가이드발동()


class 가이드발동(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200001,200002,200003,200004,200005,200011,200012,200013,200014,200015,200021,200022,200023,200024,200025,200031,200032,200033,200034,200035], visible=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_buff(boxIds=[1001], skillId=75000001, level=1)

    def on_tick(self) -> state.State:
        if user_value(key='Lapenta_Attack_Guide', value=0):
            return 가이드종료()


class 가이드종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200001,200002,200003,200004,200005,200011,200012,200013,200014,200015,200021,200022,200023,200024,200025,200031,200032,200033,200034,200035], visible=False)

    def on_tick(self) -> state.State:
        if user_value(key='Lapenta_Attack_Guide', value=2):
            return 시작()


