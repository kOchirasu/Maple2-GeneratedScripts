using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004257: Steam Plume
/// </summary>
public class _11004257 : NpcScript {
    internal _11004257(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0829171107010974$ 
                // - <font color="#909090">(Hot steam rises from deep underground.)</font>
                return true;
            case 10:
                // $script:0829171107010975$ 
                // - <font color="#909090">(Hot steam rises from deep underground.)</font>
                // $script:0831140807011026$ 
                // - <font color="#909090">(Steam rises up from what appears to be a bottomless chasm. It's quite hot, and you think you smell sulfur.)</font>
                // $script:0831140807011027$ 
                // - <font color="#909090">(Rumor has it that $npcNamePlural:21000053$ make their den below. The steam that rises from deep underground is said to be toxic to humans.)</font>
                return true;
            default:
                return true;
        }
    }
}
