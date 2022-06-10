using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003244: Armano
/// </summary>
public class _11003244 : NpcScript {
    internal _11003244(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008147$ 
                // - No... This c-can't...
                return true;
            case 30:
                // $script:0403155707008149$ 
                // - Not this... Anything but this...
                //   <font color="#909090">($npcName:11003240[gender:0]$ lowers his head, his shoulders trembling ever so slightly.)</font>
                return true;
            default:
                return true;
        }
    }
}
