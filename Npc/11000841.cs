using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000841: Miruka
/// </summary>
public class _11000841 : NpcScript {
    internal _11000841(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003076$ 
                // - Sigh... 
                return true;
            case 30:
                // $script:0831180407003079$ 
                // - I think that doctor is a quack. The more he treats me, the worse I feel. Sigh... 
                return true;
            default:
                return true;
        }
    }
}
