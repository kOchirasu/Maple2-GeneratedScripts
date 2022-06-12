using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000612: 
/// </summary>
public class _11000612 : NpcScript {
    protected override void FirstScript() {
        // TODO: Job 20
        // (Id, Button) = (20, NpcTalkButton.Close);
        // TODO: RandomPick 10
        // (Id, Button) = (10, NpcTalkButton.Close);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:0831180610000870$ 
                // - How may I help you?
                return default;
            case 20:
                // $script:0831180610000872$ 
                // - I hope you enjoyed your stay.
                //   Would you like to leave the Guild Lounge now?
                return default;
            case 10:
                // $script:0831180610000871$ 
                // - Only members can use the Guild Lounge.
                return default;
        }
        
        return default;
    }
}
