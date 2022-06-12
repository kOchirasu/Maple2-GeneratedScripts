using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004322: Startz
/// </summary>
public class _11004322 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;30
    }

    protected override int Select() {
        // Select 0:
        // $script:1102172107011627$
        // - Hm...
        // Select 20:
        // $script:1010140307011471$
        // - Hm...
        // TODO: 0,20
        return 0;
    }

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1102172107011628$
                // - That might look good on my menu...
                return -1;
            case (30, 0):
                // $script:1010140307011472$
                // - Hmm?
                switch (selection) {
                    // $script:1010140307011473$
                    // - Good to see you! It's been a while.
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:1010140307011474$
                // - Yeah, whatever.
                switch (selection) {
                    // $script:1010140307011475$
                    // - What are you doing here?
                    case 0:
                        return 50;
                }
                return -1;
            case (50, 0):
                // $script:1010140307011476$
                // - $npcName:11004319[gender:1]$ dragged us here to search for dark dragons.
                switch (selection) {
                    // $script:1010140307011477$
                    // - Really? Have you found anything?
                    case 0:
                        return 60;
                }
                return -1;
            case (60, 0):
                // $script:1010140307011478$
                // - I have actually. <b>New ingredients.</b>
                return 60;
            case (60, 1):
                // $script:1010140307011479$
                // - This place is littered with ingredients Maple World has never seen before!
                return 60;
            case (60, 2):
                // $script:1010140307011480$
                // - When I integrate them into my menu, it'll blow people's minds. You should stop by my restaurant some time.
                switch (selection) {
                    // $script:0111224807012689$
                    // - I'll definitely pay you a visit.
                    case 0:
                        return 70;
                }
                return -1;
            case (70, 0):
                // $script:0111224807012690$
                // - Cool.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.Next,
            (60, 1) => NpcTalkButton.Next,
            (60, 2) => NpcTalkButton.SelectableDistractor,
            (70, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
