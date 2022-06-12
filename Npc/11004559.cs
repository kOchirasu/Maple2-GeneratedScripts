using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004559: Mint
/// </summary>
public class _11004559 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0220211107014487$
    // - Aaaah.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0220211107014488$
                // - Aaaah.
                return 10;
            case (10, 1):
                // $script:0220211107014489$
                // - Oh, hello! I remember you.
                switch (selection) {
                    // $script:0220211107014490$
                    // - Yeah, and I've seen you around.
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:0220211107014491$
                // - I suppose it would be weird if you <i>didn't</i> know who I am.
                return 20;
            case (20, 1):
                // $script:0220211107014492$
                // - So, you're here for the Queen Bean Rumble, right? Are you sure you're up to fighting me?
                switch (selection) {
                    // $script:0220211107014493$
                    // - I was about to ask you the same.
                    case 0:
                        return 30;
                }
                return -1;
            case (30, 0):
                // $script:0220211107014494$
                // - Oh, you think you can take me on just because I dance all day? Well, I have news for you, $male:buddy,female:lady$. Dancing is fantastic exercise. I'm going to crush you like a teeny tiny bug!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
