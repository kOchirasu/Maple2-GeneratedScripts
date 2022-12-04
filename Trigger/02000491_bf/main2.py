""" trigger/02000491_bf/main2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3107,3108,3109,3110,3111,3112], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3115,3116], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000989], state=2)
        self.set_interact_object(triggerIds=[10000990], state=2)
        self.set_interact_object(triggerIds=[10000991], state=2)
        self.set_interact_object(triggerIds=[10000992], state=2)
        self.set_interact_object(triggerIds=[10000993], state=2)
        self.set_interact_object(triggerIds=[10000994], state=2)
        self.set_interact_object(triggerIds=[10000997], state=2)
        self.set_interact_object(triggerIds=[10000998], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1002]):
            return 전투01(self.ctx)


class 전투01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[21101,21102,21103,21104,21105,21106,21107,21201,21202,21203,21204,21205], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[21101,21102,21103,21104,21105,21106,21107,21201,21202,21203,21204,21205]):
            return 전투02(self.ctx)


class 전투02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3107,3108], visible=False, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000989], state=1)
        self.set_interact_object(triggerIds=[10000990], state=1)
        self.create_monster(spawnIds=[22101,22102,22103,22104,22105,22106,22107,22201,22202,22203,22204,22205], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[22101,22102,22103,22104,22105,22106,22107,22201,22202,22203,22204,22205]):
            return 전투03(self.ctx)


class 전투03(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3109,3110], visible=False, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000991], state=1)
        self.set_interact_object(triggerIds=[10000992], state=1)
        self.create_monster(spawnIds=[23102,23103,23104,23105,23106,23107,23108,23201,23202,23203,23204,23205], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[23102,23103,23104,23105,23106,23107,23108,23201,23202,23203,23204,23205]):
            self.set_mesh(triggerIds=[3111,3112], visible=False, arg3=0, delay=0, scale=0)
            self.set_interact_object(triggerIds=[10000993], state=1)
            self.set_interact_object(triggerIds=[10000994], state=1)
            self.set_user_value(triggerId=9999901, key='main', value=1)
            return 합류대기(self.ctx)


class 합류대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='main2', value=1):
            return 전투04(self.ctx)


class 전투04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[51101,51102,51103,51104,51105,51106,51107,51108,51201,51202,51203,51204,51205,51206], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[51101,51102,51103,51104,51105,51106,51107,51108,51201,51202,51203,51204,51205,51206]):
            self.set_mesh(triggerIds=[3115,3116], visible=False, arg3=0, delay=0, scale=0)
            self.set_interact_object(triggerIds=[10000997], state=1)
            self.set_interact_object(triggerIds=[10000998], state=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
