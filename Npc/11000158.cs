using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000158: Bruno
/// </summary>
public class _11000158 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30;40
    }

    // Select 0:
    // $script:0831180407000666$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000668$
                // - This is bad. The monsters are growing stronger by the day.
                return -1;
            case (30, 0):
                // $script:0831180407000669$
                // - If you're looking for $itemPlural:20000014$, the monsters around here are running around with them.
                return -1;
            case (40, 0):
                // $script:0116162507009777$
                // - What brings you here, $MyPCName$?
                return 40;
            case (40, 1):
                // $script:0116162507009778$
                // - Are you really working with $npcName:11003534[gender:0]$? Do you think you could put in a good word?
                switch (selection) {
                    // $script:0116162507009779$
                    // - Uhh... About what?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0116162507009780$
                // - Becoming his apprentice! He says that I'm still a rookie, but in just ten years under his tutelage, I could become one of the greatest guards of all time!
                switch (selection) {
                    // $script:0116162507009781$
                    // - Ten years?!
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:0116162507009782$
                // - Anyway, why are you here?
                switch (selection) {
                    // $script:0116162507009783$
                    // - I'm looking into rumors about places affected by extreme heat.
                    case 0:
                        return 43;
                }
                return -1;
            case (43, 0):
                // $script:0116162507009784$
                // - Extreme heat. I see... 
                return 43;
            case (43, 1):
                // $script:0116170407009790$
                // - I don't know anything about that!
                return 43;
            case (43, 2):
                // $script:0116162507009785$
                // - They say $npcName:11000005[gender:1]$ knows just about everything. You could head to $map:02000031$ and ask her.
                switch (selection) {
                    // $script:0116162507009786$
                    // - Thank you for your time.
                    case 0:
                        return 44;
                }
                return -1;
            case (44, 0):
                // $script:0116162507009787$
                // - It was my pleasure! Please tell $npcName:11003534[gender:0]$ I said hello.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.SelectableDistractor,
            (43, 0) => NpcTalkButton.Next,
            (43, 1) => NpcTalkButton.Next,
            (43, 2) => NpcTalkButton.SelectableDistractor,
            (44, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
