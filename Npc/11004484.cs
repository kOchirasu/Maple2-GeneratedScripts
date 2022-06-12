using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004484: Ambulia
/// </summary>
public class _11004484 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012258$
    // - Keep quiet! Stay down! It's over if the enemy spots us!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012259$
                // - Keep quiet! Stay down! It's over if the enemy spots us!
                switch (selection) {
                    // $script:1227192907012260$
                    // - Something wrong?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012261$
                // - Something wrong? Is something <i>wrong</i>?! Look at the chaos out here! I came here to discover new lands, not risk my life!
                return 11;
            case (11, 1):
                // $script:1227192907012262$
                // - That so-called Daemon Army ambushed me, so I ran away... only to find myself in the middle of a Tairen raid!
                return 11;
            case (11, 2):
                // $script:1227192907012263$
                // - At this rate, I'll get tombstoned before I discovery anything worthwhile. If you really want to help, then get rid of those bad guys for me!
                switch (selection) {
                    // $script:0114161407012705$
                    // - Okay.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0114161407012706$
                // - I leave it to you!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Next,
            (11, 2) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
