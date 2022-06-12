using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004522: Friendly Soldieretto
/// </summary>
public class _11004522 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;50
    }

    protected override int Select() {
        // Select 0:
        // $script:0103163407012492$
        // - Beeep... Beeep...
        // Select 40:
        // $script:0104140207012576$
        // - Beeep... Beeep...
        // TODO: 0,40
        return 0;
    }

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0103163407012493$
                // - Initiating greeting protocol! The weather is nice today, is it not?
                switch (selection) {
                    // $script:0103163407012494$
                    // - How's your work coming?
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:0103163407012495$
                // - Initiating reassurance protocol! We soldierettos are doing our best. You can count upon us.
                return 20;
            case (20, 1):
                // $script:0103163407012496$
                // - Initiating gratitude protocol! We are grateful to the humans who gave us new purpose.
                return 20;
            case (20, 2):
                // $script:0103163407012497$
                // - Initiating brusque farewell protocol! This time has been very pleasant, but I have over one hundred tasks remaining for today. Please excuse me.
                switch (selection) {
                    // $script:0103163407012498$
                    // - I'll leave you to it, then.
                    case 0:
                        return 30;
                }
                return -1;
            case (30, 0):
                // $script:0103163407012499$
                // - Scanning records on aetherine air brake experiment... Scan complete.
                return -1;
            case (50, 0):
                // $script:0104140207012577$
                // - Initiating excitement protocols! Oh, I have uncovered records about Vanheim. Archiving now.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Next,
            (20, 2) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
