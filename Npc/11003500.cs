using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003500: Temporary Dimensional Portal
/// </summary>
public class _11003500 : NpcScript {
    internal _11003500(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0727033607008748$ 
                // - A temporary portal for you, lost soul! Courtesy of $npcName:11003257$, genius mage!
                return true;
            case 10:
                // $script:0727033607008749$ 
                // - A temporary portal for you, lost soul! Now servicing the $map:02000179$.
                switch (selection) {
                    // $script:0727033607008750$
                    // - (Go to the $map:02000179$.)
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0727033607008751$
                    // - (Stay here.)
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 11:
                // $script:0727033607008752$ functionID=1 
                // - You're on your way!
                return true;
            case 12:
                // $script:0727033607008753$ 
                // - Come find me if you change your mind.
                return true;
            default:
                return true;
        }
    }
}
