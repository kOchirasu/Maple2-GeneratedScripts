""" trigger/02020111_bf/lapenta_attack_2.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_ambient_light(primary=[183,189,201])
        set_directional_light(diffuseColor=[192,210,211], specularColor=[170,170,170])

    def on_tick(self) -> state.State:
        if user_value(key='Lapenta_Attack_2', value=1):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=23501011, illust='Turned_Renduebian_normal', script='$02020111_BF__LAPENTA_ATTACK_2__0$', duration=3525, voice='ko/Npc/00002200')
        set_ambient_light(primary=[52,48,38])
        set_directional_light(diffuseColor=[0,0,0], specularColor=[206,174,84])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3525):
            return 스킬발동()


class 스킬발동(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200001,200002,200003,200004,200005,200011,200012,200013,200014,200015,200021,200022,200023,200024,200025,200031,200032,200033,200034,200035], visible=False)
        set_skill(triggerIds=[5002], isEnable=True)
        add_buff(boxIds=[101], skillId=62100026, level=1, arg4=True)
        add_buff(boxIds=[1001], skillId=75000002, level=1)
        add_buff(boxIds=[1002], skillId=75000002, level=1)
        add_buff(boxIds=[1003], skillId=75000002, level=1)
        add_buff(boxIds=[1004], skillId=75000002, level=1)
        add_buff(boxIds=[1005], skillId=75000002, level=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 실패조건버프()


class 실패조건버프(state.State):
    def on_enter(self):
        set_user_value(triggerId=900204, key='Message', value=1)
        add_buff(boxIds=[101], skillId=70002181, level=1, arg4=True)

    def on_tick(self) -> state.State:
        if user_value(key='Lapenta_Attack_2', value=0):
            return 시작()


