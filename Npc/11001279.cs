using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001279: Ishura
/// </summary>
public class _11001279 : NpcScript {
    internal _11001279(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1208175407004839$ 
                // - $npcName:11001231[gender:0]$ has struck again...
                return true;
            case 30:
                // $script:1208175407004842$ 
                // - We can discuss it later.
                return true;
            default:
                return true;
        }
    }
}
