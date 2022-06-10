using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000485: Mushkid
/// </summary>
public class _11000485 : NpcScript {
    internal _11000485(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002129$ 
                // - What's up?
                return true;
            case 30:
                // $script:0831180407002132$ 
                // - Down below, $npcName:22000321$ has claimed all of the $map:2000202$ for herself!
                // $script:0831180407002133$ 
                // - She's bad, but... so cool! I want to be a monster mushroom like her!
                return true;
            default:
                return true;
        }
    }
}
