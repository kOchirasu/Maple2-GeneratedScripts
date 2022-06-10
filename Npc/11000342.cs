using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000342: Nomm
/// </summary>
public class _11000342 : NpcScript {
    internal _11000342(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001372$ 
                // - May I... help you?
                return true;
            case 20:
                // $script:0831180407001374$ 
                // - I can't believe this is happening to me... 
                switch (selection) {
                    // $script:0831180407001375$
                    // - What is it?
                    case 0:
                        Id = 21;
                        return false;
                }
                return true;
            case 21:
                // $script:0831180407001376$ 
                // - For years, I saved as much money as I could so that I could one day build a house of my own. And the day my dream finally becomes a reality, a giant mushroom comes and chases me away!
                // $script:0831180407001377$ 
                // - Curse that $npcName:22000321$... What does a mushroom need with a house, anyway?
                // $script:0831180407001378$ 
                // - I paid for that house and the land under it, it belongs to me! This is completely unfair!
                return true;
            default:
                return true;
        }
    }
}
