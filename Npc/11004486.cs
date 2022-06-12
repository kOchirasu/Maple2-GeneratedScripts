using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004486: Vivipara
/// </summary>
public class _11004486 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012275$
    // - Hey, you're from Maple World, right?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012276$
                // - Hey, you're from Maple World, right?
                switch (selection) {
                    // $script:1227192907012277$
                    // - Is something wrong?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012278$
                // - Everything's wrong! I loathe field work. Everything around here wants to tombstone me. And it's been days since I had a proper bath! This assignment must be a sick joke on the part of my boss.
                return 11;
            case (11, 1):
                // $script:1227192907012279$
                // - I miss my lab in Tria. I hope this mission ends soon...
                switch (selection) {
                    // $script:1227192907012280$
                    // - Cheer up!
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1227192907012281$
                // - I hadn't thought of it that way. Thank you. You cheer up, too!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
