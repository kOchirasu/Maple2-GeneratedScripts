""" trigger/63000054_cs/01_portalevent.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=20007001, visible=False, enable=False, minimapVisible=True) # 자쿰
        self.set_portal(portalId=20023001, visible=False, enable=False, minimapVisible=True) # 핑크빈
        self.create_widget(type='ReverseRaidPortal')


initial_state = Wait
