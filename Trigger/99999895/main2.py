""" trigger/99999895/main2.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[902]):
            return 딜레이(self.ctx)


class 딜레이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 몬스터스폰대기1(self.ctx)


class 몬스터스폰대기1(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='첫 번째 상대가 곧 출현합니다. 전투 준비를 하세요!!', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카운트1_1(self.ctx)


class 카운트1_1(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='3', arg3='1000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카운트1_2(self.ctx)


class 카운트1_2(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='2', arg3='1000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카운트1_3(self.ctx)


class 카운트1_3(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='1', arg3='1000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터스폰1(self.ctx)


class 몬스터스폰1(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='시작!!', arg3='1000')
        self.create_monster(spawnIds=[201], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 스폰대사1(self.ctx)


class 스폰대사1(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=201, msg='네 마음가짐과 기량을 한 번 볼까?', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[201]):
            self.add_balloon_talk(spawnId=201, msg='너 따위 애송이에게 지다니...', duration=3000)
            return 몬스터스폰대기2(self.ctx)


class 몬스터스폰대기2(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='첫 전투에서 승리하셨습니다. 잠시만 기다려주세요 다음전투가 기다리고 있습니다!!', arg3='5000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 카운트2_1(self.ctx)


class 카운트2_1(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='3', arg3='1000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카운트2_2(self.ctx)


class 카운트2_2(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='2', arg3='1000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카운트2_3(self.ctx)


class 카운트2_3(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='1', arg3='1000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터스폰2(self.ctx)


class 몬스터스폰2(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='시작!!', arg3='1000')
        self.create_monster(spawnIds=[202], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 스폰대사2(self.ctx)


class 스폰대사2(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=202, msg='와라!! 얼마나 성장했는지 보겠다!', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[202]):
            self.add_balloon_talk(spawnId=202, msg='꽤 하는군. 즐거운 싸움이었다.', duration=3000)
            return 몬스터스폰대기3(self.ctx)


class 몬스터스폰대기3(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='두 번째 전투에서 승리하셨습니다. 잠시만 기다려주세요 마지막 전투가 기다리고 있습니다!!', arg3='5000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 카운트3_1(self.ctx)


class 카운트3_1(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='3', arg3='1000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카운트3_2(self.ctx)


class 카운트3_2(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='2', arg3='1000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카운트3_3(self.ctx)


class 카운트3_3(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='1', arg3='1000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터스폰3(self.ctx)


class 몬스터스폰3(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='시작!!', arg3='1000')
        self.create_monster(spawnIds=[203], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 스폰대사3(self.ctx)


class 스폰대사3(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=203, msg='그동안 어떤 성과를 이루셨는지 보여주세요.', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[203]):
            self.add_balloon_talk(spawnId=203, msg='좋은 실력입니다. 엘리넬 학생들에게 귀감이 될 분이시군요.', duration=3000)
            return 대사(self.ctx)


class 대사(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=7, arg2='SUCCESS', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 안내(self.ctx)


class 안내(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='곧 다시 전투가 시작됩니다. 준비하세요!!', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 대기(self.ctx)


initial_state = 대기
