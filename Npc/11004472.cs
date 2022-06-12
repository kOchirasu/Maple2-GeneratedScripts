using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004472: Coryne
/// </summary>
public class _11004472 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0104110407012538$
    // - Huh? Who're you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0104110407012539$
                // - Huh? Who're you?
                return 10;
            case (10, 1):
                // $script:0104110407012540$
                // - Why're you dressed like that? You look like a big dummy with a side of dummy sauce.
                switch (selection) {
                    // $script:0104110407012541$
                    // - You practicing for a marathon, kid?
                    case 0:
                        return 11;
                    // $script:0104110407012542$
                    // - This is cutting-edge fashion where I'm from!
                    case 1:
                        return 14;
                }
                return -1;
            case (11, 0):
                // $script:0104110407012543$
                // - I'm training so I can join the resistance! I'm gonna beat up those Tairen doody-heads good.
                return 11;
            case (11, 1):
                // $script:0104110407012544$
                // - But Humanitas only lets the strongest people ever join them. That's why I gotta run so much.
                return 11;
            case (11, 2):
                // $script:0104110407012545$
                // - You look pretty strong, though. How do you do it?
                switch (selection) {
                    // $script:0104110407012546$
                    // - Just keep training.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0104110407012547$
                // - I was afraid you were gonna say that. Hey... If you see my ma and pa, could you rescue them from the bad guys?
                switch (selection) {
                    // $script:0104110407012548$
                    // - Absolutely.
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:0104110407012549$
                // - Wow, really? Okay! Then I gotta keep training so I can help you!
                return -1;
            case (14, 0):
                // $script:0104110407012550$
                // - And where are you from? A butt?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Next,
            (11, 2) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.Close,
            (14, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
