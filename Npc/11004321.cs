using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004321: Tara
/// </summary>
public class _11004321 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;30
    }

    protected override int Select() {
        // Select 0:
        // $script:1102172107011625$
        // - This won't do...
        // Select 20:
        // $script:1010140307011458$
        // - This won't do...
        // TODO: 0,20
        return 0;
    }

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1102172107011626$
                // - It's hard to get my bearings in a weird place like this.
                return -1;
            case (30, 0):
                // $script:1010140307011459$
                // - Huh?
                return 30;
            case (30, 1):
                // $script:1010140307011460$
                // - Ah! It's you! How have you been?
                switch (selection) {
                    // $script:1010140307011461$
                    // - I'm doing pretty well, thanks.
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:1010140307011462$
                // - That's good to hear. So what brings you here?
                switch (selection) {
                    // $script:1010140307011463$
                    // - I came here on an investigation.
                    case 0:
                        return 50;
                }
                return -1;
            case (50, 0):
                // $script:1010140307011464$
                // - I see, you too... Sigh.
                return 50;
            case (50, 1):
                // $script:1010140307011465$
                // - We're here researching the dark dragons that Biset used to talk about.
                switch (selection) {
                    // $script:1010140307011466$
                    // - How did you get here?
                    case 0:
                        return 60;
                }
                return -1;
            case (60, 0):
                // $script:1010140307011467$
                // - $npcName:11004319[gender:1]$ brought us here with her dragon power. It seems she's come a long way.
                return 60;
            case (60, 1):
                // $script:1010140307011468$
                // - So far this new land seems like an amazing place, but some of us are having a harder time adjusting than others. $npcName:11004320[gender:0]$'s not acting like himself. Do you think you could offer him some words of encouragement?
                switch (selection) {
                    // $script:1010140307011469$
                    // - I'll see what I can do.
                    case 0:
                        return 70;
                }
                return -1;
            case (70, 0):
                // $script:1010140307011470$
                // - Thanks! I'm counting on you!
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
            (50, 1) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.Next,
            (60, 1) => NpcTalkButton.SelectableDistractor,
            (70, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
