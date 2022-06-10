using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004281: Unmarked Sarcophagus
/// </summary>
public class _11004281 : NpcScript {
    internal _11004281(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011294$ 
                // - <font color="#909090">(This sarcophagus has no name engraved upon it. Does an ancient lumarigon slumber within?)</font>
                return true;
            case 10:
                // $script:0911203207011295$ 
                // - <font color="#909090">(This sarcophagus has no name engraved upon it. Does an ancient lumarigon slumber within?)</font>
                // $script:0913151207011307$ 
                // - <font color="#909090">(It's covered in a thick layer of dust. Still, the elaborate carvings are the work of a master artisan.)</font>
                // $script:0913151207011308$ 
                // - <font color="#909090">(As you gaze upon the sarcophagus, you're overcome by a sudden feeling of melancholy.)</font>
                return true;
            default:
                return true;
        }
    }
}
