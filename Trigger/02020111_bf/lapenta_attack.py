""" trigger/02020111_bf/lapenta_attack.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_ambient_light(primary=[183,189,201])
        self.set_directional_light(diffuseColor=[192,210,211], specularColor=[170,170,170])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Lapenta_Attack', value=1):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=23501011, illust='Turned_Renduebian_normal', script='$02020111_BF__LAPENTA_ATTACK__0$', duration=3432, voice='ko/Npc/00002199')
        self.set_ambient_light(primary=[52,48,38])
        self.set_directional_light(diffuseColor=[0,0,0], specularColor=[206,174,84])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3432):
            return 스킬발동(self.ctx)


class 스킬발동(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[200001,200002,200003,200004,200005,200011,200012,200013,200014,200015,200021,200022,200023,200024,200025,200031,200032,200033,200034,200035], visible=False)
        self.set_skill(triggerIds=[5001], enable=True)
        self.add_buff(boxIds=[101], skillId=62100026, level=1, isPlayer=True)
        self.add_buff(boxIds=[1001], skillId=75000002, level=1)
        self.add_buff(boxIds=[1002], skillId=75000002, level=1)
        self.add_buff(boxIds=[1003], skillId=75000002, level=1)
        self.add_buff(boxIds=[1004], skillId=75000002, level=1)
        self.add_buff(boxIds=[1005], skillId=75000002, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 실패조건버프(self.ctx)


class 실패조건버프(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=900204, key='Message', value=1)
        self.add_buff(boxIds=[101], skillId=70002181, level=1, isPlayer=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Lapenta_Attack', value=0):
            return 시작(self.ctx)


initial_state = 시작
