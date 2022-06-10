using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004021: Tinchai
/// </summary>
public class _11004021 : NpcScript {
    internal _11004021(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010029$ 
                // - I really hope Brother Junta and the expedition members get better soon. 
                return true;
            case 20:
                // $script:0614185307010030$ 
                // - I really hope Brother Junta and the expedition members get better soon. 
                return true;
            default:
                return true;
        }
    }
}
