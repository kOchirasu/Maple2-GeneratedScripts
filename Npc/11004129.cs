using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004129: Landevian
/// </summary>
public class _11004129 : NpcScript {
    internal _11004129(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720143007010501$ 
                // - I'm still confused. 
                return true;
            case 10:
                // $script:0720143007010502$ 
                // - I'm so lost... 
                return true;
            default:
                return true;
        }
    }
}
