""" trigger/02000207_bf/999990_ground.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5001,5002,5003,5004,5005,5006], visible=False, arg3=0, arg4=0, arg5=0) # 자쿰과의 전투 장소 3층 지형의 일부 바닥 큐브를 숨김 처리함

    def on_tick(self) -> state.State:
        if user_value(key='ZakumBodyAppearance', value=1):
            return 층지형의숨겨진바닥생성3()


class 층지형의숨겨진바닥생성3(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5001,5002,5003,5004,5005,5006], visible=True, arg3=1, arg4=120, arg5=0.5) # 자쿰 본체 하고 전투가 시작되면 자쿰본체한테 신호 받아서 3층 지형의 일부 바닥이 생성되도록 함


