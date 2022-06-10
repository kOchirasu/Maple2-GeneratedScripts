using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004120: Lumiknight Mage
/// </summary>
public class _11004120 : NpcScript {
    internal _11004120(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010483$ 
                // - I'm helping $npcName:11004108[gender:0]$ research the blackshard.
                return true;
            case 10:
                // $script:0720125407010484$ 
                // - I'd say you yourself are worth studying, after surviving an explosion of this magnitude.
                return true;
            default:
                return true;
        }
    }
}
