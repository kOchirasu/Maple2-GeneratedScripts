using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000482: Puzroon's Message
/// </summary>
public class _11000482 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407002109$
    // - Judging by the rough handwriting, I think $npcName:11000441[gender:0]$ wrote this note.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002110$
                // - Judging by the rough handwriting, I think $npcName:11000441[gender:0]$ wrote this note.
                switch (selection) {
                    // $script:0831180407002111$
                    // - Check the note about the starting time.
                    case 0:
                        return 11;
                    // $script:0831180407002112$
                    // - Check the note about how to play the game.
                    case 1:
                        return 12;
                    // $script:0831180407002113$
                    // - Check the note about earning rewards.
                    case 2:
                        return 13;
                }
                return -1;
            case (11, 0):
                // $script:0831180407002114$
                // - I know these folks aren't just here to see $npcName:11000441[gender:0]$. Don't worry, I'll start the game when we've got enough people.
                return -1;
            case (12, 0):
                // $script:0831180407002115$
                // - Step on the red tile to jump to the center of the cave. Once there, you can step on the blue tile there when you want to leave.
                return 12;
            case (12, 1):
                // $script:0831180407002116$
                // - When the game begins, the tiles you're standing on will start disappearing. Last as long as you can without falling, and if you're the last one standing, you win! Easy, right?
                return -1;
            case (13, 0):
                // $script:0831180407002117$
                // - In addition to mesos, the winners will get a special reward: $npcName:11000441[gender:0]$'s Blessing, which increases their Movement Speed for 15 seconds.
                return 13;
            case (13, 1):
                // $script:0831180407002118$
                // - Do you want a reward? Then join up and complete the game!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            (12, 0) => NpcTalkButton.Next,
            (12, 1) => NpcTalkButton.Close,
            (13, 0) => NpcTalkButton.Next,
            (13, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
