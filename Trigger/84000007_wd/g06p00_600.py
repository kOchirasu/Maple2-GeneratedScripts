""" trigger/84000007_wd/g06p00_600.xml """
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
        if self.user_value(key='G06P101Set', value=1):
            return NumberOnP101(self.ctx)
        if self.user_value(key='G06P102Set', value=1):
            return NumberOnP102(self.ctx)
        if self.user_value(key='G06P103Set', value=1):
            return NumberOnP103(self.ctx)
        if self.user_value(key='G06P104Set', value=1):
            return NumberOnP104(self.ctx)
        if self.user_value(key='G06P105Set', value=1):
            return NumberOnP105(self.ctx)
        if self.user_value(key='G06P106Set', value=1):
            return NumberOnP106(self.ctx)
        if self.user_value(key='G06P107Set', value=1):
            return NumberOnP107(self.ctx)
        if self.user_value(key='G06P108Set', value=1):
            return NumberOnP108(self.ctx)
        if self.user_value(key='G06P109Set', value=1):
            return NumberOnP109(self.ctx)
        if self.user_value(key='G06P110Set', value=1):
            return NumberOnP110(self.ctx)
        if self.user_value(key='G06P201Set', value=1):
            return NumberOnP201(self.ctx)
        if self.user_value(key='G06P202Set', value=1):
            return NumberOnP202(self.ctx)
        if self.user_value(key='G06P203Set', value=1):
            return NumberOnP203(self.ctx)
        if self.user_value(key='G06P204Set', value=1):
            return NumberOnP204(self.ctx)
        if self.user_value(key='G06P205Set', value=1):
            return NumberOnP205(self.ctx)
        if self.user_value(key='G06P206Set', value=1):
            return NumberOnP206(self.ctx)
        if self.user_value(key='G06P207Set', value=1):
            return NumberOnP207(self.ctx)
        if self.user_value(key='G06P208Set', value=1):
            return NumberOnP208(self.ctx)
        if self.user_value(key='G06P209Set', value=1):
            return NumberOnP209(self.ctx)
        if self.user_value(key='G06P210Set', value=1):
            return NumberOnP210(self.ctx)
        if self.user_value(key='G06P211Set', value=1):
            return NumberOnP211(self.ctx)
        if self.user_value(key='G06P212Set', value=1):
            return NumberOnP212(self.ctx)
        if self.user_value(key='G06P213Set', value=1):
            return NumberOnP213(self.ctx)
        if self.user_value(key='G06P214Set', value=1):
            return NumberOnP214(self.ctx)
        if self.user_value(key='G06P215Set', value=1):
            return NumberOnP215(self.ctx)
        if self.user_value(key='G06P216Set', value=1):
            return NumberOnP216(self.ctx)
        if self.user_value(key='G06P217Set', value=1):
            return NumberOnP217(self.ctx)
        if self.user_value(key='G06P218Set', value=1):
            return NumberOnP218(self.ctx)
        if self.user_value(key='G06P219Set', value=1):
            return NumberOnP219(self.ctx)
        if self.user_value(key='G06P220Set', value=1):
            return NumberOnP220(self.ctx)
        if self.user_value(key='G06P301Set', value=1):
            return NumberOnP301(self.ctx)
        if self.user_value(key='G06P302Set', value=1):
            return NumberOnP302(self.ctx)
        if self.user_value(key='G06P303Set', value=1):
            return NumberOnP303(self.ctx)
        if self.user_value(key='G06P304Set', value=1):
            return NumberOnP304(self.ctx)
        if self.user_value(key='G06P305Set', value=1):
            return NumberOnP305(self.ctx)
        if self.user_value(key='G06P306Set', value=1):
            return NumberOnP306(self.ctx)
        if self.user_value(key='G06P307Set', value=1):
            return NumberOnP307(self.ctx)
        if self.user_value(key='G06P308Set', value=1):
            return NumberOnP308(self.ctx)
        if self.user_value(key='G06P309Set', value=1):
            return NumberOnP309(self.ctx)
        if self.user_value(key='G06P310Set', value=1):
            return NumberOnP310(self.ctx)
        if self.user_value(key='G06P311Set', value=1):
            return NumberOnP311(self.ctx)
        if self.user_value(key='G06P312Set', value=1):
            return NumberOnP312(self.ctx)
        if self.user_value(key='G06P313Set', value=1):
            return NumberOnP313(self.ctx)
        if self.user_value(key='G06P314Set', value=1):
            return NumberOnP314(self.ctx)
        if self.user_value(key='G06P315Set', value=1):
            return NumberOnP315(self.ctx)
        if self.user_value(key='G06P316Set', value=1):
            return NumberOnP316(self.ctx)
        if self.user_value(key='G06P317Set', value=1):
            return NumberOnP317(self.ctx)
        if self.user_value(key='G06P318Set', value=1):
            return NumberOnP318(self.ctx)
        if self.user_value(key='G06P319Set', value=1):
            return NumberOnP319(self.ctx)
        if self.user_value(key='G06P320Set', value=1):
            return NumberOnP320(self.ctx)
        if self.user_value(key='G06P401Set', value=1):
            return NumberOnP401(self.ctx)
        if self.user_value(key='G06P402Set', value=1):
            return NumberOnP402(self.ctx)
        if self.user_value(key='G06P403Set', value=1):
            return NumberOnP403(self.ctx)
        if self.user_value(key='G06P404Set', value=1):
            return NumberOnP404(self.ctx)
        if self.user_value(key='G06P405Set', value=1):
            return NumberOnP405(self.ctx)
        if self.user_value(key='G06P406Set', value=1):
            return NumberOnP406(self.ctx)
        if self.user_value(key='G06P407Set', value=1):
            return NumberOnP407(self.ctx)
        if self.user_value(key='G06P408Set', value=1):
            return NumberOnP408(self.ctx)
        if self.user_value(key='G06P409Set', value=1):
            return NumberOnP409(self.ctx)
        if self.user_value(key='G06P410Set', value=1):
            return NumberOnP410(self.ctx)


# G06 P101
class NumberOnP101(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        self.set_mesh(triggerIds=[121], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[141], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[2307], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 7 gamble
        self.set_mesh(triggerIds=[241], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 1
        self.set_mesh(triggerIds=[311], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[321], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[411], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[431], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[441], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 1
        self.set_user_value(triggerId=8110, key='Barrier11', value=1)
        self.set_user_value(triggerId=8120, key='Barrier12', value=1)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=1)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=7) # 7 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=1)
        self.set_user_value(triggerId=8310, key='Barrier31', value=1)
        self.set_user_value(triggerId=8320, key='Barrier32', value=1)
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=1)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=1)
        self.set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P101TimeLimit', value=1):
            return CheckP101(self.ctx)


class CheckP101(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=1)
        self.set_user_value(triggerId=9120, key='Box12Check', value=1)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=1)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=1)
        self.set_user_value(triggerId=9310, key='Box31Check', value=1)
        self.set_user_value(triggerId=9320, key='Box32Check', value=1)
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=1)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=1)
        self.set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP101(self.ctx)


class NumberOffP101(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[111], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 1
        self.set_mesh(triggerIds=[121], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[141], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[2307], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 7 gamble
        self.set_mesh(triggerIds=[241], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 1
        self.set_mesh(triggerIds=[311], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[321], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[411], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[431], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[441], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP101(self.ctx)


class ResetP101(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P101End', value=1)
        self.set_user_value(key='G06P101Set', value=0)
        self.set_user_value(key='G06P101TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P102
class NumberOnP102(trigger_api.Trigger):
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
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[120], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[221], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[3207], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 7 gamble
        self.set_mesh(triggerIds=[330], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[341], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[420], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[431], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=0)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=1)
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=7) # 7 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=0)
        self.set_user_value(triggerId=8340, key='Barrier34', value=1)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=0)
        self.set_user_value(triggerId=8430, key='Barrier43', value=1)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P102TimeLimit', value=1):
            return CheckP102(self.ctx)


class CheckP102(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=0)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=1)
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=0)
        self.set_user_value(triggerId=9340, key='Box34Check', value=1)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=0)
        self.set_user_value(triggerId=9430, key='Box43Check', value=1)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP102(self.ctx)


class NumberOffP102(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[120], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[221], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[3207], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 7 gamble
        self.set_mesh(triggerIds=[330], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[341], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[420], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[431], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP102(self.ctx)


class ResetP102(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P102End', value=1)
        self.set_user_value(key='G06P102Set', value=0)
        self.set_user_value(key='G06P102TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P103
class NumberOnP103(trigger_api.Trigger):
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
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[110], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[221], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[245], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[310], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[325], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[3307], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 7 gamble
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[410], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[430], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[441], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 1
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=1)
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=5)
        self.set_user_value(triggerId=8310, key='Barrier31', value=0)
        self.set_user_value(triggerId=8320, key='Barrier32', value=5)
        self.set_user_value(triggerId=8330, key='Barrier33', value=7) # 7 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=0)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=0)
        self.set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P103TimeLimit', value=1):
            return CheckP103(self.ctx)


class CheckP103(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=1)
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=5)
        self.set_user_value(triggerId=9310, key='Box31Check', value=0)
        self.set_user_value(triggerId=9320, key='Box32Check', value=5)
        self.set_user_value(triggerId=9330, key='Box33Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=0)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=0)
        self.set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP103(self.ctx)


class NumberOffP103(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[221], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[245], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[310], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[325], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[3307], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 7 gamble
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[410], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[430], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[441], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP103(self.ctx)


class ResetP103(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P103End', value=1)
        self.set_user_value(key='G06P103Set', value=0)
        self.set_user_value(key='G06P103TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P104
class NumberOnP104(trigger_api.Trigger):
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
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[111], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 1
        self.set_mesh(triggerIds=[121], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[210], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[230], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 0
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[311], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[3208], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[331], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[340], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[421], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 1
        self.set_mesh(triggerIds=[430], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=1)
        self.set_user_value(triggerId=8120, key='Barrier12', value=1)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=0)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=0)
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=1)
        self.set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=1)
        self.set_user_value(triggerId=8340, key='Barrier34', value=0)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=1)
        self.set_user_value(triggerId=8430, key='Barrier43', value=0)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P104TimeLimit', value=1):
            return CheckP104(self.ctx)


class CheckP104(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=1)
        self.set_user_value(triggerId=9120, key='Box12Check', value=1)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=0)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=0)
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=1)
        self.set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=1)
        self.set_user_value(triggerId=9340, key='Box34Check', value=0)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=1)
        self.set_user_value(triggerId=9430, key='Box43Check', value=0)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP104(self.ctx)


class NumberOffP104(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[111], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 1
        self.set_mesh(triggerIds=[121], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[210], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[230], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 0
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[311], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[3208], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[331], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[340], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[421], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 1
        self.set_mesh(triggerIds=[430], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP104(self.ctx)


class ResetP104(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P104End', value=1)
        self.set_user_value(key='G06P104Set', value=0)
        self.set_user_value(key='G06P104TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P105
class NumberOnP105(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[144], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[210], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[2308], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 8 gamble
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[310], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[410], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[424], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=4)
        self.set_user_value(triggerId=8210, key='Barrier21', value=0)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=8) # 8 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=0)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=0)
        self.set_user_value(triggerId=8420, key='Barrier42', value=4)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P105TimeLimit', value=1):
            return CheckP105(self.ctx)


class CheckP105(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=4)
        self.set_user_value(triggerId=9210, key='Box21Check', value=0)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=0)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=0)
        self.set_user_value(triggerId=9420, key='Box42Check', value=4)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP105(self.ctx)


class NumberOffP105(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[144], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[210], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[2308], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 8 gamble
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[310], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[410], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[424], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP105(self.ctx)


class ResetP105(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P105End', value=1)
        self.set_user_value(key='G06P105Set', value=0)
        self.set_user_value(key='G06P105TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P106
class NumberOnP106(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
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
        self.set_mesh(triggerIds=[120], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[2208], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 8 gamble
        self.set_mesh(triggerIds=[235], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[310], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[325], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[340], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[420], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[430], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=0)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=8) # 8 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=5)
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=0)
        self.set_user_value(triggerId=8320, key='Barrier32', value=5)
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=0)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=0)
        self.set_user_value(triggerId=8430, key='Barrier43', value=0)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P106TimeLimit', value=1):
            return CheckP106(self.ctx)


class CheckP106(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=0)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=5)
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=0)
        self.set_user_value(triggerId=9320, key='Box32Check', value=5)
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=0)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=0)
        self.set_user_value(triggerId=9430, key='Box43Check', value=0)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP106(self.ctx)


class NumberOffP106(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[120], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[2208], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 8 gamble
        self.set_mesh(triggerIds=[235], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[310], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[325], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[340], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[420], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[430], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP106(self.ctx)


class ResetP106(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P106End', value=1)
        self.set_user_value(key='G06P106Set', value=0)
        self.set_user_value(key='G06P106TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P107
class NumberOnP107(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[130], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[210], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[2309], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[310], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[420], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=0)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=0)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=0)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=0)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P107TimeLimit', value=1):
            return CheckP107(self.ctx)


class CheckP107(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=0)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=0)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=0)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=0)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP107(self.ctx)


class NumberOffP107(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[130], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[210], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[2309], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[310], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[420], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP107(self.ctx)


class ResetP107(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P107End', value=1)
        self.set_user_value(key='G06P107Set', value=0)
        self.set_user_value(key='G06P107TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P108
class NumberOnP108(trigger_api.Trigger):
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
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[110], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[221], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[241], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 1
        self.set_mesh(triggerIds=[311], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[3209], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 9 gamble
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[411], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[430], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=1)
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=1)
        self.set_user_value(triggerId=8310, key='Barrier31', value=1)
        self.set_user_value(triggerId=8320, key='Barrier32', value=9) # 9 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=1)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=0)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P108TimeLimit', value=1):
            return CheckP108(self.ctx)


class CheckP108(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=1)
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=1)
        self.set_user_value(triggerId=9310, key='Box31Check', value=1)
        self.set_user_value(triggerId=9320, key='Box32Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=1)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=0)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP108(self.ctx)


class NumberOffP108(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[221], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[241], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 1
        self.set_mesh(triggerIds=[311], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[3209], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 9 gamble
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[411], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[430], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP108(self.ctx)


class ResetP108(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P108End', value=1)
        self.set_user_value(key='G06P108Set', value=0)
        self.set_user_value(key='G06P108TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P109
class NumberOnP109(trigger_api.Trigger):
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
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[110], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[130], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[210], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[225], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[231], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 1
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[310], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[321], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[3309], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 9 gamble
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[420], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[434], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[441], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 1
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=0)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=0)
        self.set_user_value(triggerId=8220, key='Barrier22', value=5)
        self.set_user_value(triggerId=8230, key='Barrier23', value=1)
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=0)
        self.set_user_value(triggerId=8320, key='Barrier32', value=1)
        self.set_user_value(triggerId=8330, key='Barrier33', value=9) # 9 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=0)
        self.set_user_value(triggerId=8430, key='Barrier43', value=4)
        self.set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P109TimeLimit', value=1):
            return CheckP109(self.ctx)


class CheckP109(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=0)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=0)
        self.set_user_value(triggerId=9220, key='Box22Check', value=5)
        self.set_user_value(triggerId=9230, key='Box23Check', value=1)
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=0)
        self.set_user_value(triggerId=9320, key='Box32Check', value=1)
        self.set_user_value(triggerId=9330, key='Box33Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=0)
        self.set_user_value(triggerId=9430, key='Box43Check', value=4)
        self.set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP109(self.ctx)


class NumberOffP109(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[130], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[210], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[225], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[231], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 1
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[310], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[321], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[3309], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 9 gamble
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[420], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[434], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[441], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP109(self.ctx)


class ResetP109(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P109End', value=1)
        self.set_user_value(key='G06P109Set', value=0)
        self.set_user_value(key='G06P109TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P110
class NumberOnP110(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[130], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[145], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[221], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[23010], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[23000], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[240], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[310], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[321], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[334], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[341], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[420], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=0)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=1)
        self.set_user_value(triggerId=8230, key='Barrier23', value=6) # 10 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=0)
        self.set_user_value(triggerId=8310, key='Barrier31', value=0)
        self.set_user_value(triggerId=8320, key='Barrier32', value=1)
        self.set_user_value(triggerId=8330, key='Barrier33', value=4)
        self.set_user_value(triggerId=8340, key='Barrier34', value=1)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=0)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P110TimeLimit', value=1):
            return CheckP110(self.ctx)


class CheckP110(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=0)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=1)
        self.set_user_value(triggerId=9230, key='Box23Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=0)
        self.set_user_value(triggerId=9310, key='Box31Check', value=0)
        self.set_user_value(triggerId=9320, key='Box32Check', value=1)
        self.set_user_value(triggerId=9330, key='Box33Check', value=4)
        self.set_user_value(triggerId=9340, key='Box34Check', value=1)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=0)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP110(self.ctx)


class NumberOffP110(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[130], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[145], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[221], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[23010], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[23000], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[240], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[310], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[321], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[334], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[341], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[420], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP110(self.ctx)


class ResetP110(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P110End', value=1)
        self.set_user_value(key='G06P110Set', value=0)
        self.set_user_value(key='G06P110TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P201
class NumberOnP201(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[124], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[2207], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 7 gamble
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[240], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[310], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[33010], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[33000], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[420], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[434], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=4)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=7) # 7 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=0)
        self.set_user_value(triggerId=8310, key='Barrier31', value=0)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=6) # 10 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=0)
        self.set_user_value(triggerId=8430, key='Barrier43', value=4)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P201TimeLimit', value=1):
            return CheckP201(self.ctx)


class CheckP201(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=4)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=0)
        self.set_user_value(triggerId=9310, key='Box31Check', value=0)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=0)
        self.set_user_value(triggerId=9430, key='Box43Check', value=4)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP201(self.ctx)


class NumberOffP201(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[124], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[2207], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 7 gamble
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[240], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[310], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[33010], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[33000], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[420], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[434], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP201(self.ctx)


class ResetP201(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P201End', value=1)
        self.set_user_value(key='G06P201Set', value=0)
        self.set_user_value(key='G06P201TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P202
class NumberOnP202(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[130], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[2309], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3208], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=0)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P202TimeLimit', value=1):
            return CheckP202(self.ctx)


class CheckP202(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=0)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP202(self.ctx)


class NumberOffP202(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[130], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[2309], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3208], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP202(self.ctx)


class ResetP202(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P202End', value=1)
        self.set_user_value(key='G06P202Set', value=0)
        self.set_user_value(key='G06P202TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P203
class NumberOnP203(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        self.set_mesh(triggerIds=[130], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[145], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[2208], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 8 gamble
        self.set_mesh(triggerIds=[2308], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 8 gamble
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[310], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[410], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[444], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 4
        self.set_user_value(triggerId=8110, key='Barrier11', value=4)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=0)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=8) # 8 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=8) # 8 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=0)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=0)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P203TimeLimit', value=1):
            return CheckP203(self.ctx)


class CheckP203(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=4)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=0)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=0)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=0)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP203(self.ctx)


class NumberOffP203(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[114], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[130], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[145], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[2208], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 8 gamble
        self.set_mesh(triggerIds=[2308], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 8 gamble
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[310], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[410], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[444], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP203(self.ctx)


class ResetP203(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P203End', value=1)
        self.set_user_value(key='G06P203Set', value=0)
        self.set_user_value(key='G06P203TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P204
class NumberOnP204(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[110], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[124], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[22010], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[22000], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[3209], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 9 gamble
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[340], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[424], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[430], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=4)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=6) # 10 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=9) # 9 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=0)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=4)
        self.set_user_value(triggerId=8430, key='Barrier43', value=0)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P204TimeLimit', value=1):
            return CheckP204(self.ctx)


class CheckP204(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=4)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=0)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=4)
        self.set_user_value(triggerId=9430, key='Box43Check', value=0)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP204(self.ctx)


class NumberOffP204(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[124], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[22010], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[22000], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[3209], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 9 gamble
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[340], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[424], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[430], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP204(self.ctx)


class ResetP204(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P204End', value=1)
        self.set_user_value(key='G06P204Set', value=0)
        self.set_user_value(key='G06P204TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P205
class NumberOnP205(trigger_api.Trigger):
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
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[120], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[310], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[32010], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[32000], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[3308], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[444], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 4
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=0)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=0)
        self.set_user_value(triggerId=8320, key='Barrier32', value=6) # 10 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=8) # 8 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P205TimeLimit', value=1):
            return CheckP205(self.ctx)


class CheckP205(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=0)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=0)
        self.set_user_value(triggerId=9320, key='Box32Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP205(self.ctx)


class NumberOffP205(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[120], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[310], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[32010], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[32000], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[3308], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[444], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP205(self.ctx)


class ResetP205(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P205End', value=1)
        self.set_user_value(key='G06P205Set', value=0)
        self.set_user_value(key='G06P205TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P206
class NumberOnP206(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[110], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[120], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[210], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[225], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[2309], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3207], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 7 gamble
        self.set_mesh(triggerIds=[335], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[414], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[430], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=0)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=0)
        self.set_user_value(triggerId=8220, key='Barrier22', value=5)
        self.set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=7) # 7 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=5)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=4)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=0)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P206TimeLimit', value=1):
            return CheckP206(self.ctx)


class CheckP206(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=0)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=0)
        self.set_user_value(triggerId=9220, key='Box22Check', value=5)
        self.set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=5)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=4)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=0)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP206(self.ctx)


class NumberOffP206(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[120], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[210], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[225], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[2309], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3207], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 7 gamble
        self.set_mesh(triggerIds=[335], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[414], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[430], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP206(self.ctx)


class ResetP206(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P206End', value=1)
        self.set_user_value(key='G06P206Set', value=0)
        self.set_user_value(key='G06P206TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P207
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
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[120], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[215], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[224], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 4
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3208], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[3307], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 7 gamble
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[410], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[434], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=0)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=5)
        self.set_user_value(triggerId=8220, key='Barrier22', value=4)
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=7) # 7 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=0)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=4)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P207TimeLimit', value=1):
            return CheckP207(self.ctx)


class CheckP207(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=0)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=5)
        self.set_user_value(triggerId=9220, key='Box22Check', value=4)
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=0)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=4)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP207(self.ctx)


class NumberOffP207(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[120], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[215], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[224], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 4
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3208], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[3307], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 7 gamble
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[410], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[434], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP207(self.ctx)


class ResetP207(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P207End', value=1)
        self.set_user_value(key='G06P207Set', value=0)
        self.set_user_value(key='G06P207TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P208
class NumberOnP208(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[130], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[144], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[2209], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 9 gamble
        self.set_mesh(triggerIds=[234], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[240], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[314], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[322], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[3309], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 9 gamble
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[410], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[430], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=0)
        self.set_user_value(triggerId=8140, key='Barrier14', value=4)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=9) # 9 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=4)
        self.set_user_value(triggerId=8240, key='Barrier24', value=0)
        self.set_user_value(triggerId=8310, key='Barrier31', value=4)
        self.set_user_value(triggerId=8320, key='Barrier32', value=2)
        self.set_user_value(triggerId=8330, key='Barrier33', value=9) # 9 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=0)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=0)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P208TimeLimit', value=1):
            return CheckP208(self.ctx)


class CheckP208(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=0)
        self.set_user_value(triggerId=9140, key='Box14Check', value=4)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=4)
        self.set_user_value(triggerId=9240, key='Box24Check', value=0)
        self.set_user_value(triggerId=9310, key='Box31Check', value=4)
        self.set_user_value(triggerId=9320, key='Box32Check', value=2)
        self.set_user_value(triggerId=9330, key='Box33Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=0)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=0)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP208(self.ctx)


class NumberOffP208(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[130], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[144], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[2209], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 9 gamble
        self.set_mesh(triggerIds=[234], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[240], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[314], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[322], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[3309], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 9 gamble
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[410], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[430], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP208(self.ctx)


class ResetP208(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P208End', value=1)
        self.set_user_value(key='G06P208Set', value=0)
        self.set_user_value(key='G06P208TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P209
class NumberOnP209(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[110], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[134], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[210], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[23010], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[23000], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3207], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 7 gamble
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[344], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=4)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=0)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=6) # 10 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=7) # 7 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=4)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P209TimeLimit', value=1):
            return CheckP209(self.ctx)


class CheckP209(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=4)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=0)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=4)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP209(self.ctx)


class NumberOffP209(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[134], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[210], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[23010], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[23000], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3207], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 7 gamble
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[344], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP209(self.ctx)


class ResetP209(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P209End', value=1)
        self.set_user_value(key='G06P209Set', value=0)
        self.set_user_value(key='G06P209TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P210
class NumberOnP210(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[110], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[22010], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[22000], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[33010], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[33000], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=6) # 10 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=6) # 10 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P210TimeLimit', value=1):
            return CheckP210(self.ctx)


class CheckP210(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP210(self.ctx)


class NumberOffP210(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[22010], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[22000], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[33010], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[33000], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP210(self.ctx)


class ResetP210(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P210End', value=1)
        self.set_user_value(key='G06P210Set', value=0)
        self.set_user_value(key='G06P210TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P211
class NumberOnP211(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[121], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[134], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[2307], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 7 gamble
        self.set_mesh(triggerIds=[245], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[315], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[3207], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 7 gamble
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[410], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[431], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=1)
        self.set_user_value(triggerId=8130, key='Barrier13', value=4)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=7) # 7 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=5)
        self.set_user_value(triggerId=8310, key='Barrier31', value=5)
        self.set_user_value(triggerId=8320, key='Barrier32', value=7) # 7 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=0)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=1)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P211TimeLimit', value=1):
            return CheckP211(self.ctx)


class CheckP211(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=1)
        self.set_user_value(triggerId=9130, key='Box13Check', value=4)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=5)
        self.set_user_value(triggerId=9310, key='Box31Check', value=5)
        self.set_user_value(triggerId=9320, key='Box32Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=0)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=1)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP211(self.ctx)


class NumberOffP211(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[121], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[134], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[2307], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 7 gamble
        self.set_mesh(triggerIds=[245], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[315], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[3207], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 7 gamble
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[410], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[431], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP211(self.ctx)


class ResetP211(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P211End', value=1)
        self.set_user_value(key='G06P211Set', value=0)
        self.set_user_value(key='G06P211TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P212
class NumberOnP212(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[134], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[210], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[2308], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 8 gamble
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[324], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[340], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[410], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=4)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=0)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=8) # 8 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=4)
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=0)
        self.set_user_value(triggerId=8410, key='Barrier41', value=0)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P212TimeLimit', value=1):
            return CheckP212(self.ctx)


class CheckP212(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=4)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=0)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=4)
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=0)
        self.set_user_value(triggerId=9410, key='Box41Check', value=0)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP212(self.ctx)


class NumberOffP212(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[134], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[210], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[2308], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 8 gamble
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[324], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[340], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[410], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP212(self.ctx)


class ResetP212(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P212End', value=1)
        self.set_user_value(key='G06P212Set', value=0)
        self.set_user_value(key='G06P212TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P213
class NumberOnP213(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
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
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[2208], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 8 gamble
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[240], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[322], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[330], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=8) # 8 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=0)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=2)
        self.set_user_value(triggerId=8330, key='Barrier33', value=0)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P213TimeLimit', value=1):
            return CheckP213(self.ctx)


class CheckP213(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=0)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=2)
        self.set_user_value(triggerId=9330, key='Box33Check', value=0)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP213(self.ctx)


class NumberOffP213(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[2208], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 8 gamble
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[240], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[322], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[330], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP213(self.ctx)


class ResetP213(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P213End', value=1)
        self.set_user_value(key='G06P213Set', value=0)
        self.set_user_value(key='G06P213TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P214
class NumberOnP214(trigger_api.Trigger):
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
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[130], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[144], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[221], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[241], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 1
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[322], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[3309], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 9 gamble
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[410], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[435], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[441], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 1
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=0)
        self.set_user_value(triggerId=8140, key='Barrier14', value=4)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=1)
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=1)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=2)
        self.set_user_value(triggerId=8330, key='Barrier33', value=9) # 9 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=0)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=5)
        self.set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P214TimeLimit', value=1):
            return CheckP214(self.ctx)


class CheckP214(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=0)
        self.set_user_value(triggerId=9140, key='Box14Check', value=4)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=1)
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=1)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=2)
        self.set_user_value(triggerId=9330, key='Box33Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=0)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=5)
        self.set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP214(self.ctx)


class NumberOffP214(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[130], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[144], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[221], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[241], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 1
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[322], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[3309], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 9 gamble
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[410], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[435], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[441], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP214(self.ctx)


class ResetP214(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P214End', value=1)
        self.set_user_value(key='G06P214Set', value=0)
        self.set_user_value(key='G06P214TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P215
class NumberOnP215(trigger_api.Trigger):
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
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[131], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[210], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[245], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[310], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[3209], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 9 gamble
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[341], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[431], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=1)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=0)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=5)
        self.set_user_value(triggerId=8310, key='Barrier31', value=0)
        self.set_user_value(triggerId=8320, key='Barrier32', value=9) # 9 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=1)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=1)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P215TimeLimit', value=1):
            return CheckP215(self.ctx)


class CheckP215(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=1)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=0)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=5)
        self.set_user_value(triggerId=9310, key='Box31Check', value=0)
        self.set_user_value(triggerId=9320, key='Box32Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=1)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=1)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP215(self.ctx)


class NumberOffP215(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[131], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[210], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[245], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[310], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[3209], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 9 gamble
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[341], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[431], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP215(self.ctx)


class ResetP215(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P215End', value=1)
        self.set_user_value(key='G06P215Set', value=0)
        self.set_user_value(key='G06P215TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P216
class NumberOnP216(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        self.set_mesh(triggerIds=[121], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[135], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[2309], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[315], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[322], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[331], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[340], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[411], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[425], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=1)
        self.set_user_value(triggerId=8130, key='Barrier13', value=5)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=5)
        self.set_user_value(triggerId=8320, key='Barrier32', value=2)
        self.set_user_value(triggerId=8330, key='Barrier33', value=1)
        self.set_user_value(triggerId=8340, key='Barrier34', value=0)
        self.set_user_value(triggerId=8410, key='Barrier41', value=1)
        self.set_user_value(triggerId=8420, key='Barrier42', value=5)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P216TimeLimit', value=1):
            return CheckP216(self.ctx)


class CheckP216(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=1)
        self.set_user_value(triggerId=9130, key='Box13Check', value=5)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=5)
        self.set_user_value(triggerId=9320, key='Box32Check', value=2)
        self.set_user_value(triggerId=9330, key='Box33Check', value=1)
        self.set_user_value(triggerId=9340, key='Box34Check', value=0)
        self.set_user_value(triggerId=9410, key='Box41Check', value=1)
        self.set_user_value(triggerId=9420, key='Box42Check', value=5)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP216(self.ctx)


class NumberOffP216(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[121], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[135], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[2309], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[315], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[322], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[331], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[340], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[411], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[425], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP216(self.ctx)


class ResetP216(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P216End', value=1)
        self.set_user_value(key='G06P216Set', value=0)
        self.set_user_value(key='G06P216TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P217
class NumberOnP217(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
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
        self.set_mesh(triggerIds=[111], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 1
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[141], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[22010], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[22000], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[230], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 0
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[325], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[411], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[420], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=1)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=1)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=6) # 10 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=0)
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=5)
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=1)
        self.set_user_value(triggerId=8420, key='Barrier42', value=0)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P217TimeLimit', value=1):
            return CheckP217(self.ctx)


class CheckP217(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=1)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=1)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=0)
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=5)
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=1)
        self.set_user_value(triggerId=9420, key='Box42Check', value=0)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP217(self.ctx)


class NumberOffP217(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[111], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 1
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[141], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[22010], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[22000], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[230], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 0
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[325], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[411], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[420], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP217(self.ctx)


class ResetP217(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P217End', value=1)
        self.set_user_value(key='G06P217Set', value=0)
        self.set_user_value(key='G06P217TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P218
class NumberOnP218(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        self.set_mesh(triggerIds=[141], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[211], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[23010], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[23000], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[331], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[344], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[414], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[421], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 1
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=4)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=1)
        self.set_user_value(triggerId=8210, key='Barrier21', value=1)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=6) # 10 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=1)
        self.set_user_value(triggerId=8340, key='Barrier34', value=4)
        self.set_user_value(triggerId=8410, key='Barrier41', value=4)
        self.set_user_value(triggerId=8420, key='Barrier42', value=1)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P218TimeLimit', value=1):
            return CheckP218(self.ctx)


class CheckP218(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=4)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=1)
        self.set_user_value(triggerId=9210, key='Box21Check', value=1)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=1)
        self.set_user_value(triggerId=9340, key='Box34Check', value=4)
        self.set_user_value(triggerId=9410, key='Box41Check', value=4)
        self.set_user_value(triggerId=9420, key='Box42Check', value=1)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP218(self.ctx)


class NumberOffP218(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[114], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[141], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[211], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[23010], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[23000], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[331], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[344], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[414], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[421], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 1
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP218(self.ctx)


class ResetP218(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P218End', value=1)
        self.set_user_value(key='G06P218Set', value=0)
        self.set_user_value(key='G06P218TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P219
class NumberOnP219(trigger_api.Trigger):
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
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[130], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[220], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 0
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[32010], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[32000], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[420], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=0)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=0)
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=6) # 10 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=0)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P219TimeLimit', value=1):
            return CheckP219(self.ctx)


class CheckP219(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=0)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=0)
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=0)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP219(self.ctx)


class NumberOffP219(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[130], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[220], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 0
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[32010], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[32000], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[420], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP219(self.ctx)


class ResetP219(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P219End', value=1)
        self.set_user_value(key='G06P219Set', value=0)
        self.set_user_value(key='G06P219TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P220
class NumberOnP220(trigger_api.Trigger):
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
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[125], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[235], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[241], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 1
        self.set_mesh(triggerIds=[310], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[33010], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[33000], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[424], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[430], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[441], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 1
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=5)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=5)
        self.set_user_value(triggerId=8240, key='Barrier24', value=1)
        self.set_user_value(triggerId=8310, key='Barrier31', value=0)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=6) # 10 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=4)
        self.set_user_value(triggerId=8430, key='Barrier43', value=0)
        self.set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P220TimeLimit', value=1):
            return CheckP220(self.ctx)


class CheckP220(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=5)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=5)
        self.set_user_value(triggerId=9240, key='Box24Check', value=1)
        self.set_user_value(triggerId=9310, key='Box31Check', value=0)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=4)
        self.set_user_value(triggerId=9430, key='Box43Check', value=0)
        self.set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP220(self.ctx)


class NumberOffP220(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[125], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[235], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[241], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 1
        self.set_mesh(triggerIds=[310], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[33010], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[33000], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[424], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[430], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[441], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP220(self.ctx)


class ResetP220(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P220End', value=1)
        self.set_user_value(key='G06P220Set', value=0)
        self.set_user_value(key='G06P220TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P301
class NumberOnP301(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[135], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[23010], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[23000], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[32010], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[32000], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[344], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[425], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=5)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=6) # 10 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=6) # 10 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=4)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=5)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P301TimeLimit', value=1):
            return CheckP301(self.ctx)


class CheckP301(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=5)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=4)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=5)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP301(self.ctx)


class NumberOffP301(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[135], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[23010], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[23000], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[32010], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[32000], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[344], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[425], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP301(self.ctx)


class ResetP301(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P301End', value=1)
        self.set_user_value(key='G06P301Set', value=0)
        self.set_user_value(key='G06P301TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P302
class NumberOnP302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[125], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[144], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[2208], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 8 gamble
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[324], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[33010], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[33000], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[414], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[435], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=5)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=4)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=8) # 8 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=4)
        self.set_user_value(triggerId=8330, key='Barrier33', value=6) # 10 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=4)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=5)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P302TimeLimit', value=1):
            return CheckP302(self.ctx)


class CheckP302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=5)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=4)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=4)
        self.set_user_value(triggerId=9330, key='Box33Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=4)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=5)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP302(self.ctx)


class NumberOffP302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[125], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[144], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[2208], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 8 gamble
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[324], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[33010], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[33000], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[414], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[435], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP302(self.ctx)


class ResetP302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P302End', value=1)
        self.set_user_value(key='G06P302Set', value=0)
        self.set_user_value(key='G06P302TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P303
class NumberOnP303(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[22010], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[22000], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[2309], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[315], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[434], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=4)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=6) # 10 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=5)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=4)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P303TimeLimit', value=1):
            return CheckP303(self.ctx)


class CheckP303(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=4)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=5)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=4)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP303(self.ctx)


class NumberOffP303(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[124], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[22010], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[22000], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[2309], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[315], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[434], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP303(self.ctx)


class ResetP303(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P303End', value=1)
        self.set_user_value(key='G06P303Set', value=0)
        self.set_user_value(key='G06P303TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P304
class NumberOnP304(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
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
        self.set_mesh(triggerIds=[145], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[225], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[2309], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[32010], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[32000], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=5)
        self.set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=6) # 10 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P304TimeLimit', value=1):
            return CheckP304(self.ctx)


class CheckP304(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=5)
        self.set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP304(self.ctx)


class NumberOffP304(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[145], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[225], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[2309], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[32010], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[32000], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP304(self.ctx)


class ResetP304(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P304End', value=1)
        self.set_user_value(key='G06P304Set', value=0)
        self.set_user_value(key='G06P304TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P305
class NumberOnP305(trigger_api.Trigger):
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
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
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
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3209], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 9 gamble
        self.set_mesh(triggerIds=[3309], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 9 gamble
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[444], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 4
        self.set_user_value(triggerId=8110, key='Barrier11', value=4)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=9) # 9 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=9) # 9 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P305TimeLimit', value=1):
            return CheckP305(self.ctx)


class CheckP305(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=4)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
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
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3209], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 9 gamble
        self.set_mesh(triggerIds=[3309], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 9 gamble
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[444], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP305(self.ctx)


class ResetP305(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P305End', value=1)
        self.set_user_value(key='G06P305Set', value=0)
        self.set_user_value(key='G06P305TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P306
class NumberOnP306(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        self.set_mesh(triggerIds=[135], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[22010], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[22000], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[23010], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[23000], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[245], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[324], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[414], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=4)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=5)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=6) # 10 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=6) # 10 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=5)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=4)
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=4)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P306TimeLimit', value=1):
            return CheckP306(self.ctx)


class CheckP306(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=4)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=5)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=5)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=4)
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=4)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP306(self.ctx)


class NumberOffP306(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[114], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[135], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[22010], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[22000], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[23010], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[23000], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[245], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[324], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[414], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP306(self.ctx)


class ResetP306(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P306End', value=1)
        self.set_user_value(key='G06P306Set', value=0)
        self.set_user_value(key='G06P306TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P307
class NumberOnP307(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[144], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[23010], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[23000], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[314], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[3208], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[3307], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 7 gamble
        self.set_mesh(triggerIds=[344], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[424], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=4)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=6) # 10 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=4)
        self.set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=7) # 7 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=4)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=4)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P307TimeLimit', value=1):
            return CheckP307(self.ctx)


class CheckP307(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=4)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=4)
        self.set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=4)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=4)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP307(self.ctx)


class NumberOffP307(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[144], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[23010], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[23000], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[314], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[3208], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[3307], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 7 gamble
        self.set_mesh(triggerIds=[344], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[424], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP307(self.ctx)


class ResetP307(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P307End', value=1)
        self.set_user_value(key='G06P307Set', value=0)
        self.set_user_value(key='G06P307TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P308
class NumberOnP308(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[124], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[145], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[2207], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 7 gamble
        self.set_mesh(triggerIds=[2308], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 8 gamble
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[314], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[3209], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 9 gamble
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[425], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=4)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=7) # 7 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=8) # 8 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=4)
        self.set_user_value(triggerId=8320, key='Barrier32', value=9) # 9 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=5)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P308TimeLimit', value=1):
            return CheckP308(self.ctx)


class CheckP308(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=4)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=4)
        self.set_user_value(triggerId=9320, key='Box32Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=5)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP308(self.ctx)


class NumberOffP308(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[124], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[145], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[2207], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 7 gamble
        self.set_mesh(triggerIds=[2308], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 8 gamble
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[314], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[3209], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 9 gamble
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[425], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP308(self.ctx)


class ResetP308(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P308End', value=1)
        self.set_user_value(key='G06P308Set', value=0)
        self.set_user_value(key='G06P308TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P309
class NumberOnP309(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
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
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[2208], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 8 gamble
        self.set_mesh(triggerIds=[2308], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 8 gamble
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[3208], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[334], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[414], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[434], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[444], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 4
        self.set_user_value(triggerId=8110, key='Barrier11', value=4)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=8) # 8 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=8) # 8 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=4)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=4)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=4)
        self.set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P309TimeLimit', value=1):
            return CheckP309(self.ctx)


class CheckP309(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=4)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=4)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=4)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=4)
        self.set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP309(self.ctx)


class NumberOffP309(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[114], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[2208], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 8 gamble
        self.set_mesh(triggerIds=[2308], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 8 gamble
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[3208], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[334], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[414], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[434], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[444], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP309(self.ctx)


class ResetP309(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P309End', value=1)
        self.set_user_value(key='G06P309Set', value=0)
        self.set_user_value(key='G06P309TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P310
class NumberOnP310(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
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
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[2307], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 7 gamble
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3207], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 7 gamble
        self.set_mesh(triggerIds=[3307], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 7 gamble
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[414], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=4)
        self.set_user_value(triggerId=8130, key='Barrier13', value=4)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=7) # 7 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=7) # 7 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=7) # 7 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=4)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P310TimeLimit', value=1):
            return CheckP310(self.ctx)


class CheckP310(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=4)
        self.set_user_value(triggerId=9130, key='Box13Check', value=4)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=4)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP310(self.ctx)


class NumberOffP310(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[124], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[134], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[2307], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 7 gamble
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3207], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 7 gamble
        self.set_mesh(triggerIds=[3307], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 7 gamble
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[414], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP310(self.ctx)


class ResetP310(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P310End', value=1)
        self.set_user_value(key='G06P310Set', value=0)
        self.set_user_value(key='G06P310TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P311
class NumberOnP311(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[115], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 5
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[141], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[211], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[224], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 4
        self.set_mesh(triggerIds=[23010], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[23000], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[33010], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[33000], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[344], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[424], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[445], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 5
        self.set_user_value(triggerId=8110, key='Barrier11', value=5)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=1)
        self.set_user_value(triggerId=8210, key='Barrier21', value=1)
        self.set_user_value(triggerId=8220, key='Barrier22', value=4)
        self.set_user_value(triggerId=8230, key='Barrier23', value=6) # 10 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=6) # 10 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=4)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=4)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P311TimeLimit', value=1):
            return CheckP311(self.ctx)


class CheckP311(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=5)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=1)
        self.set_user_value(triggerId=9210, key='Box21Check', value=1)
        self.set_user_value(triggerId=9220, key='Box22Check', value=4)
        self.set_user_value(triggerId=9230, key='Box23Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=4)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=4)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP311(self.ctx)


class NumberOffP311(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[115], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 5
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[141], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[211], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[224], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 4
        self.set_mesh(triggerIds=[23010], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[23000], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[33010], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[33000], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[344], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[424], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[445], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP311(self.ctx)


class ResetP311(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P311End', value=1)
        self.set_user_value(key='G06P311Set', value=0)
        self.set_user_value(key='G06P311TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P312
class NumberOnP312(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[134], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[215], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[22010], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[22000], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[311], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[322], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[33010], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[33000], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[424], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[431], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=4)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=5)
        self.set_user_value(triggerId=8220, key='Barrier22', value=6) # 10 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=1)
        self.set_user_value(triggerId=8320, key='Barrier32', value=2)
        self.set_user_value(triggerId=8330, key='Barrier33', value=6) # 10 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=4)
        self.set_user_value(triggerId=8430, key='Barrier43', value=1)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P312TimeLimit', value=1):
            return CheckP312(self.ctx)


class CheckP312(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=4)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=5)
        self.set_user_value(triggerId=9220, key='Box22Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=1)
        self.set_user_value(triggerId=9320, key='Box32Check', value=2)
        self.set_user_value(triggerId=9330, key='Box33Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=4)
        self.set_user_value(triggerId=9430, key='Box43Check', value=1)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP312(self.ctx)


class NumberOffP312(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[134], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[215], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[22010], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[22000], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[311], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[322], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[33010], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[33000], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[424], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[431], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP312(self.ctx)


class ResetP312(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P312End', value=1)
        self.set_user_value(key='G06P312Set', value=0)
        self.set_user_value(key='G06P312TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P313
class NumberOnP313(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[2208], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 8 gamble
        self.set_mesh(triggerIds=[234], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[3208], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[344], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[434], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=8) # 8 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=4)
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=4)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=4)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P313TimeLimit', value=1):
            return CheckP313(self.ctx)


class CheckP313(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=4)
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=4)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=4)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP313(self.ctx)


class NumberOffP313(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[2208], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 8 gamble
        self.set_mesh(triggerIds=[234], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[3208], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[344], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[434], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP313(self.ctx)


class ResetP313(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P313End', value=1)
        self.set_user_value(key='G06P313Set', value=0)
        self.set_user_value(key='G06P313TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P314
class NumberOnP314(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[135], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[224], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 4
        self.set_mesh(triggerIds=[2309], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[314], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[322], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[3309], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 9 gamble
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[425], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=5)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=4)
        self.set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=4)
        self.set_user_value(triggerId=8320, key='Barrier32', value=2)
        self.set_user_value(triggerId=8330, key='Barrier33', value=9) # 9 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=5)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P314TimeLimit', value=1):
            return CheckP314(self.ctx)


class CheckP314(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=5)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=4)
        self.set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=4)
        self.set_user_value(triggerId=9320, key='Box32Check', value=2)
        self.set_user_value(triggerId=9330, key='Box33Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=5)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP314(self.ctx)


class NumberOffP314(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[135], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[224], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 4
        self.set_mesh(triggerIds=[2309], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[314], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[322], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[3309], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 9 gamble
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[425], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP314(self.ctx)


class ResetP314(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P314End', value=1)
        self.set_user_value(key='G06P314Set', value=0)
        self.set_user_value(key='G06P314TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P315
class NumberOnP315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
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
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[2207], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 7 gamble
        self.set_mesh(triggerIds=[235], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[325], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[3307], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 7 gamble
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[434], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=4)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=4)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=7) # 7 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=5)
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=5)
        self.set_user_value(triggerId=8330, key='Barrier33', value=7) # 7 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=4)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P315TimeLimit', value=1):
            return CheckP315(self.ctx)


class CheckP315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=4)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=4)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=5)
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=5)
        self.set_user_value(triggerId=9330, key='Box33Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=4)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP315(self.ctx)


class NumberOffP315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[114], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[144], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[2207], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 7 gamble
        self.set_mesh(triggerIds=[235], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[325], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[3307], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 7 gamble
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[434], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP315(self.ctx)


class ResetP315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P315End', value=1)
        self.set_user_value(key='G06P315Set', value=0)
        self.set_user_value(key='G06P315TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P316
class NumberOnP316(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[125], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[131], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[144], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[2307], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 7 gamble
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3208], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[334], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[414], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[421], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 1
        self.set_mesh(triggerIds=[435], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=5)
        self.set_user_value(triggerId=8130, key='Barrier13', value=1)
        self.set_user_value(triggerId=8140, key='Barrier14', value=4)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=7) # 7 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=4)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=4)
        self.set_user_value(triggerId=8420, key='Barrier42', value=1)
        self.set_user_value(triggerId=8430, key='Barrier43', value=5)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P316TimeLimit', value=1):
            return CheckP316(self.ctx)


class CheckP316(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=5)
        self.set_user_value(triggerId=9130, key='Box13Check', value=1)
        self.set_user_value(triggerId=9140, key='Box14Check', value=4)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=4)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=4)
        self.set_user_value(triggerId=9420, key='Box42Check', value=1)
        self.set_user_value(triggerId=9430, key='Box43Check', value=5)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP316(self.ctx)


class NumberOffP316(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[125], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[131], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[144], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[2307], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 7 gamble
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3208], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[334], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[414], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[421], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 1
        self.set_mesh(triggerIds=[435], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP316(self.ctx)


class ResetP316(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P316End', value=1)
        self.set_user_value(key='G06P316Set', value=0)
        self.set_user_value(key='G06P316TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P317
class NumberOnP317(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[111], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 1
        self.set_mesh(triggerIds=[125], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[145], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[2309], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[311], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[322], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[3308], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 8 gamble
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[435], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[441], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 1
        self.set_user_value(triggerId=8110, key='Barrier11', value=1)
        self.set_user_value(triggerId=8120, key='Barrier12', value=5)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=1)
        self.set_user_value(triggerId=8320, key='Barrier32', value=2)
        self.set_user_value(triggerId=8330, key='Barrier33', value=8) # 8 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=5)
        self.set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P317TimeLimit', value=1):
            return CheckP317(self.ctx)


class CheckP317(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=1)
        self.set_user_value(triggerId=9120, key='Box12Check', value=5)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=1)
        self.set_user_value(triggerId=9320, key='Box32Check', value=2)
        self.set_user_value(triggerId=9330, key='Box33Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=5)
        self.set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP317(self.ctx)


class NumberOffP317(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[111], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 1
        self.set_mesh(triggerIds=[125], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[145], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[2309], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[311], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[322], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[3308], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 8 gamble
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[435], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[441], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP317(self.ctx)


class ResetP317(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P317End', value=1)
        self.set_user_value(key='G06P317Set', value=0)
        self.set_user_value(key='G06P317TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P318
class NumberOnP318(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
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
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[2208], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 8 gamble
        self.set_mesh(triggerIds=[234], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[314], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[3207], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 7 gamble
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[344], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[410], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[445], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 5
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=4)
        self.set_user_value(triggerId=8130, key='Barrier13', value=5)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=8) # 8 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=4)
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=4)
        self.set_user_value(triggerId=8320, key='Barrier32', value=7) # 7 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=4)
        self.set_user_value(triggerId=8410, key='Barrier41', value=0)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P318TimeLimit', value=1):
            return CheckP318(self.ctx)


class CheckP318(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=4)
        self.set_user_value(triggerId=9130, key='Box13Check', value=5)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=4)
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=4)
        self.set_user_value(triggerId=9320, key='Box32Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=4)
        self.set_user_value(triggerId=9410, key='Box41Check', value=0)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP318(self.ctx)


class NumberOffP318(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[124], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[135], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[2208], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 8 gamble
        self.set_mesh(triggerIds=[234], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[314], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[3207], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 7 gamble
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[344], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[410], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[445], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP318(self.ctx)


class ResetP318(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P318End', value=1)
        self.set_user_value(key='G06P318Set', value=0)
        self.set_user_value(key='G06P318TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P319
class NumberOnP319(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[114], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[130], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[215], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[2308], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 8 gamble
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3209], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 9 gamble
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[414], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[425], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=4)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=0)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=5)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=8) # 8 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=9) # 9 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=4)
        self.set_user_value(triggerId=8420, key='Barrier42', value=5)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P319TimeLimit', value=1):
            return CheckP319(self.ctx)


class CheckP319(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=4)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=0)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=5)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=4)
        self.set_user_value(triggerId=9420, key='Box42Check', value=5)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP319(self.ctx)


class NumberOffP319(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[114], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[130], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[215], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[2308], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 8 gamble
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3209], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 9 gamble
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[414], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[425], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP319(self.ctx)


class ResetP319(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P319End', value=1)
        self.set_user_value(key='G06P319Set', value=0)
        self.set_user_value(key='G06P319TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P320
class NumberOnP320(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[131], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[145], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[211], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[2209], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 9 gamble
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[245], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[315], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[321], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[3309], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 9 gamble
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[425], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=1)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=1)
        self.set_user_value(triggerId=8220, key='Barrier22', value=9) # 9 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=5)
        self.set_user_value(triggerId=8310, key='Barrier31', value=5)
        self.set_user_value(triggerId=8320, key='Barrier32', value=1)
        self.set_user_value(triggerId=8330, key='Barrier33', value=9) # 9 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=5)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P320TimeLimit', value=1):
            return CheckP320(self.ctx)


class CheckP320(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=1)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=1)
        self.set_user_value(triggerId=9220, key='Box22Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=5)
        self.set_user_value(triggerId=9310, key='Box31Check', value=5)
        self.set_user_value(triggerId=9320, key='Box32Check', value=1)
        self.set_user_value(triggerId=9330, key='Box33Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=5)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP320(self.ctx)


class NumberOffP320(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[131], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[145], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[211], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[2209], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 9 gamble
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[245], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[315], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[321], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[3309], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 9 gamble
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[425], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP320(self.ctx)


class ResetP320(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P320End', value=1)
        self.set_user_value(key='G06P320Set', value=0)
        self.set_user_value(key='G06P320TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P401
class NumberOnP401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[115], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 5
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[135], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[145], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[2209], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 9 gamble
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[245], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[315], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[3208], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[3307], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 7 gamble
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[445], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 5
        self.set_user_value(triggerId=8110, key='Barrier11', value=5)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=5)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=9) # 9 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=5)
        self.set_user_value(triggerId=8310, key='Barrier31', value=5)
        self.set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=7) # 7 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P401TimeLimit', value=1):
            return CheckP401(self.ctx)


class CheckP401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=5)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=5)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=5)
        self.set_user_value(triggerId=9310, key='Box31Check', value=5)
        self.set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP401(self.ctx)


class NumberOffP401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[115], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 5
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[135], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[145], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[2209], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 9 gamble
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[245], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[315], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[3208], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[3307], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 7 gamble
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[445], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP401(self.ctx)


class ResetP401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P401End', value=1)
        self.set_user_value(key='G06P401Set', value=0)
        self.set_user_value(key='G06P401TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P402
class NumberOnP402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[115], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 5
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[134], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[145], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[2209], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 9 gamble
        self.set_mesh(triggerIds=[23010], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[23000], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[245], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3208], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[434], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[445], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 5
        self.set_user_value(triggerId=8110, key='Barrier11', value=5)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=4)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=9) # 9 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=6) # 10 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=5)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=4)
        self.set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P402TimeLimit', value=1):
            return CheckP402(self.ctx)


class CheckP402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=5)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=4)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=5)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=4)
        self.set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP402(self.ctx)


class NumberOffP402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[115], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 5
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[134], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[145], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[2209], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 9 gamble
        self.set_mesh(triggerIds=[23010], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[23000], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[245], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3208], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[434], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[445], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP402(self.ctx)


class ResetP402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P402End', value=1)
        self.set_user_value(key='G06P402Set', value=0)
        self.set_user_value(key='G06P402TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P403
class NumberOnP403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[115], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 5
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[145], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[2207], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 7 gamble
        self.set_mesh(triggerIds=[2309], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[315], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[322], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[33010], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[33000], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[344], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[425], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[445], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 5
        self.set_user_value(triggerId=8110, key='Barrier11', value=5)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=7) # 7 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=5)
        self.set_user_value(triggerId=8320, key='Barrier32', value=2)
        self.set_user_value(triggerId=8330, key='Barrier33', value=6) # 10 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=4)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=5)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P403TimeLimit', value=1):
            return CheckP403(self.ctx)


class CheckP403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=5)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=5)
        self.set_user_value(triggerId=9320, key='Box32Check', value=2)
        self.set_user_value(triggerId=9330, key='Box33Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=4)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=5)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP403(self.ctx)


class NumberOffP403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[115], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 5
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[145], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[2207], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 7 gamble
        self.set_mesh(triggerIds=[2309], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[315], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[322], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[33010], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[33000], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[344], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[425], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[445], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP403(self.ctx)


class ResetP403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P403End', value=1)
        self.set_user_value(key='G06P403Set', value=0)
        self.set_user_value(key='G06P403TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P404
class NumberOnP404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[115], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 5
        self.set_mesh(triggerIds=[124], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[145], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[225], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[23010], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[23000], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[315], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[32010], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[32000], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[33010], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[33000], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[425], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=5)
        self.set_user_value(triggerId=8120, key='Barrier12', value=4)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=5)
        self.set_user_value(triggerId=8230, key='Barrier23', value=6) # 10 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=5)
        self.set_user_value(triggerId=8320, key='Barrier32', value=6) # 10 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=6) # 10 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=5)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P404TimeLimit', value=1):
            return CheckP404(self.ctx)


class CheckP404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=5)
        self.set_user_value(triggerId=9120, key='Box12Check', value=4)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=5)
        self.set_user_value(triggerId=9230, key='Box23Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=5)
        self.set_user_value(triggerId=9320, key='Box32Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=5)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP404(self.ctx)


class NumberOffP404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[115], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 5
        self.set_mesh(triggerIds=[124], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[145], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[225], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[23010], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[23000], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 10 gamble
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[315], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[32010], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[32000], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[33010], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[33000], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[425], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP404(self.ctx)


class ResetP404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P404End', value=1)
        self.set_user_value(key='G06P404Set', value=0)
        self.set_user_value(key='G06P404TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P405
class NumberOnP405(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[125], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[135], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[215], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[2209], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 9 gamble
        self.set_mesh(triggerIds=[2309], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[3209], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 9 gamble
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[425], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[445], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 5
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=5)
        self.set_user_value(triggerId=8130, key='Barrier13', value=5)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=5)
        self.set_user_value(triggerId=8220, key='Barrier22', value=9) # 9 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=9) # 9 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=5)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P405TimeLimit', value=1):
            return CheckP405(self.ctx)


class CheckP405(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=5)
        self.set_user_value(triggerId=9130, key='Box13Check', value=5)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=5)
        self.set_user_value(triggerId=9220, key='Box22Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=5)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP405(self.ctx)


class NumberOffP405(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[125], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[135], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[215], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[2209], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 9 gamble
        self.set_mesh(triggerIds=[2309], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 9 gamble
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[3209], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 9 gamble
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[425], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[445], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP405(self.ctx)


class ResetP405(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P405End', value=1)
        self.set_user_value(key='G06P405Set', value=0)
        self.set_user_value(key='G06P405TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P406
class NumberOnP406(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[115], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 5
        self.set_mesh(triggerIds=[125], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[145], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[2308], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 8 gamble
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3208], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[3308], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 8 gamble
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[424], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[445], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 5
        self.set_user_value(triggerId=8110, key='Barrier11', value=5)
        self.set_user_value(triggerId=8120, key='Barrier12', value=5)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=8) # 8 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=8) # 8 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=4)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P406TimeLimit', value=1):
            return CheckP406(self.ctx)


class CheckP406(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=5)
        self.set_user_value(triggerId=9120, key='Box12Check', value=5)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=4)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP406(self.ctx)


class NumberOffP406(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[115], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 5
        self.set_mesh(triggerIds=[125], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[145], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[2308], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 8 gamble
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[3208], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 8 gamble
        self.set_mesh(triggerIds=[3308], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 8 gamble
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[424], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[445], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP406(self.ctx)


class ResetP406(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P406End', value=1)
        self.set_user_value(key='G06P406Set', value=0)
        self.set_user_value(key='G06P406TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P407
class NumberOnP407(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[114], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[135], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[215], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[2208], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 8 gamble
        self.set_mesh(triggerIds=[2308], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 8 gamble
        self.set_mesh(triggerIds=[245], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[315], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[325], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[3309], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 9 gamble
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[414], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[435], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[444], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 4
        self.set_user_value(triggerId=8110, key='Barrier11', value=4)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=5)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=5)
        self.set_user_value(triggerId=8220, key='Barrier22', value=8) # 8 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=8) # 8 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=5)
        self.set_user_value(triggerId=8310, key='Barrier31', value=5)
        self.set_user_value(triggerId=8320, key='Barrier32', value=5)
        self.set_user_value(triggerId=8330, key='Barrier33', value=9) # 9 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=4)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=5)
        self.set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P407TimeLimit', value=1):
            return CheckP407(self.ctx)


class CheckP407(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=4)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=5)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=5)
        self.set_user_value(triggerId=9220, key='Box22Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=5)
        self.set_user_value(triggerId=9310, key='Box31Check', value=5)
        self.set_user_value(triggerId=9320, key='Box32Check', value=5)
        self.set_user_value(triggerId=9330, key='Box33Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=4)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=5)
        self.set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP407(self.ctx)


class NumberOffP407(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[114], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[135], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[215], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[2208], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 8 gamble
        self.set_mesh(triggerIds=[2308], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 8 gamble
        self.set_mesh(triggerIds=[245], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[315], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[325], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[3309], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 9 gamble
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[414], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[435], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[444], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP407(self.ctx)


class ResetP407(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P407End', value=1)
        self.set_user_value(key='G06P407Set', value=0)
        self.set_user_value(key='G06P407TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P408
class NumberOnP408(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[125], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[134], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[145], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[22010], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[22000], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[235], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[314], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[32010], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[32000], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[3307], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 7 gamble
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[435], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[444], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 4
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=5)
        self.set_user_value(triggerId=8130, key='Barrier13', value=4)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=6) # 10 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=5)
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=4)
        self.set_user_value(triggerId=8320, key='Barrier32', value=6) # 10 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=7) # 7 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=5)
        self.set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P408TimeLimit', value=1):
            return CheckP408(self.ctx)


class CheckP408(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=5)
        self.set_user_value(triggerId=9130, key='Box13Check', value=4)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=5)
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=4)
        self.set_user_value(triggerId=9320, key='Box32Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=7) # 7 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=5)
        self.set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP408(self.ctx)


class NumberOffP408(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[125], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[134], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[145], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[22010], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[22000], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[235], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[314], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[32010], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[32000], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 10 gamble
        self.set_mesh(triggerIds=[3307], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 7 gamble
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[435], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[444], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP408(self.ctx)


class ResetP408(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P408End', value=1)
        self.set_user_value(key='G06P408Set', value=0)
        self.set_user_value(key='G06P408TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P409
class NumberOnP409(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[114], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[124], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[135], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[2209], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 9 gamble
        self.set_mesh(triggerIds=[2308], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 8 gamble
        self.set_mesh(triggerIds=[245], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[324], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[3309], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 9 gamble
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[414], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[424], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[435], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=4)
        self.set_user_value(triggerId=8120, key='Barrier12', value=4)
        self.set_user_value(triggerId=8130, key='Barrier13', value=5)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=9) # 9 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=8) # 8 gamble
        self.set_user_value(triggerId=8240, key='Barrier24', value=5)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=4)
        self.set_user_value(triggerId=8330, key='Barrier33', value=9) # 9 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=4)
        self.set_user_value(triggerId=8420, key='Barrier42', value=4)
        self.set_user_value(triggerId=8430, key='Barrier43', value=5)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P409TimeLimit', value=1):
            return CheckP409(self.ctx)


class CheckP409(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=4)
        self.set_user_value(triggerId=9120, key='Box12Check', value=4)
        self.set_user_value(triggerId=9130, key='Box13Check', value=5)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=8) # 8 gamble
        self.set_user_value(triggerId=9240, key='Box24Check', value=5)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=4)
        self.set_user_value(triggerId=9330, key='Box33Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=4)
        self.set_user_value(triggerId=9420, key='Box42Check', value=4)
        self.set_user_value(triggerId=9430, key='Box43Check', value=5)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP409(self.ctx)


class NumberOffP409(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[114], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[124], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[135], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[2209], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 9 gamble
        self.set_mesh(triggerIds=[2308], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 8 gamble
        self.set_mesh(triggerIds=[245], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[324], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[3309], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 9 gamble
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[414], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[424], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[435], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP409(self.ctx)


class ResetP409(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P409End', value=1)
        self.set_user_value(key='G06P409Set', value=0)
        self.set_user_value(key='G06P409TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G06 P410
class NumberOnP410(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        self.set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        self.set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        self.set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[125], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[135], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[215], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[22010], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[22000], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[234], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[314], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[3209], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 9 gamble
        self.set_mesh(triggerIds=[33010], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[33000], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[425], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[435], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=5)
        self.set_user_value(triggerId=8130, key='Barrier13', value=5)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=5)
        self.set_user_value(triggerId=8220, key='Barrier22', value=6) # 10 gamble
        self.set_user_value(triggerId=8230, key='Barrier23', value=4)
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=4)
        self.set_user_value(triggerId=8320, key='Barrier32', value=9) # 9 gamble
        self.set_user_value(triggerId=8330, key='Barrier33', value=6) # 10 gamble
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=5)
        self.set_user_value(triggerId=8430, key='Barrier43', value=5)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G06P410TimeLimit', value=1):
            return CheckP410(self.ctx)


class CheckP410(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=5)
        self.set_user_value(triggerId=9130, key='Box13Check', value=5)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=5)
        self.set_user_value(triggerId=9220, key='Box22Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9230, key='Box23Check', value=4)
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=4)
        self.set_user_value(triggerId=9320, key='Box32Check', value=9) # 9 gamble
        self.set_user_value(triggerId=9330, key='Box33Check', value=6) # 10 gamble
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=5)
        self.set_user_value(triggerId=9430, key='Box43Check', value=5)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP410(self.ctx)


class NumberOffP410(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[125], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[135], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[215], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[22010], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[22000], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 10 gamble
        self.set_mesh(triggerIds=[234], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[314], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[3209], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 9 gamble
        self.set_mesh(triggerIds=[33010], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[33000], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 10 gamble
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[425], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[435], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP410(self.ctx)


class ResetP410(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G06P410End', value=1)
        self.set_user_value(key='G06P410Set', value=0)
        self.set_user_value(key='G06P410TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


initial_state = Wait
