using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000118: Cliffine
/// </summary>
public class _11000118 : NpcScript {
    internal _11000118(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000503$ 
                // - Can I help you? 
                return true;
            case 30:
                // $script:0831180407000506$ 
                // - Usually this place is not so crowded. I didn't expect so many people to be so eager to make money.  
                // $script:0831180407000507$ 
                // - $MyPCName$, you looking to scare up some cash too? It's not as dangerous as I expected. Give it a try! 
                return true;
            default:
                return true;
        }
    }
}
