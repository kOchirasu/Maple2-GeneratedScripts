using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004279: Nazkar Statue
/// </summary>
public class _11004279 : NpcScript {
    internal _11004279(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011287$ 
                // - <font color="#909090">(This is a statue of the guardian deity of Nazkar.)</font>
                return true;
            case 10:
                // $script:0911203207011288$ 
                // - <font color="#909090">(This is a statue of the guardian deity of Nazkar.)</font>
                // $script:0911203207011289$ 
                // - <font color="#909090">(The $map:02010034$ was the holiest sanctum of the lumarigons, the great dragons of light. Only the worthiest of the worthy could set foot in these halls.)</font>
                // $script:0911203207011290$ 
                // - <font color="#909090">(In spite of the spreading darkness, there's still a glimmer of the light in this statue's eyes...)</font>
                return true;
            default:
                return true;
        }
    }
}
