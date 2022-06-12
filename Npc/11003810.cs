using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003810: 
/// </summary>
public class _11003810 : NpcScript {
    protected override void FirstScript() {
        (Id, Button) = (30, NpcTalkButton.Close);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:1228105615009081$ 
                // - What is it?
                return default;
            case 30:
                // $script:1228105615009084$ 
                // - Don't you want the power of the Devil Tree?
                return default;
        }
        
        return default;
    }
}
