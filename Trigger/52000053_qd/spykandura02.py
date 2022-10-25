""" trigger/52000053_qd/spykandura02.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='SpyKandura', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SpyKandura', value=1):
            return Delay01(self.ctx)


class Delay01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return KanduraAppRightRandom(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraAppRightRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=10):
            return KanduraAppRight01(self.ctx)
        if self.random_condition(rate=10):
            return KanduraAppRight02(self.ctx)
        if self.random_condition(rate=10):
            return KanduraAppRight03(self.ctx)
        if self.random_condition(rate=10):
            return KanduraAppRight04(self.ctx)
        if self.random_condition(rate=10):
            return KanduraAppRight05(self.ctx)
        if self.random_condition(rate=10):
            return KanduraAppRight06(self.ctx)


class KanduraAppLeftRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=10):
            return KanduraAppLeft01(self.ctx)
        if self.random_condition(rate=10):
            return KanduraAppLeft02(self.ctx)
        if self.random_condition(rate=10):
            return KanduraAppLeft03(self.ctx)
        if self.random_condition(rate=10):
            return KanduraAppLeft04(self.ctx)
        if self.random_condition(rate=10):
            return KanduraAppLeft05(self.ctx)
        if self.random_condition(rate=10):
            return KanduraAppLeft06(self.ctx)


class KanduraAppCenterRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=10):
            return KanduraAppCenter01(self.ctx)
        if self.random_condition(rate=10):
            return KanduraAppCenter02(self.ctx)
        if self.random_condition(rate=10):
            return KanduraAppCenter03(self.ctx)
        if self.random_condition(rate=10):
            return KanduraAppCenter04(self.ctx)


# 오른쪽
class KanduraAppRight01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[430], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraDisAppRight01(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraDisAppRight01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[430])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return KanduraAppCenterRandom(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraAppRight02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[431], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraDisAppRight02(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraDisAppRight02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[431])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return KanduraAppCenterRandom(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraAppRight03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[432], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraDisAppRight03(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraDisAppRight03(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[432])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return KanduraAppCenterRandom(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraAppRight04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[433], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraDisAppRight04(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraDisAppRight04(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[433])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return KanduraAppCenterRandom(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraAppRight05(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[434], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraDisAppRight05(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraDisAppRight05(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[434])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return KanduraAppCenterRandom(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraAppRight06(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[435], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraDisAppRight06(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraDisAppRight06(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[435])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return KanduraAppCenterRandom(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


# 가운데
class KanduraAppCenter01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[420], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraDisAppCenter01(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraDisAppCenter01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[420])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return KanduraAppLeftRandom(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraAppCenter02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[421], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraDisAppCenter02(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraDisAppCenter02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[421])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return KanduraAppLeftRandom(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraAppCenter03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[422], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraDisAppCenter03(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraDisAppCenter03(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[422])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return KanduraAppLeftRandom(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraAppCenter04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[423], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraDisAppCenter04(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraDisAppCenter04(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[423])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return KanduraAppLeftRandom(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


# 왼쪽
class KanduraAppLeft01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[410], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraDisAppLeft01(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraDisAppLeft01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[410])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return KanduraAppRightRandom(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraAppLeft02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[411], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraDisAppLeft02(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraDisAppLeft02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[411])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return KanduraAppRightRandom(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraAppLeft03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[412], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraDisAppLeft03(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraDisAppLeft03(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[412])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return KanduraAppRightRandom(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraAppLeft04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[413], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraDisAppLeft04(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraDisAppLeft04(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[413])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return KanduraAppRightRandom(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraAppLeft05(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[414], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraDisAppLeft05(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraDisAppLeft05(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[414])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return KanduraAppRightRandom(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraAppLeft06(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[415], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraDisAppLeft06(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class KanduraDisAppLeft06(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[415])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return KanduraAppRightRandom(self.ctx)
        if self.user_value(key='SpyKandura', value=2):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[410,411,412,413,414,415,420,421,422,423,430,431,432,433,434,435])
        self.set_user_value(key='SpyKandura', value=0)


initial_state = Wait
