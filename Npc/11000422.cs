using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000422: Roanna's Tombstone
/// </summary>
public class _11000422 : NpcScript {
    internal _11000422(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001763$ 
                // - <font color="#909090">(The headstone is old and worn, and there is an epitaph inscribed upon it.)</font>
                return true;
            case 10:
                // $script:0831180407001764$ 
                // - <i>Here lies Roanna Levematri. She leaves behind her lover Alberto, whose heart will never heal.</i>
                return true;
            case 20:
                // $script:0831180407001765$ 
                // - <i>Here lies Roanna Levematri. She leaves behind her lover Alberto, whose heart will never heal.</i>
                return true;
            default:
                return true;
        }
    }
}
