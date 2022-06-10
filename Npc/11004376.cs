using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004376: Snowleaf Fairfolk
/// </summary>
public class _11004376 : NpcScript {
    internal _11004376(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011789$ 
                // - Wouldn't it be something if pure white snow tasted like candy? 
                return true;
            case 10:
                // $script:1109213607011790$ 
                // - Wouldn't it be something if pure white snow tasted like candy? 
                return true;
            default:
                return true;
        }
    }
}
