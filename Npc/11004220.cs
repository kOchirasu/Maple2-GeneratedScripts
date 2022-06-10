using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004220: Agent K
/// </summary>
public class _11004220 : NpcScript {
    internal _11004220(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806222707010785$ 
                // - Can't talk. Important mission. 
                return true;
            case 10:
                // $script:0806222707010786$ 
                // - Sorry, I don't have time for games... I'm here on a special mission. My partner said to meet him at the tables on the dock over by the balloons, but he's nowhere in sight. 
                return true;
            default:
                return true;
        }
    }
}
