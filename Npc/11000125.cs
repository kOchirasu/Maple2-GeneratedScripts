using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000125: Benjamin
/// </summary>
public class _11000125 : NpcScript {
    internal _11000125(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000540$ 
                // - How did it come to this?
                return true;
            case 20:
                // $script:0831180407000542$ 
                // - I've got to determine whether the mutated DNA strand was an outside contaminant, or was somehow mistakenly synthesized inside our test subjects...
                return true;
            default:
                return true;
        }
    }
}
