using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001320: Stefan
/// </summary>
public class _11001320 : NpcScript {
    internal _11001320(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1216150106000596$ 
                // - Anyone can enjoy music any time! 
                return true;
            case 40:
                // $script:1216150106000600$ 
                // - Anyone can play music if they have an instrument. How would you like to use one created by the Royal Music Academy to begin your musical adventure?  
                switch (selection) {
                    // $script:1216150106000601$
                    // - I'd love to learn to play music!
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1216150106000602$ 
                // - If you want to play music, just click an instrument. Isn't that easy? You can improvise or use music scores. 
                switch (selection) {
                    // $script:1216150106000603$
                    // - Music scores? How?
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:1216150106000604$ 
                // - It's easy to use music scores. You can buy preset music scores or buy empty music scores and record music in them. It's a convenient method to play concerts from music you composed. Doesn't that sound like a blast?  
                // $script:1216150106000605$ 
                // - No matter where you are, music is there! Take a look at the items I have for you, and give music a try! 
                return true;
            default:
                return true;
        }
    }
}
