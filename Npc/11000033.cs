using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000033: Jorge
/// </summary>
public class _11000033 : NpcScript {
    internal _11000033(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000185$ 
                // - What brings you here? 
                return true;
            case 30:
                // $script:0831180407000188$ 
                // - Ancient tomes containing stories of this world must be handled with care. They can teach us many important lessons. 
                return true;
            case 40:
                // $script:0530154307008539$ 
                // - Are you lost? Why are you bothering me? 
                switch (selection) {
                    // $script:0530154307008540$
                    // - Take me to $map:52000133$.
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0530154307008541$
                    // - Just thought I'd pay you a social visit.
                    case 1:
                        Id = 42;
                        return false;
                }
                return true;
            case 41:
                // $script:0530154307008542$ functionID=1 
                // - $npcName:11000031[gender:0]$ says you're all right, so fine. Off you go. 
                return true;
            case 42:
                // $script:0530154307008543$ 
                // - All right, then. I hope you're enjoying $map:02000023$. 
                return true;
            case 50:
                // $script:0530154307008544$ 
                // - The ancient records of our history must be handled with care. They teach us many important lessons. 
                return true;
            default:
                return true;
        }
    }
}
