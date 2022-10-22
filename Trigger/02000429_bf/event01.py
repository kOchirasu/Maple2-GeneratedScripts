""" trigger/02000429_bf/event01.xml """
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
        show_guide_summary(entityId=20041003, textId=20041003) # 1인 퀘스트용 던전은 5분 추가 정보가 필요 없어서 이거 사용함, 참고로 10인 카오스 던전에서는 "20041010" 이거 사용함
        side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__Event01__0$', voice='ko/Npc/00002167')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 인페르녹전함파괴연출2()


class 인페르녹전함파괴연출2(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Bliche_nomal', duration=5000, script='$02000410_BF__Event01__1$', voice='ko/Npc/00002158')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 두번째페이즈_인페르녹전함()

    def on_exit(self):
        hide_guide_summary(entityId=20041003) # 1인 퀘스트용 던전은 5분 추가 정보가 필요 없어서 이거 사용함, 참고로 10인 카오스 던전에서는 "20041010" 이거 사용함


class 두번째페이즈_인페르녹전함(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='AirshipBalrogCrimsonFlameBroken', value=1):
            return 인페르녹전함파괴_인페르녹등장연출()


class 인페르녹전함파괴_인페르녹등장연출(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20041004, textId=20041004) # 1인 퀘스트용 던전은 5분 추가 정보가 필요 없어서 이거 사용함, 참고로 10인 카오스 던전에서는 "20041011" 이거 사용함
        side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=4500, script='$02000410_BF__Event01__2$', voice='ko/Npc/00002168')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 인페르녹전함파괴_인페르녹등장연출2()

    def on_exit(self):
        hide_guide_summary(entityId=20041004) # 1인 퀘스트용 던전은 5분 추가 정보가 필요 없어서 이거 사용함, 참고로 10인 카오스 던전에서는 "20041011" 이거 사용함


class 인페르녹전함파괴_인페르녹등장연출2(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Neirin_surprise', duration=3800, script='$02000410_BF__Event01__3$', voice='ko/Npc/00002169')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3800):
            return 인페르녹전함파괴_인페르녹등장연출3()


class 인페르녹전함파괴_인페르녹등장연출3(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Bliche_closeEye', duration=5200, script='$02000410_BF__Event01__4$', voice='ko/Npc/00002159')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5200):
            return 인페르녹전함파괴_인페르녹등장연출4()


class 인페르녹전함파괴_인페르녹등장연출4(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02000410_BF__Event01__8$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 인페르녹전함파괴_인페르녹등장연출5()


class 인페르녹전함파괴_인페르녹등장연출5(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02000410_BF__Event01__9$') # 원래 여기에 02000410_BF__Event01__5  가 들어가는데, NA용 인페르녹은 쉴드 설정이 없기 때문에 다른 대화가 나오도록 설정했음

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 인페르녹전함파괴_인페르녹등장연출6()


class 인페르녹전함파괴_인페르녹등장연출6(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Bliche_nomal', duration=5000, script='$02000410_BF__Event01__7$') # 원래 여기에 02000410_BF__Event01__6  가 들어가는데, NA용 인페르녹은 쉴드 설정이 없기 때문에 다른 대화가 나오도록 설정했음

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 세번째페이즈_인페르녹등장()


class 세번째페이즈_인페르녹등장(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BalrogMagicBursterBattlePhase', value=1): # 15분 다 지나 끝난 이후  실패한 경우
            return None # Missing State: 성공이벤트실행
        if user_value(key='BalrogMagicBursterBattlePhase', value=1):
            return None # Missing State: 실패이벤트실행


