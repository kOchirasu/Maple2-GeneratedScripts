""" trigger/99999895/main.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 딜레이()


class 딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 몬스터스폰대기1()


class 몬스터스폰대기1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='첫 번째 상대가 곧 출현합니다. 전투 준비를 하세요!!', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카운트1_1()


class 카운트1_1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='3', arg3='1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카운트1_2()


class 카운트1_2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='2', arg3='1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카운트1_3()


class 카운트1_3(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='1', arg3='1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 몬스터스폰1()


class 몬스터스폰1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='시작!!', arg3='1000')
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 스폰대사1()


class 스폰대사1(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='네 마음가짐과 기량을 한 번 볼까?', duration=3000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            add_balloon_talk(spawnId=101, msg='너 따위 애송이에게 지다니...', duration=3000)
            return 몬스터스폰대기2()


class 몬스터스폰대기2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='첫 전투에서 승리하셨습니다. 잠시만 기다려주세요 다음전투가 기다리고 있습니다!!', arg3='5000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 카운트2_1()


class 카운트2_1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='3', arg3='1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카운트2_2()


class 카운트2_2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='2', arg3='1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카운트2_3()


class 카운트2_3(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='1', arg3='1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 몬스터스폰2()


class 몬스터스폰2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='시작!!', arg3='1000')
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 스폰대사2()


class 스폰대사2(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=102, msg='와라!! 얼마나 성장했는지 보겠다!', duration=3000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102]):
            add_balloon_talk(spawnId=102, msg='꽤 하는군. 즐거운 싸움이었다.', duration=3000)
            return 몬스터스폰대기3()


class 몬스터스폰대기3(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='두 번째 전투에서 승리하셨습니다. 잠시만 기다려주세요 마지막 전투가 기다리고 있습니다!!', arg3='5000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 카운트3_1()


class 카운트3_1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='3', arg3='1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카운트3_2()


class 카운트3_2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='2', arg3='1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카운트3_3()


class 카운트3_3(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='1', arg3='1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 몬스터스폰3()


class 몬스터스폰3(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='시작!!', arg3='1000')
        create_monster(spawnIds=[103], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 스폰대사3()


class 스폰대사3(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=103, msg='그동안 어떤 성과를 이루셨는지 보여주세요.', duration=3000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[103]):
            add_balloon_talk(spawnId=103, msg='좋은 실력입니다. 엘리넬 학생들에게 귀감이 될 분이시군요.', duration=3000)
            return 대사()


class 대사(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_event_ui(type=7, arg2='SUCCESS', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 안내()


class 안내(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='곧 다시 전투가 시작됩니다. 준비하세요!!', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 대기()


