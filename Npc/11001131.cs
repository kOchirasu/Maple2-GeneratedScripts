using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001131: Roteo
/// </summary>
public class _11001131 : NpcScript {
    internal _11001131(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911192907003866$ 
                // - Hmm? What do you want? 
                return true;
            case 30:
                // $script:0911192907003869$ 
                // - Hah. Cold, are we? Maybe you should've worn thicker clothes. 
                switch (selection) {
                    // $script:0911192907003870$
                    // - I'm not c-c-cold.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0911192907003871$
                    // - Are you kidding? I'm <b>freezing</b>.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0911192907003872$ 
                // - Bahaha. A real tough cookie, aren't you?  I'm a professional explorer, and even I get a little cold at times like this. Maybe you belong in my line of work. 
                return true;
            case 32:
                // $script:0911192907003873$ 
                // - You look like seasoned adventurer. I'm sure you've seen worse weather than this. So suck it up! Bahaha. 
                return true;
            default:
                return true;
        }
    }
}
