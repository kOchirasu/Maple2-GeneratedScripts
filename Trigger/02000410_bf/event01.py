""" trigger/02000410_bf/event01.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=750, boxId=1):
            return 전투시작잠시대기()


class 전투시작잠시대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 전투시작_인페르녹전함()


class 전투시작_인페르녹전함(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20041002, textId=20041002)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 첫번째페이즈_인페르녹전함()

    def on_exit(self):
        hide_guide_summary(entityId=20041002)


class 첫번째페이즈_인페르녹전함(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='AirshipBalrogCrimsonBroken', value=1):
            return 인페르녹전함파괴연출()


class 인페르녹전함파괴연출(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20041003, textId=20041003)
        side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__Event01__0$', voice='ko/Npc/00002167')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 인페르녹전함파괴연출2()


class 인페르녹전함파괴연출2(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003533, illust='Bliche_nomal', duration=5000, script='$02000410_BF__Event01__1$', voice='ko/Npc/00002158')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 두번째페이즈_인페르녹전함()

    def on_exit(self):
        hide_guide_summary(entityId=20041003)


class 두번째페이즈_인페르녹전함(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='AirshipBalrogCrimsonFlameBroken', value=1):
            return 인페르녹전함파괴_인페르녹등장연출()


class 인페르녹전함파괴_인페르녹등장연출(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20041004, textId=20041004)
        side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__Event01__2$', voice='ko/Npc/00002168')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 인페르녹전함파괴_인페르녹등장연출2()

    def on_exit(self):
        hide_guide_summary(entityId=20041004)


class 인페르녹전함파괴_인페르녹등장연출2(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Neirin_surprise', duration=3000, script='$02000410_BF__Event01__3$', voice='ko/Npc/00002169')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인페르녹전함파괴_인페르녹등장연출3()


class 인페르녹전함파괴_인페르녹등장연출3(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003533, illust='Bliche_closeEye', duration=4000, script='$02000410_BF__Event01__4$', voice='ko/Npc/00002159')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 인페르녹전함파괴_인페르녹등장연출4()


class 인페르녹전함파괴_인페르녹등장연출4(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02000410_BF__Event01__5$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 인페르녹전함파괴_인페르녹등장연출5()


class 인페르녹전함파괴_인페르녹등장연출5(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02000410_BF__Event01__6$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 인페르녹전함파괴_인페르녹등장연출6()


class 인페르녹전함파괴_인페르녹등장연출6(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003533, illust='Bliche_nomal', duration=5000, script='$02000410_BF__Event01__7$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 세번째페이즈_인페르녹등장()


class 세번째페이즈_인페르녹등장(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BalrogMagicBursterBattlePhase', value=1): # 15분 다 지나 끝난 이후  실패한 경우
            return None # Missing State: 성공이벤트실행
        if user_value(key='BalrogMagicBursterBattlePhase', value=1):
            return None # Missing State: 실패이벤트실행


