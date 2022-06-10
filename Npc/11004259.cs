using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004259: Ludified Water
/// </summary>
public class _11004259 : NpcScript {
    internal _11004259(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0829171107010978$ 
                // - <font color="#909090">(The water seems to be flowing all right, but it also appears rather... viscous.)</font>
                return true;
            case 10:
                // $script:0829171107010979$ 
                // - <font color="#909090">(The water seems to be flowing all right, but it also appears rather... viscous.)</font>
                // $script:0831140807011036$ 
                // - Recently, this place has been transforming into ludibrium at a rapid pace. Once ludibrification starts, everything becomes mushy and then solidifies instantly.
                // $script:0831140807011037$ 
                // - <font color="#909090">(This ludibrification has been happening all over Maple World. There's no prevention, except to be careful.)</font>
                // $script:0831140807011038$ 
                // - <font color="#909090">(Will everything eventually become ludibrified?)</font>
                return true;
            default:
                return true;
        }
    }
}
