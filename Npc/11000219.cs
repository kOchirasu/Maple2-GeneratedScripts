using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000219: Lucia
/// </summary>
public class _11000219 : NpcScript {
    internal _11000219(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000956$ 
                // - Wah! Geez! 
                return true;
            case 30:
                // $script:0831180407000959$ 
                // - Argh, what? 
                switch (selection) {
                    // $script:0831180407000960$
                    // - What are you doing?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000961$ 
                // - Sheesh, I don't know. I can't talk. Doing this is tough as it is. My limbs are so numb I can't feel them anymore.  
                return true;
            default:
                return true;
        }
    }
}
