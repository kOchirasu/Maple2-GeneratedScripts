using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000122: Gregory
/// </summary>
public class _11000122 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000527$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000529$
                // - I see you're curious about $itemPlural:20000016$. Well... After the Blue Lapenta was destroyed, hundreds of Defenders fell to the shadow toxin that spread from the Land of Darkness.
                return 30;
            case (30, 1):
                // $script:0831180407000530$
                // - I tried everything reagent I could get my hands on to cure it, and the one that did it was the $item:20000045$, growing right here at the $map:02000146$. It took time to perfect the compounding process, but now my $itemPlural:20000016$ are key to the struggle against the darkness.
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
