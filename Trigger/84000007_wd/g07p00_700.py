""" trigger/84000007_wd/g07p00_700.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[110,111,112,113,114,115], visible=False, arg3=0, arg4=0, arg5=0) # 1,1 / Number 0 to 5
        set_mesh(triggerIds=[120,121,122,123,124,125], visible=False, arg3=0, arg4=0, arg5=0) # 1,2 / Number 0 to 5
        set_mesh(triggerIds=[130,131,132,133,134,135], visible=False, arg3=0, arg4=0, arg5=0) # 1,3 / Number 0 to 5
        set_mesh(triggerIds=[140,141,142,143,144,145], visible=False, arg3=0, arg4=0, arg5=0) # 1,4 / Number 0 to 5
        set_mesh(triggerIds=[210,211,212,213,214,215], visible=False, arg3=0, arg4=0, arg5=0) # 2,1 / Number 0 to 5
        set_mesh(triggerIds=[220,221,222,223,224,225], visible=False, arg3=0, arg4=0, arg5=0) # 2,2 / Number 0 to 5
        set_mesh(triggerIds=[230,231,232,233,234,235], visible=False, arg3=0, arg4=0, arg5=0) # 2,3 / Number 0 to 5
        set_mesh(triggerIds=[240,241,242,243,244,245], visible=False, arg3=0, arg4=0, arg5=0) # 2,4 / Number 0 to 5
        set_mesh(triggerIds=[310,311,312,313,314,315], visible=False, arg3=0, arg4=0, arg5=0) # 3,1 / Number 0 to 5
        set_mesh(triggerIds=[320,321,322,323,324,325], visible=False, arg3=0, arg4=0, arg5=0) # 3,2 / Number 0 to 5
        set_mesh(triggerIds=[330,331,332,333,334,335], visible=False, arg3=0, arg4=0, arg5=0) # 3,3 / Number 0 to 5
        set_mesh(triggerIds=[340,341,342,343,344,345], visible=False, arg3=0, arg4=0, arg5=0) # 3,4 / Number 0 to 5
        set_mesh(triggerIds=[410,411,412,413,414,415], visible=False, arg3=0, arg4=0, arg5=0) # 4,1 / Number 0 to 5
        set_mesh(triggerIds=[420,421,422,423,424,425], visible=False, arg3=0, arg4=0, arg5=0) # 4,2 / Number 0 to 5
        set_mesh(triggerIds=[430,431,432,433,434,435], visible=False, arg3=0, arg4=0, arg5=0) # 4,3 / Number 0 to 5
        set_mesh(triggerIds=[440,441,442,443,444,445], visible=False, arg3=0, arg4=0, arg5=0) # 4,4 / Number 0 to 5
        set_mesh(triggerIds=[2207,2208,2209,22000,22005,22010,22020,22030], visible=False, arg3=0, arg4=0, arg5=0) # 2,2 / Large Number
        set_mesh(triggerIds=[2307,2308,2309,23000,23005,23010,23020,23030], visible=False, arg3=0, arg4=0, arg5=0) # 2,3 / Large Number
        set_mesh(triggerIds=[3207,3208,3209,32000,32005,32010,32020,32030], visible=False, arg3=0, arg4=0, arg5=0) # 3,2 / Large Number
        set_mesh(triggerIds=[3307,3308,3309,33000,33005,33010,33020,33030], visible=False, arg3=0, arg4=0, arg5=0) # 3,3 / Large Number

    def on_tick(self) -> state.State:
        if user_value(key='G07P201Set', value=1):
            return NumberOnP201()
        if user_value(key='G07P202Set', value=1):
            return NumberOnP202()
        if user_value(key='G07P203Set', value=1):
            return NumberOnP203()
        if user_value(key='G07P204Set', value=1):
            return NumberOnP204()
        if user_value(key='G07P205Set', value=1):
            return NumberOnP205()
        if user_value(key='G07P206Set', value=1):
            return NumberOnP206()
        if user_value(key='G07P207Set', value=1):
            return NumberOnP207()
        if user_value(key='G07P208Set', value=1):
            return NumberOnP208()
        if user_value(key='G07P209Set', value=1):
            return NumberOnP209()
        if user_value(key='G07P210Set', value=1):
            return NumberOnP210()
        if user_value(key='G07P301Set', value=1):
            return NumberOnP301()
        if user_value(key='G07P302Set', value=1):
            return NumberOnP302()
        if user_value(key='G07P303Set', value=1):
            return NumberOnP303()
        if user_value(key='G07P304Set', value=1):
            return NumberOnP304()
        if user_value(key='G07P305Set', value=1):
            return NumberOnP305()
        if user_value(key='G07P306Set', value=1):
            return NumberOnP306()
        if user_value(key='G07P307Set', value=1):
            return NumberOnP307()
        if user_value(key='G07P308Set', value=1):
            return NumberOnP308()
        if user_value(key='G07P309Set', value=1):
            return NumberOnP309()
        if user_value(key='G07P310Set', value=1):
            return NumberOnP310()
        if user_value(key='G07P401Set', value=1):
            return NumberOnP401()
        if user_value(key='G07P402Set', value=1):
            return NumberOnP402()
        if user_value(key='G07P403Set', value=1):
            return NumberOnP403()
        if user_value(key='G07P404Set', value=1):
            return NumberOnP404()
        if user_value(key='G07P405Set', value=1):
            return NumberOnP405()
        if user_value(key='G07P406Set', value=1):
            return NumberOnP406()
        if user_value(key='G07P407Set', value=1):
            return NumberOnP407()


#   G07 P201 
class NumberOnP201(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start jackpot
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[110], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[120], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 0
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[22010], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 15 Jackpot
        set_mesh(triggerIds=[22005], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 15 Jackpot
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[322], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[430], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[440], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 0
        set_user_value(triggerId=8110, key='Barrier11', value=0)
        set_user_value(triggerId=8120, key='Barrier12', value=0)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=15) # 15 Jackpot
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=2)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=0)
        set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='G07P201TimeLimit', value=1):
            return CheckP201()


class CheckP201(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=0)
        set_user_value(triggerId=9120, key='Box12Check', value=0)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=15) # 15 Jackpot
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=2)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=0)
        set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP201()


class NumberOffP201(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[110], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[120], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 0
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[22010], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 15 Jackpot
        set_mesh(triggerIds=[22005], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 15 Jackpot
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[322], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[430], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[440], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 0

    def on_tick(self) -> state.State:
        if true():
            return ResetP201()


class ResetP201(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P201End', value=1)
        set_user_value(key='G07P201Set', value=0)
        set_user_value(key='G07P201TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P202 
class NumberOnP202(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start jackpot
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[210], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[23010], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 15 Jackpot
        set_mesh(triggerIds=[23005], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 15 Jackpot
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[322], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[410], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=0)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=15) # 15 Jackpot
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=2)
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=0)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G07P202TimeLimit', value=1):
            return CheckP202()


class CheckP202(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=0)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=15) # 15 Jackpot
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=2)
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=0)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP202()


class NumberOffP202(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[210], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[23010], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 15 Jackpot
        set_mesh(triggerIds=[23005], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 15 Jackpot
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[322], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[410], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP202()


class ResetP202(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P202End', value=1)
        set_user_value(key='G07P202Set', value=0)
        set_user_value(key='G07P202TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P203 
class NumberOnP203(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start jackpot
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[130], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[210], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[240], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 0
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[32010], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 15 Jackpot
        set_mesh(triggerIds=[32005], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 15 Jackpot
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[430], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=0)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=0)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=0)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=15) # 15 Jackpot
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=0)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G07P203TimeLimit', value=1):
            return CheckP203()


class CheckP203(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=0)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=0)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=0)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=15) # 15 Jackpot
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=0)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP203()


class NumberOffP203(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[130], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[210], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[240], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 0
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[32010], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 15 Jackpot
        set_mesh(triggerIds=[32005], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 15 Jackpot
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[430], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP203()


class ResetP203(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P203End', value=1)
        set_user_value(key='G07P203Set', value=0)
        set_user_value(key='G07P203TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P204 
class NumberOnP204(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start jackpot
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[120], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 0
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[140], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[240], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 0
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[33010], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 15 Jackpot
        set_mesh(triggerIds=[33005], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 15 Jackpot
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[430], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=0)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=0)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=0)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=15) # 15 Jackpot
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=0)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G07P204TimeLimit', value=1):
            return CheckP204()


class CheckP204(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=0)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=0)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=0)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=15) # 15 Jackpot
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=0)
        set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP204()


class NumberOffP204(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[120], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 0
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[140], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[240], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 0
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[33010], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 15 Jackpot
        set_mesh(triggerIds=[33005], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 15 Jackpot
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[430], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP204()


class ResetP204(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P204End', value=1)
        set_user_value(key='G07P204Set', value=0)
        set_user_value(key='G07P204TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P205 
class NumberOnP205(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start jackpot
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[120], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 0
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[22020], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 20 Jackpot
        set_mesh(triggerIds=[22000], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 20 Jackpot
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[330], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 0
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[420], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 0
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=0)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=20) # 20 Jackpot
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=0)
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=0)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G07P205TimeLimit', value=1):
            return CheckP205()


class CheckP205(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=0)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=20) # 20 Jackpot
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=0)
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=0)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP205()


class NumberOffP205(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[120], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 0
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[22020], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 20 Jackpot
        set_mesh(triggerIds=[22000], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 20 Jackpot
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[330], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 0
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[420], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 0
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP205()


class ResetP205(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P205End', value=1)
        set_user_value(key='G07P205Set', value=0)
        set_user_value(key='G07P205TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P206 
class NumberOnP206(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start jackpot
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[111], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[141], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[23020], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 20 Jackpot
        set_mesh(triggerIds=[23000], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 20 Jackpot
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[310], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[340], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 0
        set_mesh(triggerIds=[411], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=1)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=1)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=20) # 20 Jackpot
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=0)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=0)
        set_user_value(triggerId=8410, key='Barrier41', value=1)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G07P206TimeLimit', value=1):
            return CheckP206()


class CheckP206(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=1)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=1)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=20) # 20 Jackpot
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=0)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=0)
        set_user_value(triggerId=9410, key='Box41Check', value=1)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP206()


class NumberOffP206(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[111], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[141], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[23020], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 20 Jackpot
        set_mesh(triggerIds=[23000], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 20 Jackpot
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[310], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[340], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 0
        set_mesh(triggerIds=[411], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP206()


class ResetP206(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P206End', value=1)
        set_user_value(key='G07P206Set', value=0)
        set_user_value(key='G07P206TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P207 
class NumberOnP207(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start jackpot
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[110], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[131], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[210], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[221], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[32020], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 20 Jackpot
        set_mesh(triggerIds=[32000], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 20 Jackpot
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[431], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[440], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 0
        set_user_value(triggerId=8110, key='Barrier11', value=0)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=1)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=0)
        set_user_value(triggerId=8220, key='Barrier22', value=1)
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=20) # 20 Jackpot
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=1)
        set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='G07P207TimeLimit', value=1):
            return CheckP207()


class CheckP207(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=0)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=1)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=0)
        set_user_value(triggerId=9220, key='Box22Check', value=1)
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=20) # 20 Jackpot
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=1)
        set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP207()


class NumberOffP207(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[110], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[131], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[210], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[221], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[32020], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 20 Jackpot
        set_mesh(triggerIds=[32000], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 20 Jackpot
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[431], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[440], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 0

    def on_tick(self) -> state.State:
        if true():
            return ResetP207()


class ResetP207(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P207End', value=1)
        set_user_value(key='G07P207Set', value=0)
        set_user_value(key='G07P207TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P208 
class NumberOnP208(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start jackpot
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[121], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[231], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 1
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[33020], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 20 Jackpot
        set_mesh(triggerIds=[33000], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 20 Jackpot
        set_mesh(triggerIds=[341], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[441], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 1
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=1)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=1)
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=20) # 20 Jackpot
        set_user_value(triggerId=8340, key='Barrier34', value=1)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='G07P208TimeLimit', value=1):
            return CheckP208()


class CheckP208(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=1)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=1)
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=20) # 20 Jackpot
        set_user_value(triggerId=9340, key='Box34Check', value=1)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP208()


class NumberOffP208(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[121], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[231], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 1
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[33020], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 20 Jackpot
        set_mesh(triggerIds=[33000], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 20 Jackpot
        set_mesh(triggerIds=[341], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[441], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 1

    def on_tick(self) -> state.State:
        if true():
            return ResetP208()


class ResetP208(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P208End', value=1)
        set_user_value(key='G07P208Set', value=0)
        set_user_value(key='G07P208TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P209 
class NumberOnP209(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start jackpot
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[22020], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 25 Jackpot
        set_mesh(triggerIds=[22005], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 25 Jackpot
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=25) # 25 Jackpot
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G07P209TimeLimit', value=1):
            return CheckP209()


class CheckP209(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=25) # 25 Jackpot
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP209()


class NumberOffP209(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[22020], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 25 Jackpot
        set_mesh(triggerIds=[22005], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 25 Jackpot
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP209()


class ResetP209(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P209End', value=1)
        set_user_value(key='G07P209Set', value=0)
        set_user_value(key='G07P209TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P210 
class NumberOnP210(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start jackpot
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[110], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[140], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[210], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[320], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 0
        set_mesh(triggerIds=[33020], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 /25 Jackpot
        set_mesh(triggerIds=[33005], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 /25 Jackpot
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[440], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 0
        set_user_value(triggerId=8110, key='Barrier11', value=0)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=0)
        set_user_value(triggerId=8210, key='Barrier21', value=0)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=0)
        set_user_value(triggerId=8330, key='Barrier33', value=25) # 25 Jackpot
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='G07P210TimeLimit', value=1):
            return CheckP210()


class CheckP210(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=0)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=0)
        set_user_value(triggerId=9210, key='Box21Check', value=0)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=0)
        set_user_value(triggerId=9330, key='Box33Check', value=25) # 25 Jackpot
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP210()


class NumberOffP210(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[110], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[140], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[210], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[320], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 0
        set_mesh(triggerIds=[33020], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 /25 Jackpot
        set_mesh(triggerIds=[33005], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 /25 Jackpot
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[440], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 0

    def on_tick(self) -> state.State:
        if true():
            return ResetP210()


class ResetP210(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P210End', value=1)
        set_user_value(key='G07P210Set', value=0)
        set_user_value(key='G07P210TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P301 
class NumberOnP301(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start jackpot
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[33020], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 25 Jackpot
        set_mesh(triggerIds=[33005], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 25 Jackpot
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=25) # 25 Jackpot
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G07P301TimeLimit', value=1):
            return CheckP301()


class CheckP301(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=25) # 25 Jackpot
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP301()


class NumberOffP301(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[33020], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 25 Jackpot
        set_mesh(triggerIds=[33005], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 25 Jackpot
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP301()


class ResetP301(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P301End', value=1)
        set_user_value(key='G07P301Set', value=0)
        set_user_value(key='G07P301TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P302 
class NumberOnP302(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start jackpot
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[23020], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 25 Jackpot
        set_mesh(triggerIds=[23005], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 25 Jackpot
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=25) # 25 Jackpot
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G07P302TimeLimit', value=1):
            return CheckP302()


class CheckP302(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=25) # 25 Jackpot
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP302()


class NumberOffP302(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[23020], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 25 Jackpot
        set_mesh(triggerIds=[23005], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 25 Jackpot
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP302()


class ResetP302(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P302End', value=1)
        set_user_value(key='G07P302Set', value=0)
        set_user_value(key='G07P302TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P303 
class NumberOnP303(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start jackpot
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[32020], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 25 Jackpot
        set_mesh(triggerIds=[32005], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 25 Jackpot
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=25) # 25 Jackpot
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G07P303TimeLimit', value=1):
            return CheckP303()


class CheckP303(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=25) # 25 Jackpot
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP303()


class NumberOffP303(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[32020], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 25 Jackpot
        set_mesh(triggerIds=[32005], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 25 Jackpot
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP303()


class ResetP303(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P303End', value=1)
        set_user_value(key='G07P303Set', value=0)
        set_user_value(key='G07P303TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P304 
class NumberOnP304(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start jackpot
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[22020], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 20 Jackpot
        set_mesh(triggerIds=[22000], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 20 Jackpot
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[322], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=20) # 20 Jackpot
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=2)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G07P304TimeLimit', value=1):
            return CheckP304()


class CheckP304(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=20) # 20 Jackpot
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=2)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP304()


class NumberOffP304(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[22020], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 20 Jackpot
        set_mesh(triggerIds=[22000], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 20 Jackpot
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[322], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP304()


class ResetP304(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P304End', value=1)
        set_user_value(key='G07P304Set', value=0)
        set_user_value(key='G07P304TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P305 
class NumberOnP305(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start jackpot
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[211], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 1
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[23020], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 20 Jackpot
        set_mesh(triggerIds=[23000], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 20 Jackpot
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[334], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[411], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[431], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=1)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=20) # 20 Jackpot
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=4)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=1)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=1)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G07P305TimeLimit', value=1):
            return CheckP305()


class CheckP305(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=1)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=20) # 20 Jackpot
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=4)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=1)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=1)
        set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP305()


class NumberOffP305(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[211], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 1
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[23020], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 20 Jackpot
        set_mesh(triggerIds=[23000], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 20 Jackpot
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[334], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[411], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[431], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP305()


class ResetP305(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P305End', value=1)
        set_user_value(key='G07P305Set', value=0)
        set_user_value(key='G07P305TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P306 
class NumberOnP306(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start jackpot
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[141], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[33020], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 20 Jackpot
        set_mesh(triggerIds=[33000], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 20 Jackpot
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[411], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[441], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 1
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=1)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=20) # 20 Jackpot
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=1)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='G07P306TimeLimit', value=1):
            return CheckP306()


class CheckP306(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=1)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=20) # 20 Jackpot
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=1)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP306()


class NumberOffP306(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[141], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[33020], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 20 Jackpot
        set_mesh(triggerIds=[33000], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 20 Jackpot
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[411], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[441], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 1

    def on_tick(self) -> state.State:
        if true():
            return ResetP306()


class ResetP306(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P306End', value=1)
        set_user_value(key='G07P306Set', value=0)
        set_user_value(key='G07P306TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P307 
class NumberOnP307(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start jackpot
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[32030], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 30 Jackpot
        set_mesh(triggerIds=[32000], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 30 Jackpot
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=30) # 30 Jackpot
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G07P307TimeLimit', value=1):
            return CheckP307()


class CheckP307(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=30) # 30 Jackpot
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP307()


class NumberOffP307(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[32030], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 30 Jackpot
        set_mesh(triggerIds=[32000], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 30 Jackpot
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP307()


class ResetP307(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P307End', value=1)
        set_user_value(key='G07P307Set', value=0)
        set_user_value(key='G07P307TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P308 
class NumberOnP308(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start jackpot
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[115], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[131], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[23030], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 30 Jackpot
        set_mesh(triggerIds=[23000], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 30 Jackpot
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[311], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[431], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=5)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=1)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=30) # 30 Jackpot
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=1)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=1)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G07P308TimeLimit', value=1):
            return CheckP308()


class CheckP308(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=5)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=1)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=30) # 30 Jackpot
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=1)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=1)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP308()


class NumberOffP308(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[115], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[131], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[23030], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 30 Jackpot
        set_mesh(triggerIds=[23000], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 30 Jackpot
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[311], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[431], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP308()


class ResetP308(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P308End', value=1)
        set_user_value(key='G07P308Set', value=0)
        set_user_value(key='G07P308TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P309 
class NumberOnP309(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start jackpot
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start jackpot
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[22010], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 15 Jackpot
        set_mesh(triggerIds=[22005], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 15 Jackpot
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[33020], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 25 Jackpot
        set_mesh(triggerIds=[33005], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 25 Jackpot
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=15) # 15 Jackpot
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=25) # 25 Jackpot
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G07P309TimeLimit', value=1):
            return CheckP309()


class CheckP309(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=15) # 15 Jackpot
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=25) # 25 Jackpot
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP309()


class NumberOffP309(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[22010], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 15 Jackpot
        set_mesh(triggerIds=[22005], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 15 Jackpot
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[33020], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 25 Jackpot
        set_mesh(triggerIds=[33005], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 25 Jackpot
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP309()


class ResetP309(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P309End', value=1)
        set_user_value(key='G07P309Set', value=0)
        set_user_value(key='G07P309TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P310 
class NumberOnP310(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start jackpot
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start jackpot
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[224], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[23020], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 20 Jackpot
        set_mesh(triggerIds=[23000], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 20 Jackpot
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[32020], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 20 Jackpot
        set_mesh(triggerIds=[32000], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 20 Jackpot
        set_mesh(triggerIds=[334], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=4)
        set_user_value(triggerId=8230, key='Barrier23', value=20) # 20 Jackpot
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=20) # 20 Jackpot
        set_user_value(triggerId=8330, key='Barrier33', value=4)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G07P310TimeLimit', value=1):
            return CheckP310()


class CheckP310(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=4)
        set_user_value(triggerId=9230, key='Box23Check', value=20) # 20 Jackpot
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=20) # 20 Jackpot
        set_user_value(triggerId=9330, key='Box33Check', value=4)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP310()


class NumberOffP310(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[224], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[23020], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 20 Jackpot
        set_mesh(triggerIds=[23000], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 20 Jackpot
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[32020], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 20 Jackpot
        set_mesh(triggerIds=[32000], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 20 Jackpot
        set_mesh(triggerIds=[334], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP310()


class ResetP310(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P310End', value=1)
        set_user_value(key='G07P310Set', value=0)
        set_user_value(key='G07P310TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P401 
class NumberOnP401(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start jackpot
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[22030], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 30 Jackpot
        set_mesh(triggerIds=[22000], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 30 Jackpot
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[334], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=30) # 30 Jackpot
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=4)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G07P401TimeLimit', value=1):
            return CheckP401()


class CheckP401(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=30) # 30 Jackpot
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=4)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP401()


class NumberOffP401(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[22030], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 30 Jackpot
        set_mesh(triggerIds=[22000], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 30 Jackpot
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[334], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP401()


class ResetP401(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P401End', value=1)
        set_user_value(key='G07P401Set', value=0)
        set_user_value(key='G07P401TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P402 
class NumberOnP402(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start jackpot
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[224], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[33030], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 30 Jackpot
        set_mesh(triggerIds=[33000], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 30 Jackpot
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=4)
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=30) # 30 Jackpot
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G07P402TimeLimit', value=1):
            return CheckP402()


class CheckP402(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=4)
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=30) # 30 Jackpot
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP402()


class NumberOffP402(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[224], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[33030], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 30 Jackpot
        set_mesh(triggerIds=[33000], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 30 Jackpot
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP402()


class ResetP402(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P402End', value=1)
        set_user_value(key='G07P402Set', value=0)
        set_user_value(key='G07P402TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P403 
class NumberOnP403(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start jackpot
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[23020], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 25 Jackpot
        set_mesh(triggerIds=[23005], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 25 Jackpot
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=25) # 25 Jackpot
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G07P403TimeLimit', value=1):
            return CheckP403()


class CheckP403(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=25) # 25 Jackpot
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP403()


class NumberOffP403(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[23020], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 25 Jackpot
        set_mesh(triggerIds=[23005], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 25 Jackpot
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP403()


class ResetP403(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P403End', value=1)
        set_user_value(key='G07P403Set', value=0)
        set_user_value(key='G07P403TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P404 
class NumberOnP404(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start jackpot
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[115], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[32020], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 25 Jackpot
        set_mesh(triggerIds=[32005], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 25 Jackpot
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=5)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=25) # 25 Jackpot
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G07P404TimeLimit', value=1):
            return CheckP404()


class CheckP404(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=5)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=25) # 25 Jackpot
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP404()


class NumberOffP404(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[115], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[32020], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 25 Jackpot
        set_mesh(triggerIds=[32005], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 25 Jackpot
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP404()


class ResetP404(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P404End', value=1)
        set_user_value(key='G07P404Set', value=0)
        set_user_value(key='G07P404TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P405 
class NumberOnP405(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start jackpot
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start jackpot
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[32010], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 15 Jackpot
        set_mesh(triggerIds=[32005], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 15 Jackpot
        set_mesh(triggerIds=[33010], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 15 Jackpot
        set_mesh(triggerIds=[33005], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 15 Jackpot
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=15) # 15 Jackpot
        set_user_value(triggerId=8330, key='Barrier33', value=15) # 15 Jackpot
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G07P405TimeLimit', value=1):
            return CheckP405()


class CheckP405(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=15) # 15 Jackpot
        set_user_value(triggerId=9330, key='Box33Check', value=15) # 15 Jackpot
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP405()


class NumberOffP405(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[32010], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 15 Jackpot
        set_mesh(triggerIds=[32005], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 15 Jackpot
        set_mesh(triggerIds=[33010], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 15 Jackpot
        set_mesh(triggerIds=[33005], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 15 Jackpot
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP405()


class ResetP405(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P405End', value=1)
        set_user_value(key='G07P405Set', value=0)
        set_user_value(key='G07P405TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P406 
class NumberOnP406(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start jackpot
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start jackpot
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[23010], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 15 Jackpot
        set_mesh(triggerIds=[23005], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 15 Jackpot
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[32010], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 	15 Jackpot
        set_mesh(triggerIds=[32005], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 	15 Jackpot
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=15) # 15 Jackpot
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=15) # 15 Jackpot
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G07P406TimeLimit', value=1):
            return CheckP406()


class CheckP406(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=15) # 15 Jackpot
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=15) # 15 Jackpot
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP406()


class NumberOffP406(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[23010], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 15 Jackpot
        set_mesh(triggerIds=[23005], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 15 Jackpot
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[32010], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 	15 Jackpot
        set_mesh(triggerIds=[32005], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 	15 Jackpot
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP406()


class ResetP406(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P406End', value=1)
        set_user_value(key='G07P406Set', value=0)
        set_user_value(key='G07P406TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G07 P407 
class NumberOnP407(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 23 start jackpot
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start jackpot
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[22020], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 20 Jackpot
        set_mesh(triggerIds=[22000], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 20 Jackpot
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[33020], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 	20 Jackpot
        set_mesh(triggerIds=[33000], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 	20 Jackpot
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=20) # 20 Jackpot
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=20) # 20 Jackpot
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G07P407TimeLimit', value=1):
            return CheckP407()


class CheckP407(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=20) # 20 Jackpot
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=20) # 20 Jackpot
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP407()


class NumberOffP407(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[22020], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 20 Jackpot
        set_mesh(triggerIds=[22000], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 20 Jackpot
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[33020], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 	20 Jackpot
        set_mesh(triggerIds=[33000], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 	20 Jackpot
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP407()


class ResetP407(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G07P407End', value=1)
        set_user_value(key='G07P407Set', value=0)
        set_user_value(key='G07P407TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


