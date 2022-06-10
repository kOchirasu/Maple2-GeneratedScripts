using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000328: Merjafar
/// </summary>
public class _11000328 : NpcScript {
    internal _11000328(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001333$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0831180407001335$ 
                // - People nowadays tend to throw their things away the moment they're done with them. It's a shame, really. 
                // $script:0831180407001336$ 
                // - Antique items are precious relics of the past. You can trade antiques, but you can't bring the past back.
                return true;
            default:
                return true;
        }
    }
}
