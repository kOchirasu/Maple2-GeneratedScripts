using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001606: Eupheria
/// </summary>
public class _11001606 : NpcScript {
    internal _11001606(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006094$ 
                // - You're here. 
                return true;
            case 10:
                // $script:0515180307006143$ 
                // - Has the time finally come time to avenge Arazaad? $npcName:11001231[gender:0]$... I'll make you pay! 
                return true;
            default:
                return true;
        }
    }
}
