using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004084: Torchy
/// </summary>
public class _11004084 : NpcScript {
    internal _11004084(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0622133907010284$ 
                // - Shh! You'll wake up the other fireflies. No loud noises allowed. 
                return true;
            case 10:
                // $script:0622133907010285$ 
                // - Shh! You'll wake up the other fireflies. No loud noises allowed. 
                // $script:0622133907010286$ 
                // - Quietly, now... You're here looking for a quiet place to rest, aren't you? 
                switch (selection) {
                    // $script:0622133907010287$
                    // - What makes you think that?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0622133907010288$ 
                // - Humans always come here when something's on their mind. Our pretty light helps them feel better! I figured you might be the same. 
                // $script:0622133907010289$ 
                // - I can't do a danged thing to actually help you. But hey, if staring at our sparkly heinies brings you peace, then stare away! 
                return true;
            default:
                return true;
        }
    }
}
