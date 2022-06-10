using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004123: Green Hoods Ranger
/// </summary>
public class _11004123 : NpcScript {
    internal _11004123(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010489$ 
                // - What an ominous place... If $npcName:11004110[gender:1]$ didn't need us, I'd keep my distance.
                return true;
            case 10:
                // $script:0720125407010490$ 
                // - Just how big was the explosion?
                return true;
            default:
                return true;
        }
    }
}
