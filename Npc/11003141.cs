using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003141: Rina
/// </summary>
public class _11003141 : NpcScript {
    internal _11003141(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0222124707007953$ 
                // - What's the matter, dear? 
                return true;
            case 20:
                // $script:0224093607007962$ 
                // - Cooking in the kitchen is fine, but I'll always prefer cooking outdoors for how liberating it feels. 
                return true;
            default:
                return true;
        }
    }
}
