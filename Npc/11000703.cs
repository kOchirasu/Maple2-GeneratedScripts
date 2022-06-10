using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000703: Kennis
/// </summary>
public class _11000703 : NpcScript {
    internal _11000703(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002830$ 
                // - Ugh... 
                return true;
            case 20:
                // $script:0831180407002832$ 
                // - Time is of the essence. We must request backup right away.
                return true;
            default:
                return true;
        }
    }
}
