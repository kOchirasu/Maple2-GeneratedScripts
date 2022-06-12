using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004477: Soran
/// </summary>
public class _11004477 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012173$
    // - Eee! It's him! It's really him!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012174$
                // - Eee! It's him! It's really him!
                return 10;
            case (10, 1):
                // $script:1227192907012175$
                // - Ugh! What are you?
                return 10;
            case (10, 2):
                // $script:1227192907012176$
                // - Don't jump out at me like that. When I saw your ugly mug, I thought you were some kind of freaky monster.
                switch (selection) {
                    // $script:1227192907012177$
                    // - Rude!
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012178$
                // - Don't take it personally, uggo. Everyone is hideous compared to Blake!
                switch (selection) {
                    // $script:1227192907012179$
                    // - You need to get your eyes checked.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1227192907012180$
                // - A normie like you will never understand! Blake is beauty. Blake is the future!
                return 12;
            case (12, 1):
                // $script:1227192907012181$
                // - Just wait. Soon, everyone in Kritias will bow before Blake's handsomeness!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Next,
            (12, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
