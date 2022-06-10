using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004347: Mia
/// </summary>
public class _11004347 : NpcScript {
    internal _11004347(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011751$ 
                // - I must remain calm... I can resolve this... All things in their proper place... 
                return true;
            case 10:
                // $script:1109213607011752$ 
                // - If there's a problem, solve it! Blaming and complaining won't fix anything! 
                switch (selection) {
                    // $script:1109213607011753$
                    // - Things aren't looking so good right now... are you okay?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109213607011754$ 
                // - Yes, of course! Obviously we just need to remain calm and composed. CALM AND COMPOSED! 
                return true;
            default:
                return true;
        }
    }
}
