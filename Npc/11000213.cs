using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000213: Anonymous Bum
/// </summary>
public class _11000213 : NpcScript {
    internal _11000213(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000904$ 
                // - Wh-what? What do you want? 
                return true;
            case 30:
                // $script:0831180407000907$ 
                // - Leave me alone! I-I don't know anything! 
                switch (selection) {
                    // $script:0831180407000908$
                    // - Uh, what?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000909$ 
                // - O-oh, you... I thought you were going to ask me something. Nevermind, then. 
                return true;
            default:
                return true;
        }
    }
}
