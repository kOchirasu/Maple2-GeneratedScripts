using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003416: 
/// </summary>
public class _11003416 : NpcScript {
    protected override void FirstScript() {
        (Id, Button) = (10, NpcTalkButton.Close);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 10:
                // $script:0706142810001862$ functionID=1 
                // - Do you want to empower your gear and become even stronger? Then trust me with your choicest items! I only accept armor at level 50 or above!
                return default;
        }
        
        return default;
    }
}
