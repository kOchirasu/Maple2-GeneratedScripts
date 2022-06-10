using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000105: Benhurst
/// </summary>
public class _11000105 : NpcScript {
    internal _11000105(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000429$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407000432$ 
                // - Honey, if you're looking to make a splash in $map:02000001$'s social scene, you're gonna need to do something about that outfit.
                return true;
            default:
                return true;
        }
    }
}
