using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000938: 
/// </summary>
public class _11000938 : NpcScript {
    protected override void FirstScript() {
        (Id, Button) = (10, NpcTalkButton.Close);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:1121222006000861$ 
                // - Can I help you?
                return default;
            case 10:
                // $script:1121222006000862$ 
                // - Can I help you?
                return default;
        }
        
        return default;
    }
}
