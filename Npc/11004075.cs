using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004075: Chee the Caterpillar
/// </summary>
public class _11004075 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0619202207010200$
    // - Uh... Um...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0619202207010201$
                // - Uh... Um...
                return 10;
            case (10, 1):
                // $script:0619202207010202$
                // - Okay, I'm just gonna do it. I'm going to ask. Hey, human! Tell me something...
                switch (selection) {
                    // $script:0619202207010203$
                    // - Know what?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0619202207010204$
                // - What am I? I mean, what do you think I'm gonna be when I grow up?
                switch (selection) {
                    // $script:0619202207010205$
                    // - What do you mean?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0619202207010206$
                // - Am I gonna be a moth? A butterfly? Maybe a beetle?
                switch (selection) {
                    // $script:0619202207010207$
                    // - You're a beetle, for sure.
                    case 0:
                        return 40;
                    // $script:0619202207010208$
                    // - Oh, you're definitely a moth.
                    case 1:
                        return 41;
                    // $script:0619202207010209$
                    // - Hmm. Maybe a butterfly?
                    case 2:
                        return 42;
                }
                return -1;
            case (40, 0):
                // $script:0619202207010210$
                // - R-really? I guess beetles are pretty cool...
                return -1;
            case (41, 0):
                // $script:0619202207010211$
                // - Wow... A moth? So the butterflies were telling the truth... I might as well just end it now. Sniff...
                return -1;
            case (42, 0):
                // $script:0619202207010212$
                // - That's a relief! The butterflies said I was a moth, but I want to become a beautiful butterfly!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Close,
            (41, 0) => NpcTalkButton.Close,
            (42, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
