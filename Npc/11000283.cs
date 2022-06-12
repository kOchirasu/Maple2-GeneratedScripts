using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000283: Duomo
/// </summary>
public class _11000283 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;50
    }

    // Select 0:
    // $script:0831180407001102$
    // - What are you curious about now?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001105$
                // - Let me introduce myself. I am a great prophet. I can tell you of future events with unerring accuracy. Ignorant people call me a mere fortune teller or a con artist. It's their loss, really.
                return 30;
            case (30, 1):
                // $script:0831180407001106$
                // - Why, you ask? Because even people like them need something to believe in. When everything else fails them, they'll come to me. They always do. Now, how'd you like to know your fortune? 
                return -1;
            case (50, 0):
                // $script:0831180407001107$
                // - Want to know your destiny? Want to see your future? Then ask me! I can tell you anything you want. For a price, of course.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
