using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000283: Duomo
/// </summary>
public class _11000283 : NpcScript {
    internal _11000283(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001102$ 
                // - What are you curious about now? 
                return true;
            case 30:
                // $script:0831180407001105$ 
                // - Let me introduce myself. I am a great prophet. I can tell you of future events with unerring accuracy. Ignorant people call me a mere fortune teller or a con artist. It's their loss, really. 
                // $script:0831180407001106$ 
                // - Why, you ask? Because even people like them need something to believe in. When everything else fails them, they'll come to me. They always do. Now, how'd you like to know your fortune?  
                return true;
            case 50:
                // $script:0831180407001107$ 
                // - Want to know your destiny? Want to see your future? Then ask me! I can tell you anything you want. For a price, of course. 
                return true;
            default:
                return true;
        }
    }
}
