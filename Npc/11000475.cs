using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000475: Wheel of Joy
/// </summary>
public class _11000475 : NpcScript {
    internal _11000475(INpcScriptContext context) : base(context) {
        // TODO: Condition $script:0831180610000459$;$script:0831180610000460$;$script:0831180610000461$
        // Id = 30;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 30:
                // $script:0831180610000459$ 
                // - Spin, spin! 
                // $script:0831180610000460$ functionID=1 buttonSet=16 
                // - Congratulations, you're a winner!
You get to draw a <font color="#ffd200">wondrous item</font>! 
                // $script:0831180610000461$ buttonSet=1 
                // - Come on, spin the roulette for your chance to win amazing items!
May luck be with you, <font color="#ffd200">$MyPCName$</font>! 
                return true;
            case 40:
                // $script:0831180610000462$ 
                // - You get only <font color="#ffd200">one chance to spin $npc:11000475$</font>.
Want to spin again? Then you'll have to win again! 
                // $script:0831180610000463$ 
                // - I hope you come back and win again soon!
Have a lucky journey! 
                return true;
            default:
                return true;
        }
    }
}
