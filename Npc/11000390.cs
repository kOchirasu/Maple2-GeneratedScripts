using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000390: Olson
/// </summary>
public class _11000390 : NpcScript {
    internal _11000390(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001585$ 
                // - How may I help you? 
                return true;
            case 20:
                // $script:0831180407001587$ 
                // - We've been busy. People are still checking in, with no idea the empress's gathering has been canceled. 
                return true;
            case 30:
                // $script:0831180407001588$ 
                // - The empress is no longer holding court, but we're still booked up. I don't think most people have heard the news yet. 
                return true;
            default:
                return true;
        }
    }
}
