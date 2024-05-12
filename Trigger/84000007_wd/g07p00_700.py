""" trigger/84000007_wd/g07p00_700.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110,111,112,113,114,115], visible=False, arg3=0, delay=0, scale=0) # 1,1 / Number 0 to 5
        self.set_mesh(triggerIds=[120,121,122,123,124,125], visible=False, arg3=0, delay=0, scale=0) # 1,2 / Number 0 to 5
        self.set_mesh(triggerIds=[130,131,132,133,134,135], visible=False, arg3=0, delay=0, scale=0) # 1,3 / Number 0 to 5
        self.set_mesh(triggerIds=[140,141,142,143,144,145], visible=False, arg3=0, delay=0, scale=0) # 1,4 / Number 0 to 5
        self.set_mesh(triggerIds=[210,211,212,213,214,215], visible=False, arg3=0, delay=0, scale=0) # 2,1 / Number 0 to 5
        self.set_mesh(triggerIds=[220,221,222,223,224,225], visible=False, arg3=0, delay=0, scale=0) # 2,2 / Number 0 to 5
        self.set_mesh(triggerIds=[230,231,232,233,234,235], visible=False, arg3=0, delay=0, scale=0) # 2,3 / Number 0 to 5
        self.set_mesh(triggerIds=[240,241,242,243,244,245], visible=False, arg3=0, delay=0, scale=0) # 2,4 / Number 0 to 5
        self.set_mesh(triggerIds=[310,311,312,313,314,315], visible=False, arg3=0, delay=0, scale=0) # 3,1 / Number 0 to 5
        self.set_mesh(triggerIds=[320,321,322,323,324,325], visible=False, arg3=0, delay=0, scale=0) # 3,2 / Number 0 to 5
        self.set_mesh(triggerIds=[330,331,332,333,334,335], visible=False, arg3=0, delay=0, scale=0) # 3,3 / Number 0 to 5
        self.set_mesh(triggerIds=[340,341,342,343,344,345], visible=False, arg3=0, delay=0, scale=0) # 3,4 / Number 0 to 5
        self.set_mesh(triggerIds=[410,411,412,413,414,415], visible=False, arg3=0, delay=0, scale=0) # 4,1 / Number 0 to 5
        self.set_mesh(triggerIds=[420,421,422,423,424,425], visible=False, arg3=0, delay=0, scale=0) # 4,2 / Number 0 to 5
        self.set_mesh(triggerIds=[430,431,432,433,434,435], visible=False, arg3=0, delay=0, scale=0) # 4,3 / Number 0 to 5
        self.set_mesh(triggerIds=[440,441,442,443,444,445], visible=False, arg3=0, delay=0, scale=0) # 4,4 / Number 0 to 5
        self.set_mesh(triggerIds=[2207,2208,2209,22000,22005,22010,22020,22030], visible=False, arg3=0, delay=0, scale=0) # 2,2 / Large Number
        self.set_mesh(triggerIds=[2307,2308,2309,23000,23005,23010,23020,23030], visible=False, arg3=0, delay=0, scale=0) # 2,3 / Large Number
        self.set_mesh(triggerIds=[3207,3208,3209,32000,32005,32010,32020,32030], visible=False, arg3=0, delay=0, scale=0) # 3,2 / Large Number
        self.set_mesh(triggerIds=[3307,3308,3309,33000,33005,33010,33020,33030], visible=False, arg3=0, delay=0, scale=0) # 3,3 / Large Number

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P201Set', value=1):
            return NumberOnP201(self.ctx)
        if self.user_value(key='G07P202Set', value=1):
            return NumberOnP202(self.ctx)
        if self.user_value(key='G07P203Set', value=1):
            return NumberOnP203(self.ctx)
        if self.user_value(key='G07P204Set', value=1):
            return NumberOnP204(self.ctx)
        if self.user_value(key='G07P205Set', value=1):
            return NumberOnP205(self.ctx)
        if self.user_value(key='G07P206Set', value=1):
            return NumberOnP206(self.ctx)
        if self.user_value(key='G07P207Set', value=1):
            return NumberOnP207(self.ctx)
        if self.user_value(key='G07P208Set', value=1):
            return NumberOnP208(self.ctx)
        if self.user_value(key='G07P209Set', value=1):
            return NumberOnP209(self.ctx)
        if self.user_value(key='G07P210Set', value=1):
            return NumberOnP210(self.ctx)
        if self.user_value(key='G07P301Set', value=1):
            return NumberOnP301(self.ctx)
        if self.user_value(key='G07P302Set', value=1):
            return NumberOnP302(self.ctx)
        if self.user_value(key='G07P303Set', value=1):
            return NumberOnP303(self.ctx)
        if self.user_value(key='G07P304Set', value=1):
            return NumberOnP304(self.ctx)
        if self.user_value(key='G07P305Set', value=1):
            return NumberOnP305(self.ctx)
        if self.user_value(key='G07P306Set', value=1):
            return NumberOnP306(self.ctx)
        if self.user_value(key='G07P307Set', value=1):
            return NumberOnP307(self.ctx)
        if self.user_value(key='G07P308Set', value=1):
            return NumberOnP308(self.ctx)
        if self.user_value(key='G07P309Set', value=1):
            return NumberOnP309(self.ctx)
        if self.user_value(key='G07P310Set', value=1):
            return NumberOnP310(self.ctx)
        if self.user_value(key='G07P401Set', value=1):
            return NumberOnP401(self.ctx)
        if self.user_value(key='G07P402Set', value=1):
            return NumberOnP402(self.ctx)
        if self.user_value(key='G07P403Set', value=1):
            return NumberOnP403(self.ctx)
        if self.user_value(key='G07P404Set', value=1):
            return NumberOnP404(self.ctx)
        if self.user_value(key='G07P405Set', value=1):
            return NumberOnP405(self.ctx)
        if self.user_value(key='G07P406Set', value=1):
            return NumberOnP406(self.ctx)
        if self.user_value(key='G07P407Set', value=1):
            return NumberOnP407(self.ctx)


# G07 P201
class NumberOnP201(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start jackpot
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[110], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[120], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[215], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[22010], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 15 Jackpot
        self.set_mesh(triggerIds=[22005], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 15 Jackpot
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[314], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[322], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[335], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 5
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[430], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=0)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=5)
        self.set_user_value(triggerId=8220, key='Barrier22', value=15) # 15 Jackpot
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=4)
        self.set_user_value(triggerId=8320, key='Barrier32', value=2)
        self.set_user_value(triggerId=8330, key='Barrier33', value=5)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=0)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P201TimeLimit', value=1):
            return CheckP201(self.ctx)


class CheckP201(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=0)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=5)
        self.set_user_value(triggerId=9220, key='Box22Check', value=15) # 15 Jackpot
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=4)
        self.set_user_value(triggerId=9320, key='Box32Check', value=2)
        self.set_user_value(triggerId=9330, key='Box33Check', value=5)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=0)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP201(self.ctx)


class NumberOffP201(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[120], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[215], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[22010], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 15 Jackpot
        self.set_mesh(triggerIds=[22005], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 15 Jackpot
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[314], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[322], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[335], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 5
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[430], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP201(self.ctx)


class ResetP201(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P201End', value=1)
        self.set_user_value(key='G07P201Set', value=0)
        self.set_user_value(key='G07P201TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P202
class NumberOnP202(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start jackpot
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[210], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[23010], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 15 Jackpot
        self.set_mesh(triggerIds=[23005], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 15 Jackpot
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[322], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[410], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=0)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=15) # 15 Jackpot
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=2)
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=0)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P202TimeLimit', value=1):
            return CheckP202(self.ctx)


class CheckP202(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=0)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=15) # 15 Jackpot
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=2)
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=0)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP202(self.ctx)


class NumberOffP202(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[210], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[23010], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 15 Jackpot
        self.set_mesh(triggerIds=[23005], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 15 Jackpot
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[322], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[410], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP202(self.ctx)


class ResetP202(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P202End', value=1)
        self.set_user_value(key='G07P202Set', value=0)
        self.set_user_value(key='G07P202TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P203
class NumberOnP203(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start jackpot
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[124], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[130], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[210], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[234], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[240], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[32010], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 15 Jackpot
        self.set_mesh(triggerIds=[32005], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 15 Jackpot
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[344], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[430], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=4)
        self.set_user_value(triggerId=8130, key='Barrier13', value=0)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=0)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=4)
        self.set_user_value(triggerId=8240, key='Barrier24', value=0)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=15) # 15 Jackpot
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=4)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=0)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P203TimeLimit', value=1):
            return CheckP203(self.ctx)


class CheckP203(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=4)
        self.set_user_value(triggerId=9130, key='Box13Check', value=0)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=0)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=4)
        self.set_user_value(triggerId=9240, key='Box24Check', value=0)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=15) # 15 Jackpot
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=4)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=0)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP203(self.ctx)


class NumberOffP203(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[124], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[130], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[210], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[234], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[240], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[32010], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 15 Jackpot
        self.set_mesh(triggerIds=[32005], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 15 Jackpot
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[344], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[430], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP203(self.ctx)


class ResetP203(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P203End', value=1)
        self.set_user_value(key='G07P203Set', value=0)
        self.set_user_value(key='G07P203TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P204
class NumberOnP204(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start jackpot
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[114], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[120], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[225], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[235], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[240], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[325], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[33010], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 15 Jackpot
        self.set_mesh(triggerIds=[33005], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 15 Jackpot
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[430], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[444], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 4
        self.set_user_value(triggerId=8110, key='Barrier11', value=4)
        self.set_user_value(triggerId=8120, key='Barrier12', value=0)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=5)
        self.set_user_value(triggerId=8230, key='Barrier23', value=5)
        self.set_user_value(triggerId=8240, key='Barrier24', value=0)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=5)
        self.set_user_value(triggerId=8330, key='Barrier33', value=15) # 15 Jackpot
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=0)
        self.set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P204TimeLimit', value=1):
            return CheckP204(self.ctx)


class CheckP204(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=4)
        self.set_user_value(triggerId=9120, key='Box12Check', value=0)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=5)
        self.set_user_value(triggerId=9230, key='Box23Check', value=5)
        self.set_user_value(triggerId=9240, key='Box24Check', value=0)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=5)
        self.set_user_value(triggerId=9330, key='Box33Check', value=15) # 15 Jackpot
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=0)
        self.set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP204(self.ctx)


class NumberOffP204(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[114], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[120], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[225], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[235], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[240], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[325], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[33010], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 15 Jackpot
        self.set_mesh(triggerIds=[33005], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 15 Jackpot
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[430], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[444], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP204(self.ctx)


class ResetP204(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P204End', value=1)
        self.set_user_value(key='G07P204Set', value=0)
        self.set_user_value(key='G07P204TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P205
class NumberOnP205(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start jackpot
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[120], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[134], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[22020], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 20 Jackpot
        self.set_mesh(triggerIds=[22000], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 20 Jackpot
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[330], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[420], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[434], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=0)
        self.set_user_value(triggerId=8130, key='Barrier13', value=4)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=20) # 20 Jackpot
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=0)
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=0)
        self.set_user_value(triggerId=8430, key='Barrier43', value=4)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P205TimeLimit', value=1):
            return CheckP205(self.ctx)


class CheckP205(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=0)
        self.set_user_value(triggerId=9130, key='Box13Check', value=4)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=20) # 20 Jackpot
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=0)
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=0)
        self.set_user_value(triggerId=9430, key='Box43Check', value=4)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP205(self.ctx)


class NumberOffP205(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[120], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[134], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[22020], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 20 Jackpot
        self.set_mesh(triggerIds=[22000], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 20 Jackpot
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[330], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[420], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[434], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP205(self.ctx)


class ResetP205(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P205End', value=1)
        self.set_user_value(key='G07P205Set', value=0)
        self.set_user_value(key='G07P205TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P206
class NumberOnP206(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start jackpot
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[111], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 1
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[141], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[225], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[23020], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 20 Jackpot
        self.set_mesh(triggerIds=[23000], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 20 Jackpot
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[310], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[335], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 5
        self.set_mesh(triggerIds=[340], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[411], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[425], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=1)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=1)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=5)
        self.set_user_value(triggerId=8230, key='Barrier23', value=20) # 20 Jackpot
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=0)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=5)
        self.set_user_value(triggerId=8340, key='Barrier34', value=0)
        self.set_user_value(triggerId=8410, key='Barrier41', value=1)
        self.set_user_value(triggerId=8420, key='Barrier42', value=5)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P206TimeLimit', value=1):
            return CheckP206(self.ctx)


class CheckP206(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=1)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=1)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=5)
        self.set_user_value(triggerId=9230, key='Box23Check', value=20) # 20 Jackpot
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=0)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=5)
        self.set_user_value(triggerId=9340, key='Box34Check', value=0)
        self.set_user_value(triggerId=9410, key='Box41Check', value=1)
        self.set_user_value(triggerId=9420, key='Box42Check', value=5)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP206(self.ctx)


class NumberOffP206(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[111], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 1
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[141], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[225], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[23020], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 20 Jackpot
        self.set_mesh(triggerIds=[23000], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 20 Jackpot
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[310], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[335], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 5
        self.set_mesh(triggerIds=[340], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[411], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[425], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP206(self.ctx)


class ResetP206(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P206End', value=1)
        self.set_user_value(key='G07P206Set', value=0)
        self.set_user_value(key='G07P206TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P207
class NumberOnP207(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start jackpot
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[110], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[131], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[145], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[210], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[221], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[315], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[32020], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 20 Jackpot
        self.set_mesh(triggerIds=[32000], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 20 Jackpot
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[414], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[431], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=1)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=0)
        self.set_user_value(triggerId=8220, key='Barrier22', value=1)
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=5)
        self.set_user_value(triggerId=8320, key='Barrier32', value=20) # 20 Jackpot
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=4)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=1)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P207TimeLimit', value=1):
            return CheckP207(self.ctx)


class CheckP207(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=1)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=0)
        self.set_user_value(triggerId=9220, key='Box22Check', value=1)
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=5)
        self.set_user_value(triggerId=9320, key='Box32Check', value=20) # 20 Jackpot
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=4)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=1)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP207(self.ctx)


class NumberOffP207(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[131], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[145], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[210], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[221], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[315], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[32020], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 20 Jackpot
        self.set_mesh(triggerIds=[32000], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 20 Jackpot
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[414], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[431], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP207(self.ctx)


class ResetP207(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P207End', value=1)
        self.set_user_value(key='G07P207Set', value=0)
        self.set_user_value(key='G07P207TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P208
class NumberOnP208(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start jackpot
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[121], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[144], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[231], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 1
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[324], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[33020], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 20 Jackpot
        self.set_mesh(triggerIds=[33000], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 20 Jackpot
        self.set_mesh(triggerIds=[341], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[441], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 1
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=1)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=4)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=1)
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=4)
        self.set_user_value(triggerId=8330, key='Barrier33', value=20) # 20 Jackpot
        self.set_user_value(triggerId=8340, key='Barrier34', value=1)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P208TimeLimit', value=1):
            return CheckP208(self.ctx)


class CheckP208(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=1)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=4)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=1)
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=4)
        self.set_user_value(triggerId=9330, key='Box33Check', value=20) # 20 Jackpot
        self.set_user_value(triggerId=9340, key='Box34Check', value=1)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP208(self.ctx)


class NumberOffP208(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[121], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[144], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[231], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 1
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[324], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[33020], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 20 Jackpot
        self.set_mesh(triggerIds=[33000], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 20 Jackpot
        self.set_mesh(triggerIds=[341], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[441], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP208(self.ctx)


class ResetP208(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P208End', value=1)
        self.set_user_value(key='G07P208Set', value=0)
        self.set_user_value(key='G07P208TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P209
class NumberOnP209(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start jackpot
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[22020], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 25 Jackpot
        self.set_mesh(triggerIds=[22005], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 25 Jackpot
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=25) # 25 Jackpot
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P209TimeLimit', value=1):
            return CheckP209(self.ctx)


class CheckP209(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=25) # 25 Jackpot
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP209(self.ctx)


class NumberOffP209(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[22020], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 25 Jackpot
        self.set_mesh(triggerIds=[22005], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 25 Jackpot
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP209(self.ctx)


class ResetP209(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P209End', value=1)
        self.set_user_value(key='G07P209Set', value=0)
        self.set_user_value(key='G07P209TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P210
class NumberOnP210(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start jackpot
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[110], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[135], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[210], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[245], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[315], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[320], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 0
        self.set_mesh(triggerIds=[33020], visible=True, arg3=0, delay=0, scale=2) # 3,3 /25 Jackpot
        self.set_mesh(triggerIds=[33005], visible=True, arg3=0, delay=0, scale=2) # 3,3 /25 Jackpot
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[435], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=5)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=0)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=5)
        self.set_user_value(triggerId=8310, key='Barrier31', value=5)
        self.set_user_value(triggerId=8320, key='Barrier32', value=0)
        self.set_user_value(triggerId=8330, key='Barrier33', value=25) # 25 Jackpot
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=5)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P210TimeLimit', value=1):
            return CheckP210(self.ctx)


class CheckP210(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=5)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=0)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=5)
        self.set_user_value(triggerId=9310, key='Box31Check', value=5)
        self.set_user_value(triggerId=9320, key='Box32Check', value=0)
        self.set_user_value(triggerId=9330, key='Box33Check', value=25) # 25 Jackpot
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=5)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP210(self.ctx)


class NumberOffP210(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[135], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[210], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[245], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[315], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[320], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 0
        self.set_mesh(triggerIds=[33020], visible=False, arg3=0, delay=0, scale=2) # 3,3 /25 Jackpot
        self.set_mesh(triggerIds=[33005], visible=False, arg3=0, delay=0, scale=2) # 3,3 /25 Jackpot
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[435], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP210(self.ctx)


class ResetP210(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P210End', value=1)
        self.set_user_value(key='G07P210Set', value=0)
        self.set_user_value(key='G07P210TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P301
class NumberOnP301(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start jackpot
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[33020], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 25 Jackpot
        self.set_mesh(triggerIds=[33005], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 25 Jackpot
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[424], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=25) # 25 Jackpot
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=4)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P301TimeLimit', value=1):
            return CheckP301(self.ctx)


class CheckP301(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=25) # 25 Jackpot
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=4)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP301(self.ctx)


class NumberOffP301(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[33020], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 25 Jackpot
        self.set_mesh(triggerIds=[33005], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 25 Jackpot
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[424], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP301(self.ctx)


class ResetP301(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P301End', value=1)
        self.set_user_value(key='G07P301Set', value=0)
        self.set_user_value(key='G07P301TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P302
class NumberOnP302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start jackpot
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[135], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[23020], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 25 Jackpot
        self.set_mesh(triggerIds=[23005], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 25 Jackpot
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[325], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=5)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=25) # 25 Jackpot
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=5)
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P302TimeLimit', value=1):
            return CheckP302(self.ctx)


class CheckP302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=5)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=25) # 25 Jackpot
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=5)
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP302(self.ctx)


class NumberOffP302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[135], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[23020], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 25 Jackpot
        self.set_mesh(triggerIds=[23005], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 25 Jackpot
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[325], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP302(self.ctx)


class ResetP302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P302End', value=1)
        self.set_user_value(key='G07P302Set', value=0)
        self.set_user_value(key='G07P302TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P303
class NumberOnP303(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start jackpot
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[114], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[144], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[215], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[245], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[32020], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 25 Jackpot
        self.set_mesh(triggerIds=[32005], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 25 Jackpot
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[344], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[434], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=4)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=4)
        self.set_user_value(triggerId=8210, key='Barrier21', value=5)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=5)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=25) # 25 Jackpot
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=4)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=4)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P303TimeLimit', value=1):
            return CheckP303(self.ctx)


class CheckP303(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=4)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=4)
        self.set_user_value(triggerId=9210, key='Box21Check', value=5)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=5)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=25) # 25 Jackpot
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=4)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=4)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP303(self.ctx)


class NumberOffP303(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[114], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[144], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[215], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[245], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[32020], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 25 Jackpot
        self.set_mesh(triggerIds=[32005], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 25 Jackpot
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[344], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[434], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP303(self.ctx)


class ResetP303(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P303End', value=1)
        self.set_user_value(key='G07P303Set', value=0)
        self.set_user_value(key='G07P303TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P304
class NumberOnP304(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start jackpot
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[124], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[134], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[22020], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 20 Jackpot
        self.set_mesh(triggerIds=[22000], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 20 Jackpot
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[314], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[322], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[414], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[424], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=4)
        self.set_user_value(triggerId=8130, key='Barrier13', value=4)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=20) # 20 Jackpot
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=4)
        self.set_user_value(triggerId=8320, key='Barrier32', value=2)
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=4)
        self.set_user_value(triggerId=8420, key='Barrier42', value=4)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P304TimeLimit', value=1):
            return CheckP304(self.ctx)


class CheckP304(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=4)
        self.set_user_value(triggerId=9130, key='Box13Check', value=4)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=20) # 20 Jackpot
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=4)
        self.set_user_value(triggerId=9320, key='Box32Check', value=2)
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=4)
        self.set_user_value(triggerId=9420, key='Box42Check', value=4)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP304(self.ctx)


class NumberOffP304(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[124], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[134], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[22020], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 20 Jackpot
        self.set_mesh(triggerIds=[22000], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 20 Jackpot
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[314], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[322], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[414], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[424], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP304(self.ctx)


class ResetP304(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P304End', value=1)
        self.set_user_value(key='G07P304Set', value=0)
        self.set_user_value(key='G07P304TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P305
class NumberOnP305(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start jackpot
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[114], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[145], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[211], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[23020], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 20 Jackpot
        self.set_mesh(triggerIds=[23000], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 20 Jackpot
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[325], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[334], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[411], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[431], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[444], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 4
        self.set_user_value(triggerId=8110, key='Barrier11', value=4)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=1)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=20) # 20 Jackpot
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=5)
        self.set_user_value(triggerId=8330, key='Barrier33', value=4)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=1)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=1)
        self.set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P305TimeLimit', value=1):
            return CheckP305(self.ctx)


class CheckP305(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=4)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=1)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=20) # 20 Jackpot
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=5)
        self.set_user_value(triggerId=9330, key='Box33Check', value=4)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=1)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=1)
        self.set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP305(self.ctx)


class NumberOffP305(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[114], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[145], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[211], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[23020], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 20 Jackpot
        self.set_mesh(triggerIds=[23000], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 20 Jackpot
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[325], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[334], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[411], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[431], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[444], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP305(self.ctx)


class ResetP305(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P305End', value=1)
        self.set_user_value(key='G07P305Set', value=0)
        self.set_user_value(key='G07P305TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P306
class NumberOnP306(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start jackpot
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[125], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[141], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[235], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[325], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[33020], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 20 Jackpot
        self.set_mesh(triggerIds=[33000], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 20 Jackpot
        self.set_mesh(triggerIds=[344], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[411], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[434], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[441], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 1
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=5)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=1)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=5)
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=5)
        self.set_user_value(triggerId=8330, key='Barrier33', value=20) # 20 Jackpot
        self.set_user_value(triggerId=8340, key='Barrier34', value=4)
        self.set_user_value(triggerId=8410, key='Barrier41', value=1)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=4)
        self.set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P306TimeLimit', value=1):
            return CheckP306(self.ctx)


class CheckP306(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=5)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=1)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=5)
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=5)
        self.set_user_value(triggerId=9330, key='Box33Check', value=20) # 20 Jackpot
        self.set_user_value(triggerId=9340, key='Box34Check', value=4)
        self.set_user_value(triggerId=9410, key='Box41Check', value=1)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=4)
        self.set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP306(self.ctx)


class NumberOffP306(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[125], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[141], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[235], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[325], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[33020], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 20 Jackpot
        self.set_mesh(triggerIds=[33000], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 20 Jackpot
        self.set_mesh(triggerIds=[344], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[411], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[434], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[441], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP306(self.ctx)


class ResetP306(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P306End', value=1)
        self.set_user_value(key='G07P306Set', value=0)
        self.set_user_value(key='G07P306TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P307
class NumberOnP307(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start jackpot
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[215], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[235], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[32030], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 30 Jackpot
        self.set_mesh(triggerIds=[32000], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 30 Jackpot
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[414], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[434], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=5)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=5)
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=30) # 30 Jackpot
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=4)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=4)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P307TimeLimit', value=1):
            return CheckP307(self.ctx)


class CheckP307(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=5)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=5)
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=30) # 30 Jackpot
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=4)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=4)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP307(self.ctx)


class NumberOffP307(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[215], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[235], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[32030], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 30 Jackpot
        self.set_mesh(triggerIds=[32000], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 30 Jackpot
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[414], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[434], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP307(self.ctx)


class ResetP307(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P307End', value=1)
        self.set_user_value(key='G07P307Set', value=0)
        self.set_user_value(key='G07P307TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P308
class NumberOnP308(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start jackpot
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[115], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 5
        self.set_mesh(triggerIds=[124], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[131], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[23030], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 30 Jackpot
        self.set_mesh(triggerIds=[23000], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 30 Jackpot
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[311], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[325], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[424], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[431], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[445], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 5
        self.set_user_value(triggerId=8110, key='Barrier11', value=5)
        self.set_user_value(triggerId=8120, key='Barrier12', value=4)
        self.set_user_value(triggerId=8130, key='Barrier13', value=1)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=30) # 30 Jackpot
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=1)
        self.set_user_value(triggerId=8320, key='Barrier32', value=5)
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=4)
        self.set_user_value(triggerId=8430, key='Barrier43', value=1)
        self.set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P308TimeLimit', value=1):
            return CheckP308(self.ctx)


class CheckP308(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=5)
        self.set_user_value(triggerId=9120, key='Box12Check', value=4)
        self.set_user_value(triggerId=9130, key='Box13Check', value=1)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=30) # 30 Jackpot
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=1)
        self.set_user_value(triggerId=9320, key='Box32Check', value=5)
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=4)
        self.set_user_value(triggerId=9430, key='Box43Check', value=1)
        self.set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP308(self.ctx)


class NumberOffP308(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[115], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 5
        self.set_mesh(triggerIds=[124], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[131], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[23030], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 30 Jackpot
        self.set_mesh(triggerIds=[23000], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 30 Jackpot
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[311], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[325], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[424], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[431], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[445], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP308(self.ctx)


class ResetP308(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P308End', value=1)
        self.set_user_value(key='G07P308Set', value=0)
        self.set_user_value(key='G07P308TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P309
class NumberOnP309(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start jackpot
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start jackpot
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[124], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[22010], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 15 Jackpot
        self.set_mesh(triggerIds=[22005], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 15 Jackpot
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[33020], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 25 Jackpot
        self.set_mesh(triggerIds=[33005], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 25 Jackpot
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[434], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=4)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=15) # 15 Jackpot
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=25) # 25 Jackpot
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=4)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P309TimeLimit', value=1):
            return CheckP309(self.ctx)


class CheckP309(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=4)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=15) # 15 Jackpot
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=25) # 25 Jackpot
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=4)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP309(self.ctx)


class NumberOffP309(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[124], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[22010], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 15 Jackpot
        self.set_mesh(triggerIds=[22005], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 15 Jackpot
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[33020], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 25 Jackpot
        self.set_mesh(triggerIds=[33005], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 25 Jackpot
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[434], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP309(self.ctx)


class ResetP309(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P309End', value=1)
        self.set_user_value(key='G07P309Set', value=0)
        self.set_user_value(key='G07P309TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P310
class NumberOnP310(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start jackpot
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start jackpot
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[224], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 4
        self.set_mesh(triggerIds=[23020], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 20 Jackpot
        self.set_mesh(triggerIds=[23000], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 20 Jackpot
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[32020], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 20 Jackpot
        self.set_mesh(triggerIds=[32000], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 20 Jackpot
        self.set_mesh(triggerIds=[334], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=4)
        self.set_user_value(triggerId=8230, key='Barrier23', value=20) # 20 Jackpot
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=20) # 20 Jackpot
        self.set_user_value(triggerId=8330, key='Barrier33', value=4)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P310TimeLimit', value=1):
            return CheckP310(self.ctx)


class CheckP310(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=4)
        self.set_user_value(triggerId=9230, key='Box23Check', value=20) # 20 Jackpot
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=20) # 20 Jackpot
        self.set_user_value(triggerId=9330, key='Box33Check', value=4)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP310(self.ctx)


class NumberOffP310(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[224], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 4
        self.set_mesh(triggerIds=[23020], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 20 Jackpot
        self.set_mesh(triggerIds=[23000], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 20 Jackpot
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[32020], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 20 Jackpot
        self.set_mesh(triggerIds=[32000], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 20 Jackpot
        self.set_mesh(triggerIds=[334], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP310(self.ctx)


class ResetP310(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P310End', value=1)
        self.set_user_value(key='G07P310Set', value=0)
        self.set_user_value(key='G07P310TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P401
class NumberOnP401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start jackpot
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[114], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[134], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[22030], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 30 Jackpot
        self.set_mesh(triggerIds=[22000], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 30 Jackpot
        self.set_mesh(triggerIds=[234], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[314], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[334], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[344], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[424], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[444], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 4
        self.set_user_value(triggerId=8110, key='Barrier11', value=4)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=4)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=30) # 30 Jackpot
        self.set_user_value(triggerId=8230, key='Barrier23', value=4)
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=4)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=4)
        self.set_user_value(triggerId=8340, key='Barrier34', value=4)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=4)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P401TimeLimit', value=1):
            return CheckP401(self.ctx)


class CheckP401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=4)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=4)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=30) # 30 Jackpot
        self.set_user_value(triggerId=9230, key='Box23Check', value=4)
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=4)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=4)
        self.set_user_value(triggerId=9340, key='Box34Check', value=4)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=4)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP401(self.ctx)


class NumberOffP401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[114], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[134], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[22030], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 30 Jackpot
        self.set_mesh(triggerIds=[22000], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 30 Jackpot
        self.set_mesh(triggerIds=[234], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[314], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[334], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[344], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[424], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[444], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP401(self.ctx)


class ResetP401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P401End', value=1)
        self.set_user_value(key='G07P401Set', value=0)
        self.set_user_value(key='G07P401TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P402
class NumberOnP402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start jackpot
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[125], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[145], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[224], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 4
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[245], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[325], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[33030], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 30 Jackpot
        self.set_mesh(triggerIds=[33000], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 30 Jackpot
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[434], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[445], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 5
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=5)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=4)
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=5)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=5)
        self.set_user_value(triggerId=8330, key='Barrier33', value=30) # 30 Jackpot
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=4)
        self.set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P402TimeLimit', value=1):
            return CheckP402(self.ctx)


class CheckP402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=5)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=4)
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=5)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=5)
        self.set_user_value(triggerId=9330, key='Box33Check', value=30) # 30 Jackpot
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=4)
        self.set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP402(self.ctx)


class NumberOffP402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[125], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[145], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[224], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 4
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[245], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[325], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[33030], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 30 Jackpot
        self.set_mesh(triggerIds=[33000], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 30 Jackpot
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[434], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[445], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP402(self.ctx)


class ResetP402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P402End', value=1)
        self.set_user_value(key='G07P402Set', value=0)
        self.set_user_value(key='G07P402TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P403
class NumberOnP403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start jackpot
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[124], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[135], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[225], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[23020], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 25 Jackpot
        self.set_mesh(triggerIds=[23005], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 25 Jackpot
        self.set_mesh(triggerIds=[245], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[325], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[335], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 5
        self.set_mesh(triggerIds=[344], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=4)
        self.set_user_value(triggerId=8130, key='Barrier13', value=5)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=5)
        self.set_user_value(triggerId=8230, key='Barrier23', value=25) # 25 Jackpot
        self.set_user_value(triggerId=8240, key='Barrier24', value=5)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=5)
        self.set_user_value(triggerId=8330, key='Barrier33', value=5)
        self.set_user_value(triggerId=8340, key='Barrier34', value=4)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P403TimeLimit', value=1):
            return CheckP403(self.ctx)


class CheckP403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=4)
        self.set_user_value(triggerId=9130, key='Box13Check', value=5)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=5)
        self.set_user_value(triggerId=9230, key='Box23Check', value=25) # 25 Jackpot
        self.set_user_value(triggerId=9240, key='Box24Check', value=5)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=5)
        self.set_user_value(triggerId=9330, key='Box33Check', value=5)
        self.set_user_value(triggerId=9340, key='Box34Check', value=4)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP403(self.ctx)


class NumberOffP403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[124], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[135], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[225], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[23020], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 25 Jackpot
        self.set_mesh(triggerIds=[23005], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 25 Jackpot
        self.set_mesh(triggerIds=[245], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[325], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[335], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 5
        self.set_mesh(triggerIds=[344], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP403(self.ctx)


class ResetP403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P403End', value=1)
        self.set_user_value(key='G07P403Set', value=0)
        self.set_user_value(key='G07P403TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P404
class NumberOnP404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start jackpot
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[115], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 5
        self.set_mesh(triggerIds=[125], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[145], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[215], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[32020], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 25 Jackpot
        self.set_mesh(triggerIds=[32005], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 25 Jackpot
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[435], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=5)
        self.set_user_value(triggerId=8120, key='Barrier12', value=5)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=5)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=25) # 25 Jackpot
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=5)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P404TimeLimit', value=1):
            return CheckP404(self.ctx)


class CheckP404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=5)
        self.set_user_value(triggerId=9120, key='Box12Check', value=5)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=5)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=25) # 25 Jackpot
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=5)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP404(self.ctx)


class NumberOffP404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[115], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 5
        self.set_mesh(triggerIds=[125], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[145], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[215], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[32020], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 25 Jackpot
        self.set_mesh(triggerIds=[32005], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 25 Jackpot
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[435], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP404(self.ctx)


class ResetP404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P404End', value=1)
        self.set_user_value(key='G07P404Set', value=0)
        self.set_user_value(key='G07P404TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P405
class NumberOnP405(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start jackpot
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start jackpot
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[124], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[134], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[215], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[235], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[245], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[32010], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 15 Jackpot
        self.set_mesh(triggerIds=[32005], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 15 Jackpot
        self.set_mesh(triggerIds=[33010], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 15 Jackpot
        self.set_mesh(triggerIds=[33005], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 15 Jackpot
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[425], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[444], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 4
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=4)
        self.set_user_value(triggerId=8130, key='Barrier13', value=4)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=5)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=5)
        self.set_user_value(triggerId=8240, key='Barrier24', value=5)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=15) # 15 Jackpot
        self.set_user_value(triggerId=8330, key='Barrier33', value=15) # 15 Jackpot
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=5)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P405TimeLimit', value=1):
            return CheckP405(self.ctx)


class CheckP405(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=4)
        self.set_user_value(triggerId=9130, key='Box13Check', value=4)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=5)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=5)
        self.set_user_value(triggerId=9240, key='Box24Check', value=5)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=15) # 15 Jackpot
        self.set_user_value(triggerId=9330, key='Box33Check', value=15) # 15 Jackpot
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=5)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP405(self.ctx)


class NumberOffP405(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[124], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[134], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[215], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[235], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[245], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[32010], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 15 Jackpot
        self.set_mesh(triggerIds=[32005], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 15 Jackpot
        self.set_mesh(triggerIds=[33010], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 15 Jackpot
        self.set_mesh(triggerIds=[33005], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 15 Jackpot
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[425], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[444], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP405(self.ctx)


class ResetP405(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P405End', value=1)
        self.set_user_value(key='G07P405Set', value=0)
        self.set_user_value(key='G07P405TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P406
class NumberOnP406(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start jackpot
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start jackpot
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[114], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[125], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[144], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[23010], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 15 Jackpot
        self.set_mesh(triggerIds=[23005], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 15 Jackpot
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[315], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[32010], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 	15 Jackpot
        self.set_mesh(triggerIds=[32005], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 	15 Jackpot
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[344], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[424], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[435], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[445], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 5
        self.set_user_value(triggerId=8110, key='Barrier11', value=4)
        self.set_user_value(triggerId=8120, key='Barrier12', value=5)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=4)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=15) # 15 Jackpot
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=5)
        self.set_user_value(triggerId=8320, key='Barrier32', value=15) # 15 Jackpot
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=4)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=4)
        self.set_user_value(triggerId=8430, key='Barrier43', value=5)
        self.set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P406TimeLimit', value=1):
            return CheckP406(self.ctx)


class CheckP406(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=4)
        self.set_user_value(triggerId=9120, key='Box12Check', value=5)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=4)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=15) # 15 Jackpot
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=5)
        self.set_user_value(triggerId=9320, key='Box32Check', value=15) # 15 Jackpot
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=4)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=4)
        self.set_user_value(triggerId=9430, key='Box43Check', value=5)
        self.set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP406(self.ctx)


class NumberOffP406(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[114], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[125], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[144], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[23010], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 15 Jackpot
        self.set_mesh(triggerIds=[23005], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 15 Jackpot
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[315], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[32010], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 	15 Jackpot
        self.set_mesh(triggerIds=[32005], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 	15 Jackpot
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[344], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[424], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[435], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[445], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP406(self.ctx)


class ResetP406(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P406End', value=1)
        self.set_user_value(key='G07P406Set', value=0)
        self.set_user_value(key='G07P406TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G07 P407
class NumberOnP407(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 23 start jackpot
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start jackpot
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[124], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[135], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[144], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[22020], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 20 Jackpot
        self.set_mesh(triggerIds=[22000], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 20 Jackpot
        self.set_mesh(triggerIds=[234], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[314], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[325], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[33020], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 	20 Jackpot
        self.set_mesh(triggerIds=[33000], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 	20 Jackpot
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[424], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[435], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=4)
        self.set_user_value(triggerId=8130, key='Barrier13', value=5)
        self.set_user_value(triggerId=8140, key='Barrier14', value=4)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=20) # 20 Jackpot
        self.set_user_value(triggerId=8230, key='Barrier23', value=4)
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=4)
        self.set_user_value(triggerId=8320, key='Barrier32', value=5)
        self.set_user_value(triggerId=8330, key='Barrier33', value=20) # 20 Jackpot
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=4)
        self.set_user_value(triggerId=8430, key='Barrier43', value=5)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P407TimeLimit', value=1):
            return CheckP407(self.ctx)


class CheckP407(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=4)
        self.set_user_value(triggerId=9130, key='Box13Check', value=5)
        self.set_user_value(triggerId=9140, key='Box14Check', value=4)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=20) # 20 Jackpot
        self.set_user_value(triggerId=9230, key='Box23Check', value=4)
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=4)
        self.set_user_value(triggerId=9320, key='Box32Check', value=5)
        self.set_user_value(triggerId=9330, key='Box33Check', value=20) # 20 Jackpot
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=4)
        self.set_user_value(triggerId=9430, key='Box43Check', value=5)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP407(self.ctx)


class NumberOffP407(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[124], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[135], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[144], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[22020], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 20 Jackpot
        self.set_mesh(triggerIds=[22000], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 20 Jackpot
        self.set_mesh(triggerIds=[234], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[314], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[325], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[33020], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 	20 Jackpot
        self.set_mesh(triggerIds=[33000], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 	20 Jackpot
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[424], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[435], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP407(self.ctx)


class ResetP407(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G07P407End', value=1)
        self.set_user_value(key='G07P407Set', value=0)
        self.set_user_value(key='G07P407TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


initial_state = Wait
