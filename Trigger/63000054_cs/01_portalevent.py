""" trigger/63000054_cs/01_portalevent.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=20007001, visible=False, enabled=False, minimapVisible=True) # 자쿰
        set_portal(portalId=20023001, visible=False, enabled=False, minimapVisible=True) # 핑크빈
        create_widget(type='ReverseRaidPortal')


