""" trigger/02000428_bf/popupcinema.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=750, boxId=1):
            return 시작연출준비(self.ctx)


class 시작연출준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 전투시작01(self.ctx)


class 전투시작01(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Bliche_nomal', duration=5000, script='$02000410_BF__PopUpCinema__0$', voice='ko/Npc/00002157')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 전투시작02(self.ctx)


class 전투시작02(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='movie', usm='Common/WorldInvasionScene1.usm', duration=0) # duration="0" 은 영상 끝날때까지 계속 출력
        self.side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__PopUpCinema__1$', voice='ko/Npc/00002166')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 전투시작03(self.ctx)


class 전투시작03(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='infernog_nomal', duration=8500, script='$02000410_BF__PopUpCinema__2$', voice='ko/Monster/60000724')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8500):
            return 전투시작04(self.ctx)


class 전투시작04(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='infernog_nomal', duration=6000, script='$02000410_BF__PopUpCinema__3$', voice='ko/Monster/60000725')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 전투시작05(self.ctx)


class 전투시작05(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='tristan_normal', duration=6500, script='$02000410_BF__PopUpCinema__4$', voice='ko/Npc/00002172')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='WorldInvasionScene', value=2):
            return 두번째팝업영상출력(self.ctx)


class 두번째팝업영상출력(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='movie', usm='Common/WorldInvasionScene2.usm', duration=0) # duration="0" 은 영상 끝날때까지 계속 출력
        self.side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__PopUpCinema__5$', voice='ko/Npc/00002178')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 두번째팝업영상출력02(self.ctx)


class 두번째팝업영상출력02(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Bliche_nomal', duration=5000, script='$02000410_BF__PopUpCinema__6$', voice='ko/Npc/00002173')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='WorldInvasionScene', value=3):
            return 세번째팝업영상출력(self.ctx)


class 세번째팝업영상출력(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__PopUpCinema__7$', voice='ko/Npc/00002179')
        self.side_npc_talk(type='movie', usm='Common/WorldInvasionScene3.usm', duration=0) # duration="0" 은 영상 끝날때까지 계속 출력

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 세번째팝업영상출력02(self.ctx)


class 세번째팝업영상출력02(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Bliche_nomal', duration=5000, script='$02000410_BF__PopUpCinema__8$', voice='ko/Npc/00002174')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 세번째팝업영상출력03(self.ctx)


class 세번째팝업영상출력03(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__PopUpCinema__9$', voice='ko/Npc/00002180')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 세번째팝업영상출력04(self.ctx)


class 세번째팝업영상출력04(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Bliche_nomal', duration=5000, script='$02000410_BF__PopUpCinema__10$', voice='ko/Npc/00002175')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='WorldInvasionScene', value=4):
            return 네번째팝업영상출력(self.ctx)


class 네번째팝업영상출력(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='movie', usm='Common/WorldInvasionScene4.usm', duration=0) # duration="0" 은 영상 끝날때까지 계속 출력
        self.side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__PopUpCinema__11$', voice='ko/Npc/00002181')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 네번째팝업영상출력02(self.ctx)


class 네번째팝업영상출력02(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Bliche_nomal', duration=5000, script='$02000410_BF__PopUpCinema__12$', voice='ko/Npc/00002176')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 트리거종료(self.ctx)


# 팝업영상 다 띄우고 종료하기
class 트리거종료(trigger_api.Trigger):
    pass


initial_state = Ready
