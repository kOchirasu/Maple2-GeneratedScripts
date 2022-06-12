using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004254: Inscribed Totem
/// </summary>
public class _11004254 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0829171107010968$
    // - <font color="#909090">(The water in the "Demonspring", for which the surrounding area is named, is neither red nor black as one might expect, but rather a sickly translucent green.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0829171107010969$
                // - <font color="#909090">(The water in the "Demonspring", for which the surrounding area is named, is neither red nor black as one might expect, but rather a sickly translucent green.)</font>
                return 10;
            case (10, 1):
                // $script:0831140807011011$
                // - <font color="#909090">(It's said that the spring was tainted long ago by the blood of the goddess of darkness. It is <i>also</i> said that this spring contains the blood of an ancient turtle. No one knows the truth of the matter.)</font>
                return 10;
            case (10, 2):
                // $script:0831140807011012$
                // - <font color="#909090">(Nevertheless, it's probably best not to let the liquid touch you.)</font>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
