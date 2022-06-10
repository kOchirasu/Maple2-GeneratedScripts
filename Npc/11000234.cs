using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000234: Cindy
/// </summary>
public class _11000234 : NpcScript {
    internal _11000234(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000993$ 
                // - How may I help you?
                return true;
            case 20:
                // $script:0831180407000995$ 
                // - Did you come from the rich neighborhood? What are you doing here?
                switch (selection) {
                    // $script:0831180407000996$
                    // - Do you know $npcName:11000064[gender:0]$?
                    case 0:
                        Id = 21;
                        return false;
                }
                return true;
            case 21:
                // $script:0831180407000997$ 
                // - $npcName:11000064[gender:0]$? Who's that? Is he famous?
                return true;
            case 30:
                // $script:0831180407000998$ 
                // - The people living in the rich neighborhood think we're smelly and dirty. But Mr. $npcName:11000006[gender:0]$ said they're smellier and dirtier on the inside for thinking that.
                // $script:0831180407000999$ 
                // - Mr. $npcName:11000006[gender:0]$ said he'd change the world, so everyone could be equal and happy together.
                return true;
            default:
                return true;
        }
    }
}
