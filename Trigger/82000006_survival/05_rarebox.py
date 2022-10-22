""" trigger/82000006_survival/05_rarebox.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        set_user_value(key='RareBoxOnCount', value=0)
        set_user_value(key='RareBoxOff', value=0)
        set_user_value(key='RareBoxStartTowerNumber', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='RareBoxOnCount', value=1):
            return Delay()


class Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=178000):
            return BoxOnRandom()
        if user_value(key='RareBoxOff', value=1):
            return Quit()


class BoxOnRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=25):
            return StartToTower01to10()
        if random_condition(rate=25):
            return StartToTower11to20()
        if random_condition(rate=25):
            return StartToTower21to30()
        if random_condition(rate=25):
            return StartToTower31to40()


class StartToTower01to10(state.State):
    def on_enter(self):
        set_user_value(key='RareBoxStartTowerNumber', value=1)

    def on_tick(self) -> state.State:
        if true():
            return Tower01to10()


class StartToTower11to20(state.State):
    def on_enter(self):
        set_user_value(key='RareBoxStartTowerNumber', value=11)

    def on_tick(self) -> state.State:
        if true():
            return Tower11to20()


class StartToTower21to30(state.State):
    def on_enter(self):
        set_user_value(key='RareBoxStartTowerNumber', value=21)

    def on_tick(self) -> state.State:
        if true():
            return Tower21to30()


class StartToTower31to40(state.State):
    def on_enter(self):
        set_user_value(key='RareBoxStartTowerNumber', value=31)

    def on_tick(self) -> state.State:
        if true():
            return Tower31to40()


class Tower01to10(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000000,10000001,10000002,10000003,10000004,10000005,10000006,10000007,10000008,10000009], isStart=True) # 황금 상자 Rare Box Tower01to10

    def on_tick(self) -> state.State:
        if user_value(key='RareBoxStartTowerNumber', value=11):
            return BoxOn()
        if wait_tick(waitTick=500):
            return Tower11to20()


class Tower11to20(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000010,10000011,10000012,10000013,10000014,10000015,10000016,10000017,10000018,10000019], isStart=True) # 황금 상자 Rare Box Tower11to20

    def on_tick(self) -> state.State:
        if user_value(key='RareBoxStartTowerNumber', value=21):
            return BoxOn()
        if wait_tick(waitTick=500):
            return Tower21to30()


class Tower21to30(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000020,10000021,10000022,10000023,10000024,10000025,10000026,10000027,10000028,10000029], isStart=True) # 황금 상자 Rare Box Tower21to30

    def on_tick(self) -> state.State:
        if user_value(key='RareBoxStartTowerNumber', value=31):
            return BoxOn()
        if wait_tick(waitTick=500):
            return Tower31to40()


class Tower31to40(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000030,10000031,10000032,10000033,10000034,10000035,10000036,10000037,10000038,10000039], isStart=True) # 황금 상자 Rare Box Tower31to40

    def on_tick(self) -> state.State:
        if user_value(key='RareBoxStartTowerNumber', value=1):
            return BoxOn()
        if wait_tick(waitTick=500):
            return Tower01to10()


class BoxOn(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=5000, script='$82000012_survival__05_RAREBOX__0$')

    def on_tick(self) -> state.State:
        if user_value(key='RareBoxOff', value=1):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000000,10000001,10000002,10000003,10000004,10000005,10000006,10000007,10000008,10000009,10000010,10000011,10000012,10000013,10000014,10000015,10000016,10000017,10000018,10000019,10000020,10000021,10000022,10000023,10000024,10000025,10000026,10000027,10000028,10000029,10000030,10000031,10000032,10000033,10000034,10000035,10000036,10000037,10000038,10000039], isStart=False) # groupId="10000000-10000039" 황금 상자 Rare Box


