using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001620: Jayce
/// </summary>
public class _11001620 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0516130207006123$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0531170907006273$
                // - Was there something you wanted to ask me?
                switch (selection) {
                    // $script:0531170907006274$
                    // - Tell me about the champion of $map:63000020$.
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:0531170907006275$
                // - $npcName:11001547[gender:0]$ is the champion and public face of $map:63000020$. Over the course of his career here, he's had 47 wins, zero losses, and one tie.
                switch (selection) {
                    // $script:0607145407006338$
                    // - Zero losses?
                    case 0:
                        return 30;
                }
                return -1;
            case (30, 0):
                // $script:0531170907006276$
                // - His fights always end the same way: a single punch and his opponent is out like a light. He's built like a tank and moves like a panther. It's no wonder the crowds love him.
                switch (selection) {
                    // $script:0531170907006277$
                    // - You mentioned a tie.
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0531170907006278$
                // - Yes, he tied. Once. His opponent wasn't even human—it was one of those animal men. He used a very strange technique in the ring. It almost looked like magic.
                return 40;
            case (40, 1):
                // $script:0531170907006279$
                // - $map:63000020$ had never seen anything like him, and we haven't again since. Even $npcName:11001547[gender:0]$ was impressed.
                return 40;
            case (40, 2):
                // $script:0531170907006280$
                // - The challenger left as soon as the match was over, mumbling something about being "pleased with the results of his training." What was his name again...?
                return 40;
            case (40, 3):
                // $script:0531173507006320$
                // - Ah, that's right! The challenger's name was Junta. And that's everything I know about him.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Next,
            (40, 2) => NpcTalkButton.Next,
            (40, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
