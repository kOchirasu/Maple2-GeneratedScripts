using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004071: Deluded Frog
/// </summary>
public class _11004071 : NpcScript {
    internal _11004071(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0619202207010155$ 
                // - Woe is me, woe is me... 
                return true;
            case 10:
                // $script:0619202207010156$ 
                // - Woe is me, woe is me... 
                // $script:0619202207010157$ 
                // - Oh... Hey! You! Help me! 
                switch (selection) {
                    // $script:0619202207010158$
                    // - What's going on?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0619202207010159$ 
                // - Just hear me out, okay? I'm actually a noble from Tria! A mage cursed me to become a frog, until... Well, perhaps you could help me break the curse. 
                switch (selection) {
                    // $script:0619202207010160$
                    // - Don't tell me you want me to kiss you.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0619202207010161$ 
                // - But it's the only way to break the curse! 
                switch (selection) {
                    // $script:0619202207010162$
                    // -  Has anyone else tried breaking the curse yet?
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0619202207010163$ 
                // - Of course. Obviously, I haven't found the <i>right</i> human to break the curse... 
                switch (selection) {
                    // $script:0619202207010164$
                    // - Are you really cursed?
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 34:
                // $script:0619202207010165$ 
                // - That's what my ma used to tell me when I wouldn't eat my flies. The old frog must've taken me in when I was really little. 
                switch (selection) {
                    // $script:0619202207010166$
                    // - Ah. Well, I'll pass. Thanks, though.
                    case 0:
                        Id = 35;
                        return false;
                }
                return true;
            case 35:
                // $script:0619202207010167$ 
                // - Don't be so picky. I'll shower you with riches when I'm back in my rightful form! I just know in my guts that you can break this curse. 
                switch (selection) {
                    // $script:0619202207010168$
                    // - You keep telling yourself that. I'm out of here.
                    case 0:
                        Id = 36;
                        return false;
                }
                return true;
            case 36:
                // $script:0619202207010169$ 
                // - Where, oh where will I find someone to break my curse? Woe is me! 
                return true;
            default:
                return true;
        }
    }
}
