using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000252: Chairman Goldus
/// </summary>
public class _11000252 : NpcScript {
    internal _11000252(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001053$ 
                // - What do <i>you</i> want? 
                return true;
            case 30:
                // $script:0831180407001055$ 
                // - Goldus never stops moving toward the future. There's nothing we can't make or sell. 
                return true;
            default:
                return true;
        }
    }
}
