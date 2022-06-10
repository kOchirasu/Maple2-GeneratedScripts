using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004125: Commander Jin
/// </summary>
public class _11004125 : NpcScript {
    internal _11004125(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010493$ 
                // - I'm here to assist $npcName:11004109[gender:0]$.
                return true;
            case 10:
                // $script:0720125407010494$ 
                // - Have you seen anything out of the ordinary?
                return true;
            default:
                return true;
        }
    }
}
