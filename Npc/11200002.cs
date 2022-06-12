using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11200002: Antonius
/// </summary>
public class _11200002 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1214161306000880$
    // - Anyone can enjoy music any time!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1214161306000884$
                // - Anyone can play music if they have an instrument. How would you like to use one created by the Royal Music Academy to begin your musical adventure? 
                switch (selection) {
                    // $script:1214161306000885$
                    // - I'd love to learn to play music!
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1214161306000886$
                // - If you want to play music, just click an instrument. Isn't that easy? You can improvise or use music scores.
                switch (selection) {
                    // $script:1214161306000887$
                    // - Music scores? How?
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:1214161306000888$
                // - It's easy to use music scores. You can buy preset music scores or buy empty music scores and record music in them. It's a convenient method to play concerts from music you composed. Doesn't that sound like a blast? 
                return 42;
            case (42, 1):
                // $script:1214161306000889$
                // - No matter where you are, music is there! Take a look at the items I have for you, and give music a try!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Next,
            (42, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
