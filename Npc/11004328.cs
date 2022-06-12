using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004328: Tina
/// </summary>
public class _11004328 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1010140307011526$
    // - I've never heard such a call...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1010140307011527$
                // - I've never heard such a call...
                return 10;
            case (10, 1):
                // $script:1010140307011528$
                // - Hey! Fancy meeting you there.
                return 10;
            case (10, 2):
                // $script:1010140307011529$
                // - Quick question. You hear that noise?
                switch (selection) {
                    // $script:1010140307011530$
                    // - What noise?
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:1010140307011531$
                // - So, you can't hear it, either. That figures.
                return 20;
            case (20, 1):
                // $script:1010140307011532$
                // - I keep hearing this crying sound. It's like a hurt animal... but it's no animal I've ever seen.
                return 20;
            case (20, 2):
                // $script:1010140307011533$
                // - $npcName:11004327[gender:0]$ and I are new to this land, but I'm sure the crying isn't from a monster.
                return 20;
            case (20, 3):
                // $script:1010140307011534$
                // - What could it be? There are so many secrets here.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Next,
            (20, 2) => NpcTalkButton.Next,
            (20, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
