""" trigger/61000008_me/g05p00_500.xml """
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

    def on_tick(self) -> state.State:
        if user_value(key='G05P01Set', value=1):
            return NumberOnP01()
        if user_value(key='G05P02Set', value=1):
            return NumberOnP02()
        if user_value(key='G05P03Set', value=1):
            return NumberOnP03()
        if user_value(key='G05P04Set', value=1):
            return NumberOnP04()
        if user_value(key='G05P05Set', value=1):
            return NumberOnP05()
        if user_value(key='G05P06Set', value=1):
            return NumberOnP06()
        if user_value(key='G05P07Set', value=1):
            return NumberOnP07()
        if user_value(key='G05P08Set', value=1):
            return NumberOnP08()
        if user_value(key='G05P09Set', value=1):
            return NumberOnP09()
        if user_value(key='G05P10Set', value=1):
            return NumberOnP10()
        if user_value(key='G05P11Set', value=1):
            return NumberOnP11()
        if user_value(key='G05P12Set', value=1):
            return NumberOnP12()
        if user_value(key='G05P13Set', value=1):
            return NumberOnP13()
        if user_value(key='G05P14Set', value=1):
            return NumberOnP14()
        if user_value(key='G05P15Set', value=1):
            return NumberOnP15()
        if user_value(key='G05P16Set', value=1):
            return NumberOnP16()
        if user_value(key='G05P17Set', value=1):
            return NumberOnP17()
        if user_value(key='G05P18Set', value=1):
            return NumberOnP18()
        if user_value(key='G05P19Set', value=1):
            return NumberOnP19()
        if user_value(key='G05P20Set', value=1):
            return NumberOnP20()
        if user_value(key='G05P21Set', value=1):
            return NumberOnP21()
        if user_value(key='G05P22Set', value=1):
            return NumberOnP22()
        if user_value(key='G05P23Set', value=1):
            return NumberOnP23()
        if user_value(key='G05P24Set', value=1):
            return NumberOnP24()
        if user_value(key='G05P25Set', value=1):
            return NumberOnP25()
        if user_value(key='G05P26Set', value=1):
            return NumberOnP26()
        if user_value(key='G05P27Set', value=1):
            return NumberOnP27()
        if user_value(key='G05P28Set', value=1):
            return NumberOnP28()
        if user_value(key='G05P29Set', value=1):
            return NumberOnP29()
        if user_value(key='G05P30Set', value=1):
            return NumberOnP30()
        if user_value(key='G05P31Set', value=1):
            return NumberOnP31()
        if user_value(key='G05P32Set', value=1):
            return NumberOnP32()
        if user_value(key='G05P33Set', value=1):
            return NumberOnP33()
        if user_value(key='G05P34Set', value=1):
            return NumberOnP34()
        if user_value(key='G05P35Set', value=1):
            return NumberOnP35()
        if user_value(key='G05P36Set', value=1):
            return NumberOnP36()
        if user_value(key='G05P37Set', value=1):
            return NumberOnP37()
        if user_value(key='G05P38Set', value=1):
            return NumberOnP38()
        if user_value(key='G05P39Set', value=1):
            return NumberOnP39()
        if user_value(key='G05P40Set', value=1):
            return NumberOnP40()
        if user_value(key='G05P41Set', value=1):
            return NumberOnP41()
        if user_value(key='G05P42Set', value=1):
            return NumberOnP42()
        if user_value(key='G05P43Set', value=1):
            return NumberOnP43()
        if user_value(key='G05P44Set', value=1):
            return NumberOnP44()
        if user_value(key='G05P45Set', value=1):
            return NumberOnP45()
        if user_value(key='G05P46Set', value=1):
            return NumberOnP46()
        if user_value(key='G05P47Set', value=1):
            return NumberOnP47()
        if user_value(key='G05P48Set', value=1):
            return NumberOnP48()
        if user_value(key='G05P49Set', value=1):
            return NumberOnP49()
        if user_value(key='G05P50Set', value=1):
            return NumberOnP50()

    def on_exit(self):
        set_user_value(triggerId=7110, key='ColorStart', value=1) # start
        set_user_value(triggerId=7120, key='ColorStart', value=1) # start
        set_user_value(triggerId=7130, key='ColorStart', value=1) # start
        set_user_value(triggerId=7140, key='ColorStart', value=1) # start
        set_user_value(triggerId=7210, key='ColorStart', value=1) # start
        set_user_value(triggerId=7220, key='ColorStart', value=1) # start
        set_user_value(triggerId=7230, key='ColorStart', value=1) # start
        set_user_value(triggerId=7240, key='ColorStart', value=1) # start
        set_user_value(triggerId=7310, key='ColorStart', value=1) # start
        set_user_value(triggerId=7320, key='ColorStart', value=1) # start
        set_user_value(triggerId=7330, key='ColorStart', value=1) # start
        set_user_value(triggerId=7340, key='ColorStart', value=1) # start
        set_user_value(triggerId=7410, key='ColorStart', value=1) # start
        set_user_value(triggerId=7420, key='ColorStart', value=1) # start
        set_user_value(triggerId=7430, key='ColorStart', value=1) # start
        set_user_value(triggerId=7440, key='ColorStart', value=1) # start


#   G05 P01 
class NumberOnP01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[121], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[221], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[331], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=1)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=1)
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=1)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G05P01TimeLimit', value=1):
            return CheckP01()


class CheckP01(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=1)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=1)
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=1)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP01()


class NumberOffP01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[121], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[221], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[331], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP01()


class ResetP01(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P01End', value=1)
        set_user_value(key='G05P01Set', value=0)
        set_user_value(key='G05P01TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P02 
class NumberOnP02(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[115], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[131], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[211], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 1
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[341], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=5)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=1)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=1)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=1)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G05P02TimeLimit', value=1):
            return CheckP02()


class CheckP02(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=5)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=1)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=1)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=1)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP02()


class NumberOffP02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[115], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[131], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[211], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 1
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[341], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP02()


class ResetP02(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P02End', value=1)
        set_user_value(key='G05P02Set', value=0)
        set_user_value(key='G05P02TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P03 
class NumberOnP03(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[111], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[211], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 1
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[334], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[431], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=1)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=1)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=4)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=1)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G05P03TimeLimit', value=1):
            return CheckP03()


class CheckP03(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=1)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=1)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=4)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=1)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP03()


class NumberOffP03(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[111], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[211], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 1
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[334], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[431], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP03()


class ResetP03(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P03End', value=1)
        set_user_value(key='G05P03Set', value=0)
        set_user_value(key='G05P03TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P04 
class NumberOnP04(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[111], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[224], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[241], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[441], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 1
        set_user_value(triggerId=8110, key='Barrier11', value=1)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=4)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=1)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='G05P04TimeLimit', value=1):
            return CheckP04()


class CheckP04(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=1)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=4)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=1)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP04()


class NumberOffP04(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[111], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[224], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[241], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[441], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 1

    def on_tick(self) -> state.State:
        if true():
            return ResetP04()


class ResetP04(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P04End', value=1)
        set_user_value(key='G05P04Set', value=0)
        set_user_value(key='G05P04TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P05 
class NumberOnP05(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[311], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[341], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=1)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=1)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G05P05TimeLimit', value=1):
            return CheckP05()


class CheckP05(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=1)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=1)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP05()


class NumberOffP05(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[311], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[341], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP05()


class ResetP05(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P05End', value=1)
        set_user_value(key='G05P05Set', value=0)
        set_user_value(key='G05P05TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P06 
class NumberOnP06(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[131], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[211], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 1
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[341], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[421], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=1)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=1)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=1)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=1)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G05P06TimeLimit', value=1):
            return CheckP06()


class CheckP06(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=1)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=1)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=1)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=1)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP06()


class NumberOffP06(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[131], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[211], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 1
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[341], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[421], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP06()


class ResetP06(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P06End', value=1)
        set_user_value(key='G05P06Set', value=0)
        set_user_value(key='G05P06TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P07 
class NumberOnP07(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[115], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[120], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 0
        set_mesh(triggerIds=[131], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[221], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[240], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 0
        set_mesh(triggerIds=[311], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[341], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=5)
        set_user_value(triggerId=8120, key='Barrier12', value=0)
        set_user_value(triggerId=8130, key='Barrier13', value=1)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=1)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=0)
        set_user_value(triggerId=8310, key='Barrier31', value=1)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=1)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G05P07TimeLimit', value=1):
            return CheckP07()


class CheckP07(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=5)
        set_user_value(triggerId=9120, key='Box12Check', value=0)
        set_user_value(triggerId=9130, key='Box13Check', value=1)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=1)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=0)
        set_user_value(triggerId=9310, key='Box31Check', value=1)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=1)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP07()


class NumberOffP07(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[115], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[120], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 0
        set_mesh(triggerIds=[131], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[221], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[240], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 0
        set_mesh(triggerIds=[311], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[341], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP07()


class ResetP07(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P07End', value=1)
        set_user_value(key='G05P07Set', value=0)
        set_user_value(key='G05P07TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P08 
class NumberOnP08(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[231], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 1
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[322], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[334], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=1)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=2)
        set_user_value(triggerId=8330, key='Barrier33', value=4)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G05P08TimeLimit', value=1):
            return CheckP08()


class CheckP08(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=1)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=2)
        set_user_value(triggerId=9330, key='Box33Check', value=4)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP08()


class NumberOffP08(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[231], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 1
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[322], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[334], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP08()


class ResetP08(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P08End', value=1)
        set_user_value(key='G05P08Set', value=0)
        set_user_value(key='G05P08TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P09 
class NumberOnP09(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[115], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[141], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[241], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[311], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=5)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=1)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=1)
        set_user_value(triggerId=8310, key='Barrier31', value=1)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G05P09TimeLimit', value=1):
            return CheckP09()


class CheckP09(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=5)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=1)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=1)
        set_user_value(triggerId=9310, key='Box31Check', value=1)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP09()


class NumberOffP09(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[115], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[141], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[241], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[311], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP09()


class ResetP09(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P09End', value=1)
        set_user_value(key='G05P09Set', value=0)
        set_user_value(key='G05P09TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P10 
class NumberOnP10(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[111], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[224], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[230], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 0
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[321], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[334], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[441], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 1
        set_user_value(triggerId=8110, key='Barrier11', value=1)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=4)
        set_user_value(triggerId=8230, key='Barrier23', value=0)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=1)
        set_user_value(triggerId=8330, key='Barrier33', value=4)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='G05P10TimeLimit', value=1):
            return CheckP10()


class CheckP10(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=1)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=4)
        set_user_value(triggerId=9230, key='Box23Check', value=0)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=1)
        set_user_value(triggerId=9330, key='Box33Check', value=4)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP10()


class NumberOffP10(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[111], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[224], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[230], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 0
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[321], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[334], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[441], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 1

    def on_tick(self) -> state.State:
        if true():
            return ResetP10()


class ResetP10(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P10End', value=1)
        set_user_value(key='G05P10Set', value=0)
        set_user_value(key='G05P10TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P11 
class NumberOnP11(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[115], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[131], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[211], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 1
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[311], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[341], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[421], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=5)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=1)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=1)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=1)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=1)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=1)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G05P11TimeLimit', value=1):
            return CheckP11()


class CheckP11(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=5)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=1)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=1)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=1)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=1)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=1)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP11()


class NumberOffP11(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[115], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[131], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[211], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 1
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[311], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[341], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[421], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP11()


class ResetP11(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P11End', value=1)
        set_user_value(key='G05P11Set', value=0)
        set_user_value(key='G05P11TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P12 
class NumberOnP12(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[221], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[331], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=1)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=1)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G05P12TimeLimit', value=1):
            return CheckP12()


class CheckP12(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=1)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=1)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP12()


class NumberOffP12(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[221], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[331], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP12()


class ResetP12(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P12End', value=1)
        set_user_value(key='G05P12Set', value=0)
        set_user_value(key='G05P12TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P13 
class NumberOnP13(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[121], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[231], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 1
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[421], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=1)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=1)
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=1)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G05P13TimeLimit', value=1):
            return CheckP13()


class CheckP13(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=1)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=1)
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=1)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP13()


class NumberOffP13(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[121], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[231], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 1
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[421], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP13()


class ResetP13(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P13End', value=1)
        set_user_value(key='G05P13Set', value=0)
        set_user_value(key='G05P13TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P14 
class NumberOnP14(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[141], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[241], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[421], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=1)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=1)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=1)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G05P14TimeLimit', value=1):
            return CheckP14()


class CheckP14(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=1)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=1)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=1)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP14()


class NumberOffP14(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[141], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[241], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[421], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP14()


class ResetP14(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P14End', value=1)
        set_user_value(key='G05P14Set', value=0)
        set_user_value(key='G05P14TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P15
class NumberOnP15(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[111], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[224], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[331], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[421], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=1)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=4)
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=1)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=1)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G05P15TimeLimit', value=1):
            return CheckP15()


class CheckP15(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=1)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=4)
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=1)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=1)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP15()


class NumberOffP15(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[111], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[224], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[331], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[421], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP15()


class ResetP15(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P15End', value=1)
        set_user_value(key='G05P15Set', value=0)
        set_user_value(key='G05P15TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P16 
class NumberOnP16(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[115], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[131], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[231], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 1
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[321], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=5)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=1)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=1)
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=1)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G05P16TimeLimit', value=1):
            return CheckP16()


class CheckP16(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=5)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=1)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=1)
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=1)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP16()


class NumberOffP16(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[115], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[131], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[231], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 1
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[321], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP16()


class ResetP16(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P16End', value=1)
        set_user_value(key='G05P16Set', value=0)
        set_user_value(key='G05P16TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P17 
class NumberOnP17(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[141], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[321], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[411], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=1)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=1)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=1)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G05P17TimeLimit', value=1):
            return CheckP17()


class CheckP17(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=1)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=1)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=1)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP17()


class NumberOffP17(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[141], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[321], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[411], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP17()


class ResetP17(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P17End', value=1)
        set_user_value(key='G05P17Set', value=0)
        set_user_value(key='G05P17TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P18 
class NumberOnP18(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[121], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[224], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[331], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=1)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=4)
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=1)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G05P18TimeLimit', value=1):
            return CheckP18()


class CheckP18(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=1)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=4)
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=1)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP18()


class NumberOffP18(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[121], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[224], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[331], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP18()


class ResetP18(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P18End', value=1)
        set_user_value(key='G05P18Set', value=0)
        set_user_value(key='G05P18TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P19 
class NumberOnP19(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[111], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[431], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=1)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=1)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G05P19TimeLimit', value=1):
            return CheckP19()


class CheckP19(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=1)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=1)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP19()


class NumberOffP19(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[111], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[431], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP19()


class ResetP19(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P19End', value=1)
        set_user_value(key='G05P19Set', value=0)
        set_user_value(key='G05P19TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P20 
class NumberOnP20(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[121], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[241], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=1)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=1)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G05P20TimeLimit', value=1):
            return CheckP20()


class CheckP20(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=1)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=1)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP20()


class NumberOffP20(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[121], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[241], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP20()


class ResetP20(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P20End', value=1)
        set_user_value(key='G05P20Set', value=0)
        set_user_value(key='G05P20TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P21 
class NumberOnP21(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[141], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[224], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[334], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[411], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=1)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=4)
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=4)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=1)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G05P21TimeLimit', value=1):
            return CheckP21()


class CheckP21(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=1)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=4)
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=4)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=1)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP21()


class NumberOffP21(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[141], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[224], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[334], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[411], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP21()


class ResetP21(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P21End', value=1)
        set_user_value(key='G05P21Set', value=0)
        set_user_value(key='G05P21TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P22 
class NumberOnP22(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[131], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[311], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=1)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=1)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G05P22TimeLimit', value=1):
            return CheckP22()


class CheckP22(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=1)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=1)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP22()


class NumberOffP22(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[131], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[311], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP22()


class ResetP22(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P22End', value=1)
        set_user_value(key='G05P22Set', value=0)
        set_user_value(key='G05P22TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P23 
class NumberOnP23(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[221], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[431], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=1)
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=1)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G05P23TimeLimit', value=1):
            return CheckP23()


class CheckP23(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=1)
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=1)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP23()


class NumberOffP23(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[221], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[431], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP23()


class ResetP23(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P23End', value=1)
        set_user_value(key='G05P23Set', value=0)
        set_user_value(key='G05P23TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P24 
class NumberOnP24(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[141], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[321], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[334], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=1)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=1)
        set_user_value(triggerId=8330, key='Barrier33', value=4)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G05P24TimeLimit', value=1):
            return CheckP24()


class CheckP24(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=1)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=1)
        set_user_value(triggerId=9330, key='Box33Check', value=4)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP24()


class NumberOffP24(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[141], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[321], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[334], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP24()


class ResetP24(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P24End', value=1)
        set_user_value(key='G05P24Set', value=0)
        set_user_value(key='G05P24TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P25
class NumberOnP25(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[111], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[141], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[224], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[231], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 1
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[321], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[334], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[421], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[441], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 1
        set_user_value(triggerId=8110, key='Barrier11', value=1)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=1)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=4)
        set_user_value(triggerId=8230, key='Barrier23', value=1)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=1)
        set_user_value(triggerId=8330, key='Barrier33', value=4)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=1)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='G05P25TimeLimit', value=1):
            return CheckP25()


class CheckP25(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=1)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=1)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=4)
        set_user_value(triggerId=9230, key='Box23Check', value=1)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=1)
        set_user_value(triggerId=9330, key='Box33Check', value=4)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=1)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP25()


class NumberOffP25(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[111], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 1
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[141], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[224], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[231], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 1
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[321], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[334], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[421], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[441], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 1

    def on_tick(self) -> state.State:
        if true():
            return ResetP25()


class ResetP25(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P25End', value=1)
        set_user_value(key='G05P25Set', value=0)
        set_user_value(key='G05P25TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P26 
class NumberOnP26(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[334], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[341], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[431], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=4)
        set_user_value(triggerId=8340, key='Barrier34', value=1)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=1)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G05P26TimeLimit', value=1):
            return CheckP26()


class CheckP26(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=4)
        set_user_value(triggerId=9340, key='Box34Check', value=1)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=1)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP26()


class NumberOffP26(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[334], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[341], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[431], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP26()


class ResetP26(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P26End', value=1)
        set_user_value(key='G05P26Set', value=0)
        set_user_value(key='G05P26TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P27 
class NumberOnP27(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[121], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[224], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[331], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=1)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=4)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=1)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G05P27TimeLimit', value=1):
            return CheckP27()


class CheckP27(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=1)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=4)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=1)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP27()


class NumberOffP27(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[121], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[224], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[331], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP27()


class ResetP27(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P27End', value=1)
        set_user_value(key='G05P27Set', value=0)
        set_user_value(key='G05P27TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P28 
class NumberOnP28(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[131], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[323], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[421], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=1)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=3)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=1)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G05P28TimeLimit', value=1):
            return CheckP28()


class CheckP28(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=1)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=3)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=1)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP28()


class NumberOffP28(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[131], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[323], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 3
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[421], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 1
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP28()


class ResetP28(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P28End', value=1)
        set_user_value(key='G05P28Set', value=0)
        set_user_value(key='G05P28TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P29 
class NumberOnP29(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[311], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=1)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G05P29TimeLimit', value=1):
            return CheckP29()


class CheckP29(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=1)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP29()


class NumberOffP29(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[311], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP29()


class ResetP29(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P29End', value=1)
        set_user_value(key='G05P29Set', value=0)
        set_user_value(key='G05P29TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P30 
class NumberOnP30(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[322], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[332], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[341], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=2)
        set_user_value(triggerId=8330, key='Barrier33', value=2)
        set_user_value(triggerId=8340, key='Barrier34', value=1)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G05P30TimeLimit', value=1):
            return CheckP30()


class CheckP30(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=2)
        set_user_value(triggerId=9330, key='Box33Check', value=2)
        set_user_value(triggerId=9340, key='Box34Check', value=1)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP30()


class NumberOffP30(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[322], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[332], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 2
        set_mesh(triggerIds=[341], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 1
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP30()


class ResetP30(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P30End', value=1)
        set_user_value(key='G05P30Set', value=0)
        set_user_value(key='G05P30TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P31 
class NumberOnP31(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[221], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[431], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=1)
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=1)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G05P31TimeLimit', value=1):
            return CheckP31()


class CheckP31(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=1)
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=1)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP31()


class NumberOffP31(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[221], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[431], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 1
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP31()


class ResetP31(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P31End', value=1)
        set_user_value(key='G05P31Set', value=0)
        set_user_value(key='G05P31TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P32 
class NumberOnP32(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[221], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[321], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=1)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=1)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G05P32TimeLimit', value=1):
            return CheckP32()


class CheckP32(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=1)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=1)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP32()


class NumberOffP32(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[221], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[321], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP32()


class ResetP32(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P32End', value=1)
        set_user_value(key='G05P32Set', value=0)
        set_user_value(key='G05P32TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P33 
class NumberOnP33(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[115], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[231], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 1
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[441], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 1
        set_user_value(triggerId=8110, key='Barrier11', value=5)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=1)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='G05P33TimeLimit', value=1):
            return CheckP33()


class CheckP33(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=5)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=1)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP33()


class NumberOffP33(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[115], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[231], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 1
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[441], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 1

    def on_tick(self) -> state.State:
        if true():
            return ResetP33()


class ResetP33(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P33End', value=1)
        set_user_value(key='G05P33Set', value=0)
        set_user_value(key='G05P33TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P34 
class NumberOnP34(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[241], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[331], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=1)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=1)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G05P34TimeLimit', value=1):
            return CheckP34()


class CheckP34(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=1)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=1)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP34()


class NumberOffP34(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[241], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[331], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP34()


class ResetP34(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P34End', value=1)
        set_user_value(key='G05P34Set', value=0)
        set_user_value(key='G05P34TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P35 
class NumberOnP35(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[231], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 1
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[321], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=1)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=1)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G05P35TimeLimit', value=1):
            return CheckP35()


class CheckP35(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=1)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=1)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP35()


class NumberOffP35(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[231], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 1
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[321], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP35()


class ResetP35(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P35End', value=1)
        set_user_value(key='G05P35Set', value=0)
        set_user_value(key='G05P35TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P36 
class NumberOnP36(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[131], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[224], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[321], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[334], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[441], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 1
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=1)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=4)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=1)
        set_user_value(triggerId=8330, key='Barrier33', value=4)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='G05P36TimeLimit', value=1):
            return CheckP36()


class CheckP36(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=1)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=4)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=1)
        set_user_value(triggerId=9330, key='Box33Check', value=4)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=1)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP36()


class NumberOffP36(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[131], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 1
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[224], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[321], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[334], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[441], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 1

    def on_tick(self) -> state.State:
        if true():
            return ResetP36()


class ResetP36(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P36End', value=1)
        set_user_value(key='G05P36Set', value=0)
        set_user_value(key='G05P36TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P37 
class NumberOnP37(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[211], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 1
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[241], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[411], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=1)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=1)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=1)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G05P37TimeLimit', value=1):
            return CheckP37()


class CheckP37(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=1)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=1)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=1)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP37()


class NumberOffP37(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[211], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 1
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[241], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[411], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 1
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP37()


class ResetP37(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P37End', value=1)
        set_user_value(key='G05P37Set', value=0)
        set_user_value(key='G05P37TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P38 
class NumberOnP38(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[115], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[241], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[321], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=5)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=1)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=1)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G05P38TimeLimit', value=1):
            return CheckP38()


class CheckP38(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=5)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=1)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=1)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP38()


class NumberOffP38(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[115], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[241], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[321], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 1
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP38()


class ResetP38(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P38End', value=1)
        set_user_value(key='G05P38Set', value=0)
        set_user_value(key='G05P38TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P39 
class NumberOnP39(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[141], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[311], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=1)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=1)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G05P39TimeLimit', value=1):
            return CheckP39()


class CheckP39(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=1)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=1)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP39()


class NumberOffP39(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[141], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 1
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[311], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 1
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP39()


class ResetP39(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P39End', value=1)
        set_user_value(key='G05P39Set', value=0)
        set_user_value(key='G05P39TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P40 
class NumberOnP40(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[121], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[241], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[432], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=1)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=1)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=2)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G05P40TimeLimit', value=1):
            return CheckP40()


class CheckP40(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=1)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=1)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=2)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP40()


class NumberOffP40(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[121], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 1
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[241], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 1
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[432], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 2
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP40()


class ResetP40(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P40End', value=1)
        set_user_value(key='G05P40Set', value=0)
        set_user_value(key='G05P40TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P41 
class NumberOnP41(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[115], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[221], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[322], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[331], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=5)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=1)
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=2)
        set_user_value(triggerId=8330, key='Barrier33', value=1)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G05P41TimeLimit', value=1):
            return CheckP41()


class CheckP41(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=5)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=1)
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=2)
        set_user_value(triggerId=9330, key='Box33Check', value=1)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP41()


class NumberOffP41(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[115], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[221], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 1
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[322], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[331], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 1
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP41()


class ResetP41(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P41End', value=1)
        set_user_value(key='G05P41Set', value=0)
        set_user_value(key='G05P41TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P42 
class NumberOnP42(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[223], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[232], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[322], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=3)
        set_user_value(triggerId=8230, key='Barrier23', value=2)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=2)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G05P42TimeLimit', value=1):
            return CheckP42()


class CheckP42(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=3)
        set_user_value(triggerId=9230, key='Box23Check', value=2)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=2)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP42()


class NumberOffP42(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[223], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 3
        set_mesh(triggerIds=[232], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 2
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[322], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP42()


class ResetP42(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P42End', value=1)
        set_user_value(key='G05P42Set', value=0)
        set_user_value(key='G05P42TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P43 
class NumberOnP43(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=3)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G05P43TimeLimit', value=1):
            return CheckP43()


class CheckP43(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=3)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP43()


class NumberOffP43(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[143], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 3
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP43()


class ResetP43(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P43End', value=1)
        set_user_value(key='G05P43Set', value=0)
        set_user_value(key='G05P43TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P44 
class NumberOnP44(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[224], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[243], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[322], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[412], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=4)
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=3)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=2)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=2)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G05P44TimeLimit', value=1):
            return CheckP44()


class CheckP44(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=4)
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=3)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=2)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=2)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP44()


class NumberOffP44(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[224], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[243], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 3
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[322], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[412], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 2
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP44()


class ResetP44(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P44End', value=1)
        set_user_value(key='G05P44Set', value=0)
        set_user_value(key='G05P44TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P45 
class NumberOnP45(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[415], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[423], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=5)
        set_user_value(triggerId=8420, key='Barrier42', value=3)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G05P45TimeLimit', value=1):
            return CheckP45()


class CheckP45(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=5)
        set_user_value(triggerId=9420, key='Box42Check', value=3)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP45()


class NumberOffP45(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[415], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 5
        set_mesh(triggerIds=[423], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 3
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP45()


class ResetP45(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P45End', value=1)
        set_user_value(key='G05P45Set', value=0)
        set_user_value(key='G05P45TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P46 
class NumberOnP46(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[224], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[333], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[433], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=5)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=4)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=3)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=3)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=3)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G05P46TimeLimit', value=1):
            return CheckP46()


class CheckP46(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=5)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=4)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=3)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=3)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=3)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP46()


class NumberOffP46(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[145], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 5
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[224], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 3
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[333], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 3
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[433], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 3
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP46()


class ResetP46(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P46End', value=1)
        set_user_value(key='G05P46Set', value=0)
        set_user_value(key='G05P46TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P47 
class NumberOnP47(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[115], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[122], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[135], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[212], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[222], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[342], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[445], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 5
        set_user_value(triggerId=8110, key='Barrier11', value=5)
        set_user_value(triggerId=8120, key='Barrier12', value=2)
        set_user_value(triggerId=8130, key='Barrier13', value=5)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=2)
        set_user_value(triggerId=8220, key='Barrier22', value=2)
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=2)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=5)

    def on_tick(self) -> state.State:
        if user_value(key='G05P47TimeLimit', value=1):
            return CheckP47()


class CheckP47(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=5)
        set_user_value(triggerId=9120, key='Box12Check', value=2)
        set_user_value(triggerId=9130, key='Box13Check', value=5)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=2)
        set_user_value(triggerId=9220, key='Box22Check', value=2)
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=2)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=5)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP47()


class NumberOffP47(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[115], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 5
        set_mesh(triggerIds=[122], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 2
        set_mesh(triggerIds=[135], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 5
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[212], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 2
        set_mesh(triggerIds=[222], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 2
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[342], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 2
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[445], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 5

    def on_tick(self) -> state.State:
        if true():
            return ResetP47()


class ResetP47(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P47End', value=1)
        set_user_value(key='G05P47Set', value=0)
        set_user_value(key='G05P47TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P48 
class NumberOnP48(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[112], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[125], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[133], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[215], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[225], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[235], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[245], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[325], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[335], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[345], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[443], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 3
        set_user_value(triggerId=8110, key='Barrier11', value=2)
        set_user_value(triggerId=8120, key='Barrier12', value=5)
        set_user_value(triggerId=8130, key='Barrier13', value=3)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=5)
        set_user_value(triggerId=8220, key='Barrier22', value=5)
        set_user_value(triggerId=8230, key='Barrier23', value=5)
        set_user_value(triggerId=8240, key='Barrier24', value=5)
        set_user_value(triggerId=8310, key='Barrier31', value=5)
        set_user_value(triggerId=8320, key='Barrier32', value=5)
        set_user_value(triggerId=8330, key='Barrier33', value=5)
        set_user_value(triggerId=8340, key='Barrier34', value=5)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=2)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='G05P48TimeLimit', value=1):
            return CheckP48()


class CheckP48(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=2)
        set_user_value(triggerId=9120, key='Box12Check', value=5)
        set_user_value(triggerId=9130, key='Box13Check', value=3)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=5)
        set_user_value(triggerId=9220, key='Box22Check', value=5)
        set_user_value(triggerId=9230, key='Box23Check', value=5)
        set_user_value(triggerId=9240, key='Box24Check', value=5)
        set_user_value(triggerId=9310, key='Box31Check', value=5)
        set_user_value(triggerId=9320, key='Box32Check', value=5)
        set_user_value(triggerId=9330, key='Box33Check', value=5)
        set_user_value(triggerId=9340, key='Box34Check', value=5)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=2)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=3)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP48()


class NumberOffP48(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 2
        set_mesh(triggerIds=[125], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 5
        set_mesh(triggerIds=[133], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 3
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[215], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 5
        set_mesh(triggerIds=[225], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 5
        set_mesh(triggerIds=[235], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 5
        set_mesh(triggerIds=[245], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 5
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 5
        set_mesh(triggerIds=[325], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 5
        set_mesh(triggerIds=[335], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 5
        set_mesh(triggerIds=[345], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 5
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[422], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 2
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[443], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 3

    def on_tick(self) -> state.State:
        if true():
            return ResetP48()


class ResetP48(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P48End', value=1)
        set_user_value(key='G05P48Set', value=0)
        set_user_value(key='G05P48TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P49 
class NumberOnP49(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[113], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[124], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[134], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[142], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[214], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[224], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[233], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[244], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[322], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[334], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[344], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[413], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[424], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[434], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 2
        set_user_value(triggerId=8110, key='Barrier11', value=3)
        set_user_value(triggerId=8120, key='Barrier12', value=4)
        set_user_value(triggerId=8130, key='Barrier13', value=4)
        set_user_value(triggerId=8140, key='Barrier14', value=2)
        set_user_value(triggerId=8210, key='Barrier21', value=4)
        set_user_value(triggerId=8220, key='Barrier22', value=4)
        set_user_value(triggerId=8230, key='Barrier23', value=3)
        set_user_value(triggerId=8240, key='Barrier24', value=4)
        set_user_value(triggerId=8310, key='Barrier31', value=4)
        set_user_value(triggerId=8320, key='Barrier32', value=2)
        set_user_value(triggerId=8330, key='Barrier33', value=4)
        set_user_value(triggerId=8340, key='Barrier34', value=4)
        set_user_value(triggerId=8410, key='Barrier41', value=3)
        set_user_value(triggerId=8420, key='Barrier42', value=4)
        set_user_value(triggerId=8430, key='Barrier43', value=4)
        set_user_value(triggerId=8440, key='Barrier44', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='G05P49TimeLimit', value=1):
            return CheckP49()


class CheckP49(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=3)
        set_user_value(triggerId=9120, key='Box12Check', value=4)
        set_user_value(triggerId=9130, key='Box13Check', value=4)
        set_user_value(triggerId=9140, key='Box14Check', value=2)
        set_user_value(triggerId=9210, key='Box21Check', value=4)
        set_user_value(triggerId=9220, key='Box22Check', value=4)
        set_user_value(triggerId=9230, key='Box23Check', value=3)
        set_user_value(triggerId=9240, key='Box24Check', value=4)
        set_user_value(triggerId=9310, key='Box31Check', value=4)
        set_user_value(triggerId=9320, key='Box32Check', value=2)
        set_user_value(triggerId=9330, key='Box33Check', value=4)
        set_user_value(triggerId=9340, key='Box34Check', value=4)
        set_user_value(triggerId=9410, key='Box41Check', value=3)
        set_user_value(triggerId=9420, key='Box42Check', value=4)
        set_user_value(triggerId=9430, key='Box43Check', value=4)
        set_user_value(triggerId=9440, key='Box44Check', value=2)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP49()


class NumberOffP49(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 3
        set_mesh(triggerIds=[124], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 4
        set_mesh(triggerIds=[134], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 4
        set_mesh(triggerIds=[142], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 2
        set_mesh(triggerIds=[214], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 4
        set_mesh(triggerIds=[224], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[233], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 3
        set_mesh(triggerIds=[244], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 4
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 4
        set_mesh(triggerIds=[322], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 2
        set_mesh(triggerIds=[334], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[344], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 4
        set_mesh(triggerIds=[413], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 3
        set_mesh(triggerIds=[424], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 4
        set_mesh(triggerIds=[434], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 4
        set_mesh(triggerIds=[442], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 2

    def on_tick(self) -> state.State:
        if true():
            return ResetP49()


class ResetP49(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P49End', value=1)
        set_user_value(key='G05P49Set', value=0)
        set_user_value(key='G05P49TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


#   G05 P50 
class NumberOnP50(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        set_mesh(triggerIds=[114], visible=True, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[123], visible=True, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=True, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[144], visible=True, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[213], visible=True, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[224], visible=True, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[234], visible=True, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[242], visible=True, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[324], visible=True, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[334], visible=True, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[343], visible=True, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=True, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[425], visible=True, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[435], visible=True, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[444], visible=True, arg3=0, arg4=0, arg5=2) # 4,4 / 4
        set_user_value(triggerId=8110, key='Barrier11', value=4)
        set_user_value(triggerId=8120, key='Barrier12', value=3)
        set_user_value(triggerId=8130, key='Barrier13', value=2)
        set_user_value(triggerId=8140, key='Barrier14', value=4)
        set_user_value(triggerId=8210, key='Barrier21', value=3)
        set_user_value(triggerId=8220, key='Barrier22', value=4)
        set_user_value(triggerId=8230, key='Barrier23', value=4)
        set_user_value(triggerId=8240, key='Barrier24', value=2)
        set_user_value(triggerId=8310, key='Barrier31', value=2)
        set_user_value(triggerId=8320, key='Barrier32', value=4)
        set_user_value(triggerId=8330, key='Barrier33', value=4)
        set_user_value(triggerId=8340, key='Barrier34', value=3)
        set_user_value(triggerId=8410, key='Barrier41', value=4)
        set_user_value(triggerId=8420, key='Barrier42', value=5)
        set_user_value(triggerId=8430, key='Barrier43', value=5)
        set_user_value(triggerId=8440, key='Barrier44', value=4)

    def on_tick(self) -> state.State:
        if user_value(key='G05P50TimeLimit', value=1):
            return CheckP50()


class CheckP50(state.State):
    def on_enter(self):
        set_user_value(triggerId=9110, key='Box11Check', value=4)
        set_user_value(triggerId=9120, key='Box12Check', value=3)
        set_user_value(triggerId=9130, key='Box13Check', value=2)
        set_user_value(triggerId=9140, key='Box14Check', value=4)
        set_user_value(triggerId=9210, key='Box21Check', value=3)
        set_user_value(triggerId=9220, key='Box22Check', value=4)
        set_user_value(triggerId=9230, key='Box23Check', value=4)
        set_user_value(triggerId=9240, key='Box24Check', value=2)
        set_user_value(triggerId=9310, key='Box31Check', value=2)
        set_user_value(triggerId=9320, key='Box32Check', value=4)
        set_user_value(triggerId=9330, key='Box33Check', value=4)
        set_user_value(triggerId=9340, key='Box34Check', value=3)
        set_user_value(triggerId=9410, key='Box41Check', value=4)
        set_user_value(triggerId=9420, key='Box42Check', value=5)
        set_user_value(triggerId=9430, key='Box43Check', value=5)
        set_user_value(triggerId=9440, key='Box44Check', value=4)

    def on_tick(self) -> state.State:
        if true():
            return NumberOffP50()


class NumberOffP50(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=False, arg3=0, arg4=0, arg5=2) # 1,1 / 4
        set_mesh(triggerIds=[123], visible=False, arg3=0, arg4=0, arg5=2) # 1,2 / 3
        set_mesh(triggerIds=[132], visible=False, arg3=0, arg4=0, arg5=2) # 1,3 / 2
        set_mesh(triggerIds=[144], visible=False, arg3=0, arg4=0, arg5=2) # 1,4 / 4
        set_mesh(triggerIds=[213], visible=False, arg3=0, arg4=0, arg5=2) # 2,1 / 3
        set_mesh(triggerIds=[224], visible=False, arg3=0, arg4=0, arg5=2) # 2,2 / 4
        set_mesh(triggerIds=[234], visible=False, arg3=0, arg4=0, arg5=2) # 2,3 / 4
        set_mesh(triggerIds=[242], visible=False, arg3=0, arg4=0, arg5=2) # 2,4 / 2
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2) # 3,1 / 2
        set_mesh(triggerIds=[324], visible=False, arg3=0, arg4=0, arg5=2) # 3,2 / 4
        set_mesh(triggerIds=[334], visible=False, arg3=0, arg4=0, arg5=2) # 3,3 / 4
        set_mesh(triggerIds=[343], visible=False, arg3=0, arg4=0, arg5=2) # 3,4 / 3
        set_mesh(triggerIds=[414], visible=False, arg3=0, arg4=0, arg5=2) # 4,1 / 4
        set_mesh(triggerIds=[425], visible=False, arg3=0, arg4=0, arg5=2) # 4,2 / 5
        set_mesh(triggerIds=[435], visible=False, arg3=0, arg4=0, arg5=2) # 4,3 / 5
        set_mesh(triggerIds=[444], visible=False, arg3=0, arg4=0, arg5=2) # 4,4 / 4

    def on_tick(self) -> state.State:
        if true():
            return ResetP50()


class ResetP50(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='G05P50End', value=1)
        set_user_value(key='G05P50Set', value=0)
        set_user_value(key='G05P50TimeLimit', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait()


