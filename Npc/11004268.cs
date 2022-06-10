using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004268: West Auto Bridge
/// </summary>
public class _11004268 : NpcScript {
    internal _11004268(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011222$ 
                // - <font color="#909090">(This bridge connects the city to the desert of Karkar. It plays a major role in the development of the island.)</font> 
                return true;
            case 10:
                // $script:0911203207011223$ 
                // - <font color="#909090">(This bridge connects the city to the desert of Karkar. It plays a major role in the development of the island.)</font> 
                // $script:0911203207011224$ 
                // - <font color="#909090">(This wonderful bridge was co-designed by the genius architect brother Opath and Oparts. The younger brother, Oparts, was in charge of the western exchange. His flair for the fabulous is evident in the bridge's flashy lights.)</font> 
                // $script:0911203207011225$ 
                // - <font color="#909090">(There are over 100 lights in use on the West Auto Bridge, and they symbolize the glamor and promise of the big city.)</font>
 
                return true;
            default:
                return true;
        }
    }
}
