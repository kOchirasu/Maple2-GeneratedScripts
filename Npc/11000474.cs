using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000474: Wheel of Joy
/// </summary>
public class _11000474 : NpcScript {
    internal _11000474(INpcScriptContext context) : base(context) {
        // TODO: Job 30
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 30:
                // $script:0831180610000452$ 
                // - Spin, spin!
                // $script:0831180610000453$ functionID=1 buttonSet=16 
                // - Welcome!
                //   $npc:11000474$ is filled with <font color="#ffd200">wondrous items</font>!
                // $script:0831180610000454$ buttonSet=1 
                // - Spin $npc:11000474$ for your chance to win the wondrous items!
                //   May luck be with you, <font color="#ffd200">$MyPCName$</font>!
                return true;
            case 40:
                // $script:0831180610000455$ 
                // - You get only <font color="#ffd200">one chance to spin $npc:11000474$</font>.
                //   Want to spin $npc:11000474$ again? Then <font color="#ffd200">find another hat</font>!
                // $script:0831180610000456$ 
                // - This might sound crazy, but if you come across a hat in a field, don't hesitate to throw yourself inside of it! You heard me!
                return true;
            default:
                return true;
        }
    }
}
