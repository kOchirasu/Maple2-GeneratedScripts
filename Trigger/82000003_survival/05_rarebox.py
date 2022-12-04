""" trigger/82000003_survival/05_rarebox.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000342,10000343,10000344,10000345,10000346,10000347,10000348,10000349,10000350,10000351,10000352,10000353,10000354,10000355,10000356,10000357,10000358,10000359,10000360,10000361,10000362,10000363,10000364,10000365,10000366,10000367,10000368,10000369,10000370,10000371,10000372,10000373,10000374,10000375,10000376,10000377,10000378,10000379,10000380,10000381], isStart=False) # groupId="10000342-10000381" 황금 상자 Rare Box
        self.set_user_value(key='RareBoxOnCount', value=0)
        self.set_user_value(key='RareBoxOff', value=0)
        self.set_user_value(key='RareBoxStartTowerNumber', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RareBoxOnCount', value=1):
            return Delay(self.ctx)


class Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=178000):
            return BoxOnRandom(self.ctx)
        if self.user_value(key='RareBoxOff', value=1):
            return Quit(self.ctx)


class BoxOnRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=25):
            return StartToTower01to10(self.ctx)
        if self.random_condition(rate=25):
            return StartToTower11to20(self.ctx)
        if self.random_condition(rate=25):
            return StartToTower21to30(self.ctx)
        if self.random_condition(rate=25):
            return StartToTower31to40(self.ctx)
        if self.user_value(key='RareBoxOff', value=1):
            return Quit(self.ctx)


class StartToTower01to10(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='RareBoxStartTowerNumber', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Tower01to10(self.ctx)


class StartToTower11to20(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='RareBoxStartTowerNumber', value=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Tower11to20(self.ctx)


class StartToTower21to30(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='RareBoxStartTowerNumber', value=21)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Tower21to30(self.ctx)


class StartToTower31to40(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='RareBoxStartTowerNumber', value=31)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Tower31to40(self.ctx)


class Tower01to10(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000342,10000343,10000344,10000345,10000346,10000347,10000348,10000349,10000350,10000351], isStart=True) # 황금 상자 Rare Box Tower01to10

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RareBoxStartTowerNumber', value=11):
            return BoxOn(self.ctx)
        if self.wait_tick(waitTick=500):
            return Tower11to20(self.ctx)


class Tower11to20(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000352,10000353,10000354,10000355,10000356,10000357,10000358,10000359,10000360,10000361], isStart=True) # 황금 상자 Rare Box Tower11to20

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RareBoxStartTowerNumber', value=21):
            return BoxOn(self.ctx)
        if self.wait_tick(waitTick=500):
            return Tower21to30(self.ctx)


class Tower21to30(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000362,10000363,10000364,10000365,10000366,10000367,10000368,10000369,10000370,10000371], isStart=True) # 황금 상자 Rare Box Tower21to30

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RareBoxStartTowerNumber', value=31):
            return BoxOn(self.ctx)
        if self.wait_tick(waitTick=500):
            return Tower31to40(self.ctx)


class Tower31to40(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000372,10000373,10000374,10000375,10000376,10000377,10000378,10000379,10000380,10000381], isStart=True) # 황금 상자 Rare Box Tower31to40

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RareBoxStartTowerNumber', value=1):
            return BoxOn(self.ctx)
        if self.wait_tick(waitTick=500):
            return Tower01to10(self.ctx)


class BoxOn(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=5000, script='$82000002_survival__05_RAREBOX__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RareBoxOff', value=1):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000342,10000343,10000344,10000345,10000346,10000347,10000348,10000349,10000350,10000351,10000352,10000353,10000354,10000355,10000356,10000357,10000358,10000359,10000360,10000361,10000362,10000363,10000364,10000365,10000366,10000367,10000368,10000369,10000370,10000371,10000372,10000373,10000374,10000375,10000376,10000377,10000378,10000379,10000380,10000381], isStart=False) # groupId="10000342-10000381" 황금 상자 Rare Box


initial_state = Setting
