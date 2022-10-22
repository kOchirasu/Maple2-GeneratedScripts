""" trigger/02020111_bf/skillbreaksuccess_1.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 버프발동()


class 버프발동(state.State):
    def on_enter(self):
        add_buff(boxIds=[101], skillId=62100027, level=1, arg4=True)
        add_buff(boxIds=[1001], skillId=75000002, level=1)
        add_buff(boxIds=[1002], skillId=75000002, level=1)
        add_buff(boxIds=[1003], skillId=75000002, level=1)
        add_buff(boxIds=[1004], skillId=75000002, level=1)
        add_buff(boxIds=[1005], skillId=75000002, level=1)
        set_ambient_light(primary=[183,189,201])
        set_directional_light(diffuseColor=[192,210,211], specularColor=[170,170,170])
        add_buff(boxIds=[101], skillId=70002171, level=1, arg4=True, arg5=False)
        add_buff(boxIds=[101], skillId=62100026, level=1, arg4=True, arg5=False)
        set_user_value(triggerId=900103, key='Lapenta_Attack_Guide', value=2)
        set_user_value(triggerId=900204, key='Message', value=1)

    def on_tick(self) -> state.State:
        if all_of():
            return 시작()


