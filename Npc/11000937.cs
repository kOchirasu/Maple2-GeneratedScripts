using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000937: 
/// </summary>
public class _11000937 : NpcScript {
    protected override void FirstScript() {
        (Id, Button) = (10, NpcTalkButton.Close);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:1121222006000859$ 
                // - Can I help you?
                return default;
            case 10:
                // $script:1121222006000860$ 
                // - Can I help you?
                return default;
        }
        
        return default;
    }
}
