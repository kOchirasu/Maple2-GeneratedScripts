""" trigger/02000429_bf/popupcinema.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=750, boxId=1):
            return 시작연출준비()


class 시작연출준비(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 전투시작01()


class 전투시작01(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Bliche_nomal', duration=5000, script='$02000410_BF__PopUpCinema__0$', voice='ko/Npc/00002157')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 전투시작02()


class 전투시작02(state.State):
    def on_enter(self):
        side_npc_talk(type='movie', usm='Common/WorldInvasionScene1.usm', duration=0) # duration="0" 은 영상 끝날때까지 계속 출력
        side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__PopUpCinema__1$', voice='ko/Npc/00002166')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 전투시작03()


class 전투시작03(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='infernog_nomal', duration=8900, script='$02000410_BF__PopUpCinema__2$', voice='ko/Monster/60000724')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8900):
            return 전투시작04()


class 전투시작04(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='infernog_nomal', duration=6000, script='$02000410_BF__PopUpCinema__3$', voice='ko/Monster/60000725')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 전투시작05()


class 전투시작05(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='tristan_normal', duration=6500, script='$02000410_BF__PopUpCinema__4$', voice='ko/Npc/00002172')

    def on_tick(self) -> state.State:
        if user_value(key='WorldInvasionScene', value=2):
            return 두번째팝업영상출력()


class 두번째팝업영상출력(state.State):
    def on_enter(self):
        side_npc_talk(type='movie', usm='Common/WorldInvasionScene2.usm', duration=0) # duration="0" 은 영상 끝날때까지 계속 출력
        side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__PopUpCinema__5$', voice='ko/Npc/00002178')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 두번째팝업영상출력02()


class 두번째팝업영상출력02(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Bliche_nomal', duration=5000, script='$02000410_BF__PopUpCinema__6$', voice='ko/Npc/00002173')

    def on_tick(self) -> state.State:
        if user_value(key='WorldInvasionScene', value=3):
            return 세번째팝업영상출력()


class 세번째팝업영상출력(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__PopUpCinema__7$', voice='ko/Npc/00002179')
        side_npc_talk(type='movie', usm='Common/WorldInvasionScene3.usm', duration=0) # duration="0" 은 영상 끝날때까지 계속 출력

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 세번째팝업영상출력02()


class 세번째팝업영상출력02(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Bliche_nomal', duration=5000, script='$02000410_BF__PopUpCinema__8$', voice='ko/Npc/00002174')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 세번째팝업영상출력03()


class 세번째팝업영상출력03(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__PopUpCinema__9$', voice='ko/Npc/00002180')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 세번째팝업영상출력04()


class 세번째팝업영상출력04(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Bliche_nomal', duration=5000, script='$02000410_BF__PopUpCinema__10$', voice='ko/Npc/00002175')

    def on_tick(self) -> state.State:
        if user_value(key='WorldInvasionScene', value=4):
            return 네번째팝업영상출력()


class 네번째팝업영상출력(state.State):
    def on_enter(self):
        side_npc_talk(type='movie', usm='Common/WorldInvasionScene4.usm', duration=0) # duration="0" 은 영상 끝날때까지 계속 출력
        side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__PopUpCinema__11$', voice='ko/Npc/00002181')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 네번째팝업영상출력02()


class 네번째팝업영상출력02(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Bliche_nomal', duration=5000, script='$02000410_BF__PopUpCinema__12$', voice='ko/Npc/00002176')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 트리거종료()


#  팝업영상 다 띄우고 종료하기 
class 트리거종료(state.State):
    pass


