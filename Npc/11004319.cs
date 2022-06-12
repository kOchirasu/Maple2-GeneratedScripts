using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004319: Mika
/// </summary>
public class _11004319 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;30
    }

    protected override int Select() {
        // Select 0:
        // $script:1102172107011621$
        // - I've got a bad feeling...
        // Select 20:
        // $script:1010140307011441$
        // - I've got a bad feeling...
        // TODO: 0,20
        return 0;
    }

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1102172107011622$
                // - I sense draconic power... Did I finally find them?
                return -1;
            case (30, 0):
                // $script:1010140307011442$
                // - Oh, it's you!
                return 30;
            case (30, 1):
                // $script:1010140307011443$
                // - It's been a while! What're you doing here?
                switch (selection) {
                    // $script:1010140307011444$
                    // - What are you doing here?
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:1010140307011445$
                // - A few days ago I sensed an unusual energy coming from this place, so I came to investigate.
                switch (selection) {
                    // $script:1010140307011446$
                    // - Did you find anything?
                    case 0:
                        return 50;
                }
                return -1;
            case (50, 0):
                // $script:1010140307011447$
                // - Did I ever! As soon as I arrived, I felt it—that familiar aura... The traces of dragons!
                return 50;
            case (50, 1):
                // $script:1010140307011448$
                // - There's no question about it, dragons once lived in this land! I got to thinking that maybe they were related to the dark dragons that Biset told me about.
                return 50;
            case (50, 2):
                // $script:1010141507011602$
                // - Now I'm just waiting for my next big clue.
                switch (selection) {
                    // $script:0111224807012687$
                    // - Well, good luck!
                    case 0:
                        return 60;
                }
                return -1;
            case (60, 0):
                // $script:0111224807012688$
                // - Thank you!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.Next,
            (50, 1) => NpcTalkButton.Next,
            (50, 2) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
