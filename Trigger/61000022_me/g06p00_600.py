""" trigger/61000022_me/g06p00_600.xml """
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
        if user_value(key='G06P101Set', value=1):
            return NumberOnP101()
        if user_value(key='G06P102Set', value=1):
            return NumberOnP102()
        if user_value(key='G06P103Set', value=1):
            return NumberOnP103()
        if user_value(key='G06P104Set', value=1):
            return NumberOnP104()
        if user_value(key='G06P105Set', value=1):
            return NumberOnP105()
        if user_value(key='G06P106Set', value=1):
            return NumberOnP106()
        if user_value(key='G06P107Set', value=1):
            return NumberOnP107()
        if user_value(key='G06P108Set', value=1):
            return NumberOnP108()
        if user_value(key='G06P109Set', value=1):
            return NumberOnP109()
        if user_value(key='G06P110Set', value=1):
            return NumberOnP110()
        if user_value(key='G06P201Set', value=1):
            return NumberOnP201()
        if user_value(key='G06P202Set', value=1):
            return NumberOnP202()
        if user_value(key='G06P203Set', value=1):
            return NumberOnP203()
        if user_value(key='G06P204Set', value=1):
            return NumberOnP204()
        if user_value(key='G06P205Set', value=1):
            return NumberOnP205()
        if user_value(key='G06P206Set', value=1):
            return NumberOnP206()
        if user_value(key='G06P207Set', value=1):
            return NumberOnP207()
        if user_value(key='G06P208Set', value=1):
            return NumberOnP208()
        if user_value(key='G06P209Set', value=1):
            return NumberOnP209()
        if user_value(key='G06P210Set', value=1):
            return NumberOnP210()
        if user_value(key='G06P211Set', value=1):
            return NumberOnP211()
        if user_value(key='G06P212Set', value=1):
            return NumberOnP212()
        if user_value(key='G06P213Set', value=1):
            return NumberOnP213()
        if user_value(key='G06P214Set', value=1):
            return NumberOnP214()
        if user_value(key='G06P215Set', value=1):
            return NumberOnP215()
        if user_value(key='G06P216Set', value=1):
            return NumberOnP216()
        if user_value(key='G06P217Set', value=1):
            return NumberOnP217()
        if user_value(key='G06P218Set', value=1):
            return NumberOnP218()
        if user_value(key='G06P219Set', value=1):
            return NumberOnP219()
        if user_value(key='G06P220Set', value=1):
            return NumberOnP220()
        if user_value(key='G06P301Set', value=1):
            return NumberOnP301()
        if user_value(key='G06P302Set', value=1):
            return NumberOnP302()
        if user_value(key='G06P303Set', value=1):
            return NumberOnP303()
        if user_value(key='G06P304Set', value=1):
            return NumberOnP304()
        if user_value(key='G06P305Set', value=1):
            return NumberOnP305()
        if user_value(key='G06P306Set', value=1):
            return NumberOnP306()
        if user_value(key='G06P307Set', value=1):
            return NumberOnP307()
        if user_value(key='G06P308Set', value=1):
            return NumberOnP308()
        if user_value(key='G06P309Set', value=1):
            return NumberOnP309()
        if user_value(key='G06P310Set', value=1):
            return NumberOnP310()
        if user_value(key='G06P311Set', value=1):
            return NumberOnP311()
        if user_value(key='G06P312Set', value=1):
            return NumberOnP312()
        if user_value(key='G06P313Set', value=1):
            return NumberOnP313()
        if user_value(key='G06P314Set', value=1):
            return NumberOnP314()
        if user_value(key='G06P315Set', value=1):
            return NumberOnP315()
        if user_value(key='G06P316Set', value=1):
            return NumberOnP316()
        if user_value(key='G06P317Set', value=1):
            return NumberOnP317()
        if user_value(key='G06P318Set', value=1):
            return NumberOnP318()
        if user_value(key='G06P319Set', value=1):
            return NumberOnP319()
        if user_value(key='G06P320Set', value=1):
            return NumberOnP320()
        if user_value(key='G06P401Set', value=1):
            return NumberOnP401()
        if user_value(key='G06P402Set', value=1):
            return NumberOnP402()
        if user_value(key='G06P403Set', value=1):
            return NumberOnP403()
        if user_value(key='G06P404Set', value=1):
            return NumberOnP404()
        if user_value(key='G06P405Set', value=1):
            return NumberOnP405()
        if user_value(key='G06P406Set', value=1):
            return NumberOnP406()
        if user_value(key='G06P407Set', value=1):
            return NumberOnP407()
        if user_value(key='G06P408Set', value=1):
            return NumberOnP408()
        if user_value(key='G06P409Set', value=1):
            return NumberOnP409()
        if user_value(key='G06P410Set', value=1):
            return NumberOnP410()


#   G06 P101 
class NumberOnP101(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        set_mesh(triggerIds=[121], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[141], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[2307], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 7 gamble
        set_mesh(triggerIds=[241], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[311], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[321], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[411], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[431], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[441], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 1
        set_user_value(triggerId=8110, key='Barrier11', value=1)
        set_user_value(triggerId=8120, key='Barrier12', value=1)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=1)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=7) # 7 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=1)
        set_user_value(triggerId=8310, key='Barrier31', value=1)
        set_user_value(triggerId=8320, key='Barrier32', value=1)
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=1)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=1)
        set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='G06P101TimeLimit', value=1):
            return CheckP101()


class CheckP101(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=1)
        set_user_value(triggerId=9120, key='Box12Check', value=1)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=1)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=7) # 7 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=1)
        set_user_value(triggerId=9310, key='Box31Check', value=1)
        set_user_value(triggerId=9320, key='Box32Check', value=1)
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=1)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=1)
        set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP101()


class NumberOffP101(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[111], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[121], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[141], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[2307], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 7 gamble
        set_mesh(triggerIds=[241], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[311], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[321], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[411], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[431], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[441], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 1

    def on_tick(self) -> state.State:
        if true():
            return ResetP101()


class ResetP101(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P101End', value=1)
        set_user_value(key='G06P101Set', value=0)
        set_user_value(key='G06P101TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P102 
class NumberOnP102(state.State):
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
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[120], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 0
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[221], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[3207], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 7 gamble
        set_mesh(triggerIds=[330], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 0
        set_mesh(triggerIds=[341], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[420], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 0
        set_mesh(triggerIds=[431], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=0)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=1)
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=7) # 7 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=0)
        set_user_value(triggerId=8340, key='Barrier34', value=1)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=0)
        set_user_value(triggerId=8430, key='Barrier43', value=1)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G06P102TimeLimit', value=1):
            return CheckP102()


class CheckP102(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=0)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=1)
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=7) # 7 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=0)
        set_user_value(triggerId=9340, key='Box34Check', value=1)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=0)
        set_user_value(triggerId=9430, key='Box43Check', value=1)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP102()


class NumberOffP102(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[120], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 0
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[221], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[3207], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 7 gamble
        set_mesh(triggerIds=[330], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 0
        set_mesh(triggerIds=[341], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[420], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 0
        set_mesh(triggerIds=[431], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP102()


class ResetP102(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P102End', value=1)
        set_user_value(key='G06P102Set', value=0)
        set_user_value(key='G06P102TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P103 
class NumberOnP103(state.State):
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
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[110], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[140], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[221], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[310], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[3307], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 7 gamble
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[410], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[430], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[441], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 1
        set_user_value(triggerId=8110, key='Barrier11', value=0)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=0)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=1)
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=0)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=7) # 7 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=0)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=0)
        set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='G06P103TimeLimit', value=1):
            return CheckP103()


class CheckP103(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=0)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=0)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=1)
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=0)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=7) # 7 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=0)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=0)
        set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP103()


class NumberOffP103(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[110], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[140], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[221], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[310], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[3307], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 7 gamble
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[410], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[430], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[441], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 1

    def on_tick(self) -> state.State:
        if true():
            return ResetP103()


class ResetP103(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P103End', value=1)
        set_user_value(key='G06P103Set', value=0)
        set_user_value(key='G06P103TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P104 
class NumberOnP104(state.State):
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
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[111], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[121], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[140], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[210], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[230], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 0
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[311], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[3208], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[331], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[340], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 0
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[421], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[430], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=1)
        set_user_value(triggerId=8120, key='Barrier12', value=1)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=0)
        set_user_value(triggerId=8210, key='Barrier21', value=0)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=0)
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=1)
        set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=1)
        set_user_value(triggerId=8340, key='Barrier34', value=0)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=1)
        set_user_value(triggerId=8430, key='Barrier43', value=0)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G06P104TimeLimit', value=1):
            return CheckP104()


class CheckP104(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=1)
        set_user_value(triggerId=9120, key='Box12Check', value=1)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=0)
        set_user_value(triggerId=9210, key='Box21Check', value=0)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=0)
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=1)
        set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=1)
        set_user_value(triggerId=9340, key='Box34Check', value=0)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=1)
        set_user_value(triggerId=9430, key='Box43Check', value=0)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP104()


class NumberOffP104(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[111], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[121], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[140], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[210], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[230], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 0
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[311], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[3208], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[331], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[340], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 0
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[421], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[430], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP104()


class ResetP104(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P104End', value=1)
        set_user_value(key='G06P104Set', value=0)
        set_user_value(key='G06P104TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P105 
class NumberOnP105(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[210], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[2308], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 8 gamble
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[310], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[410], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[440], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 0
        set_user_value(triggerId=8110, key='Barrier11', value=0)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=0)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=8) # 8 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=0)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=0)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='G06P105TimeLimit', value=1):
            return CheckP105()


class CheckP105(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=0)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=0)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=8) # 8 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=0)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=0)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP105()


class NumberOffP105(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[110], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[210], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[2308], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 8 gamble
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[310], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[410], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[440], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 0

    def on_tick(self) -> state.State:
        if true():
            return ResetP105()


class ResetP105(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P105End', value=1)
        set_user_value(key='G06P105Set', value=0)
        set_user_value(key='G06P105TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P106 
class NumberOnP106(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
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
        set_mesh(triggerIds=[120], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 0
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[140], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[2208], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 8 gamble
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[310], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[340], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 0
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[420], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 0
        set_mesh(triggerIds=[430], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=0)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=0)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=8) # 8 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=0)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=0)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=0)
        set_user_value(triggerId=8430, key='Barrier43', value=0)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G06P106TimeLimit', value=1):
            return CheckP106()


class CheckP106(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=0)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=0)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=8) # 8 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=0)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=0)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=0)
        set_user_value(triggerId=9430, key='Box43Check', value=0)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP106()


class NumberOffP106(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[120], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 0
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[140], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[2208], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 8 gamble
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[310], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[340], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 0
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[420], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 0
        set_mesh(triggerIds=[430], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP106()


class ResetP106(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P106End', value=1)
        set_user_value(key='G06P106Set', value=0)
        set_user_value(key='G06P106TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P107 
class NumberOnP107(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[130], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[210], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[2309], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[310], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[420], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 0
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[440], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 0
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=0)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=0)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=0)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=0)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='G06P107TimeLimit', value=1):
            return CheckP107()


class CheckP107(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=0)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=0)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=0)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=0)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP107()


class NumberOffP107(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[130], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[210], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[2309], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[310], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[420], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 0
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[440], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 0

    def on_tick(self) -> state.State:
        if true():
            return ResetP107()


class ResetP107(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P107End', value=1)
        set_user_value(key='G06P107Set', value=0)
        set_user_value(key='G06P107TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P108 
class NumberOnP108(state.State):
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
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[110], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[140], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[221], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[241], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[311], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[3209], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 9 gamble
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[411], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[430], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=0)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=0)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=1)
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=1)
        set_user_value(triggerId=8310, key='Barrier31', value=1)
        set_user_value(triggerId=8320, key='Barrier32', value=9) # 9 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=1)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=0)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G06P108TimeLimit', value=1):
            return CheckP108()


class CheckP108(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=0)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=0)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=1)
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=1)
        set_user_value(triggerId=9310, key='Box31Check', value=1)
        set_user_value(triggerId=9320, key='Box32Check', value=9) # 9 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=1)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=0)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP108()


class NumberOffP108(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[110], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[140], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[221], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[241], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[311], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[3209], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 9 gamble
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[411], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[430], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP108()


class ResetP108(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P108End', value=1)
        set_user_value(key='G06P108Set', value=0)
        set_user_value(key='G06P108TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P109 
class NumberOnP109(state.State):
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
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[110], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[130], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[210], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[231], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 1
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[310], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[321], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[3309], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 9 gamble
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[420], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 0
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[441], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 1
        set_user_value(triggerId=8110, key='Barrier11', value=0)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=0)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=0)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=1)
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=0)
        set_user_value(triggerId=8320, key='Barrier32', value=1)
        set_user_value(triggerId=8330, key='Barrier33', value=9) # 9 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=0)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='G06P109TimeLimit', value=1):
            return CheckP109()


class CheckP109(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=0)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=0)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=0)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=1)
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=0)
        set_user_value(triggerId=9320, key='Box32Check', value=1)
        set_user_value(triggerId=9330, key='Box33Check', value=9) # 9 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=0)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP109()


class NumberOffP109(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[110], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[130], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[210], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[231], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 1
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[310], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[321], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[3309], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 9 gamble
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[420], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 0
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[441], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 1

    def on_tick(self) -> state.State:
        if true():
            return ResetP109()


class ResetP109(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P109End', value=1)
        set_user_value(key='G06P109Set', value=0)
        set_user_value(key='G06P109TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P110 
class NumberOnP110(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[130], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[221], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[23010], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[23000], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[240], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 0
        set_mesh(triggerIds=[310], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[321], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[334], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[341], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[420], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 0
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[440], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 0
        set_user_value(triggerId=8110, key='Barrier11', value=0)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=0)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=1)
        set_user_value(triggerId=8230, key='Barrier23', value=6) # 10 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=0)
        set_user_value(triggerId=8310, key='Barrier31', value=0)
        set_user_value(triggerId=8320, key='Barrier32', value=1)
        set_user_value(triggerId=8330, key='Barrier33', value=4)
        set_user_value(triggerId=8340, key='Barrier34', value=1)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=0)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='G06P110TimeLimit', value=1):
            return CheckP110()


class CheckP110(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=0)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=0)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=1)
        set_user_value(triggerId=9230, key='Box23Check', value=6) # 10 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=0)
        set_user_value(triggerId=9310, key='Box31Check', value=0)
        set_user_value(triggerId=9320, key='Box32Check', value=1)
        set_user_value(triggerId=9330, key='Box33Check', value=4)
        set_user_value(triggerId=9340, key='Box34Check', value=1)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=0)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP110()


class NumberOffP110(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[110], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[130], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[221], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[23010], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[23000], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[240], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 0
        set_mesh(triggerIds=[310], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[321], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[334], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[341], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[420], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 0
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[440], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 0

    def on_tick(self) -> state.State:
        if true():
            return ResetP110()


class ResetP110(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P110End', value=1)
        set_user_value(key='G06P110Set', value=0)
        set_user_value(key='G06P110TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P201 
class NumberOnP201(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[140], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[2207], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 7 gamble
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[240], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 0
        set_mesh(triggerIds=[310], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[33010], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[33000], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[420], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 0
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=0)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=7) # 7 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=0)
        set_user_value(triggerId=8310, key='Barrier31', value=0)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=6) # 10 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=0)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G06P201TimeLimit', value=1):
            return CheckP201()


class CheckP201(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=0)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=7) # 7 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=0)
        set_user_value(triggerId=9310, key='Box31Check', value=0)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=6) # 10 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=0)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP201()


class NumberOffP201(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[140], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[2207], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 7 gamble
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[240], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 0
        set_mesh(triggerIds=[310], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[33010], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[33000], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[420], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 0
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP201()


class ResetP201(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P201End', value=1)
        set_user_value(key='G06P201Set', value=0)
        set_user_value(key='G06P201TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P202 
class NumberOnP202(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[130], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[2309], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3208], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[440], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 0
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=0)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='G06P202TimeLimit', value=1):
            return CheckP202()


class CheckP202(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=0)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP202()


class NumberOffP202(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[130], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[2309], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3208], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[440], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 0

    def on_tick(self) -> state.State:
        if true():
            return ResetP202()


class ResetP202(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P202End', value=1)
        set_user_value(key='G06P202Set', value=0)
        set_user_value(key='G06P202TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P203 
class NumberOnP203(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        set_mesh(triggerIds=[130], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[2208], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 8 gamble
        set_mesh(triggerIds=[2308], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 8 gamble
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[310], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[410], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=0)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=8) # 8 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=8) # 8 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=0)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=0)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G06P203TimeLimit', value=1):
            return CheckP203()


class CheckP203(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=0)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=8) # 8 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=8) # 8 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=0)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=0)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP203()


class NumberOffP203(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[130], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[2208], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 8 gamble
        set_mesh(triggerIds=[2308], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 8 gamble
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[310], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[410], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP203()


class ResetP203(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P203End', value=1)
        set_user_value(key='G06P203Set', value=0)
        set_user_value(key='G06P203TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P204 
class NumberOnP204(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[110], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[140], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[22010], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[22000], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[3209], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 9 gamble
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[340], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 0
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[430], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=0)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=0)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=6) # 10 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=9) # 9 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=0)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=0)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G06P204TimeLimit', value=1):
            return CheckP204()


class CheckP204(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=0)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=0)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=6) # 10 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=9) # 9 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=0)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=0)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP204()


class NumberOffP204(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[110], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[140], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[22010], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[22000], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[3209], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 9 gamble
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[340], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 0
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[430], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP204()


class ResetP204(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P204End', value=1)
        set_user_value(key='G06P204Set', value=0)
        set_user_value(key='G06P204TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P205 
class NumberOnP205(state.State):
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
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[120], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 0
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[140], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[310], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[32010], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[32000], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[3308], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=0)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=0)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=0)
        set_user_value(triggerId=8320, key='Barrier32', value=6) # 10 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=8) # 8 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G06P205TimeLimit', value=1):
            return CheckP205()


class CheckP205(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=0)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=0)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=0)
        set_user_value(triggerId=9320, key='Box32Check', value=6) # 10 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=8) # 8 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP205()


class NumberOffP205(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[120], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 0
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[140], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[310], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[32010], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[32000], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[3308], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP205()


class ResetP205(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P205End', value=1)
        set_user_value(key='G06P205Set', value=0)
        set_user_value(key='G06P205TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P206 
class NumberOnP206(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[110], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[120], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 0
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[210], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[2309], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3207], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 7 gamble
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[430], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[440], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 0
        set_user_value(triggerId=8110, key='Barrier11', value=0)
        set_user_value(triggerId=8120, key='Barrier12', value=0)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=0)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=7) # 7 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=0)
        set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='G06P206TimeLimit', value=1):
            return CheckP206()


class CheckP206(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=0)
        set_user_value(triggerId=9120, key='Box12Check', value=0)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=0)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=7) # 7 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=0)
        set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP206()


class NumberOffP206(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[110], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[120], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 0
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[210], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[2309], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3207], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 7 gamble
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[430], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[440], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 0

    def on_tick(self) -> state.State:
        if true():
            return ResetP206()


class ResetP206(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P206End', value=1)
        set_user_value(key='G06P206Set', value=0)
        set_user_value(key='G06P206TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P207 
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
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[120], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 0
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[140], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[224], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3208], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[3307], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 7 gamble
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[410], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[440], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 0
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=0)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=0)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=4)
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=7) # 7 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=0)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='G06P207TimeLimit', value=1):
            return CheckP207()


class CheckP207(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=0)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=0)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=4)
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=7) # 7 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=0)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP207()


class NumberOffP207(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[120], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 0
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[140], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[224], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3208], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[3307], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 7 gamble
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[410], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[440], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 0

    def on_tick(self) -> state.State:
        if true():
            return ResetP207()


class ResetP207(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P207End', value=1)
        set_user_value(key='G06P207Set', value=0)
        set_user_value(key='G06P207TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P208 
class NumberOnP208(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[130], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[2209], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 9 gamble
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[240], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 0
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[322], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[3309], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 9 gamble
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[410], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[430], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=0)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=9) # 9 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=0)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=2)
        set_user_value(triggerId=8330, key='Barrier33', value=9) # 9 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=0)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=0)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G06P208TimeLimit', value=1):
            return CheckP208()


class CheckP208(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=0)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=9) # 9 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=0)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=2)
        set_user_value(triggerId=9330, key='Box33Check', value=9) # 9 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=0)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=0)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP208()


class NumberOffP208(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[130], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[2209], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 9 gamble
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[240], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 0
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[322], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[3309], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 9 gamble
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[410], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[430], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP208()


class ResetP208(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P208End', value=1)
        set_user_value(key='G06P208Set', value=0)
        set_user_value(key='G06P208TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P209 
class NumberOnP209(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[110], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[210], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[23010], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[23000], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3207], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 7 gamble
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[440], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 0
        set_user_value(triggerId=8110, key='Barrier11', value=0)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=0)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=6) # 10 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=7) # 7 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='G06P209TimeLimit', value=1):
            return CheckP209()


class CheckP209(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=0)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=0)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=6) # 10 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=7) # 7 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP209()


class NumberOffP209(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[110], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[210], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[23010], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[23000], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3207], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 7 gamble
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[440], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 0

    def on_tick(self) -> state.State:
        if true():
            return ResetP209()


class ResetP209(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P209End', value=1)
        set_user_value(key='G06P209Set', value=0)
        set_user_value(key='G06P209TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P210 
class NumberOnP210(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[110], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[22010], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[22000], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[33010], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[33000], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[440], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 0
        set_user_value(triggerId=8110, key='Barrier11', value=0)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=6) # 10 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=6) # 10 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='G06P210TimeLimit', value=1):
            return CheckP210()


class CheckP210(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=0)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=6) # 10 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=6) # 10 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP210()


class NumberOffP210(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[110], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[22010], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[22000], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[33010], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[33000], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[440], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 0

    def on_tick(self) -> state.State:
        if true():
            return ResetP210()


class ResetP210(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P210End', value=1)
        set_user_value(key='G06P210Set', value=0)
        set_user_value(key='G06P210TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P211 
class NumberOnP211(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[121], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[140], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[2307], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 7 gamble
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[3207], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 7 gamble
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[410], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[431], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[440], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 0
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=1)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=0)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=7) # 7 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=7) # 7 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=0)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=1)
        set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='G06P211TimeLimit', value=1):
            return CheckP211()


class CheckP211(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=1)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=0)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=7) # 7 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=7) # 7 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=0)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=1)
        set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP211()


class NumberOffP211(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[121], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[140], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[2307], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 7 gamble
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[3207], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 7 gamble
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[410], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[431], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[440], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 0

    def on_tick(self) -> state.State:
        if true():
            return ResetP211()


class ResetP211(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P211End', value=1)
        set_user_value(key='G06P211Set', value=0)
        set_user_value(key='G06P211TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P212 
class NumberOnP212(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[210], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[2308], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 8 gamble
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[340], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 0
        set_mesh(triggerIds=[410], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=0)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=0)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=8) # 8 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=0)
        set_user_value(triggerId=8410, key='Barrier41', value=0)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G06P212TimeLimit', value=1):
            return CheckP212()


class CheckP212(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=0)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=0)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=8) # 8 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=0)
        set_user_value(triggerId=9410, key='Box41Check', value=0)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP212()


class NumberOffP212(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[110], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 0
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[210], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[2308], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 8 gamble
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[340], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 0
        set_mesh(triggerIds=[410], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP212()


class ResetP212(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P212End', value=1)
        set_user_value(key='G06P212Set', value=0)
        set_user_value(key='G06P212TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P213 
class NumberOnP213(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
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
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[2208], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 8 gamble
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[240], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 0
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[322], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[330], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 0
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=8) # 8 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=0)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=2)
        set_user_value(triggerId=8330, key='Barrier33', value=0)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G06P213TimeLimit', value=1):
            return CheckP213()


class CheckP213(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=8) # 8 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=0)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=2)
        set_user_value(triggerId=9330, key='Box33Check', value=0)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP213()


class NumberOffP213(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[2208], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 8 gamble
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[240], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 0
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[322], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[330], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 0
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP213()


class ResetP213(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P213End', value=1)
        set_user_value(key='G06P213Set', value=0)
        set_user_value(key='G06P213TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P214 
class NumberOnP214(state.State):
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
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[130], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[221], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[241], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[322], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[3309], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 9 gamble
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[410], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[441], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 1
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=0)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=1)
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=1)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=2)
        set_user_value(triggerId=8330, key='Barrier33', value=9) # 9 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=0)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='G06P214TimeLimit', value=1):
            return CheckP214()


class CheckP214(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=0)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=1)
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=1)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=2)
        set_user_value(triggerId=9330, key='Box33Check', value=9) # 9 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=0)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP214()


class NumberOffP214(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[130], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[221], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[241], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[322], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[3309], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 9 gamble
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[410], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[441], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 1

    def on_tick(self) -> state.State:
        if true():
            return ResetP214()


class ResetP214(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P214End', value=1)
        set_user_value(key='G06P214Set', value=0)
        set_user_value(key='G06P214TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P215 
class NumberOnP215(state.State):
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
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[131], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[210], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[310], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[3209], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 9 gamble
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[341], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[431], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=1)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=0)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=0)
        set_user_value(triggerId=8320, key='Barrier32', value=9) # 9 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=1)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=1)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G06P215TimeLimit', value=1):
            return CheckP215()


class CheckP215(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=1)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=0)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=0)
        set_user_value(triggerId=9320, key='Box32Check', value=9) # 9 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=1)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=1)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP215()


class NumberOffP215(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[131], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[210], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 0
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[310], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[3209], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 9 gamble
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[341], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[431], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP215()


class ResetP215(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P215End', value=1)
        set_user_value(key='G06P215Set', value=0)
        set_user_value(key='G06P215TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P216 
class NumberOnP216(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        set_mesh(triggerIds=[121], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[140], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[2309], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[322], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[331], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[340], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 0
        set_mesh(triggerIds=[411], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=1)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=0)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=2)
        set_user_value(triggerId=8330, key='Barrier33', value=1)
        set_user_value(triggerId=8340, key='Barrier34', value=0)
        set_user_value(triggerId=8410, key='Barrier41', value=1)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G06P216TimeLimit', value=1):
            return CheckP216()


class CheckP216(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=1)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=0)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=2)
        set_user_value(triggerId=9330, key='Box33Check', value=1)
        set_user_value(triggerId=9340, key='Box34Check', value=0)
        set_user_value(triggerId=9410, key='Box41Check', value=1)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP216()


class NumberOffP216(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[121], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[140], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[2309], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[322], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[331], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[340], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 0
        set_mesh(triggerIds=[411], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP216()


class ResetP216(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P216End', value=1)
        set_user_value(key='G06P216Set', value=0)
        set_user_value(key='G06P216TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P217 
class NumberOnP217(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
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
        set_mesh(triggerIds=[111], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[141], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[22010], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[22000], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[230], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 0
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[411], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[420], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 0
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=1)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=1)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=6) # 10 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=0)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=1)
        set_user_value(triggerId=8420, key='Barrier42', value=0)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G06P217TimeLimit', value=1):
            return CheckP217()


class CheckP217(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=1)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=1)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=6) # 10 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=0)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=1)
        set_user_value(triggerId=9420, key='Box42Check', value=0)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP217()


class NumberOffP217(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[111], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[141], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[22010], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[22000], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[230], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 0
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[411], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[420], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 0
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP217()


class ResetP217(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P217End', value=1)
        set_user_value(key='G06P217Set', value=0)
        set_user_value(key='G06P217TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P218 
class NumberOnP218(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        set_mesh(triggerIds=[141], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[211], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 1
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[23010], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[23000], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[331], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[421], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=1)
        set_user_value(triggerId=8210, key='Barrier21', value=1)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=6) # 10 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=1)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=1)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G06P218TimeLimit', value=1):
            return CheckP218()


class CheckP218(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=1)
        set_user_value(triggerId=9210, key='Box21Check', value=1)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=6) # 10 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=1)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=1)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP218()


class NumberOffP218(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[141], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[211], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 1
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[23010], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[23000], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[331], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[421], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP218()


class ResetP218(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P218End', value=1)
        set_user_value(key='G06P218Set', value=0)
        set_user_value(key='G06P218TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P219 
class NumberOnP219(state.State):
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
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[130], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[220], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 0
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[32010], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[32000], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[420], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 0
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=0)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=0)
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=6) # 10 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=0)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G06P219TimeLimit', value=1):
            return CheckP219()


class CheckP219(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=0)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=0)
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=6) # 10 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=0)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP219()


class NumberOffP219(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[130], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[220], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 0
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[32010], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[32000], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[420], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 0
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP219()


class ResetP219(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P219End', value=1)
        set_user_value(key='G06P219Set', value=0)
        set_user_value(key='G06P219TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P220 
class NumberOnP220(state.State):
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
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[140], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[241], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[310], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[33010], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[33000], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[430], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[441], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 1
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=0)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=1)
        set_user_value(triggerId=8310, key='Barrier31', value=0)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=6) # 10 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=0)
        set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='G06P220TimeLimit', value=1):
            return CheckP220()


class CheckP220(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=0)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=1)
        set_user_value(triggerId=9310, key='Box31Check', value=0)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=6) # 10 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=0)
        set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP220()


class NumberOffP220(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[140], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[241], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[310], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 0
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[33010], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[33000], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[430], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 0
        set_mesh(triggerIds=[441], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 1

    def on_tick(self) -> state.State:
        if true():
            return ResetP220()


class ResetP220(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P220End', value=1)
        set_user_value(key='G06P220Set', value=0)
        set_user_value(key='G06P220TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P301 
class NumberOnP301(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[23010], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[23000], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[32010], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[32000], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=6) # 10 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=6) # 10 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G06P301TimeLimit', value=1):
            return CheckP301()


class CheckP301(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=6) # 10 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=6) # 10 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP301()


class NumberOffP301(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[23010], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[23000], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[32010], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[32000], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP301()


class ResetP301(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P301End', value=1)
        set_user_value(key='G06P301Set', value=0)
        set_user_value(key='G06P301TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P302 
class NumberOnP302(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[2208], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 8 gamble
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[33010], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[33000], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=8) # 8 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=6) # 10 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G06P302TimeLimit', value=1):
            return CheckP302()


class CheckP302(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=8) # 8 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=6) # 10 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP302()


class NumberOffP302(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[2208], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 8 gamble
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[33010], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[33000], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP302()


class ResetP302(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P302End', value=1)
        set_user_value(key='G06P302Set', value=0)
        set_user_value(key='G06P302TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P303 
class NumberOnP303(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[22010], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[22000], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[2309], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=6) # 10 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G06P303TimeLimit', value=1):
            return CheckP303()


class CheckP303(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=6) # 10 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP303()


class NumberOffP303(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[22010], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[22000], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[2309], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP303()


class ResetP303(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P303End', value=1)
        set_user_value(key='G06P303Set', value=0)
        set_user_value(key='G06P303TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P304 
class NumberOnP304(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
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
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[2309], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[32010], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[32000], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=6) # 10 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G06P304TimeLimit', value=1):
            return CheckP304()


class CheckP304(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=6) # 10 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP304()


class NumberOffP304(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[2309], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[32010], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[32000], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP304()


class ResetP304(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P304End', value=1)
        set_user_value(key='G06P304Set', value=0)
        set_user_value(key='G06P304TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P305 
class NumberOnP305(state.State):
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
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
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
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3209], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 9 gamble
        set_mesh(triggerIds=[3309], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 9 gamble
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=9) # 9 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=9) # 9 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G06P305TimeLimit', value=1):
            return CheckP305()


class CheckP305(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=9) # 9 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=9) # 9 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
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
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3209], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 9 gamble
        set_mesh(triggerIds=[3309], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 9 gamble
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP305()


class ResetP305(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P305End', value=1)
        set_user_value(key='G06P305Set', value=0)
        set_user_value(key='G06P305TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P306 
class NumberOnP306(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
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
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[22010], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[22000], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[23010], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[23000], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=6) # 10 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=6) # 10 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G06P306TimeLimit', value=1):
            return CheckP306()


class CheckP306(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=6) # 10 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=6) # 10 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP306()


class NumberOffP306(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[22010], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[22000], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[23010], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[23000], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP306()


class ResetP306(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P306End', value=1)
        set_user_value(key='G06P306Set', value=0)
        set_user_value(key='G06P306TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P307 
class NumberOnP307(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[23010], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[23000], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[3208], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[3307], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 7 gamble
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=6) # 10 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=7) # 7 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G06P307TimeLimit', value=1):
            return CheckP307()


class CheckP307(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=6) # 10 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=7) # 7 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP307()


class NumberOffP307(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[23010], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[23000], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[3208], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[3307], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 7 gamble
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP307()


class ResetP307(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P307End', value=1)
        set_user_value(key='G06P307Set', value=0)
        set_user_value(key='G06P307TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P308 
class NumberOnP308(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[2207], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 7 gamble
        set_mesh(triggerIds=[2308], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 8 gamble
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[3209], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 9 gamble
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=7) # 7 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=8) # 8 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=9) # 9 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G06P308TimeLimit', value=1):
            return CheckP308()


class CheckP308(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=7) # 7 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=8) # 8 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=9) # 9 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP308()


class NumberOffP308(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[2207], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 7 gamble
        set_mesh(triggerIds=[2308], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 8 gamble
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[3209], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 9 gamble
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP308()


class ResetP308(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P308End', value=1)
        set_user_value(key='G06P308Set', value=0)
        set_user_value(key='G06P308TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P309 
class NumberOnP309(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
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
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[2208], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 8 gamble
        set_mesh(triggerIds=[2308], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 8 gamble
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[3208], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[334], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=8) # 8 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=8) # 8 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=4)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G06P309TimeLimit', value=1):
            return CheckP309()


class CheckP309(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=8) # 8 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=8) # 8 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=4)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP309()


class NumberOffP309(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[2208], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 8 gamble
        set_mesh(triggerIds=[2308], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 8 gamble
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[3208], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[334], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP309()


class ResetP309(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P309End', value=1)
        set_user_value(key='G06P309Set', value=0)
        set_user_value(key='G06P309TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P310 
class NumberOnP310(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
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
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[2307], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 7 gamble
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3207], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 7 gamble
        set_mesh(triggerIds=[3307], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 7 gamble
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=7) # 7 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=7) # 7 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=7) # 7 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G06P310TimeLimit', value=1):
            return CheckP310()


class CheckP310(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=7) # 7 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=7) # 7 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=7) # 7 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP310()


class NumberOffP310(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[2307], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 7 gamble
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3207], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 7 gamble
        set_mesh(triggerIds=[3307], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 7 gamble
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP310()


class ResetP310(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P310End', value=1)
        set_user_value(key='G06P310Set', value=0)
        set_user_value(key='G06P310TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P311 
class NumberOnP311(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[115], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[141], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[211], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 1
        set_mesh(triggerIds=[224], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[23010], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[23000], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[33010], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[33000], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=5)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=1)
        set_user_value(triggerId=8210, key='Barrier21', value=1)
        set_user_value(triggerId=8220, key='Barrier22', value=4)
        set_user_value(triggerId=8230, key='Barrier23', value=6) # 10 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=6) # 10 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G06P311TimeLimit', value=1):
            return CheckP311()


class CheckP311(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=5)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=1)
        set_user_value(triggerId=9210, key='Box21Check', value=1)
        set_user_value(triggerId=9220, key='Box22Check', value=4)
        set_user_value(triggerId=9230, key='Box23Check', value=6) # 10 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=6) # 10 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP311()


class NumberOffP311(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[115], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[141], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[211], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 1
        set_mesh(triggerIds=[224], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[23010], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[23000], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[33010], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[33000], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP311()


class ResetP311(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P311End', value=1)
        set_user_value(key='G06P311Set', value=0)
        set_user_value(key='G06P311TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P312 
class NumberOnP312(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[22010], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[22000], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[311], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[322], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[33010], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[33000], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[431], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=6) # 10 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=1)
        set_user_value(triggerId=8320, key='Barrier32', value=2)
        set_user_value(triggerId=8330, key='Barrier33', value=6) # 10 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=1)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G06P312TimeLimit', value=1):
            return CheckP312()


class CheckP312(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=6) # 10 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=1)
        set_user_value(triggerId=9320, key='Box32Check', value=2)
        set_user_value(triggerId=9330, key='Box33Check', value=6) # 10 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=1)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP312()


class NumberOffP312(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[22010], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[22000], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[311], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[322], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[33010], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[33000], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[431], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP312()


class ResetP312(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P312End', value=1)
        set_user_value(key='G06P312Set', value=0)
        set_user_value(key='G06P312TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P313 
class NumberOnP313(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[2208], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 8 gamble
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[3208], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=8) # 8 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G06P313TimeLimit', value=1):
            return CheckP313()


class CheckP313(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=8) # 8 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP313()


class NumberOffP313(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[2208], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 8 gamble
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[3208], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP313()


class ResetP313(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P313End', value=1)
        set_user_value(key='G06P313Set', value=0)
        set_user_value(key='G06P313TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P314 
class NumberOnP314(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[224], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[2309], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[322], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[3309], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 9 gamble
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=4)
        set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=2)
        set_user_value(triggerId=8330, key='Barrier33', value=9) # 9 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G06P314TimeLimit', value=1):
            return CheckP314()


class CheckP314(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=4)
        set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=2)
        set_user_value(triggerId=9330, key='Box33Check', value=9) # 9 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP314()


class NumberOffP314(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[224], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[2309], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[322], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[3309], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 9 gamble
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP314()


class ResetP314(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P314End', value=1)
        set_user_value(key='G06P314Set', value=0)
        set_user_value(key='G06P314TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P315 
class NumberOnP315(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
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
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[2207], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 7 gamble
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[3307], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 7 gamble
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=7) # 7 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=7) # 7 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G06P315TimeLimit', value=1):
            return CheckP315()


class CheckP315(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=7) # 7 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=7) # 7 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP315()


class NumberOffP315(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[2207], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 7 gamble
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[3307], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 7 gamble
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP315()


class ResetP315(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P315End', value=1)
        set_user_value(key='G06P315Set', value=0)
        set_user_value(key='G06P315TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P316 
class NumberOnP316(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[131], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[2307], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 7 gamble
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3208], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[334], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[421], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=1)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=7) # 7 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=4)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=1)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G06P316TimeLimit', value=1):
            return CheckP316()


class CheckP316(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=1)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=7) # 7 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=4)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=1)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP316()


class NumberOffP316(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[131], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[2307], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 7 gamble
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3208], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[334], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[421], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP316()


class ResetP316(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P316End', value=1)
        set_user_value(key='G06P316Set', value=0)
        set_user_value(key='G06P316TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P317 
class NumberOnP317(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[111], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[2309], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[311], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[322], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[3308], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 8 gamble
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[441], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 1
        set_user_value(triggerId=8110, key='Barrier11', value=1)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=1)
        set_user_value(triggerId=8320, key='Barrier32', value=2)
        set_user_value(triggerId=8330, key='Barrier33', value=8) # 8 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='G06P317TimeLimit', value=1):
            return CheckP317()


class CheckP317(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=1)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=1)
        set_user_value(triggerId=9320, key='Box32Check', value=2)
        set_user_value(triggerId=9330, key='Box33Check', value=8) # 8 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP317()


class NumberOffP317(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[111], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[2309], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[311], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[322], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[3308], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 8 gamble
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[441], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 1

    def on_tick(self) -> state.State:
        if true():
            return ResetP317()


class ResetP317(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P317End', value=1)
        set_user_value(key='G06P317Set', value=0)
        set_user_value(key='G06P317TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P318 
class NumberOnP318(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
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
        set_mesh(triggerIds=[140], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[2208], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 8 gamble
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[3207], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 7 gamble
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[410], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=0)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=8) # 8 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=7) # 7 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=0)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G06P318TimeLimit', value=1):
            return CheckP318()


class CheckP318(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=0)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=8) # 8 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=7) # 7 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=0)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP318()


class NumberOffP318(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[140], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 0
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[2208], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 8 gamble
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[3207], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 7 gamble
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[410], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 0
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP318()


class ResetP318(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P318End', value=1)
        set_user_value(key='G06P318Set', value=0)
        set_user_value(key='G06P318TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P319 
class NumberOnP319(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[130], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[2308], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 8 gamble
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3209], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 9 gamble
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[440], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 0
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=0)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=8) # 8 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=9) # 9 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='G06P319TimeLimit', value=1):
            return CheckP319()


class CheckP319(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=0)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=8) # 8 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=9) # 9 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=0)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP319()


class NumberOffP319(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[130], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 0
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[2308], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 8 gamble
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3209], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 9 gamble
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[440], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 0

    def on_tick(self) -> state.State:
        if true():
            return ResetP319()


class ResetP319(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P319End', value=1)
        set_user_value(key='G06P319Set', value=0)
        set_user_value(key='G06P319TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P320 
class NumberOnP320(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[131], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[211], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 1
        set_mesh(triggerIds=[2209], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 9 gamble
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[321], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[3309], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 9 gamble
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=1)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=1)
        set_user_value(triggerId=8220, key='Barrier22', value=9) # 9 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=1)
        set_user_value(triggerId=8330, key='Barrier33', value=9) # 9 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G06P320TimeLimit', value=1):
            return CheckP320()


class CheckP320(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=1)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=1)
        set_user_value(triggerId=9220, key='Box22Check', value=9) # 9 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=1)
        set_user_value(triggerId=9330, key='Box33Check', value=9) # 9 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP320()


class NumberOffP320(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[131], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[211], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 1
        set_mesh(triggerIds=[2209], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 9 gamble
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[321], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[3309], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 9 gamble
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP320()


class ResetP320(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P320End', value=1)
        set_user_value(key='G06P320Set', value=0)
        set_user_value(key='G06P320TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P401 
class NumberOnP401(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[115], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[2209], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 9 gamble
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[3208], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[3307], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 7 gamble
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=5)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=9) # 9 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=7) # 7 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G06P401TimeLimit', value=1):
            return CheckP401()


class CheckP401(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=5)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=9) # 9 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=7) # 7 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP401()


class NumberOffP401(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[115], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[2209], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 9 gamble
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[3208], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[3307], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 7 gamble
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP401()


class ResetP401(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P401End', value=1)
        set_user_value(key='G06P401Set', value=0)
        set_user_value(key='G06P401TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P402 
class NumberOnP402(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[115], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[2209], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 9 gamble
        set_mesh(triggerIds=[23010], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[23000], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3208], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=5)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=9) # 9 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=6) # 10 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G06P402TimeLimit', value=1):
            return CheckP402()


class CheckP402(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=5)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=9) # 9 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=6) # 10 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP402()


class NumberOffP402(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[115], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[2209], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 9 gamble
        set_mesh(triggerIds=[23010], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[23000], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3208], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP402()


class ResetP402(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P402End', value=1)
        set_user_value(key='G06P402Set', value=0)
        set_user_value(key='G06P402TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P403 
class NumberOnP403(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[115], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[2207], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 7 gamble
        set_mesh(triggerIds=[2309], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[322], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[33010], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[33000], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=5)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=7) # 7 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=2)
        set_user_value(triggerId=8330, key='Barrier33', value=6) # 10 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G06P403TimeLimit', value=1):
            return CheckP403()


class CheckP403(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=5)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=7) # 7 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=2)
        set_user_value(triggerId=9330, key='Box33Check', value=6) # 10 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP403()


class NumberOffP403(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[115], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[2207], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 7 gamble
        set_mesh(triggerIds=[2309], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[322], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[33010], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[33000], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP403()


class ResetP403(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P403End', value=1)
        set_user_value(key='G06P403Set', value=0)
        set_user_value(key='G06P403TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P404 
class NumberOnP404(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[115], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[23010], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[23000], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[32010], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[32000], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[33010], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[33000], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=5)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=6) # 10 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=6) # 10 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=6) # 10 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G06P404TimeLimit', value=1):
            return CheckP404()


class CheckP404(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=5)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=6) # 10 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=6) # 10 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=6) # 10 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP404()


class NumberOffP404(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[115], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[23010], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[23000], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 10 gamble
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[32010], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[32000], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[33010], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[33000], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP404()


class ResetP404(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P404End', value=1)
        set_user_value(key='G06P404Set', value=0)
        set_user_value(key='G06P404TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P405 
class NumberOnP405(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[2209], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 9 gamble
        set_mesh(triggerIds=[2309], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[3209], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 9 gamble
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=9) # 9 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=9) # 9 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=9) # 9 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G06P405TimeLimit', value=1):
            return CheckP405()


class CheckP405(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=9) # 9 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=9) # 9 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=9) # 9 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP405()


class NumberOffP405(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[2209], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 9 gamble
        set_mesh(triggerIds=[2309], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 9 gamble
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[3209], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 9 gamble
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP405()


class ResetP405(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P405End', value=1)
        set_user_value(key='G06P405Set', value=0)
        set_user_value(key='G06P405TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P406 
class NumberOnP406(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[115], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[2308], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 8 gamble
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3208], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[3308], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 8 gamble
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=5)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=8) # 8 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=8) # 8 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=8) # 8 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G06P406TimeLimit', value=1):
            return CheckP406()


class CheckP406(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=5)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=8) # 8 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=8) # 8 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=8) # 8 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP406()


class NumberOffP406(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[115], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[2308], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 8 gamble
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[3208], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 8 gamble
        set_mesh(triggerIds=[3308], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 8 gamble
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP406()


class ResetP406(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P406End', value=1)
        set_user_value(key='G06P406Set', value=0)
        set_user_value(key='G06P406TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P407 
class NumberOnP407(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[2208], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 8 gamble
        set_mesh(triggerIds=[2308], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 8 gamble
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[3309], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 9 gamble
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=8) # 8 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=8) # 8 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=9) # 9 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G06P407TimeLimit', value=1):
            return CheckP407()


class CheckP407(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=8) # 8 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=8) # 8 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=9) # 9 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP407()


class NumberOffP407(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[2208], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 8 gamble
        set_mesh(triggerIds=[2308], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 8 gamble
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[3309], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 9 gamble
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP407()


class ResetP407(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P407End', value=1)
        set_user_value(key='G06P407Set', value=0)
        set_user_value(key='G06P407TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P408 
class NumberOnP408(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[22010], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[22000], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[32010], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[32000], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[3307], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 7 gamble
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=6) # 10 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=6) # 10 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=7) # 7 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G06P408TimeLimit', value=1):
            return CheckP408()


class CheckP408(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=6) # 10 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=6) # 10 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=7) # 7 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP408()


class NumberOffP408(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[22010], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[22000], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[32010], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[32000], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 10 gamble
        set_mesh(triggerIds=[3307], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 7 gamble
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP408()


class ResetP408(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P408End', value=1)
        set_user_value(key='G06P408Set', value=0)
        set_user_value(key='G06P408TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P409 
class NumberOnP409(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=6) # 23 start gamble
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[2209], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 9 gamble
        set_mesh(triggerIds=[2308], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 8 gamble
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[3309], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 9 gamble
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=9) # 9 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=8) # 8 gamble
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=9) # 9 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G06P409TimeLimit', value=1):
            return CheckP409()


class CheckP409(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=9) # 9 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=8) # 8 gamble
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=9) # 9 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP409()


class NumberOffP409(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[2209], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 9 gamble
        set_mesh(triggerIds=[2308], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 8 gamble
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[3309], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 9 gamble
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP409()


class ResetP409(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P409End', value=1)
        set_user_value(key='G06P409Set', value=0)
        set_user_value(key='G06P409TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G06 P410 
class NumberOnP410(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7120, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7130, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7140, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7210, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7220, key='ColorStart', value=6) # 22 start gamble
        set_user_value(triggerId=7230, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7240, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7310, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7320, key='ColorStart', value=6) # 32 start gamble
        set_user_value(triggerId=7330, key='ColorStart', value=6) # 33 start gamble
        set_user_value(triggerId=7340, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7410, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7420, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7430, key='ColorStart', value=1) # yellow
        set_user_value(triggerId=7440, key='ColorStart', value=1) # yellow
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[22010], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[22000], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[3209], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 9 gamble
        set_mesh(triggerIds=[33010], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[33000], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=6) # 10 gamble
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=9) # 9 gamble
        set_user_value(triggerId=8330, key='Barrier33', value=6) # 10 gamble
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G06P410TimeLimit', value=1):
            return CheckP410()


class CheckP410(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=6) # 10 gamble
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=9) # 9 gamble
        set_user_value(triggerId=9330, key='Box33Check', value=6) # 10 gamble
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP410()


class NumberOffP410(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[22010], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[22000], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 10 gamble
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[3209], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 9 gamble
        set_mesh(triggerIds=[33010], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[33000], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 10 gamble
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP410()


class ResetP410(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G06P410End', value=1)
        set_user_value(key='G06P410Set', value=0)
        set_user_value(key='G06P410TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


