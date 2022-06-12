using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004083: Junjun
/// </summary>
public class _11004083 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0622133907010276$
    // - Hm... The schedule's tight, but we should be able to finish sector B today.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0622133907010277$
                // - Hm... The schedule's tight, but we should be able to finish sector B today.
                return 10;
            case (10, 1):
                // $script:0622133907010278$
                // - Ah, a new face. What do you want?
                switch (selection) {
                    // $script:0622133907010279$
                    // - What are you building here?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0622133907010280$
                // - Ah, I see you've got an inquisitive mind. Good. I like it!
                return 31;
            case (31, 1):
                // $script:0622133907010281$
                // - We're building a geothermal plant here. Just you wait. In a few years' time, we'll be providing all the power to the nearby towns!
                return 31;
            case (31, 2):
                // $script:0622133907010282$
                // - The old... erm, tenants used this place to build a smelting furnace, but they didn't have the know-how to handle this much heat.
                return 31;
            case (31, 3):
                // $script:0622133907010283$
                // - Anyway, since this place is basically abandoned, we decided to take things over. If you want to lend a hand, we can always use another strong back or two!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Next,
            (31, 2) => NpcTalkButton.Next,
            (31, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
