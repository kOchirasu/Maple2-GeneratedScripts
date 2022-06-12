using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001429: 
/// </summary>
public class _11001429 : NpcScript {
    protected override void FirstScript() {
        (Id, Button) = (40, NpcTalkButton.Close);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:0211204406000704$ 
                // - I've got everything you need.
                return default;
            case 40:
                // $script:0809170706000907$ 
                // - Confused?
                return default;
        }
        
        return default;
    }
}
