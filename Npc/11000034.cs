using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000034: Mahio
/// </summary>
public class _11000034 : NpcScript {
    internal _11000034(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000189$ 
                // - Can I help you?
                return true;
            case 20:
                // $script:0831180407000191$ 
                // - Nothing's more important than peace of mind. I find mine snuggled up safe in bed.
                return true;
            default:
                return true;
        }
    }
}
