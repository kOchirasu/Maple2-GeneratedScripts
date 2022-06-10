using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004242: Eupheria
/// </summary>
public class _11004242 : NpcScript {
    internal _11004242(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0809223207010947$ 
                // - How can I help you?
                return true;
            case 10:
                // $script:0809223207010948$ 
                // - I feel like I'm still in a dream.
                // $script:0809223207010949$ 
                // - I'm so confused. My memories are all jumbled. I think I need some time.
                return true;
            default:
                return true;
        }
    }
}
