using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001620: Jayce
/// </summary>
public class _11001620 : NpcScript {
    internal _11001620(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0516130207006123$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:0531170907006273$ 
                // - Was there something you wanted to ask me?
                switch (selection) {
                    // $script:0531170907006274$
                    // - Tell me about the champion of $map:63000020$.
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:0531170907006275$ 
                // - $npcName:11001547[gender:0]$ is the champion and public face of $map:63000020$. Over the course of his career here, he's had 47 wins, zero losses, and one tie.
                switch (selection) {
                    // $script:0607145407006338$
                    // - Zero losses?
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 30:
                // $script:0531170907006276$ 
                // - His fights always end the same way: a single punch and his opponent is out like a light. He's built like a tank and moves like a panther. It's no wonder the crowds love him.
                switch (selection) {
                    // $script:0531170907006277$
                    // - You mentioned a tie.
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0531170907006278$ 
                // - Yes, he tied. Once. His opponent wasn't even human—it was one of those animal men. He used a very strange technique in the ring. It almost looked like magic.
                // $script:0531170907006279$ 
                // - $map:63000020$ had never seen anything like him, and we haven't again since. Even $npcName:11001547[gender:0]$ was impressed.
                // $script:0531170907006280$ 
                // - The challenger left as soon as the match was over, mumbling something about being "pleased with the results of his training." What was his name again...?
                // $script:0531173507006320$ 
                // - Ah, that's right! The challenger's name was Junta. And that's everything I know about him.
                return true;
            default:
                return true;
        }
    }
}
