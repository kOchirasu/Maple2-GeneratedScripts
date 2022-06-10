using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001724: Mystery Person
/// </summary>
public class _11001724 : NpcScript {
    internal _11001724(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0728022507006974$ 
                // - ... 
                return true;
            case 30:
                // $script:0804173107007076$ 
                // - Tell me what you have to say. 
                switch (selection) {
                    // $script:0804173107007077$
                    // - Who are those two behind you?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0804173107007078$ 
                // - These are my companions. Don't worry, they aren't nearly as violent or nasty as they look.  
                return true;
            default:
                return true;
        }
    }
}
