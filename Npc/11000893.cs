using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000893: Shaina
/// </summary>
public class _11000893 : NpcScript {
    internal _11000893(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003262$ 
                // - My head hurts...
                return true;
            case 20:
                // $script:0831180407003263$ 
                // - May the light bless you.
                return true;
            default:
                return true;
        }
    }
}
