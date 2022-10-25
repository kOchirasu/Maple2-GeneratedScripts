""" trigger/82000000_survival/05_rarebox.xml """
import common


class Setting(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000165,10000166,10000167,10000168,10000169,10000170,10000171,10000172,10000173,10000174,10000175,10000176,10000177,10000178,10000179,10000180,10000181,10000182,10000183,10000184,10000185,10000186,10000187,10000188,10000189,10000190,10000191,10000192,10000193,10000194,10000195,10000196,10000197,10000198,10000199,10000200,10000201,10000202,10000203,10000204], isStart=False) # groupId="10000165-10000204" 황금 상자 Rare Box
        self.set_user_value(key='RareBoxOnCount', value=0)
        self.set_user_value(key='RareBoxOff', value=0)
        self.set_user_value(key='RareBoxStartTowerNumber', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RareBoxOnCount', value=1):
            return Delay(self.ctx)


class Delay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=178000):
            return BoxOnRandom(self.ctx)
        if self.user_value(key='RareBoxOff', value=1):
            return Quit(self.ctx)


class BoxOnRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=25):
            return StartToTower01to10(self.ctx)
        if self.random_condition(rate=25):
            return StartToTower11to20(self.ctx)
        if self.random_condition(rate=25):
            return StartToTower21to30(self.ctx)
        if self.random_condition(rate=25):
            return StartToTower31to40(self.ctx)


class StartToTower01to10(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='RareBoxStartTowerNumber', value=1)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Tower01to10(self.ctx)


class StartToTower11to20(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='RareBoxStartTowerNumber', value=11)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Tower11to20(self.ctx)


class StartToTower21to30(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='RareBoxStartTowerNumber', value=21)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Tower21to30(self.ctx)


class StartToTower31to40(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='RareBoxStartTowerNumber', value=31)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Tower31to40(self.ctx)


class Tower01to10(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000165,10000166,10000167,10000168,10000169,10000170,10000171,10000172,10000173,10000174], isStart=True) # 황금 상자 Rare Box Tower01to10

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RareBoxStartTowerNumber', value=11):
            return BoxOn(self.ctx)
        if self.wait_tick(waitTick=500):
            return Tower11to20(self.ctx)


class Tower11to20(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000175,10000176,10000177,10000178,10000179,10000180,10000181,10000182,10000183,10000184], isStart=True) # 황금 상자 Rare Box Tower11to20

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RareBoxStartTowerNumber', value=21):
            return BoxOn(self.ctx)
        if self.wait_tick(waitTick=500):
            return Tower21to30(self.ctx)


class Tower21to30(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000185,10000186,10000187,10000188,10000189,10000190,10000191,10000192,10000193,10000194], isStart=True) # 황금 상자 Rare Box Tower21to30

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RareBoxStartTowerNumber', value=31):
            return BoxOn(self.ctx)
        if self.wait_tick(waitTick=500):
            return Tower31to40(self.ctx)


class Tower31to40(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000195,10000196,10000197,10000198,10000199,10000200,10000201,10000202,10000203,10000204], isStart=True) # 황금 상자 Rare Box Tower31to40

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RareBoxStartTowerNumber', value=1):
            return BoxOn(self.ctx)
        if self.wait_tick(waitTick=500):
            return Tower01to10(self.ctx)


class BoxOn(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=5000, script='$82000000_survival__05_RAREBOX__0$')

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RareBoxOff', value=1):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000165,10000166,10000167,10000168,10000169,10000170,10000171,10000172,10000173,10000174,10000175,10000176,10000177,10000178,10000179,10000180,10000181,10000182,10000183,10000184,10000185,10000186,10000187,10000188,10000189,10000190,10000191,10000192,10000193,10000194,10000195,10000196,10000197,10000198,10000199,10000200,10000201,10000202,10000203,10000204], isStart=False) # groupId="10000165-10000204" 황금 상자 Rare Box


initial_state = Setting
