using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000638: Prisoner 140921
/// </summary>
public class _11000638 : NpcScript {
    internal _11000638(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002600$ 
                // - Get me out of here... 
                return true;
            case 40:
                // $script:0831180407002603$ 
                // - I really want to get out of here. Please help me. I'm sorry for what I did. I really am. 
                return true;
            default:
                return true;
        }
    }
}
