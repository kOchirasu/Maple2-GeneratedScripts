using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001130: Nordan
/// </summary>
public class _11001130 : NpcScript {
    internal _11001130(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911192907003858$ 
                // - D-do you want some herbs? 
                return true;
            case 30:
                // $script:0911192907003861$ 
                // - W-what's with those weird noises? You hear them too, r-right? 
                switch (selection) {
                    // $script:0911192907003862$
                    // - I didn't hear anything.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0911192907003863$ 
                // - What?! D-don't look at me like that... I'm not crazy! 
                switch (selection) {
                    // $script:0911192907003864$
                    // - It was probably just a small animal.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0911192907003865$ 
                // - Y-you think so? You'll protect me if it's something scary though, right? Hngg... Now my heart is p-pounding. 
                return true;
            default:
                return true;
        }
    }
}
