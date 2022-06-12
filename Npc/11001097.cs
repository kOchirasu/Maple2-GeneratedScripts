using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001097: Triz
/// </summary>
public class _11001097 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003688$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003691$
                // - If I had to pick my most popular invention, it would be NSD 3200. It's a device that dismantles equipment and extracts onyx from it.
                return 30;
            case (30, 1):
                // $script:0831180407003692$
                // - People think the blacksmiths of the Nerman Forge came up with it, but I was brought in to design it for them. I was compensated for my services, of course, but if I knew it'd become so popular I would've asked for more royalties!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
