""" trigger/02000410_bf/resurrectionprohibition.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=750, boxId=1):
            return 전투시작()


class 전투시작(state.State):
    def on_tick(self) -> state.State:
        if dungeon_check_play_time(playSeconds=420):
            return 지금부터부활불가처리()
        if user_value(key='ThirdPhase', value=1):
            return 지금부터부활불가처리()
        """
        <condition name="UserValue" key="BalrogMagicBursterBattlePhase" value="1">  인페르녹과 전투 시작할 때 인페르녹  AI에서 BalrogMagicBursterBattlePhase =  1 신호를 보낼때까지 대기
            
            <transition state="지금부터부활불가처리" />
            
        </condition>
        """


class 지금부터부활불가처리(state.State):
    def on_enter(self):
        add_buff(boxIds=[750], skillId=70000073, level=1, arg4=False) # 여기서 맵 안에 있는 모든 플레이어에게 부활불가 디버프 부여함
        show_guide_summary(entityId=20041001, textId=20041001) # 부활불가 되었고 이제 파티가 전멸되면 게임오버 된다는 내여을 시스템메시지를 통해서 알려줌, 참고로 파티원전멸 체크 트리거는 ClearCheck.xml 이것임

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=20041001)


class 종료(state.State):
    pass


