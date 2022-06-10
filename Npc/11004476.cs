using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004476: Ludwigia
/// </summary>
public class _11004476 : NpcScript {
    internal _11004476(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012167$ 
                // - Sigh... I'm sick of these ration packs they have us all eating. I miss the gourmet restaurants of Tria! 
                return true;
            case 10:
                // $script:1227192907012168$ 
                // - They didn't warn us that Kritias doesn't have any proper eateries. What's a foodie supposed to do in a place like this? 
                // $script:1227192907012169$ 
                // - I would kill for a bowl of blue mushroom slime soup in cornelian cherry sauce... 
                // $script:1227192907012170$ 
                // - Ugh, talking about it just makes it worse! I'm going to be too hungry to sleep tonight... 
                return true;
            default:
                return true;
        }
    }
}
