using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001008: Faded Photo
/// </summary>
public class _11001008 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407003437$
    // - ...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407003438$
                // - <font color="#909090">(It's an old, faded picture. You brush the dust off and look closely.)</font>
                return 10;
            case (10, 1):
                // $script:0831180407003439$
                // - <font color="#909090">(It's a picture of a couple, and there's a baby between them.)</font>
                return 10;
            case (10, 2):
                // $script:0831180407003440$
                // - <font color="#909090">(Something's written on the back of the picture.)</font>
                //   "On the first birthday of our beloved daughter"
                return 10;
            case (10, 3):
                // $script:0831180407003441$
                // - <font color="#909090">(After a moment of hesitation, you return the picture to its place.)</font>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Next,
            (10, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
