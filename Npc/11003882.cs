using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003882: 
/// </summary>
public class _11003882 : NpcScript {
    protected override void FirstScript() {
        (Id, Button) = (30, NpcTalkButton.Close);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:0430025106000990$ 
                // - Empress's blessing be with you!
                return default;
            case 30:
                // $script:0601171006000994$ 
                // - SCRIPTNPCSHOP_0601171006000994_NAME
                return default;
        }
        
        return default;
    }
}
