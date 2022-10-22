""" trigger/52000053_qd/spykandura02.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='SpyKandura', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='SpyKandura', value=1):
            return Delay01()


class Delay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return KanduraAppRightRandom()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraAppRightRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=10):
            return KanduraAppRight01()
        if random_condition(rate=10):
            return KanduraAppRight02()
        if random_condition(rate=10):
            return KanduraAppRight03()
        if random_condition(rate=10):
            return KanduraAppRight04()
        if random_condition(rate=10):
            return KanduraAppRight05()
        if random_condition(rate=10):
            return KanduraAppRight06()


class KanduraAppLeftRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=10):
            return KanduraAppLeft01()
        if random_condition(rate=10):
            return KanduraAppLeft02()
        if random_condition(rate=10):
            return KanduraAppLeft03()
        if random_condition(rate=10):
            return KanduraAppLeft04()
        if random_condition(rate=10):
            return KanduraAppLeft05()
        if random_condition(rate=10):
            return KanduraAppLeft06()


class KanduraAppCenterRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=10):
            return KanduraAppCenter01()
        if random_condition(rate=10):
            return KanduraAppCenter02()
        if random_condition(rate=10):
            return KanduraAppCenter03()
        if random_condition(rate=10):
            return KanduraAppCenter04()


#  오른쪽 
class KanduraAppRight01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[430], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraDisAppRight01()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraDisAppRight01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[430])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return KanduraAppCenterRandom()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraAppRight02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[431], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraDisAppRight02()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraDisAppRight02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[431])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return KanduraAppCenterRandom()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraAppRight03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[432], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraDisAppRight03()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraDisAppRight03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[432])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return KanduraAppCenterRandom()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraAppRight04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[433], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraDisAppRight04()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraDisAppRight04(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[433])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return KanduraAppCenterRandom()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraAppRight05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[434], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraDisAppRight05()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraDisAppRight05(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[434])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return KanduraAppCenterRandom()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraAppRight06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[435], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraDisAppRight06()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraDisAppRight06(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[435])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return KanduraAppCenterRandom()
        if user_value(key='SpyKandura', value=2):
            return Quit()


#  가운데 
class KanduraAppCenter01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[420], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraDisAppCenter01()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraDisAppCenter01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[420])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return KanduraAppLeftRandom()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraAppCenter02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[421], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraDisAppCenter02()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraDisAppCenter02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[421])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return KanduraAppLeftRandom()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraAppCenter03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[422], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraDisAppCenter03()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraDisAppCenter03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[422])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return KanduraAppLeftRandom()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraAppCenter04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[423], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraDisAppCenter04()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraDisAppCenter04(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[423])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return KanduraAppLeftRandom()
        if user_value(key='SpyKandura', value=2):
            return Quit()


#  왼쪽 
class KanduraAppLeft01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[410], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraDisAppLeft01()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraDisAppLeft01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[410])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return KanduraAppRightRandom()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraAppLeft02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[411], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraDisAppLeft02()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraDisAppLeft02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[411])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return KanduraAppRightRandom()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraAppLeft03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[412], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraDisAppLeft03()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraDisAppLeft03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[412])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return KanduraAppRightRandom()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraAppLeft04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[413], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraDisAppLeft04()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraDisAppLeft04(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[413])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return KanduraAppRightRandom()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraAppLeft05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[414], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraDisAppLeft05()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraDisAppLeft05(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[414])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return KanduraAppRightRandom()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraAppLeft06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[415], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraDisAppLeft06()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class KanduraDisAppLeft06(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[415])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return KanduraAppRightRandom()
        if user_value(key='SpyKandura', value=2):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[410,411,412,413,414,415,420,421,422,423,430,431,432,433,434,435])
        set_user_value(key='SpyKandura', value=0)


