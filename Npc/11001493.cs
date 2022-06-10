using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001493: Startz
/// </summary>
public class _11001493 : NpcScript {
    internal _11001493(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0118150907005809$ 
                // - I think I'd like to talk today.
                return true;
            case 30:
                // $script:0118150907005812$ 
                // - Everything happens for a reason.
                switch (selection) {
                    // $script:0120154307005850$
                    // - Tell me about your past.
                    case 0:
                        Id = 0; // TODO: 31 | 32
                        return false;
                }
                return true;
            case 31:
                // $script:0120154307005851$ functionID=1 
                // - Ah, you want to know what happened back then.
                return true;
            case 32:
                // $script:0120154307005852$ 
                // - I can't remember.
                return true;
            case 40:
                // $script:0127102807005856$ 
                // - Everything happens for a reason.
                return true;
            default:
                return true;
        }
    }
}
