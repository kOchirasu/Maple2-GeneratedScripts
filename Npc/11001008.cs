using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001008: Faded Photo
/// </summary>
public class _11001008 : NpcScript {
    internal _11001008(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003437$ 
                // - ...
                return true;
            case 10:
                // $script:0831180407003438$ 
                // - <font color="#909090">(It's an old, faded picture. You brush the dust off and look closely.)</font>
                // $script:0831180407003439$ 
                // - <font color="#909090">(It's a picture of a couple, and there's a baby between them.)</font>
                // $script:0831180407003440$ 
                // - <font color="#909090">(Something's written on the back of the picture.)</font>
                //   "On the first birthday of our beloved daughter"
                // $script:0831180407003441$ 
                // - <font color="#909090">(After a moment of hesitation, you return the picture to its place.)</font>
                return true;
            default:
                return true;
        }
    }
}
