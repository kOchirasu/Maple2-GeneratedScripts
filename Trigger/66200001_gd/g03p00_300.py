""" trigger/66200001_gd/g03p00_300.xml """
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

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P01Set', value=1):
            return NumberOnP01(self.ctx)
        if self.user_value(key='G03P02Set', value=1):
            return NumberOnP02(self.ctx)
        if self.user_value(key='G03P03Set', value=1):
            return NumberOnP03(self.ctx)
        if self.user_value(key='G03P04Set', value=1):
            return NumberOnP04(self.ctx)
        if self.user_value(key='G03P05Set', value=1):
            return NumberOnP05(self.ctx)
        if self.user_value(key='G03P06Set', value=1):
            return NumberOnP06(self.ctx)
        if self.user_value(key='G03P07Set', value=1):
            return NumberOnP07(self.ctx)
        if self.user_value(key='G03P08Set', value=1):
            return NumberOnP08(self.ctx)
        if self.user_value(key='G03P09Set', value=1):
            return NumberOnP09(self.ctx)
        if self.user_value(key='G03P10Set', value=1):
            return NumberOnP10(self.ctx)
        if self.user_value(key='G03P11Set', value=1):
            return NumberOnP11(self.ctx)
        if self.user_value(key='G03P12Set', value=1):
            return NumberOnP12(self.ctx)
        if self.user_value(key='G03P13Set', value=1):
            return NumberOnP13(self.ctx)
        if self.user_value(key='G03P14Set', value=1):
            return NumberOnP14(self.ctx)
        if self.user_value(key='G03P15Set', value=1):
            return NumberOnP15(self.ctx)
        if self.user_value(key='G03P16Set', value=1):
            return NumberOnP16(self.ctx)
        if self.user_value(key='G03P17Set', value=1):
            return NumberOnP17(self.ctx)
        if self.user_value(key='G03P18Set', value=1):
            return NumberOnP18(self.ctx)
        if self.user_value(key='G03P19Set', value=1):
            return NumberOnP19(self.ctx)
        if self.user_value(key='G03P20Set', value=1):
            return NumberOnP20(self.ctx)
        if self.user_value(key='G03P21Set', value=1):
            return NumberOnP21(self.ctx)
        if self.user_value(key='G03P22Set', value=1):
            return NumberOnP22(self.ctx)
        if self.user_value(key='G03P23Set', value=1):
            return NumberOnP23(self.ctx)
        if self.user_value(key='G03P24Set', value=1):
            return NumberOnP24(self.ctx)
        if self.user_value(key='G03P25Set', value=1):
            return NumberOnP25(self.ctx)
        if self.user_value(key='G03P26Set', value=1):
            return NumberOnP26(self.ctx)
        if self.user_value(key='G03P27Set', value=1):
            return NumberOnP27(self.ctx)
        if self.user_value(key='G03P28Set', value=1):
            return NumberOnP28(self.ctx)
        if self.user_value(key='G03P29Set', value=1):
            return NumberOnP29(self.ctx)
        if self.user_value(key='G03P30Set', value=1):
            return NumberOnP30(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=7110, key='ColorStart', value=1)
        # start
        self.set_user_value(triggerId=7120, key='ColorStart', value=1)
        # start
        self.set_user_value(triggerId=7130, key='ColorStart', value=1)
        # start
        self.set_user_value(triggerId=7140, key='ColorStart', value=1)
        # start
        self.set_user_value(triggerId=7210, key='ColorStart', value=1)
        # start
        self.set_user_value(triggerId=7220, key='ColorStart', value=1)
        # start
        self.set_user_value(triggerId=7230, key='ColorStart', value=1)
        # start
        self.set_user_value(triggerId=7240, key='ColorStart', value=1)
        # start
        self.set_user_value(triggerId=7310, key='ColorStart', value=1)
        # start
        self.set_user_value(triggerId=7320, key='ColorStart', value=1)
        # start
        self.set_user_value(triggerId=7330, key='ColorStart', value=1)
        # start
        self.set_user_value(triggerId=7340, key='ColorStart', value=1)
        # start
        self.set_user_value(triggerId=7410, key='ColorStart', value=1)
        # start
        self.set_user_value(triggerId=7420, key='ColorStart', value=1)
        # start
        self.set_user_value(triggerId=7430, key='ColorStart', value=1)
        # start
        self.set_user_value(triggerId=7440, key='ColorStart', value=1)
        # start


# G03 P01
class NumberOnP01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[110], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[121], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[135], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[224], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 4
        self.set_mesh(triggerIds=[230], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 0
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[325], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[330], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[411], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[420], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[434], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=1)
        self.set_user_value(triggerId=8130, key='Barrier13', value=5)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=4)
        self.set_user_value(triggerId=8230, key='Barrier23', value=0)
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=5)
        self.set_user_value(triggerId=8330, key='Barrier33', value=0)
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=1)
        self.set_user_value(triggerId=8420, key='Barrier42', value=0)
        self.set_user_value(triggerId=8430, key='Barrier43', value=4)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P01TimeLimit', value=1):
            return CheckP01(self.ctx)


class CheckP01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=1)
        self.set_user_value(triggerId=9130, key='Box13Check', value=5)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=4)
        self.set_user_value(triggerId=9230, key='Box23Check', value=0)
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=5)
        self.set_user_value(triggerId=9330, key='Box33Check', value=0)
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=1)
        self.set_user_value(triggerId=9420, key='Box42Check', value=0)
        self.set_user_value(triggerId=9430, key='Box43Check', value=4)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP01(self.ctx)


class NumberOffP01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[121], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[135], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[224], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 4
        self.set_mesh(triggerIds=[230], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 0
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[325], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[330], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[411], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[420], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[434], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP01(self.ctx)


class ResetP01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P01End', value=1)
        self.set_user_value(key='G03P01Set', value=0)
        self.set_user_value(key='G03P01TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P02
class NumberOnP02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[120], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[145], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[210], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[221], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[230], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 0
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[315], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[320], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 0
        self.set_mesh(triggerIds=[330], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[411], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[424], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[430], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=0)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=0)
        self.set_user_value(triggerId=8220, key='Barrier22', value=1)
        self.set_user_value(triggerId=8230, key='Barrier23', value=0)
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=5)
        self.set_user_value(triggerId=8320, key='Barrier32', value=0)
        self.set_user_value(triggerId=8330, key='Barrier33', value=0)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=1)
        self.set_user_value(triggerId=8420, key='Barrier42', value=4)
        self.set_user_value(triggerId=8430, key='Barrier43', value=0)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P02TimeLimit', value=1):
            return CheckP02(self.ctx)


class CheckP02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=0)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=0)
        self.set_user_value(triggerId=9220, key='Box22Check', value=1)
        self.set_user_value(triggerId=9230, key='Box23Check', value=0)
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=5)
        self.set_user_value(triggerId=9320, key='Box32Check', value=0)
        self.set_user_value(triggerId=9330, key='Box33Check', value=0)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=1)
        self.set_user_value(triggerId=9420, key='Box42Check', value=4)
        self.set_user_value(triggerId=9430, key='Box43Check', value=0)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP02(self.ctx)


class NumberOffP02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[120], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[145], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[210], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[221], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[230], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 0
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[315], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[320], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 0
        self.set_mesh(triggerIds=[330], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[411], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[424], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[430], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP02(self.ctx)


class ResetP02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P02End', value=1)
        self.set_user_value(key='G03P02Set', value=0)
        self.set_user_value(key='G03P02TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P03
class NumberOnP03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[125], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[221], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[240], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[320], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 0
        self.set_mesh(triggerIds=[334], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[341], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[420], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[445], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 5
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=5)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=1)
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=0)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=0)
        self.set_user_value(triggerId=8330, key='Barrier33', value=4)
        self.set_user_value(triggerId=8340, key='Barrier34', value=1)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=0)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P03TimeLimit', value=1):
            return CheckP03(self.ctx)


class CheckP03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=5)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=1)
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=0)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=0)
        self.set_user_value(triggerId=9330, key='Box33Check', value=4)
        self.set_user_value(triggerId=9340, key='Box34Check', value=1)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=0)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP03(self.ctx)


class NumberOffP03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[125], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[221], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[240], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[320], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 0
        self.set_mesh(triggerIds=[334], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[341], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[420], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[445], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP03(self.ctx)


class ResetP03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P03End', value=1)
        self.set_user_value(key='G03P03Set', value=0)
        self.set_user_value(key='G03P03TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P04
class NumberOnP04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[111], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 1
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[130], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[141], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[235], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[310], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[324], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[331], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[410], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[430], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=1)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=0)
        self.set_user_value(triggerId=8140, key='Barrier14', value=1)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=5)
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=0)
        self.set_user_value(triggerId=8320, key='Barrier32', value=4)
        self.set_user_value(triggerId=8330, key='Barrier33', value=1)
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=0)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=0)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P04TimeLimit', value=1):
            return CheckP04(self.ctx)


class CheckP04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=1)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=0)
        self.set_user_value(triggerId=9140, key='Box14Check', value=1)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=5)
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=0)
        self.set_user_value(triggerId=9320, key='Box32Check', value=4)
        self.set_user_value(triggerId=9330, key='Box33Check', value=1)
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=0)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=0)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP04(self.ctx)


class NumberOffP04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[111], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 1
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[130], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[141], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[235], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[310], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[324], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[331], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[410], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[430], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP04(self.ctx)


class ResetP04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P04End', value=1)
        self.set_user_value(key='G03P04Set', value=0)
        self.set_user_value(key='G03P04TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P05
class NumberOnP05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[115], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 5
        self.set_mesh(triggerIds=[120], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[144], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[211], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[230], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 0
        self.set_mesh(triggerIds=[241], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 1
        self.set_mesh(triggerIds=[314], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[321], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[330], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[435], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=5)
        self.set_user_value(triggerId=8120, key='Barrier12', value=0)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=4)
        self.set_user_value(triggerId=8210, key='Barrier21', value=1)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=0)
        self.set_user_value(triggerId=8240, key='Barrier24', value=1)
        self.set_user_value(triggerId=8310, key='Barrier31', value=4)
        self.set_user_value(triggerId=8320, key='Barrier32', value=1)
        self.set_user_value(triggerId=8330, key='Barrier33', value=0)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=5)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P05TimeLimit', value=1):
            return CheckP05(self.ctx)


class CheckP05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=5)
        self.set_user_value(triggerId=9120, key='Box12Check', value=0)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=4)
        self.set_user_value(triggerId=9210, key='Box21Check', value=1)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=0)
        self.set_user_value(triggerId=9240, key='Box24Check', value=1)
        self.set_user_value(triggerId=9310, key='Box31Check', value=4)
        self.set_user_value(triggerId=9320, key='Box32Check', value=1)
        self.set_user_value(triggerId=9330, key='Box33Check', value=0)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=5)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP05(self.ctx)


class NumberOffP05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[115], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 5
        self.set_mesh(triggerIds=[120], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[144], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[211], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[230], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 0
        self.set_mesh(triggerIds=[241], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 1
        self.set_mesh(triggerIds=[314], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[321], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[330], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[435], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 5
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP05(self.ctx)


class ResetP05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P05End', value=1)
        self.set_user_value(key='G03P05Set', value=0)
        self.set_user_value(key='G03P05TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P06
class NumberOnP06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[114], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[131], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[141], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[221], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[235], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[241], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 1
        self.set_mesh(triggerIds=[311], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[324], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[331], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[411], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[421], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 1
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[441], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 1
        self.set_user_value(triggerId=8110, key='Barrier11', value=4)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=1)
        self.set_user_value(triggerId=8140, key='Barrier14', value=1)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=1)
        self.set_user_value(triggerId=8230, key='Barrier23', value=5)
        self.set_user_value(triggerId=8240, key='Barrier24', value=1)
        self.set_user_value(triggerId=8310, key='Barrier31', value=1)
        self.set_user_value(triggerId=8320, key='Barrier32', value=4)
        self.set_user_value(triggerId=8330, key='Barrier33', value=1)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=1)
        self.set_user_value(triggerId=8420, key='Barrier42', value=1)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P06TimeLimit', value=1):
            return CheckP06(self.ctx)


class CheckP06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=4)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=1)
        self.set_user_value(triggerId=9140, key='Box14Check', value=1)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=1)
        self.set_user_value(triggerId=9230, key='Box23Check', value=5)
        self.set_user_value(triggerId=9240, key='Box24Check', value=1)
        self.set_user_value(triggerId=9310, key='Box31Check', value=1)
        self.set_user_value(triggerId=9320, key='Box32Check', value=4)
        self.set_user_value(triggerId=9330, key='Box33Check', value=1)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=1)
        self.set_user_value(triggerId=9420, key='Box42Check', value=1)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP06(self.ctx)


class NumberOffP06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[114], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[131], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[141], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[221], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[235], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[241], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 1
        self.set_mesh(triggerIds=[311], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[324], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[331], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[411], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[421], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 1
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[441], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP06(self.ctx)


class ResetP06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P06End', value=1)
        self.set_user_value(key='G03P06Set', value=0)
        self.set_user_value(key='G03P06TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P07
class NumberOnP07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[211], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[322], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[341], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=1)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=2)
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=1)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P07TimeLimit', value=1):
            return CheckP07(self.ctx)


class CheckP07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=1)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=2)
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=1)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP07(self.ctx)


class NumberOffP07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[211], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[322], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[341], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP07(self.ctx)


class ResetP07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P07End', value=1)
        self.set_user_value(key='G03P07Set', value=0)
        self.set_user_value(key='G03P07TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P08
class NumberOnP08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[321], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=1)
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P08TimeLimit', value=1):
            return CheckP08(self.ctx)


class CheckP08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=1)
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP08(self.ctx)


class NumberOffP08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[321], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP08(self.ctx)


class ResetP08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P08End', value=1)
        self.set_user_value(key='G03P08Set', value=0)
        self.set_user_value(key='G03P08TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P09
class NumberOnP09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[120], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[211], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[230], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 0
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[420], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[431], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=0)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=1)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=0)
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=0)
        self.set_user_value(triggerId=8430, key='Barrier43', value=1)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P09TimeLimit', value=1):
            return CheckP09(self.ctx)


class CheckP09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=0)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=1)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=0)
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=0)
        self.set_user_value(triggerId=9430, key='Box43Check', value=1)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP09(self.ctx)


class NumberOffP09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[120], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[211], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[230], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 0
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[420], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[431], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP09(self.ctx)


class ResetP09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P09End', value=1)
        self.set_user_value(key='G03P09Set', value=0)
        self.set_user_value(key='G03P09TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P10
class NumberOnP10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[110], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[121], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[130], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[215], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[220], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 0
        self.set_mesh(triggerIds=[235], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[240], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[325], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[330], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[421], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 1
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=1)
        self.set_user_value(triggerId=8130, key='Barrier13', value=0)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=5)
        self.set_user_value(triggerId=8220, key='Barrier22', value=0)
        self.set_user_value(triggerId=8230, key='Barrier23', value=5)
        self.set_user_value(triggerId=8240, key='Barrier24', value=0)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=5)
        self.set_user_value(triggerId=8330, key='Barrier33', value=0)
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=1)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P10TimeLimit', value=1):
            return CheckP10(self.ctx)


class CheckP10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=1)
        self.set_user_value(triggerId=9130, key='Box13Check', value=0)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=5)
        self.set_user_value(triggerId=9220, key='Box22Check', value=0)
        self.set_user_value(triggerId=9230, key='Box23Check', value=5)
        self.set_user_value(triggerId=9240, key='Box24Check', value=0)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=5)
        self.set_user_value(triggerId=9330, key='Box33Check', value=0)
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=1)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP10(self.ctx)


class NumberOffP10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[121], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[130], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[215], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[220], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 0
        self.set_mesh(triggerIds=[235], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[240], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[325], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 5
        self.set_mesh(triggerIds=[330], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[421], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 1
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP10(self.ctx)


class ResetP10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P10End', value=1)
        self.set_user_value(key='G03P10Set', value=0)
        self.set_user_value(key='G03P10TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P11
class NumberOnP11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[120], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[134], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[141], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[230], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 0
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[314], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[320], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 0
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[344], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[411], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[424], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[430], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=0)
        self.set_user_value(triggerId=8130, key='Barrier13', value=4)
        self.set_user_value(triggerId=8140, key='Barrier14', value=1)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=0)
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=4)
        self.set_user_value(triggerId=8320, key='Barrier32', value=0)
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=4)
        self.set_user_value(triggerId=8410, key='Barrier41', value=1)
        self.set_user_value(triggerId=8420, key='Barrier42', value=4)
        self.set_user_value(triggerId=8430, key='Barrier43', value=0)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P11TimeLimit', value=1):
            return CheckP11(self.ctx)


class CheckP11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=0)
        self.set_user_value(triggerId=9130, key='Box13Check', value=4)
        self.set_user_value(triggerId=9140, key='Box14Check', value=1)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=0)
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=4)
        self.set_user_value(triggerId=9320, key='Box32Check', value=0)
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=4)
        self.set_user_value(triggerId=9410, key='Box41Check', value=1)
        self.set_user_value(triggerId=9420, key='Box42Check', value=4)
        self.set_user_value(triggerId=9430, key='Box43Check', value=0)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP11(self.ctx)


class NumberOffP11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[120], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[134], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[141], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[230], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 0
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[314], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[320], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 0
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[344], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[411], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[424], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[430], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP11(self.ctx)


class ResetP11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P11End', value=1)
        self.set_user_value(key='G03P11Set', value=0)
        self.set_user_value(key='G03P11TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P12
class NumberOnP12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[111], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 1
        self.set_mesh(triggerIds=[121], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[141], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[225], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[231], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 1
        self.set_mesh(triggerIds=[241], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 1
        self.set_mesh(triggerIds=[311], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[322], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[331], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[344], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[421], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 1
        self.set_mesh(triggerIds=[431], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[441], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 1
        self.set_user_value(triggerId=8110, key='Barrier11', value=1)
        self.set_user_value(triggerId=8120, key='Barrier12', value=1)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=1)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=5)
        self.set_user_value(triggerId=8230, key='Barrier23', value=1)
        self.set_user_value(triggerId=8240, key='Barrier24', value=1)
        self.set_user_value(triggerId=8310, key='Barrier31', value=1)
        self.set_user_value(triggerId=8320, key='Barrier32', value=2)
        self.set_user_value(triggerId=8330, key='Barrier33', value=1)
        self.set_user_value(triggerId=8340, key='Barrier34', value=4)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=1)
        self.set_user_value(triggerId=8430, key='Barrier43', value=1)
        self.set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P12TimeLimit', value=1):
            return CheckP12(self.ctx)


class CheckP12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=1)
        self.set_user_value(triggerId=9120, key='Box12Check', value=1)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=1)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=5)
        self.set_user_value(triggerId=9230, key='Box23Check', value=1)
        self.set_user_value(triggerId=9240, key='Box24Check', value=1)
        self.set_user_value(triggerId=9310, key='Box31Check', value=1)
        self.set_user_value(triggerId=9320, key='Box32Check', value=2)
        self.set_user_value(triggerId=9330, key='Box33Check', value=1)
        self.set_user_value(triggerId=9340, key='Box34Check', value=4)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=1)
        self.set_user_value(triggerId=9430, key='Box43Check', value=1)
        self.set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP12(self.ctx)


class NumberOffP12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[111], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 1
        self.set_mesh(triggerIds=[121], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[141], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[225], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[231], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 1
        self.set_mesh(triggerIds=[241], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 1
        self.set_mesh(triggerIds=[311], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[322], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 2
        self.set_mesh(triggerIds=[331], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[344], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[421], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 1
        self.set_mesh(triggerIds=[431], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[441], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP12(self.ctx)


class ResetP12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P12End', value=1)
        self.set_user_value(key='G03P12Set', value=0)
        self.set_user_value(key='G03P12TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P13
class NumberOnP13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[121], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[131], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[211], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[231], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 1
        self.set_mesh(triggerIds=[245], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[311], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[331], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[341], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[411], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[424], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[441], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 1
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=1)
        self.set_user_value(triggerId=8130, key='Barrier13', value=1)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=1)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=1)
        self.set_user_value(triggerId=8240, key='Barrier24', value=5)
        self.set_user_value(triggerId=8310, key='Barrier31', value=1)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=1)
        self.set_user_value(triggerId=8340, key='Barrier34', value=1)
        self.set_user_value(triggerId=8410, key='Barrier41', value=1)
        self.set_user_value(triggerId=8420, key='Barrier42', value=4)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P13TimeLimit', value=1):
            return CheckP13(self.ctx)


class CheckP13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=1)
        self.set_user_value(triggerId=9130, key='Box13Check', value=1)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=1)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=1)
        self.set_user_value(triggerId=9240, key='Box24Check', value=5)
        self.set_user_value(triggerId=9310, key='Box31Check', value=1)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=1)
        self.set_user_value(triggerId=9340, key='Box34Check', value=1)
        self.set_user_value(triggerId=9410, key='Box41Check', value=1)
        self.set_user_value(triggerId=9420, key='Box42Check', value=4)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP13(self.ctx)


class NumberOffP13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[121], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[131], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[211], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[231], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 1
        self.set_mesh(triggerIds=[245], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[311], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[331], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[341], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[411], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[424], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[441], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP13(self.ctx)


class ResetP13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P13End', value=1)
        self.set_user_value(key='G03P13Set', value=0)
        self.set_user_value(key='G03P13TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P14
class NumberOnP14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[110], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[131], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[222], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[241], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 1
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[320], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 0
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[411], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=1)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=2)
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=1)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=0)
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=1)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P14TimeLimit', value=1):
            return CheckP14(self.ctx)


class CheckP14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=1)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=2)
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=1)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=0)
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=1)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP14(self.ctx)


class NumberOffP14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[131], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[222], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 2
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[241], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 1
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[320], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 0
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[411], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP14(self.ctx)


class ResetP14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P14End', value=1)
        self.set_user_value(key='G03P14Set', value=0)
        self.set_user_value(key='G03P14TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P15
class NumberOnP15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[121], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[141], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[220], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 0
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[330], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[343], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[411], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[431], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=1)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=1)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=0)
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=0)
        self.set_user_value(triggerId=8340, key='Barrier34', value=3)
        self.set_user_value(triggerId=8410, key='Barrier41', value=1)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=1)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P15TimeLimit', value=1):
            return CheckP15(self.ctx)


class CheckP15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=1)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=1)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=0)
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=0)
        self.set_user_value(triggerId=9340, key='Box34Check', value=3)
        self.set_user_value(triggerId=9410, key='Box41Check', value=1)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=1)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP15(self.ctx)


class NumberOffP15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[121], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[141], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[220], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 0
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[330], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[343], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 3
        self.set_mesh(triggerIds=[411], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[431], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP15(self.ctx)


class ResetP15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P15End', value=1)
        self.set_user_value(key='G03P15Set', value=0)
        self.set_user_value(key='G03P15TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P16
class NumberOnP16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[111], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 1
        self.set_mesh(triggerIds=[120], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[130], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[143], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[220], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 0
        self.set_mesh(triggerIds=[234], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[245], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[315], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[331], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[340], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[414], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[420], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=1)
        self.set_user_value(triggerId=8120, key='Barrier12', value=0)
        self.set_user_value(triggerId=8130, key='Barrier13', value=0)
        self.set_user_value(triggerId=8140, key='Barrier14', value=3)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=0)
        self.set_user_value(triggerId=8230, key='Barrier23', value=4)
        self.set_user_value(triggerId=8240, key='Barrier24', value=5)
        self.set_user_value(triggerId=8310, key='Barrier31', value=5)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=1)
        self.set_user_value(triggerId=8340, key='Barrier34', value=0)
        self.set_user_value(triggerId=8410, key='Barrier41', value=4)
        self.set_user_value(triggerId=8420, key='Barrier42', value=0)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P16TimeLimit', value=1):
            return CheckP16(self.ctx)


class CheckP16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=1)
        self.set_user_value(triggerId=9120, key='Box12Check', value=0)
        self.set_user_value(triggerId=9130, key='Box13Check', value=0)
        self.set_user_value(triggerId=9140, key='Box14Check', value=3)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=0)
        self.set_user_value(triggerId=9230, key='Box23Check', value=4)
        self.set_user_value(triggerId=9240, key='Box24Check', value=5)
        self.set_user_value(triggerId=9310, key='Box31Check', value=5)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=1)
        self.set_user_value(triggerId=9340, key='Box34Check', value=0)
        self.set_user_value(triggerId=9410, key='Box41Check', value=4)
        self.set_user_value(triggerId=9420, key='Box42Check', value=0)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP16(self.ctx)


class NumberOffP16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[111], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 1
        self.set_mesh(triggerIds=[120], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[130], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[143], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 3
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[220], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 0
        self.set_mesh(triggerIds=[234], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[245], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[315], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[331], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[340], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[414], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[420], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP16(self.ctx)


class ResetP16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P16End', value=1)
        self.set_user_value(key='G03P16Set', value=0)
        self.set_user_value(key='G03P16TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P17
class NumberOnP17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[110], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[135], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[210], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[221], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[230], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 0
        self.set_mesh(triggerIds=[240], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[314], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[321], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[335], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 5
        self.set_mesh(triggerIds=[340], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[434], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=5)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=0)
        self.set_user_value(triggerId=8220, key='Barrier22', value=1)
        self.set_user_value(triggerId=8230, key='Barrier23', value=0)
        self.set_user_value(triggerId=8240, key='Barrier24', value=0)
        self.set_user_value(triggerId=8310, key='Barrier31', value=4)
        self.set_user_value(triggerId=8320, key='Barrier32', value=1)
        self.set_user_value(triggerId=8330, key='Barrier33', value=5)
        self.set_user_value(triggerId=8340, key='Barrier34', value=0)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=4)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P17TimeLimit', value=1):
            return CheckP17(self.ctx)


class CheckP17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=5)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=0)
        self.set_user_value(triggerId=9220, key='Box22Check', value=1)
        self.set_user_value(triggerId=9230, key='Box23Check', value=0)
        self.set_user_value(triggerId=9240, key='Box24Check', value=0)
        self.set_user_value(triggerId=9310, key='Box31Check', value=4)
        self.set_user_value(triggerId=9320, key='Box32Check', value=1)
        self.set_user_value(triggerId=9330, key='Box33Check', value=5)
        self.set_user_value(triggerId=9340, key='Box34Check', value=0)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=4)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP17(self.ctx)


class NumberOffP17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[135], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[210], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[221], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[230], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 0
        self.set_mesh(triggerIds=[240], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[314], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[321], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[335], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 5
        self.set_mesh(triggerIds=[340], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[434], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP17(self.ctx)


class ResetP17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P17End', value=1)
        self.set_user_value(key='G03P17Set', value=0)
        self.set_user_value(key='G03P17TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P18
class NumberOnP18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[120], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[144], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[211], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[234], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[241], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 1
        self.set_mesh(triggerIds=[310], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[324], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[340], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[414], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[421], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 1
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[444], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 4
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=0)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=4)
        self.set_user_value(triggerId=8210, key='Barrier21', value=1)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=4)
        self.set_user_value(triggerId=8240, key='Barrier24', value=1)
        self.set_user_value(triggerId=8310, key='Barrier31', value=0)
        self.set_user_value(triggerId=8320, key='Barrier32', value=4)
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=0)
        self.set_user_value(triggerId=8410, key='Barrier41', value=4)
        self.set_user_value(triggerId=8420, key='Barrier42', value=1)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P18TimeLimit', value=1):
            return CheckP18(self.ctx)


class CheckP18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=0)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=4)
        self.set_user_value(triggerId=9210, key='Box21Check', value=1)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=4)
        self.set_user_value(triggerId=9240, key='Box24Check', value=1)
        self.set_user_value(triggerId=9310, key='Box31Check', value=0)
        self.set_user_value(triggerId=9320, key='Box32Check', value=4)
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=0)
        self.set_user_value(triggerId=9410, key='Box41Check', value=4)
        self.set_user_value(triggerId=9420, key='Box42Check', value=1)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP18(self.ctx)


class NumberOffP18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[120], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[144], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[211], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[234], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[241], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 1
        self.set_mesh(triggerIds=[310], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[324], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[340], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[414], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 4
        self.set_mesh(triggerIds=[421], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 1
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[444], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP18(self.ctx)


class ResetP18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P18End', value=1)
        self.set_user_value(key='G03P18Set', value=0)
        self.set_user_value(key='G03P18TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P19
class NumberOnP19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[121], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[134], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[221], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[310], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[324], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[334], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[341], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[410], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[434], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[444], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 4
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=1)
        self.set_user_value(triggerId=8130, key='Barrier13', value=4)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=1)
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=0)
        self.set_user_value(triggerId=8320, key='Barrier32', value=4)
        self.set_user_value(triggerId=8330, key='Barrier33', value=4)
        self.set_user_value(triggerId=8340, key='Barrier34', value=1)
        self.set_user_value(triggerId=8410, key='Barrier41', value=0)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=4)
        self.set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P19TimeLimit', value=1):
            return CheckP19(self.ctx)


class CheckP19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=1)
        self.set_user_value(triggerId=9130, key='Box13Check', value=4)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=1)
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=0)
        self.set_user_value(triggerId=9320, key='Box32Check', value=4)
        self.set_user_value(triggerId=9330, key='Box33Check', value=4)
        self.set_user_value(triggerId=9340, key='Box34Check', value=1)
        self.set_user_value(triggerId=9410, key='Box41Check', value=0)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=4)
        self.set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP19(self.ctx)


class NumberOffP19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[121], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[134], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 4
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[221], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[310], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 0
        self.set_mesh(triggerIds=[324], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[334], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[341], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[410], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[434], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 4
        self.set_mesh(triggerIds=[444], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP19(self.ctx)


class ResetP19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P19End', value=1)
        self.set_user_value(key='G03P19Set', value=0)
        self.set_user_value(key='G03P19TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P20
class NumberOnP20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[221], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[321], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=1)
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=1)
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P20TimeLimit', value=1):
            return CheckP20(self.ctx)


class CheckP20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=1)
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=1)
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP20(self.ctx)


class NumberOffP20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[221], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[321], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP20(self.ctx)


class ResetP20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P20End', value=1)
        self.set_user_value(key='G03P20Set', value=0)
        self.set_user_value(key='G03P20TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P21
class NumberOnP21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[110], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[121], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[135], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[210], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[225], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[245], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[311], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[320], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 0
        self.set_mesh(triggerIds=[335], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 5
        self.set_mesh(triggerIds=[341], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[415], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[420], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=1)
        self.set_user_value(triggerId=8130, key='Barrier13', value=5)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=0)
        self.set_user_value(triggerId=8220, key='Barrier22', value=5)
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=5)
        self.set_user_value(triggerId=8310, key='Barrier31', value=1)
        self.set_user_value(triggerId=8320, key='Barrier32', value=0)
        self.set_user_value(triggerId=8330, key='Barrier33', value=5)
        self.set_user_value(triggerId=8340, key='Barrier34', value=1)
        self.set_user_value(triggerId=8410, key='Barrier41', value=5)
        self.set_user_value(triggerId=8420, key='Barrier42', value=0)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P21TimeLimit', value=1):
            return CheckP21(self.ctx)


class CheckP21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=1)
        self.set_user_value(triggerId=9130, key='Box13Check', value=5)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=0)
        self.set_user_value(triggerId=9220, key='Box22Check', value=5)
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=5)
        self.set_user_value(triggerId=9310, key='Box31Check', value=1)
        self.set_user_value(triggerId=9320, key='Box32Check', value=0)
        self.set_user_value(triggerId=9330, key='Box33Check', value=5)
        self.set_user_value(triggerId=9340, key='Box34Check', value=1)
        self.set_user_value(triggerId=9410, key='Box41Check', value=5)
        self.set_user_value(triggerId=9420, key='Box42Check', value=0)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP21(self.ctx)


class NumberOffP21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[121], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[135], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 5
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[210], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[225], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[245], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 5
        self.set_mesh(triggerIds=[311], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[320], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 0
        self.set_mesh(triggerIds=[335], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 5
        self.set_mesh(triggerIds=[341], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[415], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 5
        self.set_mesh(triggerIds=[420], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP21(self.ctx)


class ResetP21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P21End', value=1)
        self.set_user_value(key='G03P21Set', value=0)
        self.set_user_value(key='G03P21TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P22
class NumberOnP22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[114], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[120], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[132], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[144], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[211], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[224], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 4
        self.set_mesh(triggerIds=[234], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[240], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[314], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[320], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 0
        self.set_mesh(triggerIds=[330], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[341], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[424], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[430], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[444], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 4
        self.set_user_value(triggerId=8110, key='Barrier11', value=4)
        self.set_user_value(triggerId=8120, key='Barrier12', value=0)
        self.set_user_value(triggerId=8130, key='Barrier13', value=2)
        self.set_user_value(triggerId=8140, key='Barrier14', value=4)
        self.set_user_value(triggerId=8210, key='Barrier21', value=1)
        self.set_user_value(triggerId=8220, key='Barrier22', value=4)
        self.set_user_value(triggerId=8230, key='Barrier23', value=4)
        self.set_user_value(triggerId=8240, key='Barrier24', value=0)
        self.set_user_value(triggerId=8310, key='Barrier31', value=4)
        self.set_user_value(triggerId=8320, key='Barrier32', value=0)
        self.set_user_value(triggerId=8330, key='Barrier33', value=0)
        self.set_user_value(triggerId=8340, key='Barrier34', value=1)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=4)
        self.set_user_value(triggerId=8430, key='Barrier43', value=0)
        self.set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P22TimeLimit', value=1):
            return CheckP22(self.ctx)


class CheckP22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=4)
        self.set_user_value(triggerId=9120, key='Box12Check', value=0)
        self.set_user_value(triggerId=9130, key='Box13Check', value=2)
        self.set_user_value(triggerId=9140, key='Box14Check', value=4)
        self.set_user_value(triggerId=9210, key='Box21Check', value=1)
        self.set_user_value(triggerId=9220, key='Box22Check', value=4)
        self.set_user_value(triggerId=9230, key='Box23Check', value=4)
        self.set_user_value(triggerId=9240, key='Box24Check', value=0)
        self.set_user_value(triggerId=9310, key='Box31Check', value=4)
        self.set_user_value(triggerId=9320, key='Box32Check', value=0)
        self.set_user_value(triggerId=9330, key='Box33Check', value=0)
        self.set_user_value(triggerId=9340, key='Box34Check', value=1)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=4)
        self.set_user_value(triggerId=9430, key='Box43Check', value=0)
        self.set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP22(self.ctx)


class NumberOffP22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[114], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 4
        self.set_mesh(triggerIds=[120], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[132], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 2
        self.set_mesh(triggerIds=[144], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 4
        self.set_mesh(triggerIds=[211], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[224], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 4
        self.set_mesh(triggerIds=[234], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 4
        self.set_mesh(triggerIds=[240], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[314], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[320], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 0
        self.set_mesh(triggerIds=[330], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[341], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[424], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 4
        self.set_mesh(triggerIds=[430], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[444], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP22(self.ctx)


class ResetP22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P22End', value=1)
        self.set_user_value(key='G03P22Set', value=0)
        self.set_user_value(key='G03P22TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P23
class NumberOnP23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[123], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[130], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[215], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[220], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 0
        self.set_mesh(triggerIds=[235], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[311], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[331], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[410], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[420], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[433], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=3)
        self.set_user_value(triggerId=8130, key='Barrier13', value=0)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=5)
        self.set_user_value(triggerId=8220, key='Barrier22', value=0)
        self.set_user_value(triggerId=8230, key='Barrier23', value=5)
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=1)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=1)
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=0)
        self.set_user_value(triggerId=8420, key='Barrier42', value=0)
        self.set_user_value(triggerId=8430, key='Barrier43', value=3)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P23TimeLimit', value=1):
            return CheckP23(self.ctx)


class CheckP23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=3)
        self.set_user_value(triggerId=9130, key='Box13Check', value=0)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=5)
        self.set_user_value(triggerId=9220, key='Box22Check', value=0)
        self.set_user_value(triggerId=9230, key='Box23Check', value=5)
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=1)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=1)
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=0)
        self.set_user_value(triggerId=9420, key='Box42Check', value=0)
        self.set_user_value(triggerId=9430, key='Box43Check', value=3)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP23(self.ctx)


class NumberOffP23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[123], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 3
        self.set_mesh(triggerIds=[130], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[215], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[220], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 0
        self.set_mesh(triggerIds=[235], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[311], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[331], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[410], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[420], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[433], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 3
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP23(self.ctx)


class ResetP23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P23End', value=1)
        self.set_user_value(key='G03P23Set', value=0)
        self.set_user_value(key='G03P23TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P24
class NumberOnP24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[122], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[141], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[213], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[232], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[321], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[333], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[341], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[432], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[441], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 1
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=2)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=1)
        self.set_user_value(triggerId=8210, key='Barrier21', value=3)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=2)
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=1)
        self.set_user_value(triggerId=8330, key='Barrier33', value=3)
        self.set_user_value(triggerId=8340, key='Barrier34', value=1)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=2)
        self.set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P24TimeLimit', value=1):
            return CheckP24(self.ctx)


class CheckP24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=2)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=1)
        self.set_user_value(triggerId=9210, key='Box21Check', value=3)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=2)
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=1)
        self.set_user_value(triggerId=9330, key='Box33Check', value=3)
        self.set_user_value(triggerId=9340, key='Box34Check', value=1)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=2)
        self.set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP24(self.ctx)


class NumberOffP24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[122], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 2
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[141], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 1
        self.set_mesh(triggerIds=[213], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 3
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[232], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 2
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[321], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[333], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 3
        self.set_mesh(triggerIds=[341], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[432], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 2
        self.set_mesh(triggerIds=[441], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP24(self.ctx)


class ResetP24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P24End', value=1)
        self.set_user_value(key='G03P24Set', value=0)
        self.set_user_value(key='G03P24TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P25
class NumberOnP25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[110], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[124], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[131], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[214], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[221], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[244], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[313], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[324], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[334], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[341], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[410], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[430], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=4)
        self.set_user_value(triggerId=8130, key='Barrier13', value=1)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=4)
        self.set_user_value(triggerId=8220, key='Barrier22', value=1)
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=4)
        self.set_user_value(triggerId=8310, key='Barrier31', value=3)
        self.set_user_value(triggerId=8320, key='Barrier32', value=4)
        self.set_user_value(triggerId=8330, key='Barrier33', value=4)
        self.set_user_value(triggerId=8340, key='Barrier34', value=1)
        self.set_user_value(triggerId=8410, key='Barrier41', value=0)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=0)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P25TimeLimit', value=1):
            return CheckP25(self.ctx)


class CheckP25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=4)
        self.set_user_value(triggerId=9130, key='Box13Check', value=1)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=4)
        self.set_user_value(triggerId=9220, key='Box22Check', value=1)
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=4)
        self.set_user_value(triggerId=9310, key='Box31Check', value=3)
        self.set_user_value(triggerId=9320, key='Box32Check', value=4)
        self.set_user_value(triggerId=9330, key='Box33Check', value=4)
        self.set_user_value(triggerId=9340, key='Box34Check', value=1)
        self.set_user_value(triggerId=9410, key='Box41Check', value=0)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=0)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP25(self.ctx)


class NumberOffP25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[124], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[131], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[214], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 4
        self.set_mesh(triggerIds=[221], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[244], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 4
        self.set_mesh(triggerIds=[313], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 3
        self.set_mesh(triggerIds=[324], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[334], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[341], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 1
        self.set_mesh(triggerIds=[410], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[430], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP25(self.ctx)


class ResetP25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P25End', value=1)
        self.set_user_value(key='G03P25Set', value=0)
        self.set_user_value(key='G03P25TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P26
class NumberOnP26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[124], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[130], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[145], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[210], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[224], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 4
        self.set_mesh(triggerIds=[231], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 1
        self.set_mesh(triggerIds=[242], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[315], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[321], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[334], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[340], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[412], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[425], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[431], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=4)
        self.set_user_value(triggerId=8130, key='Barrier13', value=0)
        self.set_user_value(triggerId=8140, key='Barrier14', value=5)
        self.set_user_value(triggerId=8210, key='Barrier21', value=0)
        self.set_user_value(triggerId=8220, key='Barrier22', value=4)
        self.set_user_value(triggerId=8230, key='Barrier23', value=1)
        self.set_user_value(triggerId=8240, key='Barrier24', value=2)
        self.set_user_value(triggerId=8310, key='Barrier31', value=5)
        self.set_user_value(triggerId=8320, key='Barrier32', value=1)
        self.set_user_value(triggerId=8330, key='Barrier33', value=4)
        self.set_user_value(triggerId=8340, key='Barrier34', value=0)
        self.set_user_value(triggerId=8410, key='Barrier41', value=2)
        self.set_user_value(triggerId=8420, key='Barrier42', value=5)
        self.set_user_value(triggerId=8430, key='Barrier43', value=1)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P26TimeLimit', value=1):
            return CheckP26(self.ctx)


class CheckP26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=4)
        self.set_user_value(triggerId=9130, key='Box13Check', value=0)
        self.set_user_value(triggerId=9140, key='Box14Check', value=5)
        self.set_user_value(triggerId=9210, key='Box21Check', value=0)
        self.set_user_value(triggerId=9220, key='Box22Check', value=4)
        self.set_user_value(triggerId=9230, key='Box23Check', value=1)
        self.set_user_value(triggerId=9240, key='Box24Check', value=2)
        self.set_user_value(triggerId=9310, key='Box31Check', value=5)
        self.set_user_value(triggerId=9320, key='Box32Check', value=1)
        self.set_user_value(triggerId=9330, key='Box33Check', value=4)
        self.set_user_value(triggerId=9340, key='Box34Check', value=0)
        self.set_user_value(triggerId=9410, key='Box41Check', value=2)
        self.set_user_value(triggerId=9420, key='Box42Check', value=5)
        self.set_user_value(triggerId=9430, key='Box43Check', value=1)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP26(self.ctx)


class NumberOffP26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[124], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[130], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 0
        self.set_mesh(triggerIds=[145], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 5
        self.set_mesh(triggerIds=[210], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 0
        self.set_mesh(triggerIds=[224], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 4
        self.set_mesh(triggerIds=[231], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 1
        self.set_mesh(triggerIds=[242], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 2
        self.set_mesh(triggerIds=[315], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[321], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[334], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 4
        self.set_mesh(triggerIds=[340], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 0
        self.set_mesh(triggerIds=[412], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 2
        self.set_mesh(triggerIds=[425], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[431], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP26(self.ctx)


class ResetP26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P26End', value=1)
        self.set_user_value(key='G03P26Set', value=0)
        self.set_user_value(key='G03P26TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P27
class NumberOnP27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[110], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[124], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[131], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[215], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[220], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 0
        self.set_mesh(triggerIds=[233], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[240], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[324], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[330], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[410], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[423], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[430], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[441], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 1
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=4)
        self.set_user_value(triggerId=8130, key='Barrier13', value=1)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=5)
        self.set_user_value(triggerId=8220, key='Barrier22', value=0)
        self.set_user_value(triggerId=8230, key='Barrier23', value=3)
        self.set_user_value(triggerId=8240, key='Barrier24', value=0)
        self.set_user_value(triggerId=8310, key='Barrier31', value=2)
        self.set_user_value(triggerId=8320, key='Barrier32', value=4)
        self.set_user_value(triggerId=8330, key='Barrier33', value=0)
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=0)
        self.set_user_value(triggerId=8420, key='Barrier42', value=3)
        self.set_user_value(triggerId=8430, key='Barrier43', value=0)
        self.set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P27TimeLimit', value=1):
            return CheckP27(self.ctx)


class CheckP27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=4)
        self.set_user_value(triggerId=9130, key='Box13Check', value=1)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=5)
        self.set_user_value(triggerId=9220, key='Box22Check', value=0)
        self.set_user_value(triggerId=9230, key='Box23Check', value=3)
        self.set_user_value(triggerId=9240, key='Box24Check', value=0)
        self.set_user_value(triggerId=9310, key='Box31Check', value=2)
        self.set_user_value(triggerId=9320, key='Box32Check', value=4)
        self.set_user_value(triggerId=9330, key='Box33Check', value=0)
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=0)
        self.set_user_value(triggerId=9420, key='Box42Check', value=3)
        self.set_user_value(triggerId=9430, key='Box43Check', value=0)
        self.set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP27(self.ctx)


class NumberOffP27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[124], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 4
        self.set_mesh(triggerIds=[131], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[215], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 5
        self.set_mesh(triggerIds=[220], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 0
        self.set_mesh(triggerIds=[233], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 3
        self.set_mesh(triggerIds=[240], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 2
        self.set_mesh(triggerIds=[324], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 4
        self.set_mesh(triggerIds=[330], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 0
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[410], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[423], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 3
        self.set_mesh(triggerIds=[430], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[441], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP27(self.ctx)


class ResetP27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P27End', value=1)
        self.set_user_value(key='G03P27Set', value=0)
        self.set_user_value(key='G03P27TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P28
class NumberOnP28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[112], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[120], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[133], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[211], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[225], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[235], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[240], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[314], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[320], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 0
        self.set_mesh(triggerIds=[331], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[344], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[413], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[420], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[430], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[442], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 2
        self.set_user_value(triggerId=8110, key='Barrier11', value=2)
        self.set_user_value(triggerId=8120, key='Barrier12', value=0)
        self.set_user_value(triggerId=8130, key='Barrier13', value=3)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=1)
        self.set_user_value(triggerId=8220, key='Barrier22', value=5)
        self.set_user_value(triggerId=8230, key='Barrier23', value=5)
        self.set_user_value(triggerId=8240, key='Barrier24', value=0)
        self.set_user_value(triggerId=8310, key='Barrier31', value=4)
        self.set_user_value(triggerId=8320, key='Barrier32', value=0)
        self.set_user_value(triggerId=8330, key='Barrier33', value=1)
        self.set_user_value(triggerId=8340, key='Barrier34', value=4)
        self.set_user_value(triggerId=8410, key='Barrier41', value=3)
        self.set_user_value(triggerId=8420, key='Barrier42', value=0)
        self.set_user_value(triggerId=8430, key='Barrier43', value=0)
        self.set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P28TimeLimit', value=1):
            return CheckP28(self.ctx)


class CheckP28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=2)
        self.set_user_value(triggerId=9120, key='Box12Check', value=0)
        self.set_user_value(triggerId=9130, key='Box13Check', value=3)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=1)
        self.set_user_value(triggerId=9220, key='Box22Check', value=5)
        self.set_user_value(triggerId=9230, key='Box23Check', value=5)
        self.set_user_value(triggerId=9240, key='Box24Check', value=0)
        self.set_user_value(triggerId=9310, key='Box31Check', value=4)
        self.set_user_value(triggerId=9320, key='Box32Check', value=0)
        self.set_user_value(triggerId=9330, key='Box33Check', value=1)
        self.set_user_value(triggerId=9340, key='Box34Check', value=4)
        self.set_user_value(triggerId=9410, key='Box41Check', value=3)
        self.set_user_value(triggerId=9420, key='Box42Check', value=0)
        self.set_user_value(triggerId=9430, key='Box43Check', value=0)
        self.set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP28(self.ctx)


class NumberOffP28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[112], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 2
        self.set_mesh(triggerIds=[120], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 0
        self.set_mesh(triggerIds=[133], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 3
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[211], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[225], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 5
        self.set_mesh(triggerIds=[235], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[240], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[314], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 4
        self.set_mesh(triggerIds=[320], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 0
        self.set_mesh(triggerIds=[331], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[344], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 4
        self.set_mesh(triggerIds=[413], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 3
        self.set_mesh(triggerIds=[420], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 0
        self.set_mesh(triggerIds=[430], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 0
        self.set_mesh(triggerIds=[442], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP28(self.ctx)


class ResetP28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P28End', value=1)
        self.set_user_value(key='G03P28Set', value=0)
        self.set_user_value(key='G03P28TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P29
class NumberOnP29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[110], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[125], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[131], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[140], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[211], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[221], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[235], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[240], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[315], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[321], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[331], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[345], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[410], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[425], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[431], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[440], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 0
        self.set_user_value(triggerId=8110, key='Barrier11', value=0)
        self.set_user_value(triggerId=8120, key='Barrier12', value=5)
        self.set_user_value(triggerId=8130, key='Barrier13', value=1)
        self.set_user_value(triggerId=8140, key='Barrier14', value=0)
        self.set_user_value(triggerId=8210, key='Barrier21', value=1)
        self.set_user_value(triggerId=8220, key='Barrier22', value=1)
        self.set_user_value(triggerId=8230, key='Barrier23', value=5)
        self.set_user_value(triggerId=8240, key='Barrier24', value=0)
        self.set_user_value(triggerId=8310, key='Barrier31', value=5)
        self.set_user_value(triggerId=8320, key='Barrier32', value=1)
        self.set_user_value(triggerId=8330, key='Barrier33', value=1)
        self.set_user_value(triggerId=8340, key='Barrier34', value=5)
        self.set_user_value(triggerId=8410, key='Barrier41', value=0)
        self.set_user_value(triggerId=8420, key='Barrier42', value=5)
        self.set_user_value(triggerId=8430, key='Barrier43', value=1)
        self.set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P29TimeLimit', value=1):
            return CheckP29(self.ctx)


class CheckP29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=0)
        self.set_user_value(triggerId=9120, key='Box12Check', value=5)
        self.set_user_value(triggerId=9130, key='Box13Check', value=1)
        self.set_user_value(triggerId=9140, key='Box14Check', value=0)
        self.set_user_value(triggerId=9210, key='Box21Check', value=1)
        self.set_user_value(triggerId=9220, key='Box22Check', value=1)
        self.set_user_value(triggerId=9230, key='Box23Check', value=5)
        self.set_user_value(triggerId=9240, key='Box24Check', value=0)
        self.set_user_value(triggerId=9310, key='Box31Check', value=5)
        self.set_user_value(triggerId=9320, key='Box32Check', value=1)
        self.set_user_value(triggerId=9330, key='Box33Check', value=1)
        self.set_user_value(triggerId=9340, key='Box34Check', value=5)
        self.set_user_value(triggerId=9410, key='Box41Check', value=0)
        self.set_user_value(triggerId=9420, key='Box42Check', value=5)
        self.set_user_value(triggerId=9430, key='Box43Check', value=1)
        self.set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP29(self.ctx)


class NumberOffP29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[110], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 0
        self.set_mesh(triggerIds=[125], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 5
        self.set_mesh(triggerIds=[131], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[140], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 0
        self.set_mesh(triggerIds=[211], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 1
        self.set_mesh(triggerIds=[221], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 1
        self.set_mesh(triggerIds=[235], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 5
        self.set_mesh(triggerIds=[240], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 0
        self.set_mesh(triggerIds=[315], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 5
        self.set_mesh(triggerIds=[321], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 1
        self.set_mesh(triggerIds=[331], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 1
        self.set_mesh(triggerIds=[345], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 5
        self.set_mesh(triggerIds=[410], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 0
        self.set_mesh(triggerIds=[425], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 5
        self.set_mesh(triggerIds=[431], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[440], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP29(self.ctx)


class ResetP29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P29End', value=1)
        self.set_user_value(key='G03P29Set', value=0)
        self.set_user_value(key='G03P29TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


# G03 P30
class NumberOnP30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(triggerIds=[113], visible=True, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[121], visible=True, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[131], visible=True, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[142], visible=True, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[212], visible=True, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[223], visible=True, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[231], visible=True, arg3=0, delay=0, scale=2) # 2,3 / 1
        self.set_mesh(triggerIds=[243], visible=True, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[311], visible=True, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[323], visible=True, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[332], visible=True, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[342], visible=True, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[411], visible=True, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[422], visible=True, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[431], visible=True, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[443], visible=True, arg3=0, delay=0, scale=2) # 4,4 / 3
        self.set_user_value(triggerId=8110, key='Barrier11', value=3)
        self.set_user_value(triggerId=8120, key='Barrier12', value=1)
        self.set_user_value(triggerId=8130, key='Barrier13', value=1)
        self.set_user_value(triggerId=8140, key='Barrier14', value=2)
        self.set_user_value(triggerId=8210, key='Barrier21', value=2)
        self.set_user_value(triggerId=8220, key='Barrier22', value=3)
        self.set_user_value(triggerId=8230, key='Barrier23', value=1)
        self.set_user_value(triggerId=8240, key='Barrier24', value=3)
        self.set_user_value(triggerId=8310, key='Barrier31', value=1)
        self.set_user_value(triggerId=8320, key='Barrier32', value=3)
        self.set_user_value(triggerId=8330, key='Barrier33', value=2)
        self.set_user_value(triggerId=8340, key='Barrier34', value=2)
        self.set_user_value(triggerId=8410, key='Barrier41', value=1)
        self.set_user_value(triggerId=8420, key='Barrier42', value=2)
        self.set_user_value(triggerId=8430, key='Barrier43', value=1)
        self.set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G03P30TimeLimit', value=1):
            return CheckP30(self.ctx)


class CheckP30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=9110, key='Box11Check', value=3)
        self.set_user_value(triggerId=9120, key='Box12Check', value=1)
        self.set_user_value(triggerId=9130, key='Box13Check', value=1)
        self.set_user_value(triggerId=9140, key='Box14Check', value=2)
        self.set_user_value(triggerId=9210, key='Box21Check', value=2)
        self.set_user_value(triggerId=9220, key='Box22Check', value=3)
        self.set_user_value(triggerId=9230, key='Box23Check', value=1)
        self.set_user_value(triggerId=9240, key='Box24Check', value=3)
        self.set_user_value(triggerId=9310, key='Box31Check', value=1)
        self.set_user_value(triggerId=9320, key='Box32Check', value=3)
        self.set_user_value(triggerId=9330, key='Box33Check', value=2)
        self.set_user_value(triggerId=9340, key='Box34Check', value=2)
        self.set_user_value(triggerId=9410, key='Box41Check', value=1)
        self.set_user_value(triggerId=9420, key='Box42Check', value=2)
        self.set_user_value(triggerId=9430, key='Box43Check', value=1)
        self.set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NumberOffP30(self.ctx)


class NumberOffP30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[113], visible=False, arg3=0, delay=0, scale=2) # 1,1 / 3
        self.set_mesh(triggerIds=[121], visible=False, arg3=0, delay=0, scale=2) # 1,2 / 1
        self.set_mesh(triggerIds=[131], visible=False, arg3=0, delay=0, scale=2) # 1,3 / 1
        self.set_mesh(triggerIds=[142], visible=False, arg3=0, delay=0, scale=2) # 1,4 / 2
        self.set_mesh(triggerIds=[212], visible=False, arg3=0, delay=0, scale=2) # 2,1 / 2
        self.set_mesh(triggerIds=[223], visible=False, arg3=0, delay=0, scale=2) # 2,2 / 3
        self.set_mesh(triggerIds=[231], visible=False, arg3=0, delay=0, scale=2) # 2,3 / 1
        self.set_mesh(triggerIds=[243], visible=False, arg3=0, delay=0, scale=2) # 2,4 / 3
        self.set_mesh(triggerIds=[311], visible=False, arg3=0, delay=0, scale=2) # 3,1 / 1
        self.set_mesh(triggerIds=[323], visible=False, arg3=0, delay=0, scale=2) # 3,2 / 3
        self.set_mesh(triggerIds=[332], visible=False, arg3=0, delay=0, scale=2) # 3,3 / 2
        self.set_mesh(triggerIds=[342], visible=False, arg3=0, delay=0, scale=2) # 3,4 / 2
        self.set_mesh(triggerIds=[411], visible=False, arg3=0, delay=0, scale=2) # 4,1 / 1
        self.set_mesh(triggerIds=[422], visible=False, arg3=0, delay=0, scale=2) # 4,2 / 2
        self.set_mesh(triggerIds=[431], visible=False, arg3=0, delay=0, scale=2) # 4,3 / 1
        self.set_mesh(triggerIds=[443], visible=False, arg3=0, delay=0, scale=2) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ResetP30(self.ctx)


class ResetP30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='G03P30End', value=1)
        self.set_user_value(key='G03P30Set', value=0)
        self.set_user_value(key='G03P30TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Wait(self.ctx)


initial_state = Wait
