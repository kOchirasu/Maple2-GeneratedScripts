using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004259: Ludified Water
/// </summary>
public class _11004259 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0829171107010978$
    // - <font color="#909090">(The water seems to be flowing all right, but it also appears rather... viscous.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0829171107010979$
                // - <font color="#909090">(The water seems to be flowing all right, but it also appears rather... viscous.)</font>
                return 10;
            case (10, 1):
                // $script:0831140807011036$
                // - Recently, this place has been transforming into ludibrium at a rapid pace. Once ludibrification starts, everything becomes mushy and then solidifies instantly.
                return 10;
            case (10, 2):
                // $script:0831140807011037$
                // - <font color="#909090">(This ludibrification has been happening all over Maple World. There's no prevention, except to be careful.)</font>
                return 10;
            case (10, 3):
                // $script:0831140807011038$
                // - <font color="#909090">(Will everything eventually become ludibrified?)</font>
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
