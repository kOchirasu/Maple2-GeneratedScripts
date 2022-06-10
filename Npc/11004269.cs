using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004269: East Auto Bridge
/// </summary>
public class _11004269 : NpcScript {
    internal _11004269(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011226$ 
                // - <font color="#909090">(This bridge connects the city to the desert of Karkar. It plays a major role in the development of the island.)</font>
                return true;
            case 10:
                // $script:0911203207011227$ 
                // - <font color="#909090">(This bridge connects the city to the desert of Karkar. It plays a major role in the development of the island.)</font>
                // $script:0911203207011228$ 
                // - <font color="#909090">(This wonderful bridge was designed by the genius architect brother Opath and Oparts. The older brother, Opath, was in charge of the eastern exchange.)</font>
                // $script:0911203207011229$ 
                // - <font color="#909090">(He added intriguing detail and a touch of mischief to the design, including hidden magic portals and shortcuts.)</font>
                return true;
            default:
                return true;
        }
    }
}
