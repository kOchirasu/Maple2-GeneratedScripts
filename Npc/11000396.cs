using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000396: Ivan
/// </summary>
public class _11000396 : NpcScript {
    internal _11000396(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001606$ 
                // - Why me? What did I do? 
                return true;
            case 20:
                // $script:0831180407001608$ 
                // - Keep those thugs away from me... 
                return true;
            case 30:
                // $script:0831180407001609$ 
                // - So hungry... 
                return true;
            default:
                return true;
        }
    }
}
