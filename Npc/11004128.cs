using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004128: Ishura
/// </summary>
public class _11004128 : NpcScript {
    internal _11004128(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720143007010499$ 
                // - I'm sorry I made you worry... 
                return true;
            case 10:
                // $script:0720143007010500$ 
                // - I'm not sure how I can face everyone... 
                return true;
            default:
                return true;
        }
    }
}
