using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001665: Karl
/// </summary>
public class _11001665 : NpcScript {
    internal _11001665(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0617211107006378$ 
                // - So, it's you. 
                return true;
            case 10:
                // $script:0617211107006379$ 
                // - The empress has placed her faith in you. 
                return true;
            case 20:
                // $script:0617211107006380$ 
                // - Your eyes speak volumes about your character, $MyPCName$. I believe I can trust you. We are depending on you to protect the peace of Maple World. 
                return true;
            case 30:
                // $script:0426090007008441$ 
                // - What does Her Highness see in this stranger...? 
                return true;
            default:
                return true;
        }
    }
}
