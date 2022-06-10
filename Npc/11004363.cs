using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004363: Aiden
/// </summary>
public class _11004363 : NpcScript {
    internal _11004363(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011775$ 
                // - So much commotion here... What's the big deal about a tree and some presents? Chill already! 
                return true;
            case 10:
                // $script:1109213607011776$ 
                // - What's so exciting about snow? It's just ice crystals. Nobody gets excited about an ice machine. 
                // $script:1120223207011901$ 
                // - ...Though I admit, it's kinda pretty out here. 
                return true;
            default:
                return true;
        }
    }
}
