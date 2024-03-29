""" trigger/02000428_bf/event01.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=750, boxId=1):
            return 전투시작잠시대기(self.ctx)


class 전투시작잠시대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 전투시작_인페르녹전함(self.ctx)


class 전투시작_인페르녹전함(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20041002, textId=20041002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 첫번째페이즈_인페르녹전함(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20041002)


class 첫번째페이즈_인페르녹전함(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AirshipBalrogCrimsonBroken', value=1):
            return 인페르녹전함파괴연출(self.ctx)


class 인페르녹전함파괴연출(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20041010, textId=20041010)
        self.side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__Event01__0$', voice='ko/Npc/00002167')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 인페르녹전함파괴연출2(self.ctx)


class 인페르녹전함파괴연출2(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Bliche_nomal', duration=5000, script='$02000410_BF__Event01__1$', voice='ko/Npc/00002158')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 두번째페이즈_인페르녹전함(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20041010)


class 두번째페이즈_인페르녹전함(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AirshipBalrogCrimsonFlameBroken', value=1):
            return 인페르녹전함파괴_인페르녹등장연출(self.ctx)


class 인페르녹전함파괴_인페르녹등장연출(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20041011, textId=20041011)
        self.side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__Event01__2$', voice='ko/Npc/00002168')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 인페르녹전함파괴_인페르녹등장연출2(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20041011)


class 인페르녹전함파괴_인페르녹등장연출2(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Neirin_surprise', duration=4000, script='$02000410_BF__Event01__3$', voice='ko/Npc/00002169')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 인페르녹전함파괴_인페르녹등장연출3(self.ctx)


class 인페르녹전함파괴_인페르녹등장연출3(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Bliche_closeEye', duration=5200, script='$02000410_BF__Event01__4$', voice='ko/Npc/00002159')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5200):
            return 인페르녹전함파괴_인페르녹등장연출4(self.ctx)


class 인페르녹전함파괴_인페르녹등장연출4(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02000410_BF__Event01__8$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 인페르녹전함파괴_인페르녹등장연출5(self.ctx)


class 인페르녹전함파괴_인페르녹등장연출5(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02000410_BF__Event01__9$') # 원래 여기에 02000410_BF__Event01__5  가 들어가는데, NA용 인페르녹은 쉴드 설정이 없기 때문에 다른 대화가 나오도록 설정했음

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 인페르녹전함파괴_인페르녹등장연출6(self.ctx)


class 인페르녹전함파괴_인페르녹등장연출6(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Bliche_nomal', duration=5000, script='$02000410_BF__Event01__7$') # 원래 여기에 02000410_BF__Event01__6  가 들어가는데, NA용 인페르녹은 쉴드 설정이 없기 때문에 다른 대화가 나오도록 설정했음

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 세번째페이즈_인페르녹등장(self.ctx)


class 세번째페이즈_인페르녹등장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BalrogMagicBursterBattlePhase', value=1): # 15분 다 지나 끝난 이후  실패한 경우
            return None # Missing State: 성공이벤트실행
        if self.user_value(key='BalrogMagicBursterBattlePhase', value=1):
            return None # Missing State: 실패이벤트실행


initial_state = Ready
